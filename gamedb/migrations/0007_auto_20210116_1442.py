# Generated by Django 3.1.4 on 2021-01-16 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamedb', '0006_auto_20210116_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='platform',
            field=models.ManyToManyField(related_name='platforms', to='gamedb.Platform'),
        ),
    ]
