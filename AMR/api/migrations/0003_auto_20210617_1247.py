# Generated by Django 3.1.7 on 2021-06-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210617_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amr00',
            name='UPDATED_DATE',
            field=models.DateField(blank=True, null=True),
        ),
    ]
