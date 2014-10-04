import unittest

from nmf_converter_core import nmf_converter

class NMFConverterTest(unittest.TestCase):
  """Test Class for nmf_converter module"""

  def test_parse_cl_args_no_output(self):
      """
      Tests the commandline parser.
      No output file is specified.
      """
      args = nmf_converter.parse_cl_args(['input.midi'])

      assert args.input_file == 'input.midi'
      assert args.output_file == None

  def test_parse_cl_args_with_output(self):
      """
      Tests the commandline parser.
      An output file is specified.
      """
      args = nmf_converter.parse_cl_args(['input.midi', 'output.nmf'])

      assert args.input_file == 'input.midi'
      assert args.output_file == 'output.nmf'

  def test_determine_source_format(self):
      """
      Tests the extraction of file extensions.
      """
      file_extension = nmf_converter.determine_source_format('/foo/bar/myFile.nmf')

      assert file_extension == '.nmf'