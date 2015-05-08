import unittest
from music21.articulations import Staccato, Staccatissimo, StrongAccent, Accent, Tenuto
from vmf_converter.core.articulation_converter import ArticulationConverter


class ArticulationConverterTest(unittest.TestCase):
    """Test Class for ArticulationConverter module"""

    def test_articulation_to_vmf_001(self):
        """
        Tests the Articulation to VMF conversion for staccato articulation.
        """
        assert ArticulationConverter.articulation_to_vmf(Staccato()) == 3

    def test_articulation_to_vmf_002(self):
        """
        Tests the Articulation to VMF conversion for staccatissimo articulation.
        """
        assert ArticulationConverter.articulation_to_vmf(Staccatissimo()) == 4

    def test_articulation_to_vmf_003(self):
        """
        Tests the Articulation to VMF conversion for strong accent articulation.
        """
        assert ArticulationConverter.articulation_to_vmf(StrongAccent()) == 5

    def test_articulation_to_vmf_004(self):
        """
        Tests the Articulation to VMF conversion for accent articulation.
        """
        assert ArticulationConverter.articulation_to_vmf(Accent())== 6

    def test_articulation_to_vmf_005(self):
        """
        Tests the Articulation to VMF conversion for Tenuto articulation.
        """
        assert ArticulationConverter.articulation_to_vmf(Tenuto()) == 7

    def test_vmf_to_articulation_001(self):
        """
        Tests the VMF to Articulation conversion for staccato articulation.
        """
        assert type(ArticulationConverter.vmf_to_articulation(3)) == Staccato

    def test_vmf_to_articulation_002(self):
        """
        Tests the VMF to Articulation conversion for staccatissimo articulation.
        """
        assert type(ArticulationConverter.vmf_to_articulation(4)) == Staccatissimo

    def test_vmf_to_articulation_003(self):
        """
        Tests the VMF to Articulation conversion for strong accent articulation.
        """
        assert type(ArticulationConverter.vmf_to_articulation(5)) == StrongAccent

    def test_vmf_to_articulation_004(self):
        """
        Tests the VMF to Articulation conversion for accent articulation.
        """
        assert type(ArticulationConverter.vmf_to_articulation(6)) == Accent

    def test_vmf_to_articulation_005(self):
        """
        Tests the VMF to Articulation conversion for Tenuto articulation.
        """
        assert type(ArticulationConverter.vmf_to_articulation(7)) == Tenuto