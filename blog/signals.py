from django.contrib.auth.models import Group, Permission


def create_groups_permissions(sender, **kwargs):
    #importing Group model and create groups
    readers_group = Group.objects.get_or_create(name="Readers")
    authours_group = Group.objects.get_or_create(name="Authors")
    editors_group = Group.objects.get_or_create(name="Editors")

    #creating a permissions for readers
    readers_permission = [
        Permission.objects.get(codename="view_post")
    ]
    
    #creating a permissions for authours
    authours_permisssion = [
        Permission.objects.get(codename="add_post"),
        Permission.objects.get(codename="change_post"),
        Permission.objects.get(codename="delete_post"),
    ]

    #editors permissions creating manually withh reference of content type table
    editors_permisssion = [
        Permission.objects.get_or_create(codename="can_publish", content_type_id = 7, name = "Can Publish Post"),
        Permission.objects.get(codename="add_post"),
        Permission.objects.get(codename="change_post"),
        Permission.objects.get(codename="delete_post"),

    ]

