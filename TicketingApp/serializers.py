from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'ticket_id',
            'ticket_name',
            'ticket_desc',
            'ticket_created'
        ]

class TicketJoingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'testing',
            'testing1'
        ]