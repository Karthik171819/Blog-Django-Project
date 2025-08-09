from django.contrib.auth.models import Group, Permission

def create_groups_permissions(sender, **kwargs):
    try:
        # Creating groups
        readers_group,created  = Group.objects.get_or_create(name="Readers")
        authors_group,created  = Group.objects.get_or_create(name="Authors")
        editors_group,created = Group.objects.get_or_create(name="Editors")

        # Permissions for Readers
        readers_permission = [
            Permission.objects.get(codename="view_post")
        ]

        # Permissions for Authors
        authors_permission = [
            Permission.objects.get(codename="add_post"),
            Permission.objects.get(codename="change_post"),
            Permission.objects.get(codename="delete_post"),
        ]

        #editors permissions creating manually with reference of content type table
        can_publish, created =  Permission.objects.get_or_create(codename="can_publish", content_type_id = 7, name = "Can Publish Post")
        editors_permission = [
            can_publish,
            Permission.objects.get(codename="add_post"),
            Permission.objects.get(codename="change_post"),
            Permission.objects.get(codename="delete_post"),

        ]

        # Assigning permissions to groups
        readers_group.permissions.set(readers_permission)
        authors_group.permissions.set(authors_permission)
        editors_group.permissions.set(editors_permission)
        print("Groups and Permissions created successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
