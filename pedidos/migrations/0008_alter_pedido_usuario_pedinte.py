# Generated by Django 4.1.2 on 2022-10-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_item_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='usuario_pedinte',
            field=models.CharField(max_length=255),
        ),
    ]
