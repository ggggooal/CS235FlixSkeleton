
class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        test1 = self.__director_full_name
        test2 = other.__director_full_name
        return test1 == test2

    def __lt__(self, other):
        test1 = self.__director_full_name
        test2 = other.__director_full_name
        return test1 < test2

    def __hash__(self):
        return 0


class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None


	
director1 = Director("Cameron Diaz")
director2 = Director("Angelina Jolie")
director3 = Director("Brad Pitt")
print(director1 > director2)
print(director1 > director3)
print(director2 < director3
