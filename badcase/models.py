"""Models for the application"""
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from oauth2_provider.models import AccessToken


class TokenSession(models.Model):
    """An additional options holder to be linked to the token as a session"""
    token = models.OneToOneField(
        # CASE 1/2: there is no difference between, direct, indirect, or swappable reference here
        AccessToken, on_delete=models.CASCADE,
        verbose_name=_('Token'), help_text=_('Token to which the session belongs'),
        related_name='session'
    )

    user =  models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='token_sessions',
            blank=True, null=True,
            verbose_name=_('User'), help_text=_('Cached User')
    )

    class Meta:
        verbose_name = _('Token Session')
        verbose_name_plural = _('Token Sessions')

    def __str__(self):
        return _('%s') % self.token
