# Generated by Django 2.0.1 on 2018-01-05 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20180105_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='top_four',
            field=models.BooleanField(default=True),
        ),
    ]
