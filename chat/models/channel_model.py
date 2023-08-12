#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""channel_model --

"""
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


class ChannelModel(models.Model):
    """ChannelModel

    ChannelModel is a models.Model.
    Responsibility:
    """
    name = models.CharField(
        _('Name'),
        max_length=30,
        help_text=_('30 characters'),
        null=False,
        default='',
        blank=False)
    channel = models.CharField(
        _('Channel'),
        max_length=9,
        help_text=_('9 character token'),
        unique=True,
        null=False,
        blank=False)
    description = models.TextField(
        _('Description'),
        default='',
        null=False,
        blank=True,
        help_text=_('description'),
    )

    class Meta(object):
        verbose_name = _('Channel')
        verbose_name_plural = _('Channel')

    def __str__(self):
        return '{0}: {1}'.format(self.name, self.channel)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# channel_model.py ends here
