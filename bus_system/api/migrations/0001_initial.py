# Generated by Django 4.1.7 on 2023-11-12 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timing', models.DateTimeField()),
                ('destination', models.CharField(max_length=100)),
                ('fare', models.DecimalField(decimal_places=2, max_digits=5)),
                ('capacity', models.PositiveIntegerField(default=50)),
            ],
        ),
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='bus_stop_images/')),
            ],
        ),
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bus_detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.busdetail')),
            ],
        ),
        migrations.AddField(
            model_name='busdetail',
            name='bus_stop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.busstop'),
        ),
    ]
