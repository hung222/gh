# Generated by Django 4.0.2 on 2022-08-23 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='giachoi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tencachchuabenh', models.CharField(max_length=300)),
                ('cachchoi', models.CharField(max_length=500)),
                ('loaibenhdechua', models.CharField(max_length=400)),
            ],
        ),
    ]
