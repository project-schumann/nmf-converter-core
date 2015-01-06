import unittest

from music21 import converter
from nmf_converter_core import nmf_converter

class NMFConverterTest(unittest.TestCase):
  """Test Class for nmf_converter module"""

  def test_parse_cl_args_no_output(self):
      """
      Tests the commandline parser.
      No output file is specified.
      """
      args = nmf_converter.parse_cl_args(['input.mid'])

      assert args.input_file == 'input.mid'
      assert args.output_file is None

  def test_parse_cl_args_with_output(self):
      """
      Tests the commandline parser.
      An output file is specified.
      """
      args = nmf_converter.parse_cl_args(['input.mid', 'output.vmf'])

      assert args.input_file == 'input.mid'
      assert args.output_file == 'output.vmf'

  def test_determine_source_format(self):
      """
      Tests the extraction of file extensions.
      """
      file_extension = nmf_converter.determine_source_format('/foo/bar/myFile.vmf')

      assert file_extension == '.vmf'

  @unittest.skip("vmf file missing")
  def test_convert_score_to_nmf(self):
      """
      Tests the conversion of a score stream to an nmf data structure.
      """
      score = converter.parse('./tests/fixtures/aus_meines_herz.mid')
      vmf = str(nmf_converter.convert_score_to_nmf(score))

      with open('./tests/expected/aus_meines_herz.vmf', 'r') as expected_file:
          expected = expected_file.read()

          assert expected == vmf