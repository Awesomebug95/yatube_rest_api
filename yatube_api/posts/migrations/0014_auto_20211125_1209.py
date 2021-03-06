# Generated by Django 2.2.16 on 2021-11-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20211125_1128'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_user_follower',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='user',
            new_name='author',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('author', 'following'), name='unique_user_follower'),
        ),
    ]
