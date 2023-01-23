from django.urls import path
from .views import home, quem_somos, contato

urlpatterns = [
    path("", home, name='index'),
    path("quem-somos", quem_somos, name='quem-somos'),
    path("contato", contato, name='contato'),
]