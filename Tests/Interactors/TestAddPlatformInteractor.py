from Interactors.AddPlatformInteractor import AddPlatformInteractor
from Interactors.Interactor import Interactor
from Platform import Platform
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestAddPlatformInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = AddPlatformInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_string_field = self.validate_string_field
        self.__target.validate_integer_field = self.validate_integer_field

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_with_none_platform_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_with_non_blank_id_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.get_platform(platform_id="id"))

    def test_execute_validates_platform_name_field(self):
        platform = self.get_platform(name="")
        self.__target.execute(platform)
        self.assertTrue(self.validate_string_field_was_called_with("Platform name", platform.name))

    def test_execute_calls_persistence(self):
        self.__target.execute(self.get_platform(name="platform"))
        self.assertTrue(self.persistence.add_platform.called)

