from django.urls import path, include
from rest_framework.routers import DefaultRouter

from prima_italica.app import views

app_name = 'app'

router = DefaultRouter()
router.register('voluntario', views.VoluntarioViewSet, basename='voluntario')
router.register('acao', views.AcaoViewSet)

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('', include(router.urls))
]
