import unittest
from unittest.mock import Mock
from Hardware import Hardware
from Interactors.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Handler import Handler
from UI.Handlers.SortHardwareHandler import SortHardwareHandler
from UI.TemplateRenderer import TemplateRenderer

class TestSortHardwareHandler(unittest.TestCase):

    def setUp(self):
        self.__hardware = [Hardware()]
        self.__interactor = Mock(GetHardwareListInteractor)
        self.__interactor.execute = Mock(return_value=self.__hardware)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = SortHardwareHandler(interactor_factory, self.__renderer)

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_interactor(self):
        args = self.__get_args()
        self.__target.get_page(args)
        self.__interactor.execute.assert_called_with(args["field"], args["sortdir"])

    def test_get_page_executes_renderer(self):
        args = self.__get_args()
        self.__target.get_page(args)
        self.__renderer.render.assert_called_with("hardware.html", hardware=self.__hardware,
                                                  hw_sort_field=args["field"], hw_sort_dir=args["sortdir"])

    def __get_args(self):
        return {"field": "title", "sortdir": "asc", "numrows": 2}