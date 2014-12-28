import json

from Genre import Genre


class LoadGenres(object):
    def __init__(self):
        with open("Data/Genres.json") as f:
            data = json.load(f)
            self.__data = data["genres"]

    def get(self):
        genres = []
        for item in self.__data:
            genres.append(self.__build_genre(item))
        return genres

    def __build_genre(self, item):
        genre = Genre()
        genre.name = item["name"]
        genre.description = item["description"]
        return genre
