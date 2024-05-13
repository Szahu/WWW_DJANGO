from django.core.management.base import BaseCommand, CommandError
from obrazki.models import Picture, Rectangle
from django.utils import timezone
from django.contrib.auth.models import User

import random

class Command(BaseCommand):
    help = 'Adds a random picture'


    def handle(self, *args, **options):
        width = random.randint(100, 1000)
        height = random.randint(100, 1000)
        # List of English words
        english_words = ["apple", "banana", "car", "dog", "elephant", "flower", "guitar", "house", "island", "jungle"]

        # Generate two random words
        word1 = random.choice(english_words)
        word2 = random.choice(english_words)

        name = f"{word1} {word2}"

        picture = Picture(name=name, size_x=width, size_y=height, pub_date=timezone.now())
        picture.save()
        picture.editors.add(User.objects.get(username="admin"))
        picture.save()

        num_of_rects = random.randint(1, 10)
        for i in range(num_of_rects):
            rect = Rectangle(width=random.randint(10, width), height=random.randint(10, height),
                             color=f"#{random.randint(0, 0xFFFFFF):06x}",
                             x=random.randint(0, width), y=random.randint(0, height))
            rect.save()
            picture.rectangles.add(rect)

        self.stdout.write(self.style.SUCCESS(f"Successfully added picture with {num_of_rects} rectangles"))