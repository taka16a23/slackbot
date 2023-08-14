from django.apps import AppConfig


class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'

    def ready(self, ):
        from django_apscheduler.jobstores import register_events
        from chat.crons import scheduler
        register_events(scheduler)
        scheduler.start()
