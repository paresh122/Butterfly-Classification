import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tqdm import tqdm

# Define path
train_dir = 'D:/Youtube chanel/Project-butterfly/archive/labelled'

# Define augmentation settings
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

def get_current_max_number(directory):
    """Extract the current maximum number in the directory based on the naming convention."""
    numbers = []
    for filename in os.listdir(directory):
        try:
            number = int(filename.split('-')[-1].split('.')[0])
            numbers.append(number)
        except:
            continue
    return max(numbers) if numbers else 0

# Iterate over all the images in train_dir and apply augmentations
for species in os.listdir(train_dir):
    species_dir = os.path.join(train_dir, species)
    
    # Get the current highest number of images in the directory to continue the naming from there
    current_max_number = get_current_max_number(species_dir)
    
    for file_name in tqdm(os.listdir(species_dir)):
        image_path = os.path.join(species_dir, file_name)
        image = load_img(image_path)  # Load the image
        x = img_to_array(image)  # Convert the image to array
        x = np.expand_dims(x, axis=0)  # Add an extra dimension
        
        # Generate and save augmented images to the same directory
        i = 0
        for batch in datagen.flow(x, batch_size=1, save_to_dir=species_dir, save_prefix=f"{species}-{current_max_number+i+1}", save_format='jpeg'):
            i += 1
            if i > 3:  # Adjust this number to create 3-5 variations as per your need.
                break
                
        current_max_number += i