"""Provides persistence using MongoDB"""
# Copyright (c) 2015, 2026 David Wilson
# Icarus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Icarus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>.

import sys

from bson import ObjectId
from bson.errors import InvalidId
from logging import Logger
from typing import Any
from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.errors import ConnectionFailure

from data.config import Config
from genre import Genre
from hardware_type import HardwareType
from interactors.params.get_games_interactor_params import GetGamesInteractorParams
from interactors.params.get_hardware_list_interactor_params import GetHardwareListInteractorParams
from persistence.abstract_persistence import AbstractPersistence
from persistence.exceptions import GameNotFoundException, HardwareNotFoundException
from persistence.mappers.hardware_sort_field_mapper import HardwareSortFieldMapper
from persistence.mappers.mongo_sort_direction_mapper import MongoSortDirectionMapper
from persistence.mappers.sort_field_mapper import SortFieldMapper
from game import Game
from hardware import Hardware
import hardware_type as ht
from icarus_platform import Platform
from icarus_user import User

class MongoPersistence:
    """Provide persistence using MongoDB"""

    def __init__(self,
                 logger: Logger,
                 config : Config,
                 mongo_client: MongoClient[Any] = MongoClient()):
        """Initialise object state"""
        self.__client = None
        self.__config = config
        self.__logger = logger
        self.__mongo_client = mongo_client
        self.__client = self.__init_mongo_client()
        self.__db = self.__client.GamesCollection

    def __init_mongo_client(self) -> MongoClient[Any]:
        """Initialise the database connection."""
        try:
            mongo_url = self.__config.get_mongo_url()
            mongo_port = self.__config.get_mongo_port()
            if self.__mongo_client is None:
                self.__logger.info(f'Connecting to MongoDB at {mongo_url}')
                client = MongoClient(host=mongo_url, port=mongo_port, connect=True)
                self.__logger.info('Connected to MongoDB(?)')
            else:
                client = self.__mongo_client
        except ConnectionFailure:
            print("No instance of MongoDB detected. Did you forget to start it?")
            sys.exit(-1)
        return client

    def __del__(self) -> None:
        """Destructor. Make sure the connection to MongoDB is closed."""
        if self.__client is not None:
            self.__client.close()

    def add_game(self, game: Game, user_id: str) -> None:
        """Add a single game.
        :param params: An object of type Game
        :param user_id: The id of the current user (actual id rather than username)
        :returns: None
        """
        gd = game.__dict__
        gd["user_id"] = str(user_id)
        self.__db.games.insert_one(gd)

    def get_all_games(self, params: GetGamesInteractorParams) -> list[Game]:
        """Gets a list of games.
        :param params: An object of type GetGamesInteractorParams
        :returns: A list of Game
        """
        sorder = MongoSortDirectionMapper().map(params.sort_direction)
        mapped_sort_field = SortFieldMapper().map(params.sort_field)
        games = self.__db.games.find({"user_id": str(params.user_id)}, limit=params.number_of_games)
        return self.__map_games_list(games.sort(mapped_sort_field, sorder))

    def get_all_games_for_platform(self, params: GetGamesInteractorParams) -> list[Game]:
        """Gets a list of games for a platform.
        :param params: An object of type GetGamesInteractorParams
        :returns: A list of Game
        """
        sorder = MongoSortDirectionMapper().map(params.sort_direction)
        mapped_sort_field = SortFieldMapper().map(params.sort_field)
        games = self.__db.games.find(
            {"_Game__platform": params.platform, "user_id": str(params.user_id)},
            limit=params.number_of_games)
        return self.__map_games_list(games.sort(mapped_sort_field, sorder))

    def count_games(self, user_id: str) -> int:
        """Counts the games in the user's collection.
        :param user_id: The uuid of the current user.
        :returns: The number of games in the user's collection
        """
        return self.__db.games.count_documents({"user_id": str(user_id)})

    def count_hardware(self, user_id: str) -> int:
        """Counts the items of hardware
        :param user_id: The uuid of the current user.
        :returns: The number of items of hardware
        """
        return self.__db.hardware.count_documents({"user_id": str(user_id)})

    def count_hardware_types(self) -> int:
        """Counts the number of hardware types in the system
        :returns: The number of hardware types in the system
        """
        return self.__db.hardware_types.count_documents({})

    def get_game(self, game_id: str, user_id: str) -> Game:
        """Gets a specific game if it matches the given user.
        :param game_id: A string containing the uuid of the game
        :param user_id: A string containing the uuid of the given user
        :returns: An object of type Game
        """
        try:
            cursor = self.__db.games.find_one({
                "_id": ObjectId(game_id),
                "user_id": str(user_id)
            })

            if cursor is None:
                raise GameNotFoundException()

            return MongoPersistence.game_from_mongo_result(cursor)
        except InvalidId as exc:
            raise GameNotFoundException from exc

    def __map_games_list(self, result_set: Cursor[Any]) -> list[Game]:
        return list(map(MongoPersistence.game_from_mongo_result, result_set))

    @staticmethod
    def game_from_mongo_result(mongo_result: dict[str, Any]) -> Game:
        """Initialises an instance of Game from a MongoDB result.
        :param mongo_result: A MongoDB result as a dictionary. 
                             See mappings below for details on expected keys.
        :returns: An instance of Game with its properties set.
                  Missing keys from mongo_result will have their property set as the default.
        """

        # game.attr, mongo_result.key
        mappings = {"genre": "_Game__genre",
                    "id": "_id",
                    "title":"_Game__title",
                    "platform": "_Game__platform",
                    "num_copies": "_Game__num_copies",
                    "num_boxed": "_Game__num_boxed",
                    "num_manuals": "_Game__num_manuals",
                    "notes": "_Game__notes",
                    "date_purchased": "_Game__date_purchased",
                    "approximate_date_purchased": "_Game__approximate_date_purchased"}

        return Game._from_dict(mongo_result, mappings)


    def get_platforms(self) -> list[Platform]:
        """Get a list of platforms
        :returns: A list of type Platform of all stored platforms
        """
        result = self.__db.platforms.find().sort("_Platform__name")
        platforms = list(map(MongoPersistence.platform_from_mongo_result, result))
        return platforms

    def get_platform(self, platform_id: str) -> Platform:
        """Get a platform
        :param platform_id: The uuid of a platform
        :returns: an object of type platform containing the requested platform
        """
        mongo_result = self.__db.platforms.find_one({"_id": ObjectId(platform_id)})
        
        if mongo_result is None:
            raise GameNotFoundException()

        return MongoPersistence.platform_from_mongo_result(mongo_result)

    def add_platform(self, platform: Platform) -> None:
        """Add a platform
        :param platform: An object of type platform. The platform to be added.
        """
        self.__db.platforms.insert_one(platform.__dict__)

    def update_platform(self, platform: Platform) -> None:
        """Update the details of a platform
        :param platform: An object of type platform. The platform to be updated.
        """
        self.__db.platforms.update_one(
            {"_id": ObjectId(platform.id)}, {"$set": platform.__dict__}, upsert=False)

    def update_game(self, game: Game, user_id: str) -> None:
        """Update the given game if it belongs to the given user
        :param game_id: An object of type Game -- the game to be updated
        :param user_id: A string containing the uuid of the given user
        :returns: None
        """
        gd = game.__dict__
        gd["user_id"] = str(user_id)
        self.__db.games.update_one({
            "_id": ObjectId(game.id),
            "user_id": str(user_id)
        }, {"$set": gd}, upsert=False)

    #TODO: ultimately rename
    @staticmethod
    def platform_from_mongo_result(mongo_result: dict[str, Any]) -> Platform:
        """Initialises an instance of Platform from a dictionary.
        :param mongo_result: A MongoDB result as a dictionary. The following keys are expected:
           * _id
           * _Platform__name
           * _Platform__description
        :returns: An instance of Platform with its properties set. Keys missing from mongo_result
                  will be initialised to their default values.
        """
        d = mongo_result
        platform = Platform()
        platform.id = d["_id"]
        platform.name = d["_Platform__name"]
        platform.description = d["_Platform__description"]
        return platform

    def get_hardware_details(self, platform_id: str, user_id: str) -> Hardware:
        """Gets the details of a specific item of hardware.
        :param hardware_id: The uuid of the item of hardware to retrieve.
        :param user_id: The uuid of the current user.
        :returns: An instance of Hardware containing the requested item of hardware.
        """
        try:
            h = self.__db.hardware.find_one({
                "_id": ObjectId(platform_id),
                "user_id": str(user_id)
            })

            if h is None:
                raise HardwareNotFoundException()

        except InvalidId as exc:
            raise HardwareNotFoundException() from exc
        return MongoPersistence.hardware_from_mongo_result(h)

    @staticmethod
    def hardware_from_mongo_result(mongo_result: dict[str, Any]) -> "Hardware":
        """Initialises Hardware object from a MongoDB result.
        :param mongo_result: A MongoDB result as a dictionary. The following keys are expected:
                             * _id
                             * _Hardware__name
                             * _Hardware__num_owned
                             * _Hardware__num_boxed
                             * _Hardware__notes
                             * _Hardware__hardware_type
        :returns: A Hardware object with its properties properly initialised. 
                  Any missing keys from mongo_db will cause the object to have that property 
                  initialised as its default.
        """
        # hardware.attr, mongo_result.key
        mappings = {"id": "_id",
                    "name": "_Hardware__name",
                    "platform": "_Hardware__platform",
                    "num_owned": "_Hardware__num_owned",
                    "num_boxed": "_Hardware__num_boxed",
                    "notes": "_Hardware__notes",
                    "hardware_type": "_Hardware__hardware_type"}

        return Hardware._from_dict(mongo_result, mappings)


    def get_hardware_types_list(self) -> list[HardwareType]:
        """Gets the list of hardware types
        :returns: A list of objects of type HardwareType containing the list of hardware.
        """
        return list(map(
            MongoPersistence.hardware_type_from_mongo_result,
            self.__db.hardware_types.find().sort("_HardwareType__name")))

    def update_hardware_type(self, hardware_type: HardwareType) -> None:
        """Update the given hardware type
        :param hardware_type: The hardware type to be updated
        """
        self.__db.hardware_types.update({"_id": ObjectId(hardware_type.id)},
                                        {"$set": hardware_type.__dict__}, upsert=False)

    def delete_hardware_type(self, hardware_type: HardwareType) -> None:
        """Delete the given hardware type.
        :param hardware_type: The hardware type to be deleted
        """
        self.__db.hardware_types.delete_one({"_id": ObjectId(hardware_type.id)})

    def update_genre(self, genre: Genre) -> None:
        """Update the details of a genre
        :param genre: An object of type genre. The genre to be updated.
        """
        self.__db.genres.update_one(
            {"_id": ObjectId(genre.id)}, {"$set": genre.__dict__}, upsert=False)

    def delete_platform(self, platform_id: str) -> None:
        """Delete a platform
        :param platform_id: The id of the platform to be deleted
        """
        self.__db.platforms.delete_one({"_id": ObjectId(platform_id)})

    def delete_game(self, game: Game, user_id: str) -> None:
        """Delete the given game if it belongs to the given user
        :param game: An object of type Game -- the game to be deleted
        :param user_id: A string containing the uuid of the given user
        :returns: None
        """
        self.__db.games.delete_one({
            "_id": ObjectId(game.id),
            "user_id": str(user_id)
        })

    def add_hardware_type(self, hardware_type: HardwareType) -> None:
        """Add a hardware type.
        :param hardware_type: An object of type HardwareType. The hardware type to add.
        """
        self.__db.hardware_types.insert_one(hardware_type.__dict__)

    def get_hardware_list(self, params: GetHardwareListInteractorParams) -> list[Hardware]:
        """Get a list of all hardware in the user's collection
        :param params: An instance of GetHardwareListInteractorParams
        :returns: A list of instances of Hardware 
        """
        sorder = MongoSortDirectionMapper().map(params.sort_direction)
        mapped_sort_field = HardwareSortFieldMapper().map(params.sort_field)
        result = self.__db.hardware.find(
            {"user_id": str(params.user_id)},
            limit=params.number_of_items).sort(mapped_sort_field, sorder)

        return list(map(lambda p: MongoPersistence.hardware_from_mongo_result(p), result))

    def get_hardware_list_for_platform(self, params: GetHardwareListInteractorParams) -> list[Hardware]:
        """Get a list of all hardware for a platform in the user's collection
        param params: An instance of GetHardwareListInteractorParams
        returns: A list of instances of Hardware
        """
        hardware = self.__db.hardware.find(
            {"_Hardware__platform": params.platform, "user_id": str(params.user_id)},
            limit=params.number_of_items)
        return list(map(MongoPersistence.hardware_from_mongo_result, hardware))

    def get_hardware_type(self, hardware_type: HardwareType) -> HardwareType:
        """Get a specific hardware type record.
        :param hardware_type: An instance of HardwareType. The hardware type to get.
        :return: An instance of HardwareType. The requested hardware type.
        """
        h = self.__db.hardware_types.find_one({"_id": ObjectId(hardware_type.id)})
        if h is None:
            raise HardwareNotFoundException()

        return MongoPersistence.hardware_type_from_mongo_result(h)

    @staticmethod
    def hardware_type_from_mongo_result(dictionary: dict[str, Any]) -> HardwareType:
        """Create HardwareType from MongoDB result dictionary"""
        mappings = {"_id": "id",
                    "_HardwareType__name": "name",
                    "_HardwareType__description": "description"}
        return HardwareType._map_from_dict(dictionary, mappings)

    def save_hardware(self, hardware: Hardware, user_id: str) -> None:
        """Save an item of hardware.
        :param hardware: An instance of Hardware. The item of hardware to be saved.
        :param user_id: The uuid of the user whose collection the item of hardware should be 
        added to.
        :returns: None
        """
        hd = hardware.__dict__
        hd["user_id"] = str(user_id)
        self.__db.hardware.insert_one(hd)

    def update_hardware(self, hardware: Hardware, user_id: str) -> None:
        """Update the given item of hardware.
        :param hardware: An instance of Hardware. The item of hardware to be updated.
        :param user_id: The uuid of the current user.
        :returns: None
        """
        hd = hardware.__dict__
        hd["user_id"] = str(user_id)
        self.__db.hardware.update_one({
            "_id": ObjectId(hardware.id),
            "user_id": str(user_id)
        }, {"$set": hd}, upsert=False)

    def delete_hardware(self, hardware_id: str, user_id: str) -> None:
        """Delete the given item of hardware.
        :param hardware_id: The uuid of the item of hardware to be deleted
        :param user_id: The uuid of the current user
        """
        self.__db.hardware.delete_one({
            "_id": ObjectId(hardware_id),
            "user_id": str(user_id)
        })

    def get_genres(self) -> list[Genre]:
        """Get all genres.
        :returns: A list of type Genre that contains all genres in the system.
        """
        return list(map(MongoPersistence.genre_from_mongo_result, self.__db.genres.find().sort("_Genre__name")))

    def add_genre(self, genre: Genre) -> None:
        """Add a genre
        :param genre: An object of type Genre. The genre to be added.
        """
        self.__db.genres.insert_one(genre.__dict__)

    def get_genre_details(self, genre_id: str) -> Genre:
        """Get the details of a genre.
        :param genre_id: The object id of the genre to be retrieved.
        :returns: An object of type Genre containing the genre.
        """
        g = self.__db.genres.find_one({"_id": ObjectId(genre_id)})

        if g is None:
            raise GameNotFoundException()

        return MongoPersistence.genre_from_mongo_result(g)

    @staticmethod
    def genre_from_mongo_result(mongo_result: dict[str, str]) -> 'Genre':
        """Creates a nw Genre object based on the provided result from MongoDB.
        :param mongo_result: A dictionary wiht the following keys:
           * _id
           * _Genre__name
           * _Genre__description
        :returns: An object of type Genre with its properties set. Missing keys
        from the dictionary will cause that parameter in the object to be left as its default."""
        genre = Genre()
        genre.id = mongo_result.get("_id", genre.id)
        genre.name = mongo_result.get("_Genre__name", genre.name)
        genre.description = mongo_result.get("_Genre__description", genre.description)
        return genre

    def delete_genre(self, genre_id: str) -> None:
        """Delete a genre.
        :param genre_id: The ObjectId of the genre to be deleted.
        :returns: None
        """
        self.__db.genres.delete_one({"_id": ObjectId(genre_id)})

    def search(self, search_term: str, sort_field: str, sort_dir: str, user_id: str) -> list[Game]:
        """Search the games collection
        :param search_term: The term to do the search upon
        :param sort_field: The field to sort results by
        :param sort_dir: The direction to sort results in
        :param user_id: The uuid of the current user
        :returns: A list of instances of Game -- the search results
        """
        mapped_sort_field = SortFieldMapper().map(sort_field)
        sorder = MongoSortDirectionMapper().map(sort_dir)
        results = self.__db.games.find(
            {"user_id": str(user_id),  "$or": [
                 {"_Game__title": {"$regex": f".*{search_term}.*", "$options": "i"}},
                 {"_Game__platform": {"$regex": f".*{search_term}.*", "$options": "i"}}]})
        return list(map(MongoPersistence.game_from_mongo_result, results.sort(mapped_sort_field, sorder)))

    def get_user(self, user: User) -> User:
        """Get a user by their user_id
        :param: An object of type User. The user to get. If the user's id property is set then it 
                is used to retrieve the user. Otherwise, the user_id attribute is used.
        :returns: An object of type User. The desired user.
        """
        result_set: Cursor[Any] | None
        if user.id != "":
            result_set = self.__db.users.find_one({"_id": ObjectId(user.id)})
        else:
            result_set = self.__db.users.find_one({"_User__user_id": user.user_id})

        if result_set is None:
            raise GameNotFoundException()
        return MongoPersistence.user_from_mongo_result(result_set)

    @staticmethod
    def user_from_mongo_result(mongo_result: dict[str, str]) -> 'User':
        """Initialises a User object from a MongoDB resultset
        :param mongo_result: A dictionary with the following keys:
           * _id
           * _User__user_id
           * _User__password
        :returns: A populated User object.
                 Any keys missing from mongo_result will have their values left as default.
        """
        user = User()

        if mongo_result is None:
            return user

        user.id = mongo_result.get("_id", user.id)
        user.user_id = mongo_result.get("_User__user_id", user.user_id)
        user.password = mongo_result.get("_User__password", user.password)
        return user

    def get_all_users(self: Any) -> list[User]:
        """Get all users
        :returns: A list of User. All users.
        """
        return list(map(MongoPersistence.user_from_mongo_result, self.__db.users.find().sort("_User__user_id")))

    def add_user(self, user: User) -> None:
        """Add a user
        :param: An object of type User. The user to add.
        """
        self.__db.users.insert_one(user.__dict__)

    def update_user(self, user: User) -> None:
        """Update the details of a user
        :param user: An object of type User. The id field is set to the id of the user to update. 
                     The rest of the fields contain the new values.
        """
        self.__db.users.update({"_id": ObjectId(user.id)}, {"$set": user.__dict__}, upsert=False)

    def delete_user(self, user: User) -> None:
        """Delete a user
        :param user: An object of type user. Contains the id of the user to be deleted.
        """
        self.__db.users.remove({"_id": ObjectId(user.id)})

    def change_password(self, user: User) -> None:
        """Change a user's password
        :param user: An object of type user. The user whose password is to be changed. 
                     The password property is the new password.
        """
        self.__db.users.update({
            "_User__user_id": user.user_id
        }, {"$set": user.__dict__}, upsert=False)
