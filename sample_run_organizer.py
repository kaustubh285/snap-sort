from image_organizer import ImageOrganizer
import os


categories = [
    {"name": "coding", "keywords": ["coding", "programming", "code"]},
    {"name": "studies", "keywords": ["study", "learning", "education"]},
    {
        "name": "recreation",
        "keywords": ["entertainment", "fun", "recreation"],
    },
    {"name": "document", "keywords": ["document", "text", "paper"]},
]

imageOrganizer = ImageOrganizer(model_name="llava:7b")
imageOrganizer.start_processing(path=os.getcwd() + "/test/", categories=categories)
