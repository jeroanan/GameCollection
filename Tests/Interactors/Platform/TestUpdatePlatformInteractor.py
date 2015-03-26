from Interactors.Interactor import Interactor
from Interactors.Platform.UpdatePlatformInteractor import UpdatePlatformInteractor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestUpdatePlatformInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = UpdatePlatformInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_integer_field = self.validate_integer_field
        self.__target.validate_string_field = self.validate_string_field
        self.__platform = self.get_platform()

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_update_platform(self):
        platform = self.get_platform()
        self.__target.execute(platform)
        self.persistence.update_platform.assert_called_with(platform)

    def test_execute_with_none_platform_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_validates_name_field(self):
        self.__target.execute(self.__platform)
        self.validate_string_field_was_called_with("Platform name", self.__platform.name)
