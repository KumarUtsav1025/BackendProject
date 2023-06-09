# Generated by Django 4.1.4 on 2023-03-27 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0009_alter_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
