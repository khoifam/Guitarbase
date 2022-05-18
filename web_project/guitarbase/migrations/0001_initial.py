# Generated by Django 4.0.3 on 2022-04-27 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=360)),
                ('capo', models.IntegerField()),
                ('tuning', models.CharField(max_length=120)),
                ('url', models.URLField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guitarbase.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verse_chord_prog', models.CharField(max_length=360)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guitarbase.song')),
            ],
        ),
        migrations.CreateModel(
            name='Chorus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chorus_chord_prog', models.CharField(max_length=360)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guitarbase.song')),
            ],
            options={
                'verbose_name_plural': 'Choruses',
            },
        ),
        migrations.CreateModel(
            name='Bridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bridge_chord_prog', models.CharField(max_length=360)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guitarbase.song')),
            ],
        ),
    ]
