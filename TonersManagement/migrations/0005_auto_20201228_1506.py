# Generated by Django 3.1.3 on 2020-12-28 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TonersManagement', '0004_auto_20201128_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrption', models.CharField(max_length=150)),
                ('price', models.FloatField(default=0)),
                ('sim_type', models.CharField(choices=[('MOBILE', 'MOBILE'), ('DATA', 'DATA')], max_length=10)),
            ],
        ),
        migrations.AlterModelOptions(
            name='consumption',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='toner',
            name='color',
            field=models.CharField(choices=[('BK', 'BLACK'), ('MG', 'MAGENTA'), ('CN', 'CYAN'), ('YW', 'YELLOW')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='toner',
            name='toners_type',
            field=models.CharField(choices=[('COMPATIBLE', 'COMPATIBLE'), ('ORIGINAL', 'ORIGINAL')], max_length=100, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='consumption',
            unique_together={('release_voucher', 'toner')},
        ),
        migrations.CreateModel(
            name='Simcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('starting_date', models.DateField()),
                ('operator', models.CharField(choices=[('DJEZZY', 'DJEZZY'), ('MOBILIS', 'MIBILIS'), ('OOREDOO', 'OOREDOO')], max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TonersManagement.customer')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TonersManagement.offer')),
            ],
        ),
    ]
