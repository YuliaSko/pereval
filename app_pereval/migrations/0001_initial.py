# Generated by Django 4.2.16 on 2024-11-24 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=10)),
                ('longitude', models.FloatField(max_length=10)),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(choices=[('1A', '1A'), ('1B', '1B'), ('2A', '2A'), ('2B', '2B'), ('3A', '3A'), ('3B', '3B')], max_length=2)),
                ('summer', models.CharField(choices=[('1A', '1A'), ('1B', '1B'), ('2A', '2A'), ('2B', '2B'), ('3A', '3A'), ('3B', '3B')], max_length=2)),
                ('autumn', models.CharField(choices=[('1A', '1A'), ('1B', '1B'), ('2A', '2A'), ('2B', '2B'), ('3A', '3A'), ('3B', '3B')], max_length=2)),
                ('spring', models.CharField(choices=[('1A', '1A'), ('1B', '1B'), ('2A', '2A'), ('2B', '2B'), ('3A', '3A'), ('3B', '3B')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('other_titles', models.CharField(max_length=50)),
                ('connect', models.CharField(max_length=250)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'Новый'), ('pnd', 'На модерации'), ('acp', 'Принято'), ('rej', 'Отклонено')], max_length=3)),
                ('coord_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pereval.coord')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pereval.level')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('fam', models.CharField(max_length=50)),
                ('oct', models.CharField(blank=True, default=None, max_length=50)),
                ('phone', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PerevalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.URLField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('pereval_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pereval.pereval')),
            ],
        ),
        migrations.AddField(
            model_name='pereval',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pereval.user'),
        ),
    ]