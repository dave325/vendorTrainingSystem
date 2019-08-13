from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt

from . import user
from . import vendor
from . import authetication
from . import super
from . import admin
from . import views
from django.urls import include, path

router = DefaultRouter()
router.register('user', user.UserView) #-- user profile route -- to access any function use "192.168.99.100:3000/user/<functionName>/" to access
router.register('vendor', vendor.VendorView) #-- 192.168.99.100:3000/vendor/<functionName>/
# router.register('super', super.SuperView) #-- 192.168.99.100:3000/vendor/<functionName>/
router.register('test', authetication.UserAuthetication) #-- 192.168.99.100:3000/vendor/<functionName>/
router.register('admin', admin.AdminView)
router.register('views', views.UserView)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
]

# urlpatters = [
#     path('', include(?????))
# ]
