from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt

from . import user
from . import vendor
from . import authetication
from . import super
from . import admin

from django.urls import include, path

router = DefaultRouter()
# -- user profile route -- to access any function use "192.168.99.100:3000/user/<functionName>/" to access
router.register('user', user.UserView)
# -- 192.168.99.100:3000/vendor/<functionName>/
router.register('vendor', vendor.VendorView)
# router.register('super', super.SuperView) #-- 192.168.99.100:3000/vendor/<functionName>/
# -- 192.168.99.100:3000/vendor/<functionName>/
router.register('auth', authetication.UserAuthetication)
router.register('admin', admin.AdminView)

#router.register('views', views.UserView)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]