# Generated by Django 2.1.2 on 2018-11-23 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('dt_nasc', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('sexo', models.CharField(max_length=1)),
            ],
        ),
    ]
