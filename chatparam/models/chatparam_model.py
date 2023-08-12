#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""chatparam_model --

"""
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

from chatparam.models.channel_model import ChannelModel


class ChatParamModel(models.Model):
    r"""ChatParamModel

    ChatParamModel is a models.Model.
    Responsibility:
    """
    channel = models.ForeignKey(
        ChannelModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    text = models.TextField(
        _('Message Text'),
        default='',
        null=False,
        blank=True,
        help_text=_('Message Text'),
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
        help_text=_('Has been sent'),
    )

    class Meta:
        verbose_name = u'Chat Parameters'
        verbose_name_plural = u'Chat Parameters'
        ordering = ['schedule_datetime', ]

    def __str__(self):
        return '{0}: {1} : {2}'.format(self.schedule_datetime, self.channel, self.text)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# chatparam_model.py ends here
