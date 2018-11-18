# Generated by Django 2.1.3 on 2018-11-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_education_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='school',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='company',
            new_name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
