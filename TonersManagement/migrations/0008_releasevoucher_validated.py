# Generated by Django 3.1.3 on 2020-12-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TonersManagement', '0007_auto_20201229_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='releasevoucher',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]
