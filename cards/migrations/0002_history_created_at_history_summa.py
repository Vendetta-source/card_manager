# Generated by Django 4.1.3 on 2022-12-05 16:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='summa',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
