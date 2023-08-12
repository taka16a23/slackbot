#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""

from django.contrib import admin

from chat.models.channel_model import ChannelModel
from chat.models.post_schedule_model import PostScheduleModel

from chat.admin.channel_model_admin import ChannelModelAdmin
from chat.admin.post_schedule_model_admin import PostScheduleModelAdmin


__all__ = [
    'ChannelModelAdmin',
    'PostScheduleModelAdmin',
]


admin.site.register(ChannelModel, ChannelModelAdmin)
admin.site.register(PostScheduleModel, PostScheduleModelAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
