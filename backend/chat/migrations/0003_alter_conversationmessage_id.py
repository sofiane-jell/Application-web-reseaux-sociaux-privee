# Generated by Django 5.0.3 on 2024-04-17 08:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_conversation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationmessage',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
