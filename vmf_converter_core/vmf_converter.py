"""Bi-directional converter for the vector music format (VMF)."""
from music21.converter.subConverters import SubConverter
from vmf_converter_core.converter import vmf_converter_core

class VMFConverter(SubConverter):
    """Converter for parsing and writing VMF files."""
    registerFormats = ('vmf',)
    registerInputExtensions = ('vmf',)
    registerOutputExtensions = ('vmf',)

    def parseData(self, strData, number=None):
        """Parses a string containing VMF data into a music21 stream."""
        self.stream = vmf_converter_core.read_vmf_string(strData)
        pass

    def parseFile(self, filePath, number=None):
        """Parses a file containing VMF data into a music21 stream."""
        self.stream = vmf_converter_core.read_vmf_file(filePath)
    