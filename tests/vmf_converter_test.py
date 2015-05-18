import unittest
import json

from music21 import converter
from music21 import duration
from music21.chord import Chord
from music21.meter import TimeSignature
from music21.note import Note, Rest
from music21.key import KeySignature
from music21.tempo import MetronomeMark

from vmf_converter.core import vmf_converter_core


class vmfConverterTest(unittest.TestCase):
    """Test Class for vmf_converter_core module"""

    def test_convert_score_to_vmf_001(self):
        """
        Tests the conversion of a score stream to an vmf data structure.
        """
        score = converter.parse('./fixtures/simple.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./expected/simple.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_002(self):
        """
        Tests the conversion of a score stream with ties to a vmf data structure.
        """
        score = converter.parse('./fixtures/ties.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./expected/ties.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_003(self):
        """
        Tests the conversion of a score stream with triplets to a vmf data structure.
        """
        score = converter.parse('./fixtures/triplets.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./expected/triplets.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_004(self):
        """
        Tests the conversion of a score stream with duplets to a vmf data structure.
        """
        score = converter.parse('./fixtures/duplets.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./expected/duplets.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_005(self):
        """
        Tests the conversion of a score stream with quintuplets to a vmf data structure.
        """
        score = converter.parse('./fixtures/quintuplets.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./expected/quintuplets.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_006(self):
        """
        Tests the conversion of a score stream with a simple to simple meter change to a vmf data structure.
        """
        score = converter.parse('./fixtures/SimpleToSimple.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./expected/SimpleToSimple.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)
            print(actual)
            assert expected == actual

    def test_convert_score_to_vmf_007(self):
        """
        Tests the conversion of a score stream with a compound to compound meter change to a vmf data structure.
        """
        score = converter.parse('./fixtures/CompoundToCompound.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./expected/CompoundToCompound.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)
            print(actual)
            assert expected == actual

    def test_convert_score_to_vmf_008(self):
        """
        Tests the conversion of a score stream with a simple to compound meter change to a vmf data structure.
        """
        score = converter.parse('./fixtures/SimpleToCompound.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./expected/SimpleToCompound.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_009(self):
        """
        Tests the conversion of a score stream with a compound to simple meter change to a vmf data structure.
        """
        score = converter.parse('./fixtures/CompoundToSimple.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./expected/CompoundToSimple.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_010(self):
        """
        Tests the conversion of a score stream with chords to a vmf data structure.
        """
        score = converter.parse('./fixtures/chords.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./expected/chords.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_011(self):
        """
        Tests the conversion of a score stream with multiple voices to a vmf data structure.
        """
        score = converter.parse('./fixtures/voices.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./expected/voices.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_012(self):
        """
        Tests the conversion of a score stream with dynamics to a vmf data structure.
        """
        score = converter.parse('./fixtures/dynamics.mid')
        first_phrase = score.measures(0, 5)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./expected/dynamics.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_013(self):
        """
        Tests the conversion of a score stream with dynamics to a vmf data structure.
        """
        score = converter.parse('./fixtures/dottedQuarter.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./expected/dottedQuarter.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_014(self):
        """
        Tests a key signature change.
        """
        score = converter.parse('./fixtures/keyChange.mid')

        actual = vmf_converter_core.convert_score_to_vmf(score)

        with open('./expected/keyChange.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_015(self):
        """
        Tests a tempo change.
        """
        score = converter.parse('./fixtures/tempoChange.mid')

        actual = vmf_converter_core.convert_score_to_vmf(score)

        with open('./expected/tempoChange.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_016(self):
        """
        Tests an explicit anacrusis.
        """
        score = converter.parse('./fixtures/anacrusis2.xml')

        actual = vmf_converter_core.convert_score_to_vmf(score)

        with open('./expected/anacrusis.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_017(self):
        """
        Tests the conversion of a score stream with chords and sustained notes..
        """
        score = converter.parse('./fixtures/chordsAndSustain.xml')

        actual = vmf_converter_core.convert_score_to_vmf(score)

        with open('./expected/chordsAndSustain.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_scan_score_durations_001(self):
        """
        Tests the scanning function which pre-analyzes the score to determine the
        smallest necessary note value to accurately encode the score as a vmf.
        """
        score = converter.parse('./fixtures/aus_meines_herz.mid')
        shortest_duration = vmf_converter_core.scan_score_durations(score)

        assert shortest_duration == duration.convertTypeToQuarterLength('eighth')

    def test_scan_score_for_largest_chord_001(self):
        """
        Tests the scanning function which pre-analyzes the score to determine the
        largest chord size.
        """

        score = converter.parse('./fixtures/chords.mid')
        largest_chord_size = vmf_converter_core.scan_score_for_largest_chord(score)

        assert largest_chord_size == 3

    def test_scan_score_for_number_of_voices_001(self):
        """
        Tests the scanning function which pre-analyzes the score to determine the
        number of voices in each part.
        """

        score = converter.parse('./fixtures/voices.mid')
        first_phrase = score.measures(0, 2)
        number_of_parts = vmf_converter_core.scan_score_for_number_of_voices(first_phrase)

        assert number_of_parts == 3

    def test_convert_vmf_to_midi_001(self):
        """
        Tests the conversion of a simple vmf file to a midi file.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/simple.vmf')
        expected_score = converter.parse('./fixtures/simple.mid')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements, actual.flat.notesAndRests.elements):
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

    def test_convert_vmf_to_midi_002(self):
        """
        Tests the conversion of a vmf file with ties to a midi file.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/ties.vmf')
        expected_score = converter.parse('./fixtures/ties.mid')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements, actual.flat.notesAndRests.elements):
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

    def test_convert_vmf_to_midi_003(self):
        """
        Tests the conversion of a vmf file with rhythmic dots to a midi file.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/dottedQuarter.vmf')
        expected_score = converter.parse('./fixtures/dottedQuarter.mid')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements, actual.flat.notesAndRests.elements):
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

    def test_convert_vmf_to_midi_004(self):
        """
        Tests the conversion of a vmf file with triplets to a midi file.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/triplets.vmf')
        expected_score = converter.parse('./fixtures/triplets.mid')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements, actual.flat.notesAndRests.elements):
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

    def test_convert_vmf_to_midi_005(self):
        """
        Tests the conversion of a vmf file with duplets to a midi file.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/duplets.vmf')
        expected_score = converter.parse('./fixtures/duplets.mid')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements, actual.flat.notesAndRests.elements):
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

    def test_convert_vmf_to_midi_006(self):
        """
        Tests the conversion of a vmf file with a simple to simple meter change to a midi file.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/SimpleToSimple.vmf')
        expected_score = converter.parse('./fixtures/SimpleToSimple.mid')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements, actual.flat.notesAndRests.elements):
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

        # Check that the time signatures are encoded.
        expected_time_signatures = expected_score.flat.getElementsByClass(TimeSignature)
        actual_time_signatures = actual_score.flat.getElementsByClass(TimeSignature)

        # Ensure we have the right number of time signatures.
        assert len(expected_time_signatures) == len(actual_time_signatures)

        for expected, actual in zip(expected_time_signatures, actual_time_signatures):
            assert expected.ratioString == actual.ratioString
            assert expected.offset == actual.offset

    def test_convert_vmf_to_midi_007(self):
        """
        Tests the conversion of a vmf file with a compound to compound meter change to a midi file.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/CompoundToCompound.vmf')
        expected_score = converter.parse('./fixtures/CompoundToCompound.mid')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements, actual.flat.notesAndRests.elements):
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

        # Check that the time signatures are encoded.
        expected_time_signatures = expected_score.flat.getElementsByClass(TimeSignature)
        actual_time_signatures = actual_score.flat.getElementsByClass(TimeSignature)

        # Ensure we have the right number of time signatures.
        assert len(expected_time_signatures) == len(actual_time_signatures)

        for expected, actual in zip(expected_time_signatures, actual_time_signatures):
            assert expected.ratioString == actual.ratioString
            assert expected.offset == actual.offset

    def test_convert_vmf_to_midi_008(self):
        """
        Tests the conversion of a vmf file with a simple to compound meter change to a midi file.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/SimpleToCompound.vmf')
        expected_score = converter.parse('./fixtures/SimpleToCompound.mid')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements, actual.flat.notesAndRests.elements):
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

        # Check that the time signatures are encoded.
        expected_time_signatures = expected_score.flat.getElementsByClass(TimeSignature)
        actual_time_signatures = actual_score.flat.getElementsByClass(TimeSignature)

        # Ensure we have the right number of time signatures.
        assert len(expected_time_signatures) == len(actual_time_signatures)

        for expected, actual in zip(expected_time_signatures, actual_time_signatures):
            assert expected.ratioString == actual.ratioString
            assert expected.offset == actual.offset

    def test_convert_vmf_to_midi_009(self):
        """
        Tests the conversion of a vmf file with a compound to simple meter change to a midi file.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/CompoundToSimple.vmf')
        expected_score = converter.parse('./fixtures/CompoundToSimple.mid')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements, actual.flat.notesAndRests.elements):
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

        # Check that the time signatures are encoded.
        expected_time_signatures = expected_score.flat.getElementsByClass(TimeSignature)
        actual_time_signatures = actual_score.flat.getElementsByClass(TimeSignature)

        # Ensure we have the right number of time signatures.
        assert len(expected_time_signatures) == len(actual_time_signatures)

        for expected, actual in zip(expected_time_signatures, actual_time_signatures):
            assert expected.ratioString == actual.ratioString
            assert expected.offset == actual.offset

    def test_convert_vmf_to_midi_010(self):
        """
        Tests the conversion of a vmf file with chords to a midi file.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/chords.vmf')
        expected_score = converter.parse('./fixtures/chords.mid')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements, actual.flat.notesAndRests.elements):
                if type(expected_element) is Chord:
                    assert len(expected_element.pitches) == len(actual_element.pitches)
                    assert expected_element.quarterLength == actual_element.quarterLength
                    for actual_pitch, expected_pitch in zip(expected_element.pitches, actual_element.pitches):
                        assert expected_pitch.pitchClass == actual_pitch.pitchClass
                        assert expected_pitch.octave == actual_pitch.octave
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

        # Check that the time signatures are encoded.
        expected_time_signatures = expected_score.flat.getElementsByClass(TimeSignature)
        actual_time_signatures = actual_score.flat.getElementsByClass(TimeSignature)

        # Ensure we have the right number of time signatures.
        assert len(expected_time_signatures) == len(actual_time_signatures)

        for expected, actual in zip(expected_time_signatures, actual_time_signatures):
            assert expected.ratioString == actual.ratioString
            assert expected.offset == actual.offset

    def test_convert_vmf_to_midi_011(self):
        """
        Tests the conversion of a vmf file with multiple voices to a midi file.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/voices.vmf')
        expected_score = converter.parse('./fixtures/voices.mid')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements, actual.flat.notesAndRests.elements):
                if type(expected_element) is Chord:
                    assert len(expected_element.pitches) == len(actual_element.pitches)
                    assert expected_element.quarterLength == actual_element.quarterLength
                    for actual_pitch, expected_pitch in zip(expected_element.pitches, actual_element.pitches):
                        assert expected_pitch.pitchClass == actual_pitch.pitchClass
                        assert expected_pitch.octave == actual_pitch.octave
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

    def test_convert_vmf_to_midi_012(self):
        """
        Tests the conversion of a vmf file with dynamics to a midi file.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/dynamics.vmf')
        expected_score = converter.parse('./fixtures/dynamics.mid')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements, actual.flat.notesAndRests.elements):
                if type(expected_element) is Chord:
                    assert len(expected_element.pitches) == len(actual_element.pitches)
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.volume.velocity == actual_element.volume.velocity
                    for actual_pitch, expected_pitch in zip(expected_element.pitches, actual_element.pitches):
                        assert expected_pitch.pitchClass == actual_pitch.pitchClass
                        assert expected_pitch.octave == actual_pitch.octave
                elif type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                    assert expected_element.volume.velocity == actual_element.volume.velocity
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

    def test_convert_vmf_to_midi_013(self):
        """
        Tests a key signature change.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/keyChange.vmf')
        expected_score = converter.parse('./fixtures/keyChange.mid')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements,
                                                        actual.flat.notesAndRests.elements):
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

        # Check that the key signatures are encoded.
        expected_key_signatures = expected_score.flat.getElementsByClass(KeySignature)
        actual_key_signatures = actual_score.flat.getElementsByClass(KeySignature)

        # Ensure we have the right number of key signatures.
        assert len(expected_key_signatures) == len(actual_key_signatures)

        for expected, actual in zip(expected_key_signatures, actual_key_signatures):
            assert expected.sharps == actual.sharps
            assert expected.offset == actual.offset

    def test_convert_vmf_to_midi_014(self):
        """
        Tests a tempo change.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/tempoChange.vmf')
        expected_score = converter.parse('./fixtures/tempoChange.mid')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements,
                                                        actual.flat.notesAndRests.elements):
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

        # Check that the tempos are encoded.
        expected_tempos = expected_score.flat.getElementsByClass(MetronomeMark)
        actual_tempos = actual_score.flat.getElementsByClass(MetronomeMark)

        # Ensure we have the right number of tempos.
        assert len(expected_tempos) == len(actual_tempos)

        for expected, actual in zip(expected_tempos, actual_tempos):
            assert expected.number == actual.number
            assert expected.offset == actual.offset

    def test_read_vmf_string_001(self):
        """
        Tests reading a VMF file with articulations
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/articulation.vmf')
        expected_score = converter.parse('./fixtures/articulation.xml')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements,
                                                        actual.flat.notesAndRests.elements):
                if type(expected_element) is Chord:
                    assert len(expected_element.pitches) == len(actual_element.pitches)
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.volume.velocity == actual_element.volume.velocity
                    for actual_pitch, expected_pitch in zip(expected_element.pitches, actual_element.pitches):
                        assert expected_pitch.pitchClass == actual_pitch.pitchClass
                        assert expected_pitch.octave == actual_pitch.octave
                elif type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                    # Equality on articulations is not well implemented in music21.
                    for a, b in zip(expected_element.articulations, actual_element.articulations):
                        assert type(a) == type(b)
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

    def test_read_vmf_string_002(self):
        """
        Tests reading a VMF file with a pickup measure.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/anacrusis.vmf')
        expected_score = converter.parse('./fixtures/anacrusis.xml')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements,
                                                        actual.flat.notesAndRests.elements):
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

    def test_read_vmf_string_003(self):
        """
        Tests reading a VMF file with a pickup and a measure of rests.
        """
        actual_score = vmf_converter_core.read_vmf_file('./expected/anacrusisAndRests.vmf')
        expected_score = converter.parse('./fixtures/anacrusisAndRests.xml')

        # Assert that the file has the right number of parts.
        assert len(expected_score.parts) == len(actual_score.parts)

        # Assert that the notes and rests match
        for expected, actual in zip(expected_score.parts, actual_score.parts):
            for expected_element, actual_element in zip(expected.flat.notesAndRests.elements,
                                                        actual.flat.notesAndRests.elements):
                if type(expected_element) is Note:
                    assert expected_element.quarterLength == actual_element.quarterLength
                    assert expected_element.pitch.pitchClass == actual_element.pitch.pitchClass
                    assert expected_element.pitch.octave == actual_element.pitch.octave
                elif type(expected_element) is Rest:
                    assert expected_element.quarterLength == actual_element.quarterLength

    def test_find_number_of_notes_in_tick_001(self):
        """
        Tests finding the number of notes in a tick
        """
        tick = [1,-1,0,0,4,-1,-1,-1,-1,0]

        number_of_notes = vmf_converter_core.find_number_of_notes_in_tick(tick)

        assert number_of_notes == 1

    def test_find_number_of_notes_in_tick_002(self):
        """
        Tests finding the number of notes in a tick
        """
        tick = [1,-1,0,0,4,0,0,-1,-1,0]

        number_of_notes = vmf_converter_core.find_number_of_notes_in_tick(tick)

        assert number_of_notes == 2