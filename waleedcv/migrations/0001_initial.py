# Generated by Django 4.2.4 on 2023-08-11 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Subject', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('Message', models.TextField()),
            ],
        ),
    ]
