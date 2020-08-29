from datetime import datetime

from domainmodel.movie import Movie


class Review:
    
    def __init__(self, movie: Movie, review_text: str, rating: int):
        if movie == "" and type(movie) is not str:
            self.__movie = None
        else:
            self.__movie = movie
        if review_text == "" and type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text = review_text
        if rating < 1 or rating > 10:
            self.__rating = None
        else:
            self.__rating = rating
        now = datetime.now()
        self.__timestamp = datetime.timestamp(now)
    
    @property
    def movie(self) -> Movie:
        return self.__movie
        
    @property
    def review_text(self) -> str:
        return self.__review_text
        
    @property
    def rating(self) -> int:
        return self.__rating
        
    @property
    def timestamp(self) -> float:
        return self.__timestamp
    
    def __eq__(self, other):
        if self.__movie == other.__movie:
            if self.__review_text == other.__review_text:
                if self.__rating == other.__rating:
                    if self.__timestamp == other.__timestamp:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __repr__(self):
        return ""
