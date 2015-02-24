class DynamicConverter:
    """
    Converts between velocities and VMF dynamics.
    """

    __PPPP_VELOCITY = 10
    __PPP_VELOCITY = 23
    __PP_VELOCITY = 36
    __P_VELOCITY = 49
    __MP_VELOCITY = 62
    __MF_VELOCITY = 75
    __F_VELOCITY = 88
    __FF_VELOCITY = 101
    __FFF_VELOCITY = 114
    __FFFF_VELOCITY = 127

    __PPPP_MIN = 0
    __PPPP_MAX = 12
    __PPP_MIN = 13
    __PPP_MAX = 25
    __PP_MIN = 26
    __PP_MAX = 38
    __P_MIN = 39
    __P_MAX = 51
    __MP_MIN = 52
    __MP_MAX = 64
    __MF_MIN = 65
    __MF_MAX = 77
    __F_MIN = 78
    __F_MAX = 90
    __FF_MIN = 91
    __FF_MAX = 103
    __FFF_MIN = 104
    __FFF_MAX = 116
    __FFFF_MIN = 117
    __FFFF_MAX = 127

    @classmethod
    def velocity_to_vmf(cls, velocity):
        """
        Converts a midi velocity to a VMF dynamic symbol.
        :param velocity: The midi velocity.
        :rtype int: The corresponding value for VMF.
        :return: A value representing a dynamic in VMF.
        """
        if DynamicConverter.__PPPP_MIN <= velocity <= DynamicConverter.__PPPP_MAX:
            return -5
        elif DynamicConverter.__PPP_MIN <= velocity <= DynamicConverter.__PPP_MAX:
            return -4
        elif DynamicConverter.__PP_MIN <= velocity <= DynamicConverter.__PP_MAX:
            return -3
        elif DynamicConverter.__P_MIN <= velocity <= DynamicConverter.__P_MAX:
            return -2
        elif DynamicConverter.__MP_MIN <= velocity <= DynamicConverter.__MP_MAX:
            return -1
        elif DynamicConverter.__MF_MIN <= velocity <= DynamicConverter.__MF_MAX:
            return 1
        elif DynamicConverter.__F_MIN <= velocity <= DynamicConverter.__F_MAX:
            return 2
        elif DynamicConverter.__FF_MIN <= velocity <= DynamicConverter.__FF_MAX:
            return 3
        elif DynamicConverter.__FFF_MIN <= velocity <= DynamicConverter.__FFF_MAX:
            return 4
        elif DynamicConverter.__FFFF_MIN <= velocity <= DynamicConverter.__FFFF_MAX:
            return 5

    @classmethod
    def vmf_to_velocity(cls, vmf_value):
        """
        Converts a VMF dynamic value to a velocity.
        :param vmf_value: The dynamic value in VMF format.
        :rtype: int
        :return: The corresponding MIDI velocity value.
        """
        if vmf_value == -5:
            return DynamicConverter.__PPPP_VELOCITY
        elif vmf_value == -4:
            return DynamicConverter.__PPP_VELOCITY
        elif vmf_value == -3:
            return DynamicConverter.__PP_VELOCITY
        elif vmf_value == -2:
            return DynamicConverter.__P_VELOCITY
        elif vmf_value == -1:
            return DynamicConverter.__MP_VELOCITY
        elif vmf_value == 1:
            return DynamicConverter.__MF_VELOCITY
        elif vmf_value == 2:
            return DynamicConverter.__F_VELOCITY
        elif vmf_value == 3:
            return DynamicConverter.__FF_VELOCITY
        elif vmf_value == 4:
            return DynamicConverter.__FFF_VELOCITY
        elif vmf_value == 5:
            return DynamicConverter.__FFFF_VELOCITY