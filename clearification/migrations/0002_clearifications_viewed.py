# Generated by Django 2.1.7 on 2019-06-29 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clearification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='clearifications_viewed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('clearifications_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clearification.clearifications')),
            ],
        ),
    ]
