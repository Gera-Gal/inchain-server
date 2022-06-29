from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from django.config import settings
from django.config.urls.static import static

from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
    path('', include('users.urls')),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
