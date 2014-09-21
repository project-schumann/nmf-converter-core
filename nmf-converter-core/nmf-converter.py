from music21 import corpus
from music21 import stream
from music21 import note
from music21 import chord
from pprint import pprint
import argparse

def convert_nmf_to_midi():
    '''Converts an NMF file to a MIDI file.'''
    # TODO: Implement me.
    pass

def convert_midi_to_nmf():
    '''Converts a MIDI file to an NMF file.'''

    # The smallest duration covered. Expressed as a percentage of a quarter note.
    smallest_note = 1.0 / 2.0

    reference_note = None
    reference_octave = None

    tie_active = False

    parts = []

    sBach = corpus.parse('bach/bwv7.7')

    # Find the lowest note in the first measure.
    # This is the reference
    chordStream = sBach.measures(0, 0, ignoreNumbers=True).chordify()

    for measure in chordStream:
        for element in measure:
            if type(element) is chord.Chord:
                reference_note = element.bass().pitchClass
                reference_octave = element.bass().octave

    # IgnoreNumbers means to start from 0 always.
    # part = sBach.parts[0].measures(0, 3,  ignoreNumbers=True)

    for part in sBach.parts:
        pitches = []
        for element in part:
            if type(element) is stream.Measure:
                for el in element:
                    if type(el) is note.Note:

                        # Calculate the octave displacement.
                        octave_displacement = el.pitch.octave - reference_octave

                        # Store the distance from the reference.
                        pitch = (el.pitch.pitchClass - reference_note) + octave_displacement * 12

                        n_frames = el.duration.quarterLength / smallest_note

                        for i in range(int(n_frames)):
                            if i == 0:
                                if not tie_active:
                                    pitches.append([1, pitch])
                                else:
                                    pitches.append([2, pitch])

                                # a tie can only begin or end at a new note.
                                if el.tie is not None and el.tie.type == 'start':
                                    tie_active = True
                                else:
                                    tie_active = False
                            else:
                                pitches.append([2, pitch])

                    elif type(el) is note.Rest:
                        n_frames = el.duration.quarterLength / smallest_note

                        for i in range(int(n_frames)):
                            pitches.append([0, 0])
        parts.append(pitches)

    pprint(zip(*parts))

def determine_source_format(input_file_path):
    '''Determines the format of the input file based on its extension.'''
    # TODO: Implement me.
    pass

def parse_cl_args(arg_vector):
    '''Parses the command line arguments'''
    parser = argparse.ArgumentParser(description='Converts to and from NMF into MIDI.')

    parser.add_argument('input_file', metavar='input_file', help='The path of the input file to be converted.')
    parser.add_argument('output_file', metavar='output_file', help='The path of the output file.', required=False)

    return parser.parse_args(arg_vector)

def run():
    '''Converts to and from NMF into MIDI.'''
    args = parse_cl_args(sys.argc[1:])

    source_format = determine_source_format(args.input_file)

    if source_format is 'nmf':
        convert_nmf_to_midi()
    elif source_format is 'midi':
        convert_midi_to_nmf()
    else:
        print('Please provide either an nmf or midi file as your input.')

if __name__ == '__main__':
    convert_midi_to_nmf()
    # run()