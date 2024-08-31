# Generated by Django 5.1 on 2024-08-28 19:59

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
            name='Profile',
            fields=[
                ('id_user', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('bio', models.TextField(blank=True, default='')),
                ('profile_img', models.ImageField(default='https://tse2.mm.bing.net/th?id=OIG4.xDrW4Yp4C8ElAsk2hZSZ&w=270&h=270&c=6&r=0&o=5&pid=ImgGn', upload_to='profile_images')),
                ('location', models.CharField(blank=True, default='', max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
