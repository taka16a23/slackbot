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
    channel = models.CharField(
        u'Channel',
        max_length=9,
        help_text=u'9 length',
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
        verbose_name = u'Channel'
        verbose_name_plural = u'Channel'

    def __str__(self):
        return '{0}: {1}'.format(self.channel, self.description)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# channel_model.py ends here
