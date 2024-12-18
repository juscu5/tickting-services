from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Ticket
from .serializers import TicketSerializer
from django.db import transaction, connection

@api_view(['GET'])
def GetTicket(request):
    ticket = Ticket.objects.all()
    serializer = TicketSerializer(ticket, many=True)
    return Response(serializer.data)

@transaction.atomic
@api_view(['POST'])
def AddTicket(request, ticket_name, ticket_desc):
    data = {'ticket_name': ticket_name, 'ticket_desc': ticket_desc}
    serializer = TicketSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def RawSQLGet(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Ticket_Table")

        #Convert SQL Result to JSON
        data = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]

        #Serialize the JSON Converted result
        serializer = TicketSerializer(data, many=True)
    return Response(serializer.data)