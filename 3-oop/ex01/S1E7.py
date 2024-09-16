from S1E9 import Character

class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True) -> None:
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

    def __repr__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __str__(self):
        return self.__repr__()

class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True) -> None:
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

    def __repr__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Your docstring for classmethod"""
        return cls(first_name, is_alive)

    def __str__(self):
        return self.__repr__()
