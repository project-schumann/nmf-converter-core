import unittest
from nose.tools import raises
from vmf_converter_core.dynamic_converter import DynamicConverter


class DynamicConverterTest(unittest.TestCase):
    """Test Class for DynamicConverter module"""

    def test_velocity_to_vmf_001(self):
        """
        Tests the Velocity to VMF conversion for pppp dynamic.
        """
        assert DynamicConverter.velocity_to_vmf(5) == -5

    def test_velocity_to_vmf_002(self):
        """
        Tests the Velocity to VMF conversion for ppp dynamic.
        """
        assert DynamicConverter.velocity_to_vmf(15) == -4

    def test_velocity_to_vmf_003(self):
        """
        Tests the Velocity to VMF conversion for pp dynamic.
        """
        assert DynamicConverter.velocity_to_vmf(30) == -3

    def test_velocity_to_vmf_004(self):
        """
        Tests the Velocity to VMF conversion for p dynamic.
        """
        assert DynamicConverter.velocity_to_vmf(45) == -2

    def test_velocity_to_vmf_005(self):
        """
        Tests the Velocity to VMF conversion for mp dynamic.
        """
        assert DynamicConverter.velocity_to_vmf(55) == -1

    def test_velocity_to_vmf_006(self):
        """
        Tests the Velocity to VMF conversion for mf dynamic.
        """
        assert DynamicConverter.velocity_to_vmf(66) == 1

    def test_velocity_to_vmf_007(self):
        """
        Tests the Velocity to VMF conversion for f dynamic.
        """
        assert DynamicConverter.velocity_to_vmf(80) == 2

    def test_velocity_to_vmf_008(self):
        """
        Tests the Velocity to VMF conversion for ff dynamic.
        """
        assert DynamicConverter.velocity_to_vmf(95) == 3

    def test_velocity_to_vmf_009(self):
        """
        Tests the Velocity to VMF conversion for fff dynamic.
        """
        assert DynamicConverter.velocity_to_vmf(105) == 4

    def test_velocity_to_vmf_010(self):
        """
        Tests the Velocity to VMF conversion for ffff dynamic.
        """
        assert DynamicConverter.velocity_to_vmf(120) == 5

    @raises(ValueError)
    def test_velocity_to_vmf_011(self):
        """
        Tests the Velocity to VMF conversion for a lower extreme bound.
        """
        DynamicConverter.velocity_to_vmf(-5)

    @raises(ValueError)
    def test_velocity_to_vmf_012(self):
        """
        Tests the Velocity to VMF conversion for a upper extreme bound
        """
        DynamicConverter.velocity_to_vmf(150)

    def test_vmf_to_velocity_001(self):
        """
        Tests the VMF to Velocity conversion for a pppp dynamic.
        """
        assert DynamicConverter.vmf_to_velocity(-5) == 10

    def test_vmf_to_velocity_002(self):
        """
        Tests the VMF to Velocity conversion for a ppp dynamic.
        """
        assert DynamicConverter.vmf_to_velocity(-4) == 23

    def test_vmf_to_velocity_003(self):
        """
        Tests the VMF to Velocity conversion for a pp dynamic.
        """
        assert DynamicConverter.vmf_to_velocity(-3) == 36

    def test_vmf_to_velocity_004(self):
        """
        Tests the VMF to Velocity conversion for a p dynamic.
        """
        assert DynamicConverter.vmf_to_velocity(-2) == 49

    def test_vmf_to_velocity_005(self):
        """
        Tests the VMF to Velocity conversion for a mp dynamic.
        """
        assert DynamicConverter.vmf_to_velocity(-1) == 62

    def test_vmf_to_velocity_006(self):
        """
        Tests the VMF to Velocity conversion for a mf dynamic.
        """
        assert DynamicConverter.vmf_to_velocity(1) == 75

    def test_vmf_to_velocity_007(self):
        """
        Tests the VMF to Velocity conversion for a f dynamic.
        """
        assert DynamicConverter.vmf_to_velocity(2) == 88

    def test_vmf_to_velocity_008(self):
        """
        Tests the VMF to Velocity conversion for a ff dynamic.
        """
        assert DynamicConverter.vmf_to_velocity(3) == 101

    def test_vmf_to_velocity_009(self):
        """
        Tests the VMF to Velocity conversion for a fff dynamic.
        """
        assert DynamicConverter.vmf_to_velocity(4) == 114

    def test_vmf_to_velocity_010(self):
        """
        Tests the VMF to Velocity conversion for a ffff dynamic.
        """
        assert DynamicConverter.vmf_to_velocity(5) == 127

    @raises(ValueError)
    def test_vmf_to_velocity_011(self):
        """
        Tests the VMF to Velocity conversion for a 0 dynamic (invalid).
        """
        DynamicConverter.vmf_to_velocity(0)