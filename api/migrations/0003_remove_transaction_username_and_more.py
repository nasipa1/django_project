# Generated by Django 5.1.4 on 2024-12-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_transaction_amount_alter_transaction_operation_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transaction",
            name="username",
        ),
        migrations.AlterField(
            model_name="transaction",
            name="operation",
            field=models.CharField(
                choices=[("BUY", "Buy"), ("SELL", "Sell")], max_length=10
            ),
        ),
    ]
