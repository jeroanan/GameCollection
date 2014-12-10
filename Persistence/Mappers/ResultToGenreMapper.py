from Genre import Genre


class ResultToGenreMapper(object):

    def map(self, mongo_result):
        genre = Genre()
        genre.id = mongo_result["_id"]
        genre.name = mongo_result["_Genre__name"]
        genre.description = mongo_result["_Genre__description"]
        return genre