# Generated by Django 4.2 on 2023-04-19 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(db_index=True, unique=True, verbose_name='Название набора тем')),
            ],
            options={
                'verbose_name': 'Набор тем для меню',
                'db_table': 'menu_setup',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='MenuTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_value', models.TextField(db_index=True, unique=True, verbose_name='Тема')),
                ('menu_setup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menusetup')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
                'db_table': 'titles',
                'ordering': ['title_value'],
            },
        ),
        migrations.CreateModel(
            name='MenuSubtitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle_value', models.TextField(db_index=True, verbose_name='Подтема')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menutitle')),
            ],
            options={
                'verbose_name': 'Подтема',
                'verbose_name_plural': 'Подтемы',
                'db_table': 'subtitles',
                'ordering': ['subtitle_value'],
            },
        ),
    ]