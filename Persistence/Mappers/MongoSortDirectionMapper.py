import pymongo


class MongoSortDirectionMapper(object):

    def map(self, sort_order):
        if sort_order is not None and sort_order.upper() == "DESC":
            return pymongo.DESCENDING
        return pymongo.ASCENDING