# Screenshot Organizer

Snap Sort is a python script written to organize your screenshots based on their content. It uses the `LLaVA` model (https://llava-vl.github.io/) for image analysis, and providing keywords to determine the screenshot category. The script has five predefined categories: 'studies', 'coding', 'recreation', 'document', and 'others'. More can be added or updated, based on requirement.

## Installation

1. Clone the repository to your local machine:

```bash

git clone https://github.com/kaustubh285/snap-sort.git

```

2. Install the required dependencies:

```bash

pip install -r requirements.txt

```

3. Create a new Python script (e.g., `run_organizer.py`) to execute the organizer file:

```python

import os

from image_organizer import ImageOrganizer



imageOrganizer =  ImageOrganizer(model_name="llava:7b")



# Depending on where the executing file is stored, set the absolute path.

path = os.getcwd()  +  "/images/"

imageOrganizer.start_processing(path=path,  categories=[{"name":  "coding",  "keywords":  ["coding",  "programming",  "code"]},{"name":  "studies",  "keywords":  ["study",  "learning",  "education"]}])



```

## Usage

This script will process the images in the specified folder (or the images folder within the current working directory if no path is provided) and categorize them based on their content. The categorized images will be moved into subfolders for each category.

Running the script:

```bash

python  run_organizer.py

```

Note: In case of any doubts, check the sample_run_organizer.py file for structure.

## Supported formats

The script currently supports jpg, jpeg, png and heic formats.

## Configuration

You can customize the behavior of the script by adjusting the parameters in the `ImageOrganizer` class. Open the `run_organizer.py` file and modify the following parameters:

- `folder_path`: Set the target folder path for organizing screenshots.

- `model_name`: Set the name of the `ollama` model to be used for image analysis.

- `categories`: The categories you want the images to be organised in. Is has to be an array of objects containing the name of the category, and the keywords for it.

```python

imageOrganizer =  ImageOrganizer(model_name="llava:7b")

imageOrganizer.start_processing(path=os.getcwd()  +  "/test/",  categories=[{"name":  "coding",  "keywords":  ["coding",  "programming",  "code"]},{"name":  "studies",  "keywords":  ["study",  "learning",  "education"]}])

```

## Dependencies

- ollama

Ollama needs to be installed from the website (ollama.com). Additionally, llava 7b model also needs to be downloaded (` ollama pull llava:7b`).

- Pillow

- OpenCV
