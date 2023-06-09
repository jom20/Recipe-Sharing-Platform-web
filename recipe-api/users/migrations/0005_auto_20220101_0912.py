# Generated by Django 3.2.9 on 2022-01-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_recipelike'),
        ('users', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favorites',
        ),
        migrations.AddField(
            model_name='profile',
            name='bookmarks',
            field=models.ManyToManyField(related_name='bookmarked_by', to='recipe.Recipe'),
        ),
    ]
