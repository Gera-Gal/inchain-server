from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'media-files', views.MediaFileViewSet)
router.register(r'courses', views.CourseViewSet)

app_name = 'courses'
urlpatterns = router.urls