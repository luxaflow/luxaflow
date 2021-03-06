# Generated by Django 2.1.3 on 2018-11-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20181118_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='is_language',
            new_name='language',
        ),
        migrations.AddField(
            model_name='skill',
            name='framework',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='skill',
            name='soft_skill',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='skill',
            name='software',
            field=models.BooleanField(default=False),
        ),
    ]
