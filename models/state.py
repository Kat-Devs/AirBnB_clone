"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.
    Attributes:
        name (str): The name of the state.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize User instance """
        super().__init__(*args, **kwargs)