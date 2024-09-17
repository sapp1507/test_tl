from django.db import models

from employee.enums import SectionsEnum
from utils.fake_generator import fake
from utils.models import SoftDeletionModel


class Section(SoftDeletionModel):
    level = models.SmallIntegerField(
        choices=SectionsEnum,
        default=SectionsEnum.LEVEL_1,
        verbose_name='Уровень'
    )
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
    def fake_generator(cls, level: int) -> 'Section':
        section = cls.objects.create(name=fake.company(), level=level)
        if section.level > SectionsEnum.LEVEL_1.value:
            section.parent = fake.random_element(Section.objects.filter(level=section.level-1))
            section.save()
        return section

    def __str__(self):
        return self.name[:20]

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Job(SoftDeletionModel):
    name = models.CharField(max_length=128, verbose_name='Название')

    @classmethod
    def fake_generator(cls) -> 'Job':
        return cls(name=fake.job())

    def __str__(self):
        return self.name

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

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.sur_name}'

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
