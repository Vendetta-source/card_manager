# Generated by Django 4.1.3 on 2022-12-05 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.PositiveIntegerField()),
                ('number', models.PositiveBigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date_end', models.DateTimeField()),
                ('use_date', models.DateTimeField()),
                ('summa', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive'), ('Overdue', 'Overdue')], max_length=10)),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase', models.CharField(max_length=500)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.card')),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'История',
            },
        ),
    ]
