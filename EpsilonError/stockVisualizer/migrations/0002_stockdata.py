# Generated by Django 4.2.7 on 2023-11-18 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockVisualizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.TextField(null=True)),
                ('data', models.TextField(null=True)),
            ],
        ),
    ]
