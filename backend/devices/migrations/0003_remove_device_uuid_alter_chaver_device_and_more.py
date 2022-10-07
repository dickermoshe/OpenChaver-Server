# Generated by Django 4.1.2 on 2022-10-07 01:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_device_updated_device_user_chaver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='chaver',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chavers', to='devices.device'),
        ),
        migrations.AlterField(
            model_name='device',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
