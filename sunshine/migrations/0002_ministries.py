
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunshine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ministries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ministry', models.CharField(max_length=40)),
                ('goals', models.CharField(max_length=80)),
                ('mission', models.CharField(max_length=80)),
                ('vision', models.CharField(max_length=80)),
                ('images', models.ImageField(null=True, upload_to='')),
                ('contacts', models.CharField(max_length=80)),
            ],
        ),
    ]
