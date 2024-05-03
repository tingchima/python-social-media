# Generated by Django 5.0.4 on 2024-04-29 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                (
                    'last_login',
                    models.DateTimeField(blank=True, null=True, verbose_name='last login'),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(db_comment='username', default='', max_length=255)),
                (
                    'email',
                    models.EmailField(
                        db_comment='email', db_index=True, max_length=255, unique=True
                    ),
                ),
                (
                    'user_type',
                    models.CharField(
                        choices=[(1, 'Common'), (2, 'Official')],
                        db_comment='type of user',
                        default=1,
                    ),
                ),
                ('avatar_url', models.URLField(db_comment='url of user avatar', default='')),
                (
                    'is_disabled',
                    models.BooleanField(db_comment='status of user was not actived', default=False),
                ),
                (
                    'disabled_at',
                    models.DateTimeField(
                        db_comment='the datetime of user was not actived', null=True
                    ),
                ),
            ],
            options={
                'db_table': 'users',
                'db_table_comment': 'user data',
            },
        ),
    ]