# Generated by Django 2.1.7 on 2019-04-10 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_chathistory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChatHistory',
            new_name='Message',
        ),
    ]
