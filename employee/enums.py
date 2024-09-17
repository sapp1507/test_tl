from django.db.models import IntegerChoices


class SectionsEnum(IntegerChoices):
    LEVEL_1 = 1, 'Первый уровень'
    LEVEL_2 = 2, 'Второй уровень'
    LEVEL_3 = 3, 'Третий уровень'
    LEVEL_4 = 4, 'Четвертый уровень'
    LEVEL_5 = 5, 'Пятый уровень'
