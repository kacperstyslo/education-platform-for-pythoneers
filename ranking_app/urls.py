from django.urls import path

# Own
from . import views

urlpatterns = [
    path("", views.RankingView.as_view(), name="ranking-page"),
]
