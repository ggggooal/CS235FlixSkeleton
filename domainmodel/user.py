from domainmodel.movie import Movie
from domainmodel.review import Review


class User:

    def __init__(self, user_name: str, password: str):
        self.__colleague_list = []
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            k = user_name.strip()
            k = user_name.lower()
            self.__user_name = k
        self.__password = password
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

        

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password
    
    @property
    def watched_movies(self) -> list:
        return self.__watched_movies
    
    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes
    
    @property
    def reviews(self) -> list\
            :
        return self.__reviews
    

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        test1 = self.__user_name
        test2 = other.__user_name
        return test1 == test2

    def __lt__(self, other):
        test1 = self.__user_name
        test2 = other.__user_name
        return test1 < test2

    def __hash__(self):
        return hash((self.__user_name, self.__password))
    
    def watch_movie(self, movie):
        self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes = self.__time_spent_watching_movies_minutes + movie.runtime_minutes
    
    def add_review(self, review):
        self.__reviews.append(review)