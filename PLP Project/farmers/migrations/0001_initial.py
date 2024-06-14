# Generated by Django 4.1.7 on 2023-06-28 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(default='DEFAULT VALUE', upload_to='profile_pics/')),
                ('bio', models.TextField(blank=True, default='My Bio', max_length=300)),
                ('name', models.CharField(blank=True, max_length=120)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='DEFAULT VALUE', upload_to='images/')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('likes', models.IntegerField(default=0)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='farmers.profile')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='farmers.profile')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='farmers.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='farmers.image')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='farmers.profile')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
