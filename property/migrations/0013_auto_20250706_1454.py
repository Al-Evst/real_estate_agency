from django.db import migrations


def link_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.iterator():
        if not flat.owner:
            continue

        owner, _ = Owner.objects.get_or_create(
            full_name=flat.owner,
            phone_number=flat.owners_phonenumber,
            defaults={'pure_phone': flat.owner_pure_phone}
        )

       
        flat.owners.set([owner])


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_remove_owner_flats_flat_owners'), 
    ]

    operations = [
        migrations.RunPython(link_owners),
    ]