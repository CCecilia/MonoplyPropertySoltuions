# Generated by Django 2.0.1 on 2018-01-05 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
