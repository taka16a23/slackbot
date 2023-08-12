# Create your models here.
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
