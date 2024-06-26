# Generated by Django 5.0.6 on 2024-06-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('quantity_value', models.CharField(choices=[('liters', 'Liters'), ('pieces', 'Pieces'), ('kilos', 'Kilos'), ('grams', 'Grams'), ('packs', 'Packs')], default='pieces', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FoodRecipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('needed_ings_amount', models.PositiveIntegerField(default=0)),
                ('recipe', models.ManyToManyField(to='food.ingredients')),
            ],
        ),
    ]
