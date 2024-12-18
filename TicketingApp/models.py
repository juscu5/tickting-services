from django.db import models
import uuid

class Ticket(models.Model):
    ticket_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket_name = models.CharField(max_length=200)
    ticket_desc = models.CharField(max_length=500)
    ticket_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Ticket_Table"