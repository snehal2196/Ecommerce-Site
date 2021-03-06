# Generated by Django 3.2.4 on 2021-10-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('zip_code', models.TextField()),
            ],
        ),
    ]
