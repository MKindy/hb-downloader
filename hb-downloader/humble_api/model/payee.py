from base_model import BaseModel

__author__ = "Joel Pedraza"
__copyright__ = "Copyright 2014, Joel Pedraza"
__license__ = "MIT"


class Payee(BaseModel):
    """
        Represents the recipient of funds for a given application.

        Example Data:
            "payee": {"human_name": "O'Reilly", "machine_name": "oreilly"}
            "payee": {"human_name": "Pasta Games", "machine_name": "pastagames"}
            "payee": {"human_name": "Humble Bundle, Inc", "machine_name": "humblebundle"}

        human_name:  The human readable name of the payee.
        machine_name:  The name of the payee usable on a PC.
    """

    def __init__(self, data):
        """
            Parameterized constructor for the Payee object.

            :param data: The JSON data to define the object with.
        """
        super(Payee, self).__init__(data)

        self.human_name = data.get("human_name", None)
        self.machine_name = data.get("machine_name", None)

    def __repr__(self):
        """ Representation of the current Payee object. """
        return "Payee: <%s>" % self.machine_name
