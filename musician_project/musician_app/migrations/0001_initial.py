# Generated by Django 3.2.3 on 2021-05-20 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('release_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician_app.album')),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician_app.musician')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='musician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician_app.musician'),
        ),
    ]