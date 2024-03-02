# Generated by Django 5.0.2 on 2024-02-28 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_doctors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='doc_spec',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_phone', models.CharField(max_length=100)),
                ('p_email', models.EmailField(max_length=254)),
                ('booked_on', models.DateField(auto_now=True)),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.doctors')),
            ],
        ),
    ]
