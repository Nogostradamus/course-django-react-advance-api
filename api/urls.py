from django.conf.urls import url, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewset)
router.register(r'events', views.EventViewset)
router.register(r'bets', views.BetViewset)
router.register(r'members', views.MemberViewset)
router.register(r'comments', views.CommentViewset)
router.register(r'users', views.UserViewSet)
router.register(r'profile', views.UserProfileViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url('authenticate/', views.CustomObtainAuthToken.as_view())
]

