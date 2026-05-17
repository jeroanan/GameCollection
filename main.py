"""The main entry point for the Icarus application."""
#!/usr/bin/env python3

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

import logging
import os

from data.config import Config
from interactors.interactor_factory import InteractorFactory
from persistence.mongo_persistence import MongoPersistence
from ui.web_server import WebServer

WorkingDirectory = os.path.dirname(os.path.abspath(__file__))

def init_logger():
    """Initializes and returns the application logger."""
    _logger = logging.getLogger("Icarus")
    _logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler("main.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    _logger.addHandler(file_handler)
    return _logger

if __name__ == "__main__":
    logger = init_logger()
    logger.info("Starting up...")

    config = Config()
    persistence = MongoPersistence(logger=logger, config=config)
    interactor_factory = InteractorFactory(persistence, logger)

    ui = WebServer()
    ui.start(interactor_factory=interactor_factory, config=config, logger=logger)
