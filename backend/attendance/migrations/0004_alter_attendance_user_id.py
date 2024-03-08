# Generated by Django 4.2.9 on 2024-02-27 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0003_alter_attendance_attendance_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='user_id',
            field=models.ForeignKey(help_text='사용자 ID', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
