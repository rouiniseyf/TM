# Generated by Django 3.1.3 on 2020-11-23 19:14

import TonersManagement.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Toner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('color', models.CharField(choices=[('BLACK', 'BLACK'), ('MAGENTA', 'MAGENTA'), ('CYAN', 'CYAN'), ('YELLOW', 'YELLOW')], max_length=10, null=True)),
                ('toners_type', models.CharField(choices=[('Compatible', 'Compatible'), ('Original', 'Original')], max_length=100, null=True)),
                ('Quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseVoucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_number', models.CharField(default=TonersManagement.models.increment_invoice_number, max_length=9)),
                ('release_date', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TonersManagement.customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TonersManagement.direction'),
        ),
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('release_voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TonersManagement.releasevoucher')),
                ('toner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TonersManagement.toner')),
            ],
        ),
    ]