# Generated by Django 5.0.4 on 2024-05-01 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='last_message_timestamp',
            field=models.PositiveIntegerField(db_comment='the last message of created at timestmap', default=0, null=True),
        ),
        migrations.AlterField(
            model_name='chatroommember',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='chat.chatroom'),
        ),
    ]