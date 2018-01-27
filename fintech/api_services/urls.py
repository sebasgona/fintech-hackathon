from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserCreateView,INECreateView,PassportCreateView

urlpatterns = {
    url(r'^users/$', UserCreateView.as_view(), name="create_user"),
    url(r'^ines/$', INECreateView.as_view(), name="create_INE"),
    url(r'^passports/$', PassportCreateView.as_view(), name="create_passport"),
}

urlpatterns = format_suffix_patterns(urlpatterns)