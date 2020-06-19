# Generated by Django 3.0.5 on 2020-06-19 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Bath Date')),
                ('chinchilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Chinchilla')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
