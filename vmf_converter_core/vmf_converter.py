from functools import reduce
from music21 import note, chord
from music21 import converter

import argparse
import sys
import os
from music21.common import approximateGCD


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

    # Set comprehension: Get a set of durations in the measure.
    durations = {element.duration.quarterLength for element in notes_and_rests}

    # We need a list, not a set. Convert here. The GCD is the largest common subdivision we can use.
    return approximateGCD(list(durations))

def scan_score_for_largest_chord(score):
    """
    Scans the entire score for the largest chord.
    This determines how many notes entries should be available in a tick.
    :param score: Score
    :rtype: int
    :return: An integer denoting the size of the largest chord.
    """
    # Flatten the score into one stream and extract the notes.
    notes = score.flat.notes

    # Flatten the score into one stream and extract the chords.
    chords = [element for element in score.flat.notes.elements if type(element) is chord.Chord]

    largest_size = 0

    # Find the largest chord size.
    for c in chords:
        largest_size = max(c.multisetCardinality, largest_size)

    return largest_size

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

    # The number of notes in largest chord in the file.
    largest_chord = scan_score_for_largest_chord(score)

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

                        # Pad remaining note positions for chords smaller than largest.
                        for i in range(largest_chord - 1):
                            pitches[-1].append(-1)
                            pitches[-1].append(-1)

                        # a tie can only begin or end at a new note.
                        if element.tie is not None and element.tie.type == 'start':
                            tie_active = True
                        else:
                            tie_active = False
                    else:
                        pitches.append([2, 0, 0, element.pitchClass, element.octave])

                        # Pad remaining note positions for chords smaller than largest.
                        for i in range(largest_chord - 1):
                            pitches[-1].append(-1)
                            pitches[-1].append(-1)

            elif type(element) is chord.Chord:
                n_frames = element.duration.quarterLength / smallest_note

                for i in range (int(n_frames)):
                    if i == 0:
                        if not tie_active:
                            current_chord = [1, 0, 0]

                            # add in each pitch.
                            for pitch in element.pitches:
                                current_chord.append(pitch.pitchClass)
                                current_chord.append(pitch.octave)

                            # Pad remaining note positions for chords smaller than largest.
                            for i in range(largest_chord - element.multisetCardinality):
                                current_chord.append(-1)
                                current_chord.append(-1)

                            pitches.append(current_chord)
                        else:
                            current_chord = [2, 0, 0]

                            # add in each pitch.
                            for pitch in element.pitches:
                                current_chord.append(pitch.pitchClass)
                                current_chord.append(pitch.octave)

                            # Pad remaining note positions for chords smaller than largest.
                            for i in range(largest_chord - element.multisetCardinality):
                                current_chord.append(-1)
                                current_chord.append(-1)

                            pitches.append(current_chord)

                        # a tie can only begin or end at a new chord.
                        if element.tie is not None and element.tie.type == 'start':
                            tie_active = True
                        else:
                            tie_active = False
                    else:
                        current_chord = [2, 0, 0]

                        # add in each pitch.
                        for pitch in element.pitches:
                            current_chord.append(pitch.pitchClass)
                            current_chord.append(pitch.octave)


                        # Pad remaining note positions for chords smaller than largest.
                        for i in range(largest_chord - element.multisetCardinality):
                            current_chord.append(-1)
                            current_chord.append(-1)

                        pitches.append(current_chord)

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