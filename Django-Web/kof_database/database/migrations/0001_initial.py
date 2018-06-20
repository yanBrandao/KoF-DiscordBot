# Generated by Django 2.0.5 on 2018-06-20 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dateStart', models.DateField()),
                ('dateEnd', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('picked', models.IntegerField()),
                ('round_win', models.IntegerField()),
                ('round_loss', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game_version',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('version', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('victories', models.IntegerField()),
                ('defeats', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Podium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerPosition', models.IntegerField()),
                ('championship_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Championship')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Round_Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roundWin', models.IntegerField()),
                ('roundDefeated', models.IntegerField()),
                ('char_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Characters')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('characters', models.ManyToManyField(to='database.Characters')),
            ],
        ),
        migrations.AddField(
            model_name='round_score',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Team'),
        ),
        migrations.AddField(
            model_name='matches',
            name='players',
            field=models.ManyToManyField(to='database.Player'),
        ),
        migrations.AddField(
            model_name='characters',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Game_version'),
        ),
    ]
