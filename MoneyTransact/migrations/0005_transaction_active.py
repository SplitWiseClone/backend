# Generated by Django 4.1.4 on 2023-01-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoneyTransact', '0004_remove_transaction_giver_transaction_giver'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
