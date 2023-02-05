
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunshine', '0008_ministries_leader'),
    ]

    operations = [
        migrations.AddField(
            model_name='head',
            name='pastor',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
