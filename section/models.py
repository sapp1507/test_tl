from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')

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
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
