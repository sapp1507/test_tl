from django.contrib import admin
from django.urls import path, include

urlpatterns_api_v1 = [
    path('api/v1/', include('employee.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    *urlpatterns_api_v1
]
