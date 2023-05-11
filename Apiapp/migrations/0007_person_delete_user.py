# Generated by Django 4.1.7 on 2023-04-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apiapp', '0006_user_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
