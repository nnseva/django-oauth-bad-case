"""Models for the application"""
from oauth2_provider.models import AbstractApplication, ApplicationManager

from django.db import models
from django.utils.translation import gettext_lazy as _


class OAuth2App(AbstractApplication):
    """Project-related OAuth2 Application"""

    objects = ApplicationManager()

    class Meta(AbstractApplication.Meta):
        swappable = 'OAUTH2_PROVIDER_APPLICATION_MODEL'
        verbose_name = _('OAuth2 Application')
        verbose_name_plural = _('OAuth2 Applications')

    def natural_key(self):
        """Returns natural key for the object manager"""
        return (self.client_id,)
