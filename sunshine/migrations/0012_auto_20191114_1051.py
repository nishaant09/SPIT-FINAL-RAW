
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunshine', '0011_head_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='head',
            name='departmentaim',
        ),
        migrations.AddField(
            model_name='head',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
