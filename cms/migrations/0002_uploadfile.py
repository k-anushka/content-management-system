# Generated by Django 5.0.6 on 2024-06-21 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('filename', models.CharField(max_length=10)),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]