from Interactors.DeletePlatformInteractor import DeletePlatformInteractor
from Interactors.Interactor import Interactor
from Platform import Platform
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestDeletePlatformInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = DeletePlatformInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_integer_field = self.validate_integer_field
        self.__target.validate_string_field = self.validate_string_field

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        platform = Platform()
        platform.id = "id"
        self.__target.execute(platform=platform)
        self.persistence.delete_platform.assert_called_with(platform)

    def test_execute_with_none_platform_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_validates_id_field(self):
        self.__target.execute(self.get_platform(platform_id="platform_id"))
        self.assertTrue(self.validate_string_field_was_called_with("Platform id", "platform_id"))
