# Generated by Django 2.2.17 on 2020-12-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='name',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='test',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
