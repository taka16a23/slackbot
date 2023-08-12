#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from django.contrib import admin

from chatparam.models.channel_model import ChannelModel
from chatparam.models.chatparam_model import ChatParamModel

from chatparam.admin.channel_model_admin import ChannelModelAdmin
from chatparam.admin.chatparam_model_admin import ChatParamModelAdmin


__all__ = [
    'ChannelModelAdmin',
    'ChatParamModelAdmin',
]


admin.site.register(ChannelModel, ChannelModelAdmin)
admin.site.register(ChatParamModel, ChatParamModelAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
