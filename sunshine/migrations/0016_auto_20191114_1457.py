
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sunshine', '0015_auto_20191114_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
