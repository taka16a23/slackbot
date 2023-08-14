"""ui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import pytz
import datetime
import requests

from django.contrib import admin
from django.urls import path
from django.utils.translation import gettext, gettext_lazy as _

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from slackbot.settings import SLACK_POST_INTERVAL_SECONDS, SLACK_OAUTH_TOKEN, SLACK_POST_URL

from chat.models.post_schedule_model import PostScheduleModel

HEADERS = {"Authorization": "Bearer " + SLACK_OAUTH_TOKEN}


scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

def post_slack(channel, text):
    data  = {
        'channel': channel,
        'text': text,
        'as_user': True,
    }
    response = requests.post(SLACK_POST_URL, headers=HEADERS, data=data)
    if response.status_code != 200:
        return False
    if response.ok != True:
        return False
    return True


@register_job(scheduler, "interval", seconds=SLACK_POST_INTERVAL_SECONDS, id='schedule_posts', replace_existing=True)
def schedule_posts():
    max_datetime = datetime.datetime.now(tz=pytz.utc)
    min_datetime = max_datetime - datetime.timedelta(seconds=SLACK_POST_INTERVAL_SECONDS)
    queryset = PostScheduleModel.objects.filter(
        is_deleted=False, is_send=False,
        schedule_datetime__gte=min_datetime,
        schedule_datetime__lte=max_datetime)
    for model in iter(queryset):
        if post_slack(model.channel.channel, model.text) == True:
            model.is_send = True
            model.save()


register_events(scheduler)
scheduler.start()

admin.site.site_title = _('Controll Panel')
admin.site.site_header = _('Slackbot')
admin.site.index_title = ''
admin.site.site_url = ''


urlpatterns = [
    path('admin/', admin.site.urls),
]
