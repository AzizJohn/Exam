from django.urls import path

from apps.task2.api_endpoints import VacancyListAPIView

app_name = "task2"

urlpatterns = [
    path("vacancylist/", VacancyListAPIView.as_view(), name="vacancy_list"),
]
