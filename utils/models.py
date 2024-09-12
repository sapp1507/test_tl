from django.db import models

from datetime import datetime as dt


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super(SoftDeleteManager, self).get_queryset().filter(deleted_at=None)


class SoftDeletionModel(models.Model):
    """Добавляет к модели поле с датой удаления объекта, переопределяет метод delete."""

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        default=None
    )
    deleted_by = models.IntegerField(
        null=True,
        blank=True,
        default=None,
    )
    objects = SoftDeleteManager()
    objects_all = models.Manager()

    def delete(self, force=False, *args, **kwargs):
        if force:
            super(SoftDeletionModel, self).delete()
            return
        user = kwargs.get('user', None)
        self.deleted_at = dt.now()
        self.deleted_by = user.pk if user is not None else None
        self.save()

    class Meta:
        abstract = True
