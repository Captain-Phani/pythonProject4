# Generated by Django 4.2.11 on 2024-03-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_deletion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('INACTIVE', 'inactive')], default='inactive', max_length=100),
            preserve_default=False,
        ),
    ]
