from blog.models import Category
from typing import Any
from django.core.management.base import BaseCommand



 # here im giving forloop variable


class Command(BaseCommand):
    help = "This commands insert category data"

    def handle(self, *args: Any, **options: Any):
        #Delete existing data
        Category.objects.all().delete()

        categories = ['Sports', 'Technology', 'Science', 'Art', 'Food']


 
        for category_name in categories:
            Category.objects.create(name = category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
        
    


 
