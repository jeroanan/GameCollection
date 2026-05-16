"""Load Genres from JSON file."""
import json
from genre import Genre

#TODO: Is this even used?

class LoadGenres:
    """Load Genres from JSON file."""

    def __init__(self):
        with open("Data/Genres.json", encoding="utf-8") as f:
            data = json.load(f)
            self.__data = data["genres"]

    def get(self):
        """Get list of Genres."""
        genres = []
        for item in self.__data:
            genres.append(self.__build_genre(item))
        return genres

    def __build_genre(self, genre_dict):
        """Build Genre from dictionary."""
        genre = Genre()
        genre.name = genre_dict["name"]
        genre.description = genre_dict["description"]
        return genre
