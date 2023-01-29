from django.conf.urls import url

from send_email.views import EmailsViews, thanks, track_email

urlpatterns = [
    url("choise/", EmailsViews.as_view()),
    url("thanks/", thanks),
    url(r'track_email/(?P<username>\w*)/$', track_email),
]
