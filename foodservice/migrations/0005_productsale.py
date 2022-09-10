# Generated by Django 4.0.4 on 2022-09-08 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0003_newregister'),
        ('foodservice', '0004_productbrand_company_worker_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='default.company')),
                ('company_worker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='default.companyworker')),
            ],
            options={
                'verbose_name': 'Produto para Venda',
                'verbose_name_plural': 'Produtos para Venda',
                'ordering': ('name',),
            },
        ),
    ]
