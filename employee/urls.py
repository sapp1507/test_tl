from django.urls import path, include
from rest_framework.routers import DefaultRouter

from employee.views import SectionsView, SectionsApiView, EmployeeView

router = DefaultRouter()
router.register('sections', SectionsApiView, basename='sections')
router.register('employee', EmployeeView, basename='employee')

urlpatterns = [
    path('', SectionsView.as_view()),
    path('api/v1/', include(router.urls))
]
