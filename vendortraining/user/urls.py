from rest_framework.routers import DefaultRouter

from . import views
from . import vendor
from django.urls import include, path

router = DefaultRouter()
router.register('user', views.UserView) # user profile route -- to access any funciton use "192.168.99.100:3000/users/user/<functionName>/" to access
router.register('vendor', vendor.VendorView) #-- 192.168.99.100:3000/users/vendor/<functionName>/


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

# urlpatters = [
#     path('', include(?????))
# ]
