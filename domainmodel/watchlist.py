from domainmodel.movie import Movie
from domainmodel.user import User


class WatchList:

    def __init__(self, user: User):
        self.__watch_list = []
        self.__user = user

    @property
    def user(self) -> User:
        return self.__user

    def __repr__(self):
        return f"<WatchList {self.__watch_list}>"
    
    # watchlist set to a user, user then adds to watchlist
    def add_to_watchlist(self, movie: Movie):
        if movie not in self.__watch_list:
            self.__watch_list.append(movie)
    
    def watched_movie(self, movie):
        if movie in self.__watch_list:
            self.__watch_list.remove(movie)
    
    def length(self):
        return len(self.__watch_list)
