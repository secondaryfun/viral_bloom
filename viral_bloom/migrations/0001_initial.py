# Generated by Django 3.0.7 on 2020-06-26 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Covid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('state', models.CharField(max_length=100)),
                ('positive', models.IntegerField()),
                ('death', models.IntegerField()),
                ('recovered', models.IntegerField()),
            ],
        ),
    ]
