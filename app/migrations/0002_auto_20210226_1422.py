# Generated by Django 3.1.7 on 2021-02-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labreport',
            old_name='mrdnumber',
            new_name='Lab_Number',
        ),
        migrations.AlterField(
            model_name='labreport',
            name='report',
            field=models.FileField(upload_to='LabReport/media/'),
        ),
    ]