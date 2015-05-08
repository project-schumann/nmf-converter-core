"""Main logic for parsing a VMF file."""
from fractions import Fraction
import json

from music21 import note, chord, stream, meter, key

from music21.chord import Chord
from music21.common import approximateGCD
from music21.key import KeySignature
from music21.meter import TimeSignature
from music21.note import Note, Rest
from music21.pitch import Pitch
from music21.stream import Score, Part, Stream, Voice
from vmf_converter.core.articulation_converter import ArticulationConverter

from vmf_converter.core.dynamic_converter import DynamicConverter

# The first note bit is at position 3.
INDEX_OF_FIRST_NOTE_BIT = 3
# Part id is the last bit.
INDEX_OF_PART_ID_BIT = -1

# Precision for rounding roubles.
PRECISION = 0.000000000000001
BASIC_TICK_LENGTH = 6
FIRST_PITCH_INDEX = 3
DYNAMIC_BIT = 1
ARTICULATION_BIT = 2

def find_number_of_notes_in_tick(tick):
    """
    Finds the number of notes in a tick.
    :param tick: The tick to evaluate.
    :return: An integer representing the number of notes.
    """

    # Return all the bits describing pitches, and divide by 2 (each note uses 2 bits).
    # Remove all bit pairs with -1 from the count.
    return (len(tick[3:-1]) / 2) - (tick[3:-1].count(-1) / 2)

def read_vmf_string(vmf_string):
    """
    Reads VMF data from a string to a Score Stream.
    """

    parts_converted = {}

    vmf = json.loads(vmf_string)

    # create a score
    score = Score()

    # Get the initial data
    number_of_parts = vmf['header']['number_of_parts']
    number_of_voices = vmf['header']['number_of_voices']
    smallest_note = float(Fraction(vmf['header']['tick_value']))

    # create the parts and first measure.
    for voice_number in range(number_of_parts):
        part = Part()
        voice = Voice()

        # we need new instances each time.
        try:
            initial_key_signature = KeySignature(vmf['header']['key_signature']['0.0'])
        except KeyError:
            # Key Signatures aren't mandatory. Default to C major
            initial_key_signature = KeySignature(0)

        initial_time_signature = TimeSignature(vmf['header']['time_signature']['0.0'])


        voice.append(initial_key_signature)
        voice.append(initial_time_signature)

        part.append(voice)

        score.append(part)

    # get the body of the vmf
    body = vmf['body']

    part_number = 0

    # We do this because we want to do each part at a time.
    for voice_number in range(number_of_voices):
        # Get all ticks for a given part.
        part = [tick[voice_number] for tick in body]

        current_element = None
        current_voice = None

        # iterate over each tick
        for tick in part:

            if current_voice is None:
                # Get the parent part if it exists.
                try:
                    current_part = parts_converted[tick[-1]]

                    # add a new voice and write to it.
                    voice = Voice()

                    initial_key_signature = KeySignature(vmf['header']['key_signature']['0.0'])
                    initial_time_signature = TimeSignature(vmf['header']['time_signature']['0.0'])

                    voice.append(initial_key_signature)
                    voice.append(initial_time_signature)

                    current_part.append(voice)

                except KeyError:
                    # Add it to our dictionary otherwise.
                    current_part = score.parts[part_number]
                    part_number += 1

                    parts_converted[tick[-1]] = current_part

                # Get the last voice.
                current_voice = current_part.voices[-1]

            if tick[0] == 1:
                if current_element is not None:
                    # check for precision and adjust
                    rounded = round(current_element.quarterLength)
                    if abs(current_element.quarterLength - rounded) < PRECISION:
                        current_element.quarterLength = rounded

                    # append to the part
                    current_voice.append(current_element)

                # Find how many notes to write. This will always be an int.
                number_of_notes = int(find_number_of_notes_in_tick(tick))

                if number_of_notes == 1:
                    # create a new note
                    current_element = Note(Pitch(pitchClass=tick[3], octave=tick[4]))
                else:
                    pitches = []

                    # create the pitches.
                    # From the beginning to the end of the pitch section of the tick.
                    for i in range(FIRST_PITCH_INDEX, FIRST_PITCH_INDEX + 2 * number_of_notes, 2):
                        pitch = Pitch(pitchClass=tick[i], octave=tick[i + 1])
                        pitches.append(pitch)

                    # create a new chord with these pitches.
                    current_element = Chord(pitches)


                # set the velocity of the note.
                current_element.volume.velocity = DynamicConverter.vmf_to_velocity(tick[DYNAMIC_BIT])
                # set the articulation
                if tick[ARTICULATION_BIT] != 0:
                    current_element.articulations.append(
                        ArticulationConverter.vmf_to_articulation(tick[ARTICULATION_BIT]))

                # set the value for this tick.
                current_element.quarterLength = smallest_note
            elif tick[0] == 2:
                # extend previous note
                current_element.quarterLength += smallest_note

            elif tick[0] == 0 and (isinstance(current_element, note.Note) or current_element is None):
                if current_element is not None:
                    # check for precision and adjust
                    rounded = round(current_element.quarterLength)
                    if abs(current_element.quarterLength - rounded) < PRECISION:
                        current_element.quarterLength = rounded

                    # append to the part
                    current_voice.append(current_element)

                # create new rest
                current_element = Rest()

                # Set the value for this tick.
                current_element.quarterLength = smallest_note

            elif tick[0] == 0 and isinstance(current_element, note.Rest):
                # extend previous rest.
                current_element.quarterLength += smallest_note

        # Append the last element in progress.
        if current_element is not None:
            # check for precision and adjust
            rounded = round(current_element.quarterLength)
            if abs(current_element.quarterLength - rounded) < PRECISION:
                current_element.quarterLength = rounded

            # append to the part
            current_voice.append(current_element)

    # create the stream for time signature changes
    time_signature_stream = Stream()

    for offset, time_signature_str in sorted(vmf['header']['time_signature'].items()):
        time_signature = TimeSignature(time_signature_str)
        time_signature_stream.append(time_signature)
        time_signature_stream[-1].offset = float(offset)

    # finish up the file.
    for part in score.parts:
        for voice in part.voices:
            voice.makeMeasures(inPlace=True, meterStream=time_signature_stream)

    return score

