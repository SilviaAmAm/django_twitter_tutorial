from django.urls import path
from . import views

urlpatterns = [
    path('<pk>', views.Profile.as_view(), name='user-profile')
]