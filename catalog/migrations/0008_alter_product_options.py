# Generated by Django 5.1.3 on 2024-12-24 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_alter_product_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "permissions": [("can_unpublish_product", "Can unpublish product")],
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
    ]
