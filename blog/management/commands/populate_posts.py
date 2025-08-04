from blog.models import Post, Category
from typing import Any
from django.core.management.base import BaseCommand
import random



 # here im giving forloop variable


class Command(BaseCommand):
    help = "This commands insert posts data"

    def handle(self, *args: Any, **options: Any):
        #Delete existing data
        Post.objects.all().delete()


        titles =[
    "the Future of AI",
    "Climate Change Solitions",
    "Remote Work Trends",
    "Quantumn Computing Explanation",
    "Rnewable Energy Inovation",
    "Deep Learning",
    "Post-Pandemic Outlook",
    "Blockchain in Finance",
]

        contents = [
    "AI occupy the whole world",
    "climate disaster would lead us badly in nature conflicts to the future genratin",
    " digital era Techies are more likely to work on own pace without pressure like WFH",
    "dsncdsjkcnjcb  djbcb jnjdcncxn mnjnjc nbdjcbbnj huefjnsjdn ehdsjbncjn iwiekjcsnj uhdj",
    "lorem jnasknxkm  iosxnnzjb  uhsjcnjnn uhjscajb ggvfbv iohdiuncx  hnjvndshb yguhbf ijIn ",
    "20 dhbcvbh  uhjbsdjcn   iuyehfujcn uhuefhknds hjenfskc jklnfvn uhefwsiljdvhyt wudhjnchj",
    "gefbchjnbdsc uhujudnksjnxk iiewjoskmcb, wuiehijkivmdbdsjkkml hjndklvmksmioefkn huekjvn",
    " ehfdskjbncjknkjcsmn hkjncskmn  iefjdsklvmklmn hfejkcnklsn ijuikijm juijgnkm iiknf jklm",
]

        img_urls = [
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
]
        
        categories = Category.objects.all()
        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
        
    


 
