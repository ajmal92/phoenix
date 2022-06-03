from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "world_cup_bidding_game.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import world_cup_bidding_game.users.signals  # noqa F401
        except ImportError:
            pass