def read_vmf_file(vmf_score):
    """
    Reads VMF to Score Stream.
    """

    with open(vmf_score, 'r') as file:
        file_contents = file.read()

        return read_vmf_string(file_contents)

def scan_score_durations(score):
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

    # Flatten the score into one stream and extract the chords.
    chords = [element for element in score.flat.notes.elements if isinstance(element, chord.Chord)]

    largest_size = 0

    # Find the largest chord size.
    for current_chord in chords:
        largest_size = max(current_chord.multisetCardinality, largest_size)

    return largest_size


def convert_voices_to_parts(score, id_map):
    """
    Removes polyphonic voices and replaces them with part representations of its voices.
    :param score: Score
    :param id_map: A mapping of music21 ids to vmf part ids.
    """
    parts_to_insert = {}
    next_part_id = 0

    for i in range(len(score.parts)):
        part = score.parts[i]

        # OLD: list(filter(lambda m: issubclass(type(m), Stream) and m.hasVoices(), part.elements))
        if len([m for m in part.elements if issubclass(type(m), Stream) and m.hasVoices()]) > 0:
            # break the voices into parts.
            exploded_stream = part.explode()

            # assign the part id to all exploded parts.
            # and add the exploded parts to the original stream. Mark where to insert the parts.
            for current_stream in exploded_stream.parts:
                # all related parts share the same id.
                id_map[current_stream.id] = next_part_id
                parts_to_insert[i] = exploded_stream.parts
        else:
            # Just record the id.
            id_map[part.id] = next_part_id

        next_part_id += 1

    new_parts = list(score.parts)

    # Iterate over the parts_to_insert in reverse, otherwise
    # recorded indices are obsolete.
    for i in sorted(parts_to_insert, reverse=True):
        # Reverse insertion order so that ordering is properly preserved.
        for current_part in reversed(parts_to_insert[i].elements):
            new_parts.insert(i + 1, current_part)

        # Remove the exploded part.
        new_parts.pop(i)

    # Store the new parts back as a tuple.
    score.elements = tuple(new_parts)


def scan_score_for_number_of_voices(score):
    """
    Scans the entire score to determine how many voices there are.
    :param score: Score
    :rtype: int
    :return: The number of parts in the score.
    """

    number_of_parts = 0

    for part in score.parts:
        voices_in_part = 0
        for current_measure in part.getElementsByClass(stream.Measure):
            voices_in_measure = len(current_measure.voices)

            # If there is only 1 voice, then we have 0 voice objects.
            if voices_in_measure == 0:
                voices_in_measure = 1

            voices_in_part = max(voices_in_part, voices_in_measure)
        number_of_parts += voices_in_part

    return number_of_parts


