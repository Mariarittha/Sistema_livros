# Generated by Django 4.2.3 on 2023-07-30 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Livros', '0002_livros_descricao_alter_livros_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='descricao',
            field=models.CharField(max_length=500),
        ),
    ]
