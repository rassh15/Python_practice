# Generated by Django 4.0 on 2022-02-09 11:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='caption',
            field=models.ManyToManyField(to='mblog.Tag'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mblog.author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='caption',
        ),
        migrations.AddField(
            model_name='tag',
            name='caption',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
