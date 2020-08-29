from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:

    def __init__(self, title: str, release_year: int):

        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()

        if release_year < 1900 or type(release_year) is not int:
            self.__release_year = None
        else:
            self.__release_year = release_year
        self.director = None
        self.description = ""
        self.actors = []
        self.genres = []
        self.__runtime_minutes = 1

    @property
    def title(self) -> str:
        return self.__title

    def release_year(self) -> int:
        return self.__release_year

    def director(self) -> Director:
        return self.director

    def description(self) -> str:
        return self.description

    def actors(self) -> list:
        return self.actors

    def genres(self) -> list:
        return self.genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, x):
        if x < 1:
            raise ValueError("not positive runtime")

        self.__runtime_minutes = x

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        test1 = self.__title
        test2 = other.__title
        if test1 == test2:
            test3 = self.__release_year
            test4 = other.__release_year
            if test3 == test4:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        test1 = self.__title
        test2 = other.__title
        test3 = self.__release_year
        test4 = other.__release_year
        if test1 == test2:
            return test3 < test4
        else:
            return test1 < test2

    def __hash__(self):
        return hash((self.__title, self.__release_year))

    def add_actor(self, actor1):
        if type(actor1) is Actor:
            if actor1 not in self.actors:
                self.actors.append(actor1)

    def remove_actor(self, actor1):
        if actor1 in self.actors:
            self.actors.remove(actor1)

    def add_genre(self, genre1):
        if type(genre1) is Genre:
            if genre1 not in self.genres:
                self.genres.append(genre1)

    def remove_genre(self, genre1):
        if genre1 in self.genres:
            self.genres.remove(genre1)
