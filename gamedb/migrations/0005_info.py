# Generated by Django 3.1.4 on 2021-01-16 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamedb', '0004_auto_20210116_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev', models.CharField(max_length=50)),
                ('releasee_date', models.DateField()),
                ('genre', models.CharField(max_length=50)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamedb.game')),
                ('platform', models.ManyToManyField(to='gamedb.Platform')),
            ],
        ),
    ]