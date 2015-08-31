# Copyright (c) 2015 David Wilson
# This file is part of Icarus.

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

import Interactors.Interactor as i


class AddPlatformInteractor(i.Interactor):
    """Add a platform"""

    def execute(self, platform):
        """
        Add a platform
        :param platform: An object of type Platform. The platform to add.
        """
        self.__validate(platform)
        self.__stop_if_platform_exists(platform)
        self.persistence.add_platform(platform)

    def __stop_if_platform_exists(self, platform):
        """
        If persistence tells us that a platform with a different id but the same name already exists,
        raise PlatformExistsException.
        """
        existing_platforms = self.persistence.get_platforms()
        matching_platforms = [p for p in existing_platforms if p.name == platform.name]
        if len(matching_platforms) > 0:
            raise PlatformExistsException()

    def __validate(self, platform):
        if platform is None:
            raise TypeError("platform")
        if len(platform.id) > 0:
            raise ValueError("Id must be blank when adding a new platform")
        self.validate_string_field("Platform name", platform.name)


class DeletePlatformInteractor(i.Interactor):
    """Delete a platform"""

    def execute(self, platform):
        """
        Delete a platform

        Args:
            platform: The id of the platform to delete.
        
        Raises:
            TypeError: The platform passed in was None
        """
        if platform is None:
            raise TypeError("platform")

        platforms = self.persistence.get_platforms()
        this_platform = [x for x in platforms if str(x.id)==platform]

        if len(this_platform) == 0:
            raise PlatformNotFoundException

        self.persistence.delete_platform(platform)


class GetPlatformInteractor(i.Interactor):
    """Get details of a specific platform"""

    def execute(self, platform_id):
        """
        Get details of a specific platform
        :param platform_id: The uuid of the platform to be retrieved
        :returns: An object of type Platform. The requested platform
        """
        return self.persistence.get_platform(platform_id)


class GetPlatformsInteractor(i.Interactor):
    """Get all platforms"""

    def execute(self):
        """
        Get all platforms.
        :returns: A list of Platform objects containing details on all platforms
        """

        platforms = self.persistence.get_platforms()
        if platforms is None:
            platforms = []
        return platforms


class GetSuggestedPlatformsInteractor(i.Interactor):
    """Get the list of suggested platforms"""
    
    def __init__(self, suggested_platforms):
        """Initialise the suggested platforms"""
        super().__init__()
        self.__suggested_platforms = suggested_platforms

    def execute(self):
        """
        Get the list of suggested platforms
        :returns: A list of Platform objects sorted by name containing details of the suggested platforms
        """

        platforms = list(self.persistence.get_platforms())
        suggested_platforms = self.__suggested_platforms()        
        result = [p for p in suggested_platforms if p not in platforms]
        return sorted(result, key=lambda x: x.name)


class UpdatePlatformInteractor(i.Interactor):
    """Update the details of a platform"""

    def execute(self, platform):
        """
        Update the details of a platform.
        :param platform: An object of type Platform. The platform to be updated
        """

        self.__validate(platform)
        self.__stop_if_platform_is_invalid(platform)
        
        self.persistence.update_platform(platform)

    def __stop_if_platform_is_invalid(self, platform):
        print(platform.id)
        existing_platforms = self.persistence.get_platforms()
        matching_platforms = [x for x in existing_platforms if (x.name==platform.name and str(x.id)!=platform.id)]
        this_platform = [x for x in existing_platforms if str(x.id)==platform.id]

        if len(this_platform) == 0:
            raise PlatformNotFoundException
        if len(matching_platforms)>0:
            raise PlatformExistsException

    def __validate(self, platform):
        if platform is None:
            raise TypeError("platform")
        self.validate_string_field("Platform", platform.name)

class PlatformExistsException(Exception):
    pass

class PlatformNotFoundException(Exception):
    pass

