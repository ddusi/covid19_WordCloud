# Generated by Django 3.1 on 2020-09-01 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Covid_web', '0005_delete_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('ques', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Covid_web.question')),
            ],
        ),
    ]