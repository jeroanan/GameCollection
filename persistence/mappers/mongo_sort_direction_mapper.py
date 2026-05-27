"""Mapper to convert sort direction from string to pymongo constant."""
import pymongo


class MongoSortDirectionMapper:
    """Mapper to convert sort direction from string to pymongo constant."""

    def map(self, sort_order: str) -> int:
        """Convert sort direction from string to pymongo constant."""
        if sort_order is not None and sort_order.upper() == "DESC":
            return pymongo.DESCENDING
        return pymongo.ASCENDING
