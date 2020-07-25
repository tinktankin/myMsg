from django.urls import path
from .views import share, social

urlpatterns = [
    path('share/<int:id>', share, name="Share"),
    path('social/', social, name="Social"),
]
