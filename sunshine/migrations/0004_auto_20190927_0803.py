from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunshine', '0003_auto_20190927_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(null=True, upload_to='media/carousels'),
        ),
    ]
