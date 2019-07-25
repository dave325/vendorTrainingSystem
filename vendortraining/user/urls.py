from rest_framework.routers import DefaultRouter

from . import views
from django.urls import include, path

router = DefaultRouter()
router.register('', views.UserView)
# router.register('vendor', ????) -- will give the prefix 'vendor/'


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

# urlpatters = [
#     path('', include(?????))
# ]
