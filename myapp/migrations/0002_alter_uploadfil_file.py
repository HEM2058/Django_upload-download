# Generated by Django 4.1.4 on 2022-12-17 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfil',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
