from django.contrib import admin

from core.django_admin.admin import BaseAdminModel
from employee.models import Job, Employee, Section


@admin.register(Section)
class SectionAdmin(BaseAdminModel):
    fields = ['id', 'name', 'show_sub_sections']

    def show_sub_sections(self, section: Section):
        """Возвращает ссылку на список дочерних подразделений."""

        count = section.sub_sections.count()
        if count == 0:
            return self.get_html_bool(False)

        url = self.get_url_change_list(
            Section,
            {'sub_sections__id': section.id}
        )
        return self.get_link(url, f'{count} подразделений')
    show_sub_sections.short_description = 'Дочерние подразделения'


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    fields = ['id']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ['id']
