#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""chatparam_model_admin --

"""
from django.contrib import admin


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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# chatparam_model_admin.py ends here
