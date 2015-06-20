# Copyright (c) 20115 David Wilson
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
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from AbstractPersistence import AbstractPersistence
from Genre import Genre
from Persistence.Exceptions.GameNotFoundException import GameNotFoundException
from Persistence.Exceptions.HardwareNotFoundException import HardwareNotFoundException
from Persistence.Mappers.HardwareSortFieldMapper import HardwareSortFieldMapper
from Persistence.Mappers.MongoSortDirectionMapper import MongoSortDirectionMapper
from Persistence.Mappers.SortFieldMapper import SortFieldMapper
from Game import Game
from Hardware import Hardware
import HardwareType as ht
from Platform import Platform
from User import User

class MongoPersistence(AbstractPersistence):
    """Provide persistence using MongoDB"""

    def __init__(self):
        """Initialise object state"""
        self.__client = None
        self.__init_mongo_client()
        self.__db = self.__client.GamesCollection

    def __init_mongo_client(self):
        """Initialise the database connection."""
        try:
            self.__client = MongoClient()
        except ConnectionFailure:
            print("No instance of MongoDB detected. Did you forget to start it?")
            sys.exit(-1)

    def __del__(self):
        """Destructor. Make sure the connection to MongoDB is closed."""
        if self.__client is not None:
            self.__client.close()
    
    def add_game(self, game, user_id):
        """Add a single game.
        :param params: An object of type Game
        :param user_id: The id of the current user (actual id rather than username)
        :returns: None
        """
        gd = game.__dict__
        gd["user_id"] = str(user_id)
        self.__db.games.insert(gd)
    
    def get_all_games(self, params):
        """Gets a list of games.
        :param params: An object of type GetGamesInteractorParams
        :returns: A list of Game
        """
        sorder = MongoSortDirectionMapper().map(params.sort_direction)
        mapped_sort_field = SortFieldMapper().map(params.sort_field)
        games = self.__db.games.find({"user_id": str(params.user_id)}, limit=params.number_of_games)
        return self.__map_games_list(games.sort(mapped_sort_field, sorder))
    
    def get_all_games_for_platform(self, params):
        """Gets a list of games for a platform.
        :param params: An object of type GetGamesInteractorParams
        :returns: A list of Game
        """
        sorder = MongoSortDirectionMapper().map(params.sort_direction)
        mapped_sort_field = SortFieldMapper().map(params.sort_field)
        games = self.__db.games.find({"_Game__platform": params.platform, "user_id": str(params.user_id)}, 
                                     limit=params.number_of_games)
        return self.__map_games_list(games.sort(mapped_sort_field, sorder))
    
    def count_games(self, user_id):
        """Counts the games in the user's collection.
        :param user_id: The uuid of the current user.
        :returns: The number of games in the user's collection
        """
        return self.__db.games.find({"user_id": str(user_id)}).count()
    
    def count_hardware(self, user_id):
        """Counts the items of hardware
        :param user_id: The uuid of the current user.
        :returns: The number of items of hardware
        """
        return self.__db.hardware.find({"user_id": str(user_id)}).count()        
    
    def get_game(self, game_id, user_id):
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
            return Game.from_mongo_result(cursor)
        except InvalidId:
            raise GameNotFoundException
    
    def __map_games_list(self, result_set):
        return list(map(lambda g: Game.from_mongo_result(g), result_set))

    def get_platforms(self):
        """Get a list of platforms
        :returns: A list of type Platform of all stored platforms
        """
        result = self.__db.platforms.find().sort("_Platform__name")
        return list(map(lambda p: Platform.from_mongo_result(p), result))
    
    def get_platform(self, platform_id):
        """Get a platform
        :param platform_id: The uuid of a platform
        :returns: an object of type platform containing the requested platform
        """
        mongo_result = self.__db.platforms.find_one({"_id": ObjectId(platform_id)})
        return Platform.from_mongo_result(mongo_result)
    
    def add_platform(self, platform):
        """Add a platform
        :param platform: An object of type platform. The platform to be added.
        """
        self.__db.platforms.insert(platform.__dict__)
    
    def update_platform(self, platform):
        """Update the details of a platform
        :param platform: An object of type platform. The platform to be updated.
        """
        self.__db.platforms.update({"_id": ObjectId(platform.id)}, {"$set": platform.__dict__}, upsert=False)
    
    def delete_platform(self, platform_id):
        """Delete a platform
        :param platform_id: The id of the platform to be deleted
        """
        self.__db.platforms.remove({"_id": ObjectId(platform_id)})
    
    def update_game(self, game,  user_id):
        """Update the given game if it belongs to the given user
        :param game_id: An object of type Game -- the game to be updated
        :param user_id: A string containing the uuid of the given user
        :returns: None
        """
        gd = game.__dict__
        gd["user_id"] = str(user_id)
        self.__db.games.update({
            "_id": ObjectId(game.id),
            "user_id": str(user_id)
        }, {"$set": gd}, upsert=False)
    
    def delete_game(self, game, user_id):
        """Delete the given game if it belongs to the given user
        :param game: An object of type Game -- the game to be deleted
        :param user_id: A string containing the uuid of the given user
        :returns: None
        """
        self.__db.games.remove({
            "_id": ObjectId(game.id),
            "user_id": str(user_id)
        })
    
    def get_hardware_details(self, platform_id, user_id):
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
        except InvalidId:
            raise HardwareNotFoundException()
        return Hardware.from_mongo_result(h)
    
    def get_hardware_types_list(self):
        """Gets the list of hardware types
        :returns: A list of objects of type HardwareType containing the list of hardware.
        """
        return list(map(ht.HardwareType.from_mongo_result, self.__db.hardware_types.find()))
        

    def save_hardware(self, hardware, user_id):
        """Save an item of hardware.
        :param hardware: An instance of Hardware. The item of hardware to be saved.
        :param user_id: The uuid of the user whose collection the item of hardware should be added to.
        :returns: None
        """
        hd = hardware.__dict__
        hd["user_id"] = str(user_id)
        self.__db.hardware.insert(hd)
    
    def update_hardware(self, hardware, user_id):
        """Update the given item of hardware.
        :param hardware: An instance of Hardware. The item of hardware to be updated.
        :param user_id: The uuid of the current user.
        :returns: None
        """
        hd = hardware.__dict__
        hd["user_id"] = str(user_id)        
        self.__db.hardware.update({
            "_id": ObjectId(hardware.id),
            "user_id": str(user_id)
        }, {"$set": hd}, upsert=False)
    
    def delete_hardware(self, hardware_id, user_id):
        """Delete the given item of hardware.
        :param hardware_id: The uuid of the item of hardware to be deleted
        :param user_id: The uuid of the current user
        """
        self.__db.hardware.remove({
            "_id": ObjectId(hardware_id),
            "user_id": str(user_id)
        })

    def add_genre(self, genre):
        self.__db.genres.insert(genre.__dict__)

    def update_genre(self, genre):
        """Update the details of a genre
        :param genre: An object of type genre. The genre to be updated.
        """
        self.__db.genres.update({"_id": ObjectId(genre.id)}, {"$set": genre.__dict__}, upsert=False)
    
    def delete_platform(self, platform_id):
        """Delete a platform
        :param platform_id: The id of the platform to be deleted
        """
        self.__db.platforms.remove({"_id": ObjectId(platform_id)})
    
    def delete_game(self, game, user_id):
        """Delete the given game if it belongs to the given user
        :param game: An object of type Game -- the game to be deleted
        :param user_id: A string containing the uuid of the given user
        :returns: None
        """
        self.__db.games.remove({
            "_id": ObjectId(game.id),
            "user_id": str(user_id)
        })
    
    def add_hardware_type(self, hardware_type):
        """Add a hardware type.
        :param hardware_type: An object of type HardwareType. The hardware type to add.
        """
        self.__db.hardware_types.insert(hardware_types.__dict__)

    def get_hardware_list(self, params):
        """Get a list of all hardware in the user's collection
        :param params: An instance of GetHardwareListInteractorParams
        :returns: A list of instances of Hardware 
        """    
        sorder = MongoSortDirectionMapper().map(params.sort_direction)
        mapped_sort_field = HardwareSortFieldMapper().map(params.sort_field)
        result = self.__db.hardware.find({"user_id": str(params.user_id)}, limit=params.number_of_items).sort(
            mapped_sort_field, sorder)

        return list(map(lambda p: Hardware.from_mongo_result(p), result))
    
    def get_hardware_list_for_platform(self, params):
        """Get a list of all hardware for a platform in the user's collection
        param params: An instance of GetHardwareListInteractorParams
        returns: A list of instances of Hardware
        """
        sorder = MongoSortDirectionMapper().map(params.sort_direction)
        mapped_sort_field = HardwareSortFieldMapper().map(params.sort_field)
        hardware = self.__db.hardware.find({"_Hardware__platform": params.platform, "user_id": str(params.user_id)}, 
                                           limit=params.number_of_items)
        return list(map(lambda p: Hardware.from_mongo_result(p), hardware))

    def save_hardware(self, hardware, user_id):
        """Save an item of hardware.
        :param hardware: An instance of Hardware. The item of hardware to be saved.
        :param user_id: The uuid of the user whose collection the item of hardware should be added to.
        :returns: None
        """
        hd = hardware.__dict__
        hd["user_id"] = str(user_id)
        self.__db.hardware.insert(hd)
    
    def update_hardware(self, hardware, user_id):
        """Update the given item of hardware.
        :param hardware: An instance of Hardware. The item of hardware to be updated.
        :param user_id: The uuid of the current user.
        :returns: None
        """
        hd = hardware.__dict__
        hd["user_id"] = str(user_id)        
        self.__db.hardware.update({
            "_id": ObjectId(hardware.id),
            "user_id": str(user_id)
        }, {"$set": hd}, upsert=False)
    
    def delete_hardware(self, hardware_id, user_id):
        """Delete the given item of hardware.
        :param hardware_id: The uuid of the item of hardware to be deleted
        :param user_id: The uuid of the current user
        """
        self.__db.hardware.remove({
            "_id": ObjectId(hardware_id),
            "user_id": str(user_id)
        })

    def get_genres(self):
        """Get all genres.
        :returns: A list of type Genre that contains all genres in the system.
        """
        return list(map(Genre.from_mongo_result, self.__db.genres.find().sort("_Genre__name")))

    def add_genre(self, genre):
        """Add a genre
        :param genre: An object of type Genre. The genre to be added.
        """
        self.__db.genres.insert(genre.__dict__)

    def get_genre_details(self, genre_id):
        """Get the details of a genre.
        :param genre_id: The object id of the genre to be retrieved.
        :returns: An object of type Genre containing the genre.
        """
        g = self.__db.genres.find_one({"_id": ObjectId(genre_id)})
        return Genre.from_mongo_result(g)

    def delete_genre(self, genre_id):
        """Delete a genre.
        :param genre_id: The ObjectId of the genre to be deleted.
        :returns: None
        """
        self.__db.genres.remove({"_id": ObjectId(genre_id)})
    
    def search(self, search_term, sort_field, sort_dir, user_id):
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
                 {"_Game__title": {"$regex": ".*%s.*" % search_term, "$options": "i"}},                   
                 {"_Game__platform": {"$regex": ".*%s.*" % search_term, "$options": "i"}}]})
        return map(Game.from_mongo_result, results.sort(mapped_sort_field, sorder))
    
    def get_user(self, user):
        """Get a user by their user_id
        :param: An object of type User. The user to get. If the user's id property is set then it is used to retrieve 
                the user. Otherwise, the user_id attribute is used.
        :returns: An object of type User. The desired user.
        """
        result_set = []
        if user.id != "":
            result_set = self.__db.users.find_one({"_id": ObjectId(user.id)})
        else:
            result_set = self.__db.users.find_one({"_User__user_id": user.user_id})
        return User.from_mongo_result(result_set)
    
    def get_all_users(self):
        """Get all users
        :returns: A list of User. All users.
        """
        return map(User.from_mongo_result, self.__db.users.find().sort("_User__user_id"))

    def add_user(self, user):  
        """Add a user
        :param: An object of type User. The user to add.
        """
        self.__db.users.insert(user.__dict__)
    
    def update_user(self, user):
        """Update the details of a user
        :param user: An object of type User. The id field is set to the id of the user to update. The rest of the 
        fields contain the new values.
        """
        self.__db.users.update({"_id": ObjectId(user.id)}, {"$set": user.__dict__}, upsert=False)

    def delete_user(self, user):
        """Delete a user
        :param user: An object of type user. Contains the id of the user to be deleted.
        """
        self.__db.users.remove({"_id": ObjectId(user.id)})

    def change_password(self, user):
        """Change a user's password
        :param user: An object of type user. The user whose password is to be changed. 
                     The password property is the new password.
        """
        self.__db.users.update({
            "_User__user_id": user.user_id
        }, {"$set": user.__dict__}, upsert=False)
        
