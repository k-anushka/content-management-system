# Generated by Django 5.0.6 on 2024-06-22 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_remove_uploadfile_file_remove_uploadfile_id_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='uploadfile',
            unique_together={('filename', 'type')},
        ),
    ]