def convert_score_to_vmf(score):
    """
    Converts a MIDI file to an vmf file.
    :type score: Score
    :param score: The input score stream to convert.
    :rtype: list
    :return: A list of tuples representing the music contained in the MIDI file.
    """

    # Mapping of music21 id to vmf ids
    id_map = {}

    # The smallest duration covered. Expressed as a percentage of a quarter note.
    smallest_note = scan_score_durations(score)

    # The number of notes in largest chord in the file.
    largest_chord = scan_score_for_largest_chord(score)

    # Find number of parts for header.
    number_of_parts = len(score.parts)

    convert_voices_to_parts(score, id_map)

    tie_active = False

    parts = []

    for part in score.parts:
        pitches = []
        for element in part.flat:
            if isinstance(element, note.Note):

                n_frames = element.duration.quarterLength / smallest_note

                for i in range(int(n_frames)):

                    dynamic = DynamicConverter.velocity_to_vmf(element.volume.velocity)

                    if i == 0:
                        if not tie_active:
                            pitches.append([1, dynamic, 0, element.pitchClass, element.octave])
                        else:
                            pitches.append([2, dynamic, 0, element.pitchClass, element.octave])

                        # Pad remaining note positions for chords smaller than largest.
                        for i in range(largest_chord - 1):
                            pitches[-1].append(-1)
                            pitches[-1].append(-1)

                        # Finally, add the part id.
                        pitches[-1].append(id_map[part.id])

                        # a tie can only begin or end at a new note.
                        if element.tie is not None and element.tie.type == 'start':
                            tie_active = True
                        else:
                            tie_active = False
                    else:
                        pitches.append([2, dynamic, 0, element.pitchClass, element.octave])

                        # Pad remaining note positions for chords smaller than largest.
                        for i in range(largest_chord - 1):
                            pitches[-1].append(-1)
                            pitches[-1].append(-1)

                        # Add the part id
                        pitches[-1].append(id_map[part.id])

            elif isinstance(element, chord.Chord):
                n_frames = element.duration.quarterLength / smallest_note

                for i in range(int(n_frames)):

                    dynamic = DynamicConverter.velocity_to_vmf(element.volume.velocity)

                    if i == 0:
                        if not tie_active:
                            current_chord = [1, dynamic, 0]

                            # add in each pitch.
                            for pitch in element.pitches:
                                current_chord.append(pitch.pitchClass)
                                current_chord.append(pitch.octave)

                            # Pad remaining note positions for chords smaller than largest.
                            for i in range(largest_chord - element.multisetCardinality):
                                current_chord.append(-1)
                                current_chord.append(-1)

                            # Add the part id.
                            current_chord.append(id_map[part.id])

                            pitches.append(current_chord)
                        else:
                            current_chord = [2, dynamic, 0]

                            # add in each pitch.
                            for pitch in element.pitches:
                                current_chord.append(pitch.pitchClass)
                                current_chord.append(pitch.octave)

                            # Pad remaining note positions for chords smaller than largest.
                            for i in range(largest_chord - element.multisetCardinality):
                                current_chord.append(-1)
                                current_chord.append(-1)

                            # Add the part id.
                            current_chord.append(id_map[part.id])

                            pitches.append(current_chord)

                        # a tie can only begin or end at a new chord.
                        if element.tie is not None and element.tie.type == 'start':
                            tie_active = True
                        else:
                            tie_active = False
                    else:
                        current_chord = [2, dynamic, 0]

                        # add in each pitch.
                        for pitch in element.pitches:
                            current_chord.append(pitch.pitchClass)
                            current_chord.append(pitch.octave)

                        # Pad remaining note positions for chords smaller than largest.
                        for i in range(largest_chord - element.multisetCardinality):
                            current_chord.append(-1)
                            current_chord.append(-1)

                        # add the part id.
                        current_chord.append(id_map[part.id])

                        pitches.append(current_chord)

            elif isinstance(element, note.Rest):
                n_frames = element.duration.quarterLength / smallest_note

                for i in range(int(n_frames)):
                    pitches.append([0, 0, 0])

                    # Pad remaining note positions:
                    for i in range(largest_chord - 1):
                        pitches[-1].append(0)
                        pitches[-1].append(0)

                    # Finally add the part id.
                    pitches[-1].append(id_map[part.id])

        parts.append(pitches)

    vmf_file = {u'header': {}, u'body': [list(tick) for tick in zip(*parts)]}

    # Prepare the header.
    # Get a string of the fraction representation.
    # Limiting the denominator to get clean values (ie 1/3). The
    # limit of 64 ends up being a 256th note which is never really used.
    vmf_file['header']['tick_value'] = str(Fraction(smallest_note).limit_denominator(64))
    vmf_file['header']['number_of_voices'] = scan_score_for_number_of_voices(score)
    vmf_file['header']['number_of_parts'] = number_of_parts
    vmf_file['header']['time_signature'] = {}

    # Get the time signatures.
    for time_signature in score.flat.getElementsByClass(meter.TimeSignature):
        vmf_file['header']['time_signature'][str(time_signature.offset)] = time_signature.ratioString

    vmf_file['header']['key_signature'] = {}

    # Get the key signatures
    for key_signature in score.flat.getElementsByClass(key.KeySignature):
        vmf_file['header']['key_signature'][str(key_signature.offset)] = key_signature.sharps

    return vmf_file
