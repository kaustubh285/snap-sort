import ollama
from ollama import generate
import time
import glob
from PIL import Image
from io import BytesIO
import os


class ImageOrganizer:
    def __init__(self, *args, **kwargs):
        # self.folder_path = kwargs["folder_path"]
        # if kwargs["folder_path"] == "":
        #     self.folder_path = os.getcwd() + "/test/"

        self.model_name = kwargs["model_name"]
        if kwargs["model_name"] == "":
            self.model_name = "llava:7b"
        return

    def start_processing(self, path, categories) -> None:

        # Guard clause for the path
        if path == "":
            path = os.getcwd() + ""

        self.folder_path = path
        # Execution start time
        st = time.time()

        # Gets all the png images from the path
        image_list = self._get_images(path)

        if len(image_list) == 0:
            print("No images to be sorted in the folder. Target:" + path)
        else:
            print("{0} image(s) found. Sorting them now.".format(len(image_list)))

        for image_path in image_list:
            try:
                self._process_image(image_path, categories)
            except Exception as e:
                print(e)
                print("An Error occured. Check the following")
                print("1)Path is correct")
                print("2)Ollama is running")
                print("3)Model is installed")

        et = time.time()
        elapsed_time = et - st
        print("Execution time:", elapsed_time, "seconds")

    def _get_images(self, folder_path):
        images = []

        types = ["*.png", "*.jpg", "*.jpeg", "*.HEIC"]

        for img_type in types:
            images.extend(
                glob.glob(
                    os.path.join(folder_path, img_type),
                    recursive=True,
                )
            )
        return images

    def _process_image(self, image_path, categories):
        print(f"Processing image: {image_path}")
        with Image.open(image_path) as img:
            with BytesIO() as buffer:
                img.save(buffer, format="PNG")
                image_bytes = buffer.getvalue()

                print("Asking llava about the image...")
                response = generate(
                    model="llava:7b",
                    prompt="Analyze the image content and provide keywords describing it. Use commas to separate the keywords",
                    images=[image_bytes],
                    stream=False,
                )
                keywords = response["response"]
                print("Keywords:", keywords)

                category = self._categorize_keywords(keywords, categories)
                print("Category:", category)

                self._organize_image(image_path, category)

        return

    def _categorize_keywords(self, keywords, categories):

        # categorization logic:
        for category in categories:
            if any(keyword in keywords for keyword in category["keywords"]):
                return category["name"]
            # if any(keyword in keywords for keyword in ["coding", "programming", "code"]):
            #     return "coding"
            # elif any(keyword in keywords for keyword in ["study", "learning", "education"]):
            #     return "studies"
            # elif any(
            #     keyword in keywords for keyword in ["entertainment", "fun", "recreation"]
            # ):
            #     return "recreation"
            # elif any(keyword in keywords for keyword in ["document", "text", "paper"]):
            #     return "document"
            # else:
        return "others"

    def _organize_image(self, image_path, category):
        # Creating a folder for the category, will not create a duplicate if already exists.
        destination_folder = os.path.join(self.folder_path, category)
        os.makedirs(destination_folder, exist_ok=True)

        # moving the image to the new location
        new_image_path = os.path.join(destination_folder, os.path.basename(image_path))
        os.replace(image_path, new_image_path)
        print(f"Image moved to: {new_image_path}")


imageOrganizer = ImageOrganizer(folder_path="", model_name="llava:7b")
