from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from apps.task2.filters import VacancyFilter
from apps.task2.models import Vacancy
from .serializers import VacancySerializer


class VacancyListAPIView(generics.ListAPIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['salary', 'salary_from', 'salary_to']
    # filterset_class = VacancyFilter


__all__ = ("VacancyListAPIView",)
