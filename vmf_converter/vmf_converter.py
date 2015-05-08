"""Bi-directional converter for the vector music format (VMF)."""
from music21.converter.subConverters import SubConverter
import vmf_converter.core.vmf_converter_core as vmf_converter_core

class VMFConverter(SubConverter):
    """Converter for parsing and writing VMF files."""
    registerFormats = ('vmf',)
    registerInputExtensions = ('vmf',)
    registerOutputExtensions = ('vmf', '.vmf',)

    def parseData(self, strData, number=None):
        """Parses a string containing VMF data into a music21 stream."""
        self.stream = vmf_converter_core.read_vmf_string(strData)

    def parseFile(self, filePath, number=None):
        """Parses a file containing VMF data into a music21 stream."""
        self.stream = vmf_converter_core.read_vmf_file(filePath)
    
    def write(self, obj, fmt, fp=None, subformats=None, **keywords):
        """Writes the music21 stream to a VMF file."""
        dataStr = vmf_converter_core.convert_score_to_vmf(obj)
        self.writeDataStream(fp, dataStr)
        return fp