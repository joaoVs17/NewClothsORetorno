# Generated by Django 4.1.2 on 2022-10-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0008_alter_pedido_usuario_pedinte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('NF', 'Pedido não realizado!'), ('FE', 'Pedido encaminhado!'), ('EV', 'Pedido enviado!'), ('ET', 'Entregue!'), ('DV', 'Pedido devolvido!')], max_length=2),
        ),
        migrations.DeleteModel(
            name='StatusPedido',
        ),
    ]