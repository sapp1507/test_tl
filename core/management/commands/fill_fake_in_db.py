from django.core.management import BaseCommand
from tqdm import tqdm

from employee.enums import SectionsEnum
from employee.models import Section, Job, Employee
from utils.fake_generator import fake


class Command(BaseCommand):
    help = 'Заполняет БД фейковыми данными'
    SECTION_COUNT = 25
    EMPLOYEE_COUNT = 50000

    def add_arguments(self, parser):
        parser.add_argument('-s', '--section_count', type=int, default=self.SECTION_COUNT, help='Кол-во подразделений')
        parser.add_argument('-e', '--employee_count', type=int, default=self.EMPLOYEE_COUNT, help='Кол-во сотрудников')
        parser.add_argument('-d', '--delete', action='store_true', help='Удалить все записи из бд')

    def handle(self, *args, **options):
        if options['delete']:
            self.clear_db()
            return
        section_count = options['section_count']
        employee_count = options['employee_count']

        for level in range(SectionsEnum.LEVEL_1.value, SectionsEnum.LEVEL_5.value+1):
            for _ in tqdm(range(section_count // SectionsEnum.LEVEL_5.value), desc=f'Создание Sections level={level}'):
                Section.fake_generator(level)

        sections = Section.objects.all()

        jobs = []
        for _ in tqdm(range(fake.random_int(1000, 30000)), desc='Создание Job'):
            jobs.append(Job.fake_generator())

        Job.objects.bulk_create(jobs)
        jobs = Job.objects.all()

        employees = []
        for _ in tqdm(range(employee_count), desc='Создание Employee'):
            employees.append(
                Employee.fake_generator(
                    job=fake.random_element(jobs),
                    section=fake.random_element(sections)
                )
            )

        Employee.objects.bulk_create(employees)

    def clear_db(self):
        Section.objects.all().delete()
        Job.objects.all().delete()
        Employee.objects.all().delete()


