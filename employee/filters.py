from django_filters.rest_framework import DjangoFilterBackend


class EmployeeFilter(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        queryset = super().filter_queryset(request, queryset, view)
        queryset = self.filter_section(request, queryset, view)
        return queryset

    def filter_section(self, request, queryset, view):
        if request.query_params.get('section'):
            queryset = queryset.filter(section=request.query_params.get('section'))

        return queryset
