# Generated by Django 4.0.5 on 2022-08-03 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.TextField(max_length=80)),
                ('tel', models.TextField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('comment', models.TextField(max_length=255)),
                ('partner', models.ForeignKey(on_delete=models.SET('deleted'), to='app3.partners')),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.TextField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.TextField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_date', models.DateField()),
                ('out_date', models.DateField()),
                ('ready', models.BooleanField(default=False)),
                ('comment', models.TextField(max_length=255)),
                ('contact', models.ForeignKey(on_delete=models.SET('deleted'), to='app3.people')),
                ('partner', models.ForeignKey(on_delete=models.SET('deleted'), to='app3.partners')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=15)),
                ('sn', models.TextField(max_length=20)),
                ('integrity', models.BooleanField(default=True)),
                ('tech', models.TextField(max_length=4096)),
                ('comment', models.TextField(max_length=512)),
                ('place', models.ForeignKey(on_delete=models.SET('deleted'), to='app3.places')),
                ('responsible', models.ForeignKey(on_delete=models.SET('deleted'), to='app3.people')),
                ('shipment', models.ForeignKey(on_delete=models.SET('deleted'), to='app3.shipments')),
                ('status', models.ForeignKey(on_delete=models.SET('deleted'), to='app3.status')),
                ('typ', models.ForeignKey(on_delete=models.SET('deleted'), to='app3.types')),
                ('vendor', models.ForeignKey(on_delete=models.SET('deleted'), to='app3.vendors')),
            ],
        ),
    ]
