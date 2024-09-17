from rest_framework import mixins
from rest_framework import viewsets

from employee.filters import EmployeeFilter
from employee.models import Section, Employee
from employee.serializers import SectionSerializer, EmployeeSerializer


class EmployeeView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [EmployeeFilter]


class SectionsView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
