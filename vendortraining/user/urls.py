from rest_framework.routers import DefaultRouter

from . import views
from django.urls import include, path

router = DefaultRouter()
router.register('', views.UserView)
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]