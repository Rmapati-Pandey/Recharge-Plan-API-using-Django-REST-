# Generated by Django 4.1.3 on 2022-12-10 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_plans'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plans',
            old_name='call',
            new_name='voice',
        ),
    ]
