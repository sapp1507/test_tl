from django.db import models

from utils.fake_generator import fake
from utils.models import SoftDeletionModel


class Section(SoftDeletionModel):
    name = models.CharField(max_length=128, verbose_name='Название')
    parent = models.ForeignKey(
        'Section',
        null=True,
        blank=True,
        related_name='sub_sections',
        verbose_name='Родительское подразделение',
        on_delete=models.SET_NULL,
    )

    @classmethod
    def fake_generator(cls) -> 'Section':
        return cls(name=fake.company())

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Job(SoftDeletionModel):
    name = models.CharField(max_length=128, verbose_name='Название')

    @classmethod
    def fake_generator(cls) -> 'Job':
        return cls(name=fake.job())

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Employee(models.Model):
    first_name = models.CharField(
        max_length=64,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=64,
        verbose_name='Фамилия'
    )
    sur_name = models.CharField(
        max_length=64,
        verbose_name='Отчество',
        null=True,
        blank=True
    )
    wage = models.PositiveIntegerField(verbose_name='Заработная плата')

    job = models.ForeignKey(
        Job,
        null=True,
        blank=True,
        related_name='employees',
        verbose_name='Должность',
        on_delete=models.SET_NULL,
    )
    section = models.ForeignKey(
        Section,
        null=True,
        blank=True,
        related_name='employees',
        verbose_name='Подразделение',
        on_delete=models.SET_NULL,
    )

    @classmethod
    def fake_generator(cls, job=None, section=None) -> 'Employee':
        return cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            sur_name=fake.middle_name(),
            wage=fake.random_int(1000000, 50000000),
            job=job,
            section=section
        )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
