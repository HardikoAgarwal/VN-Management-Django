# Generated by Django 4.2.14 on 2024-07-12 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_customer_email_remove_customer_phone_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
