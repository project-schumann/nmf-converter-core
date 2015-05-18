from music21.articulations import Staccato, Staccatissimo, StrongAccent, Accent, Tenuto


class ArticulationConverter:
    """
    Converts between music21 and VMF articulations
    """

    @classmethod
    def articulation_to_vmf(cls, articulation):
        """
        Converts and articulation to a vmf articulation

        :param articulation: The music21 articulation
        :return: The vmf encoding
        """

        if type(articulation) is Staccato:
            return 3
        elif type(articulation) is Staccatissimo:
            return 4
        elif type(articulation) is StrongAccent:
            return 5
        elif type(articulation) is Accent:
            return 6
        elif type(articulation) is Tenuto:
            return 7
        else:
            raise ValueError("Articulation is not supported")

    @classmethod
    def vmf_to_articulation(cls, vmf):
        """
        Converts a vmf encoding to an articulation

        :param vmf: The vmf value
        :return: An articulation object.
        """

        if vmf == 0:
            return None
        elif vmf == 3:
            return Staccato()
        elif vmf == 4:
            return Staccatissimo()
        elif vmf == 5:
            return StrongAccent()
        elif vmf == 6:
            return Accent()
        elif vmf == 7:
            return Tenuto()
        else:
            raise ValueError("Articulation is not supported")
