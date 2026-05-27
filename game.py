"""Represents a game"""
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

from dataclasses import dataclass, field
import json
from typing import Any

@dataclass
class Game:
    """Represents a game"""
    id: str = field(default="")
    genre: str = field(default="")
    title: str = field(default="")
    platform: str = field(default="")
    num_copies: int = field(default=0)
    num_boxed: int = field(default=0)
    num_manuals: int = field(default=0)
    notes: str = field(default="")
    date_purchased: str = field(default="")
    approximate_date_purchased: bool = field(default=False)

    #TODO: Can probably clean this dict stuff up between the domain objects
    @staticmethod
    def from_dict(dictionary: dict[str, Any]) -> "Game":
        """Initialises an instance of Game from a dictionary.
        
        :param dictionary: A dictionary.  See mapping below for details on expected keys.
        :returns: An instance of Game with its properties set. Missing keys from d will have their
                  property set as the default."""

        # game.attr, dictionary.key
        mappings = {"id": "id",
                    "date_purchased": "datepurchased",
                    "approximate_date_purchased": "approximatedatepurchased",
                    "genre": "genre",
                    "title": "title",
                    "num_copies": "numcopies",
                    "num_boxed": "numboxed",
                    "num_manuals": "nummanuals",
                    "platform": "platform",
                    "notes": "notes"}

        return Game._from_dict(dictionary, mappings)

    @staticmethod
    def _from_dict(d: dict[str, Any], mappings: dict[str, str]) -> "Game":

        def dict_get(x: tuple[str, str]) -> Any:
            return d[mappings[x[0]]] if mappings[x[0]] in d else getattr(Game, x[0])

        game = Game(id=dict_get(("id", "id")),
                    genre=dict_get(("genre", "genre")),
                    title=dict_get(("title", "title")),
                    num_copies=dict_get(("num_copies", "num_copies")),
                    num_boxed=dict_get(("num_boxed", "num_boxed")),
                    num_manuals=dict_get(("num_manuals", "num_manuals")),
                    platform=dict_get(("platform", "platform")),
                    notes=dict_get(("notes", "notes")),
                    date_purchased=dict_get(("date_purchased", "date_purchased")),
                    approximate_date_purchased=dict_get((
                        "approximate_date_purchased", 
                        "approximate_date_purchased"
                    )))

        return game

    def to_json(self) -> str:
        """Convert this instance of Game to a JSON string.
        :returns: A JSON string representing this instance of Game.
        """
        attrs = [
            "date_purchased",
            "genre",
            "title",
            "num_copies",
            "num_boxed",
            "num_manuals",
            "platform",
            "notes"]

        result = {}

        result["id"] = str(self.id)

        for a in attrs:
            result[a] = getattr(self, a)

        return json.dumps(result)
