# Generated by Django 2.0 on 2020-03-19 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_project_data_current_money'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_tags',
            name='tag_id',
        ),
        migrations.AddField(
            model_name='project_tags',
            name='tag',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
