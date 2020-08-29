class Genre:

    def __init__(self, genrename: str):
        if genrename == "" or type(genrename) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genrename.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        test1 = self.__genre_name
        test2 = other.__genre_name
        return test1 == test2

    def __lt__(self, other):
        test1 = self.__genre_name
        test2 = other.__genre_name
        return test1 < test2

    def __hash__(self):
        return 0
