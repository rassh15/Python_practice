# Generated by Django 4.0 on 2022-02-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_address_author_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='published_countires',
            field=models.ManyToManyField(to='book_outlet.Country'),
        ),
    ]
