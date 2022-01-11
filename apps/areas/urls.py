from django.urls import path

from apps.areas.views import AreaView, SubAreaView
from apps.users.views import *

urlpatterns = [
    path('areas/', AreaView.as_view()),
    path('areas/<id>/', SubAreaView.as_view()),
]
