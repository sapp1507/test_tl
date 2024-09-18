from django.views.generic import TemplateView
from rest_framework import mixins
from rest_framework import viewsets

from employee.enums import SectionsEnum
from employee.filters import EmployeeFilter, SectionFilter
from employee.models import Section, Employee
from employee.serializers import EmployeeSerializer, SectionSerializer


class SectionsApiView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filter_backends = [SectionFilter]


class EmployeeView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [EmployeeFilter]


class SectionsView(TemplateView):
    template_name = 'sections.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**{
            **kwargs,
            'sections': Section.objects.filter(level=SectionsEnum.LEVEL_1.value)
        })
