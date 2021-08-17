from django.contrib import admin

# Register your models here.
class ChannelModelAdmin(admin.ModelAdmin):
    r"""ChannelModelAdmin

    ChannelModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('channel', 'description', )

class ChatParamModelAdmin(admin.ModelAdmin):
    r"""ChannelModelAdmin

    ChannelModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'channel',
        'schedule_datetime',
        'text',
        'is_send',
        'is_deleted',
    )
    list_editable = (
        'is_deleted',
    )

from chatparam.models import (
    ChannelModel, ChatParamModel, )


__all__ = ['ChannelModel', 'ChatParamModel', ]


admin.site.register(ChannelModel, ChannelModelAdmin)
admin.site.register(ChatParamModel, ChatParamModelAdmin)
