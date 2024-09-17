from rest_framework import serializers

from employee.models import Section, Job, Employee


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['name']


class EmployeeSerializer(serializers.ModelSerializer):
    job = serializers.CharField(source='job.name')

    class Meta:
        model = Employee
        fields = [
            'id',
            'full_name',
            'wage',
            'job',
            'section'
        ]


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = [
            'id',
            'level',
            'name',
            'parent',
            'sub_sections',
        ]
