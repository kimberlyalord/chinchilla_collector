# Generated by Django 3.0.5 on 2020-06-19 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_bath'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Feeding Date')),
                ('meal', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1)),
                ('chinchilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Chinchilla')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]