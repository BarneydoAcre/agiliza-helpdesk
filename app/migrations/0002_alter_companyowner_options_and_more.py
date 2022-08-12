# Generated by Django 4.0.4 on 2022-08-09 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyowner',
            options={'ordering': ('person',), 'verbose_name': 'Company Owner', 'verbose_name_plural': 'Company Owners'},
        ),
        migrations.AlterModelOptions(
            name='companyworkerposition',
            options={'ordering': ('companyWorker',), 'verbose_name': 'Company Worker Position', 'verbose_name_plural': 'Company Worker Positions'},
        ),
        migrations.RemoveField(
            model_name='companyworker',
            name='position',
        ),
    ]
