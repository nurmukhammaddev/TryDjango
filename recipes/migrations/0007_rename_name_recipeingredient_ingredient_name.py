# Generated by Django 4.1 on 2022-08-23 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_tag_recipe_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='name',
            new_name='ingredient_name',
        ),
    ]