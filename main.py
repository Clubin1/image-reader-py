import os
import glob
from PIL import Image #type:ignore 
import pytesseract #type:ignore 

def process_image(image_path): 
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return image_path, text
    except Exception as e:
        return image_path, str(e)
    
def get_all_image_names(directory):
    image_names = []
    inputs_folder = os.path.join(directory, 'inputs')
    if os.path.exists(inputs_folder):
        image_files = glob.glob(os.path.join(inputs_folder, '*.jpg')) + glob.glob(os.path.join(inputs_folder, '*.png')) 
        image_names = [os.path.basename(image_file) for image_file in image_files]
    return image_names

image_reader_directory = os.path.expanduser('~/Documents/code/python/image-reader')
all_image_names = get_all_image_names(image_reader_directory)

for image_name in all_image_names:
    img = Image.open('inputs/'+image_name)
    text = pytesseract.image_to_string(img)
    print(text)