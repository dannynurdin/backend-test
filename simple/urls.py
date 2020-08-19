from django.urls import path

from rest_framework import routers

from .views import StudentViewSet

router = routers.DefaultRouter()
router.register('Students', StudentViewSet)

urlpatterns = router.urls