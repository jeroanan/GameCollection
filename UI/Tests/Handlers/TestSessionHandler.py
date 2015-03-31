import unittest

from UI.Handlers.Handler import Handler
from UI.Handlers.SessionHandler import SessionHandler

class TestSessionHandler(unittest.TestCase):
    
    def test_is_handler(self):
        target = SessionHandler(None, None, None)
        self.assertIsInstance(target, Handler)
    

    
