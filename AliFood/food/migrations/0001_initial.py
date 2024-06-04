# Generated by Django 5.0.3 on 2024-06-04 19:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tarkibi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lavash_tarkib', models.TextField()),
                ('burger_tarkib', models.TextField()),
                ('kfc_tarkib', models.TextField()),
                ('pitsa_tarkib', models.TextField()),
                ('hotdog_tarkib', models.TextField()),
                ('umumiy_tarkib', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='food_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.foodtype'),
        ),
        migrations.AddField(
            model_name='food',
            name='tarkibi',
            field=models.ManyToManyField(to='food.tarkibi'),
        ),
    ]