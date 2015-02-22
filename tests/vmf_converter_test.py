import unittest
import json

from music21 import converter
from music21 import duration
from vmf_converter_core import vmf_converter

class vmfConverterTest(unittest.TestCase):
    """Test Class for vmf_converter module"""

    def test_parse_cl_args_no_output(self):
        """
        Tests the commandline parser.
        No output file is specified.
        """
        args = vmf_converter.parse_cl_args(['input.mid'])

        assert args.input_file == 'input.mid'
        assert args.output_file is None

    def test_parse_cl_args_with_output(self):
        """
        Tests the commandline parser.
        An output file is specified.
        """
        args = vmf_converter.parse_cl_args(['input.mid', 'output.vmf'])

        assert args.input_file == 'input.mid'
        assert args.output_file == 'output.vmf'

    def test_determine_source_format(self):
        """
        Tests the extraction of file extensions.
        """
        file_extension = vmf_converter.determine_source_format('/foo/bar/myFile.vmf')

        assert file_extension == '.vmf'

    def test_convert_score_to_vmf_001(self):
        """
        Tests the conversion of a score stream to an vmf data structure.
        """
        score = converter.parse('./tests/fixtures/simple.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter.convert_score_to_vmf(first_phrase)

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

        actual = vmf_converter.convert_score_to_vmf(first_phrase)

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

        actual = vmf_converter.convert_score_to_vmf(first_phrase)

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

        actual = vmf_converter.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/duplets.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)
            print(actual)
            assert expected == actual

    def test_convert_score_to_vmf_005(self):
        """
        Tests the conversion of a score stream with quintuplets to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/quintupletest.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/quintuplets.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)
            print(actual)
            assert expected == actual

    def test_convert_score_to_vmf_006(self):
        """
        Tests the conversion of a score stream with a simple to simple meter change to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/SimpleToSimple.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/SimpleToSimple.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_007(self):
        """
        Tests the conversion of a score stream with a compound to compound meter change to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/CompoundToCompound.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/CompoundToCompound.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)

            assert expected == actual

    def test_convert_score_to_vmf_008(self):
        """
        Tests the conversion of a score stream with a simple to compound meter change to a vmf data structure.
        """
        score = converter.parse('./tests/fixtures/SimpleToCompound.mid')
        first_phrase = score.measures(0, 2)

        actual = vmf_converter.convert_score_to_vmf(first_phrase)

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

        actual = vmf_converter.convert_score_to_vmf(first_phrase)

        with open('./tests/expected/CompoundToSimple.vmf', 'r') as expected_file:
            expected_json = expected_file.read()
            expected = json.loads(expected_json)
            print(actual)
            assert expected == actual

    def test_scan_score_for_shortest_duration(self):
        """
        Tests the scanning function which pre-analyzes the score to determine the
        smallest necessary note value to accurately encode the score as a vmf.
        """
        score = converter.parse('./tests/fixtures/aus_meines_herz.mid')
        shortest_duration = vmf_converter.scan_score_for_shortest_duration(score)

        assert shortest_duration == duration.convertTypeToQuarterLength('eighth')