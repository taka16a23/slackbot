#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""channel_model_admin --

"""
from django.contrib import admin


class ChannelModelAdmin(admin.ModelAdmin):
    r"""ChannelModelAdmin

    ChannelModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'channel',
        'description',
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# channel_model_admin.py ends here
