# Generated by Django 4.0 on 2022-02-10 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mblog', '0002_post_caption_alter_author_email_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='caption',
            new_name='tags',
        ),
    ]
