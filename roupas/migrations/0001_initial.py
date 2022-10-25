# Generated by Django 4.1.2 on 2022-10-17 16:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colecoes', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tamanho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Roupa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_roupa', models.CharField(max_length=255)),
                ('preco', models.FloatField()),
                ('data_adicao', models.DateField(default=django.utils.timezone.now)),
                ('foto', models.ImageField(null=True, upload_to='fotos_roupas/')),
                ('t1', models.PositiveIntegerField(default=0)),
                ('t2', models.PositiveIntegerField(default=0)),
                ('t3', models.PositiveIntegerField(default=0)),
                ('t4', models.PositiveIntegerField(default=0)),
                ('t5', models.PositiveIntegerField(default=0)),
                ('t6', models.PositiveIntegerField(default=0)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='roupa', to='roupas.categoria')),
                ('colecao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roupa', to='colecoes.colecao')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='categoria',
            name='tipo_tamanho',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='roupas.tamanho'),
        ),
    ]
