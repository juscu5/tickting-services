from asyncio import exceptions
from django.db import models
import uuid

class UniqueIdentifierField(models.UUIDField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('default', uuid.uuid4)
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        if self.primary_key:
            return 'uniqueidentifier DEFAULT NEWSEQUENTIALID() PRIMARY KEY'
        else:
            return 'uniqueidentifier'

    def rel_db_type(self, connection):
        return 'uniqueidentifier'

    def contribute_to_class(self, cls, name, **kwargs):
        assert not self.primary_key or (self.primary_key and not cls._meta.auto_field), "A model can't have more than one AutoField."
        super().contribute_to_class(cls, name, **kwargs)
        if self.primary_key:
            cls._meta.auto_field = self

    def get_db_prep_value(self, value, connection, prepared=False):
        if value is None:
            return None
        if not isinstance(value, uuid.UUID):
            value = self.to_python(value)

        return str(value)

    def from_db_value(self, value, expression, connection):
        return self._to_uuid(value)

    def to_python(self, value):
        return self._to_uuid(value)

    def _to_uuid(self, value):
        if value is not None and not isinstance(value, uuid.UUID):
            try:
                return uuid.UUID(value)
            except (AttributeError, ValueError):
                raise exceptions.ValidationError(
                    self.error_messages['invalid'],
                    code='invalid',
                    params={'value': value},
                )
        return value