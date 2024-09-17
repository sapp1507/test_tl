from django.urls import path, include
from rest_framework.routers import DefaultRouter

from employee.views import SectionsView, EmployeeView

router = DefaultRouter()
router.register('sections', SectionsView, basename='sections')
router.register('employee', EmployeeView, basename='employee')

urlpatterns = [
    path('', include(router.urls))
]
