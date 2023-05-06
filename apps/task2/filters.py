from django_filters import rest_framework as filters

from apps.task2.models import Vacancy


class VacancyFilter(filters.FilterSet):
    salary_from = filters.NumberFilter(salary_from="salary_from", lookup_expr='gte')
    salary_to = filters.NumberFilter(salary_to="salary_to", lookup_expr='lte')
    salary = filters.NumberFilter(salary="salary", lookup_expr='exact')

    class Meta:
        model = Vacancy
        fields = ['salary']
