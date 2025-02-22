# Generated by Django 4.2.7 on 2023-11-17 15:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('ticket_name', models.CharField(max_length=200)),
                ('ticket_desc', models.CharField(max_length=500)),
                ('ticket_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Ticket_Table',
            },
        ),
    ]
