from music21 import note
from music21 import chord

import argparse
import sys
import os

def convert_nmf_to_midi():
    """
    Converts an NMF file to a MIDI file.
    """
    # TODO: Implement me.
    pass

def convert_score_to_nmf(score):
    """
    Converts a MIDI file to an NMF file.
    :type score: Score
    :param score: The input score stream to convert.
    :rtype: list
    :return: A list of tuples representing the music contained in the MIDI file.
    """

    # The smallest duration covered. Expressed as a percentage of a quarter note.
    smallest_note = 1.0 / 2.0

    tie_active = False

    parts = []

    for part in score.parts:
        pitches = []
        for element in part:
            if type(element) is note.Note:

                n_frames = element.duration.quarterLength / smallest_note

                for i in range(int(n_frames)):
                    if i == 0:
                        if not tie_active:
                            pitches.append([1, element.pitchClass, element.octave])
                        else:
                            pitches.append([2, element.pitchClass, element.octave])

                        # a tie can only begin or end at a new note.
                        if element.tie is not None and element.tie.type == 'start':
                            tie_active = True
                        else:
                            tie_active = False
                    else:
                        pitches.append([2, element.pitchClass, element.octave])

            elif type(element) is note.Rest:
                n_frames = element.duration.quarterLength / smallest_note

                for i in range(int(n_frames)):
                    pitches.append([0, 0, 0])
        parts.append(pitches)

    return zip(*parts)

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
    parser = argparse.ArgumentParser(description='Converts to and from NMF into MIDI.')

    parser.add_argument('input_file', metavar='input_file', help='The path of the input file to be converted.')
    parser.add_argument('output_file', metavar='output_file', help='The path of the output file.', nargs='?')

    return parser.parse_args(arg_vector)

def run():
    """Converts to and from NMF into MIDI."""
    args = parse_cl_args(sys.argv[1:])

    source_format = determine_source_format(args.input_file)

    if source_format is '.nmf':
        convert_nmf_to_midi(args.input_file)
    elif source_format is '.midi':
        #TODO: Import MIDI File
        convert_score_to_nmf()
    else:
        print('Please provide either an nmf or midi file as your input.')

if __name__ == '__main__':
    run()