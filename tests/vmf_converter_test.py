import unittest
import json

from music21 import converter
from music21 import duration
from music21.chord import Chord
from music21.meter import TimeSignature
from music21.note import Note, Rest
from vmf_converter.core import vmf_converter_core

class vmfConverterTest(unittest.TestCase):
    """Test Class for vmf_converter_core module"""

    def test_convert_score_to_vmf_001(self):
        """
        Tests the conversion of a score stream to an vmf data structure.
        """
        score = converter.parse('./tests/fixtures/simple.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/simple.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_002(self):
        """
        Tests the conversion of a score stream with ties to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/ties.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/ties.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_003(self):
        """
        Tests the conversion of a score stream with triplets to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/triplets.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/triplets.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_004(self):
        """
        Tests the conversion of a score stream with duplets to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/duplets.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/duplets.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_005(self):
        """
        Tests the conversion of a score stream with quintuplets to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/quintuplets.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/quintuplets.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_006(self):
        """
        Tests the conversion of a score stream with a simple to simple meter change to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/SimpleToSimple.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/SimpleToSimple.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)
            print(actual)
            assert expected == actual

    def test_convert_score_to_vmf_007(self):
        """
        Tests the conversion of a score stream with a compound to compound meter change to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/CompoundToCompound.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/CompoundToCompound.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)
            print(actual)
            assert expected == actual

    def test_convert_score_to_vmf_008(self):
        """
        Tests the conversion of a score stream with a simple to compound meter change to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/SimpleToCompound.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/SimpleToCompound.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_009(self):
        """
        Tests the conversion of a score stream with a compound to simple meter change to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/CompoundToSimple.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/CompoundToSimple.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_010(self):
        """
        Tests the conversion of a score stream with chords to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/chords.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/chords.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_011(self):
        """
        Tests the conversion of a score stream with multiple voices to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/voices.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/voices.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_012(self):
        """
        Tests the conversion of a score stream with dynamics to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/dynamics.mid')
        first_phrase = score.measures(0, 5)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/dynamics.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_013(self):
        """
        Tests the conversion of a score stream with dynamics to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/dottedQuarter.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter_core.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/dottedQuarter.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_scan_score_durations_001(self):
        """
        Tests the scanning function which pre-analyzes the score to determine the
        smallest necessary note value to accurately encode the score as a vmf.
        """
        score = converter.parse('./tests/fixtures/aus_meines_herz.mid')
        shortest_duration = vmf_converter_core.scan_score_durations(score)

        assert shortest_duration == duration.convertTypeToQuarterLength('eighth')

    def test_scan_score_for_largest_chord_001(self):
        """
        Tests the scanning function which pre-analyzes the score to determine the
        largest chord size.
        """

        score = converter.parse('./tests/fixtures/chords.mid')
        largest_chord_size = vmf_converter_core.scan_score_for_largest_chord(score)

        assert largest_chord_size == 3

    def test_scan_score_for_number_of_voices_001(self):
        """
        Tests the scanning function which pre-analyzes the score to determine the
        number of voices in each part.
        """

        score = converter.parse('./tests/fixtures/voices.mid')
        first_phrase = score.measures(0, 2)
        number_of_parts = vmf_converter_core.scan_score_for_number_of_voices(first_phrase)

        assert number_of_parts == 3

    def test_convert_vmf_to_midi_001(self):
        """
        Tests the conversion of a simple vmf file to a midi file.
        """
        actual_score = vmf_converter_core.read_vmf_file('./tests/expected/simple.vmf')
        actual_score.write('midi', './tests/output/simple.mid')
        expected_score = converter.parse('./tests/fixtures/simple.mid')

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
        actual_score = vmf_converter_core.read_vmf_file('./tests/expected/ties.vmf')
        actual_score.write('midi', './tests/output/ties.mid')
        expected_score = converter.parse('./tests/fixtures/ties.mid')

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
        actual_score = vmf_converter_core.read_vmf_file('./tests/expected/dottedQuarter.vmf')
        actual_score.write('midi', './tests/output/dottedQuarter.mid')
        expected_score = converter.parse('./tests/fixtures/dottedQuarter.mid')

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
        actual_score = vmf_converter_core.read_vmf_file('./tests/expected/triplets.vmf')
        actual_score.write('midi', './tests/output/triplets.mid')
        expected_score = converter.parse('./tests/fixtures/triplets.mid')

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
        actual_score = vmf_converter_core.read_vmf_file('./tests/expected/duplets.vmf')
        actual_score.write('midi', './tests/output/duplets.mid')
        expected_score = converter.parse('./tests/fixtures/duplets.mid')

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
        actual_score = vmf_converter_core.read_vmf_file('./tests/expected/SimpleToSimple.vmf')
        actual_score.write('midi', './tests/output/SimpleToSimple.mid')
        expected_score = converter.parse('./tests/fixtures/SimpleToSimple.mid')

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
        actual_score = vmf_converter_core.read_vmf_file('./tests/expected/CompoundToCompound.vmf')
        actual_score.write('midi', './tests/output/CompoundToCompound.mid')
        expected_score = converter.parse('./tests/fixtures/CompoundToCompound.mid')

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
        actual_score = vmf_converter_core.read_vmf_file('./tests/expected/SimpleToCompound.vmf')
        actual_score.write('midi', './tests/output/SimpleToCompound.mid')
        expected_score = converter.parse('./tests/fixtures/SimpleToCompound.mid')

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
        actual_score = vmf_converter_core.read_vmf_file('./tests/expected/CompoundToSimple.vmf')
        actual_score.write('midi', './tests/output/CompoundToSimple.mid')
        expected_score = converter.parse('./tests/fixtures/CompoundToSimple.mid')

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
        actual_score = vmf_converter_core.read_vmf_file('./tests/expected/chords.vmf')
        actual_score.write('midi', './tests/output/chords.mid')
        expected_score = converter.parse('./tests/fixtures/chords.mid')

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
        actual_score = vmf_converter_core.read_vmf_file('./tests/expected/voices.vmf')
        actual_score.write('midi', './tests/output/voices.mid')
        expected_score = converter.parse('./tests/fixtures/voices.mid')

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
        actual_score = vmf_converter_core.read_vmf_file('./tests/expected/dynamics.vmf')
        actual_score.write('midi', './tests/output/dynamics.mid')
        expected_score = converter.parse('./tests/fixtures/dynamics.mid')

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