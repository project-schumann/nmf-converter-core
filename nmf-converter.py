import argparse

reference_note = None
reference_octave = None

pitches = []

def convert_nmf_to_midi():
    '''Converts an NMF file to a MIDI file.'''
    # TODO: Implement me.
    pass

def convert_midi_to_nmf():
    '''Converts a MIDI file to an NMF file.'''

    sBach = corpus.parse('bach/bwv7.7')

    part = sBach.parts[0].measures(0, 3)

    for element in part:
        if type(element) is stream.Measure:
            for el in element:
                if type(el) is note.Note:

    # Mark the reference note.
    # This is the lowest pitch at the beginning of the piece.
    if reference_note is None:
        reference_note = el.pitch.pitchClass
        reference_octave = el.pitch.octave

    # Calculate the octave displacement.
    octave_displacement = el.pitch.octave - reference_octave

    # Store the distance from the reference.
    pitches.append((el.pitch.pitchClass - reference_note) + octave_displacement * 12)

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
    run()