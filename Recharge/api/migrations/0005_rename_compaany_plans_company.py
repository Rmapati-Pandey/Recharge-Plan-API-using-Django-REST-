# Generated by Django 4.1.3 on 2022-12-11 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_plans_sms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plans',
            old_name='compaany',
            new_name='company',
        ),
    ]
