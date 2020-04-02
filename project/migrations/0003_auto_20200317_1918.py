# Generated by Django 2.0 on 2020-03-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20200317_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project_comments',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='project_pics',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='project_tags',
            old_name='project_id',
            new_name='project',
        ),
        migrations.AlterField(
            model_name='project_pics',
            name='image',
            field=models.ImageField(upload_to='project/static/project_pics/'),
        ),
    ]
