#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""post_schedule_model --

"""
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

from chat.models.channel_model import ChannelModel


class PostScheduleModel(models.Model):
    r"""PostScheduleModel

    PostScheduleModel is a models.Model.
    Responsibility:
    """
    channel = models.ForeignKey(
        ChannelModel,
        verbose_name=_('Channel'),
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    text = models.TextField(
        _('Message Text'),
        default='',
        null=False,
        blank=True,
    )
    schedule_datetime = models.DateTimeField(
        _('Schedule DateTime'),
        blank=False,
        null=False,
        help_text=_('Ex. 10/01/1900 01:00'),
    )
    is_deleted = models.BooleanField(
        _('Deleted'),
        default=False,
    )
    is_send = models.BooleanField(
        _('Is Send'),
        default=False,
    )

    class Meta:
        verbose_name = _('Post Schedule')
        verbose_name_plural = _('Post Schedule')
        ordering = ['schedule_datetime', ]

    def __str__(self):
        return '{0}: {1} : {2}'.format(self.schedule_datetime, self.channel, self.text)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# post_schedule_model.py ends here
