"""Bi-directional converter for the vector music format (VMF)."""
from music21 import converter, note, stream, meter
import vmf_converter.core.vmf_converter_core as vmf_converter_core

import json

class VMFConverter(converter.subConverters.SubConverter):
    """Converter for parsing and writing VMF files."""
    registerFormats = ('vmf',)
    registerInputExtensions = ('vmf',)
    registerOutputExtensions = ('vmf',)

    def parseData(self, strData, number=None):
        """Parses a string containing VMF data into a music21 stream."""
        self.stream = vmf_converter_core.read_vmf_string(strData)

    def parseFile(self, filePath, number=None):
        """Parses a file containing VMF data into a music21 stream."""
        self.stream = vmf_converter_core.read_vmf_file(filePath)
    
    def write(self, obj, fmt, fp=None, subformats=None, **keywords):
        """Writes the music21 stream to a VMF file."""
        vmfDict = vmf_converter_core.convert_score_to_vmf(obj)
        
        with open(fp, 'w') as f:
            f.write(json.dumps(vmfDict))
        
        return fp
