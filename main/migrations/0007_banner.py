# Generated by Django 4.1.1 on 2022-09-21 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_product_price_productattribute'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=250)),
                ('alt_text', models.CharField(max_length=300)),
            ],
        ),
    ]