# Generated by Django 4.1.7 on 2023-04-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_services_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='icon_class',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
