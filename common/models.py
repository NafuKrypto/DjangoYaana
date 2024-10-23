from django.db.models import Model, PositiveIntegerField, PositiveSmallIntegerField
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _

class TapStatus(Model):
    id = PositiveIntegerField(_('id'), primary_key=True)
    title = CharField(_('Title'), max_length=100, blank=True, null=True)
    order = PositiveSmallIntegerField(default=0)
    # class Meta:
