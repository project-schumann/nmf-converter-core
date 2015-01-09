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

  def test_convert_score_to_vmf(self):
      """
      Tests the conversion of a score stream to an vmf data structure.
      """
      score = converter.parse('./tests/fixtures/aus_meines_herz.mid')
      first_phrase = score.measures(0, 8)

      actual = vmf_converter.convert_score_to_vmf(first_phrase)
      
      with open('./tests/expected/aus_meines_herz.vmf', 'r') as expected_file:
          expected_json = expected_file.read()
          expected = json.loads(expected_json)

          assert expected == actual
          
  def test_scan_score_for_shortest_duration(self):
    """
    Tests the scanning function which pre-analyzes the score to determine the
    smallest necessary note value to accurately encode the score as a vmf.
    """
    score = converter.parse('./tests/fixtures/aus_meines_herz.mid')
    shortest_duration = vmf_converter.scan_score_for_shortest_duration(score)
    
    assert shortest_duration == duration.convertTypeToQuarterLength('eighth')