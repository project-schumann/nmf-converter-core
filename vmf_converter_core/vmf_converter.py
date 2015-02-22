from music21 import note
from music21 import converter

import argparse
import sys
import os

def convert_vmf_to_midi(vmfScore):
    """
    Converts an vmf file to a MIDI file.
    """
    # TODO: Implement me.
    pass

def scan_score_for_shortest_duration(score):
    """
    Scans the entire score for rhythmic analysis.
    This scan determines the smallest note value necessary to accurately
    encode the score in vmf.
    :type score: Score
    :param score: The input score stream to analyze.
    :rtype int
    :return: An integer denoting the smallest fraction of a quarter note
    necessary to accurately encode the score in vmf.
    """
    # Flatten the score into one stream and extract the notes and rests.
    notes_and_rests = score.flat.notesAndRests

    # Keep track of the smallest duple and triple. We multiply them for the shortest duration.
    # eg. eighth * triplet = 2 * 3 = 6 notes per beat
    shortest_duration_duple_inv = -1
    shortest_duration_triple_inv = -1

    for element in notes_and_rests:
        # We need to know this so we can modify the beat duration for compound times.
        current_time_signature = element.getContextByClass('TimeSignature')

        # For triplets in simple time.
        if current_time_signature.beatDuration.quarterLength is 1:
            duration = element.duration.quarterLength / current_time_signature.beatDuration.quarterLength
        else:
            duration = element.duration.quarterLength

        # We don't care if it is larger than a quarter.
        if duration > 1:
            continue

        duration_inv = round(current_time_signature.beatDuration.quarterLength / duration)

        if duration_inv % 3 == 0:
            # Multiple of 3.
            if duration < shortest_duration_triple_inv or shortest_duration_triple_inv is -1:
                shortest_duration_triple_inv = duration_inv
        elif duration_inv % 2 == 0 or duration_inv == 1:
            # Multiple of 2.
            if duration < shortest_duration_duple_inv or shortest_duration_duple_inv is -1:
                shortest_duration_duple_inv = duration_inv

    # Set -1 to 1 if we never encounter a duple or triple.
    if shortest_duration_duple_inv < 0:
        shortest_duration_duple_inv *= -1

    if shortest_duration_triple_inv < 0:
        shortest_duration_triple_inv *= -1

    # Take the product and return the smallest value.
    return current_time_signature.beatDuration.quarterLength / (shortest_duration_duple_inv * shortest_duration_triple_inv)

def convert_score_to_vmf(score):
    """
    Converts a MIDI file to an vmf file.
    :type score: Score
    :param score: The input score stream to convert.
    :rtype: list
    :return: A list of tuples representing the music contained in the MIDI file.
    """

    # The smallest duration covered. Expressed as a percentage of a quarter note.
    smallest_note = scan_score_for_shortest_duration(score)

    tie_active = False

    parts = []

    for part in score.parts:
        pitches = []
        for element in part.flat:
            if type(element) is note.Note:

                n_frames = element.duration.quarterLength / smallest_note

                for i in range(int(n_frames)):
                    if i == 0:
                        if not tie_active:
                            pitches.append([1, 0, 0, element.pitchClass, element.octave])
                        else:
                            pitches.append([2, 0, 0, element.pitchClass, element.octave])

                        # a tie can only begin or end at a new note.
                        if element.tie is not None and element.tie.type == 'start':
                            tie_active = True
                        else:
                            tie_active = False
                    else:
                        pitches.append([2, 0, 0, element.pitchClass, element.octave])

            elif type(element) is note.Rest:
                n_frames = element.duration.quarterLength / smallest_note

                for i in range(int(n_frames)):
                    pitches.append([0, 0, 0, 0, 0])
        parts.append(pitches)

    vmf_file = {u'header': {}, u'body': [list(tick) for tick in zip(*parts)]}

    return vmf_file

def determine_source_format(input_file_path):
    """
    Determines the format of the input file based on its extension.
    :type input_file_path: str
    :param input_file_path: The file path of the input file.
    :rtype: str
    :return: A dot prefixed string indicating the extension type.
    """
    file_name, file_extension = os.path.splitext(input_file_path)
    return file_extension

def parse_cl_args(arg_vector):
    """
    Parses the command line arguments
    :type arg_vector: list
    :param arg_vector: The command line arguments.
    :rtype: object
    :return: An object with attributes referring to the arguments passed by the user.
    """
    parser = argparse.ArgumentParser(description='Converts to and from vmf into MIDI.')

    parser.add_argument('input_file', metavar='input_file', help='The path of the input file to be converted.')
    parser.add_argument('output_file', metavar='output_file', help='The path of the output file.', nargs='?')

    return parser.parse_args(arg_vector)

def run():
    """
    Converts to and from vmf into MIDI.
    """
    args = parse_cl_args(sys.argv[1:])

    source_format = determine_source_format(args.input_file)

    if source_format is '.vmf':
        convert_vmf_to_midi(converter.parse(args.input_file))
    elif source_format is '.midi':
        convert_score_to_vmf(converter.parse(args.input_file))
    else:
        print('Please provide either an vmf or midi file as your input.')

if __name__ == '__main__':
    run()