"""Handler to check whether the user is auhenticated"""
from UI.Handlers.handler import Handler


class AuthenticatedHandler(Handler):
    """Handler to check whether the user is auhenticated"""

    def get_page(self, _params):
        """Check if the user is authenticated, if not redirect to the login page."""
        self.check_session()
        self.redirect_if_not_logged_in()
