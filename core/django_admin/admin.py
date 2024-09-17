from django.contrib.admin import ModelAdmin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode


class BaseAdminModel(ModelAdmin):
    """Базовая модель Django Admin."""

    def get_link(self, url, text='', target=''):
        """Возвращает ссылку в html формате"""
        return format_html(
            '<a href="{}" target="{}">{}</a>'.format(url, target, text))

    def get_url_change_list(self, model, param):
        """Возвращает ссылку на список объектов модели."""

        return reverse('admin:%s_%s_changelist' % (
            model._meta.app_label, model._meta.model_name)
                       ) + '?' + urlencode(param)

    def get_url_change(self, model, args):
        """Возвращает ссылку на объект модели"""
        return reverse('admin:%s_%s_change' % (
            model._meta.app_label, model._meta.model_name),
                       args=args)

    def get_html_bool(self, value):
        icon = '/static/admin/img/icon-yes.svg' if value else '/static/admin/img/icon-no.svg'

        return format_html(f'<img src="{icon}"')
