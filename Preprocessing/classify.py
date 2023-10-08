import pandas as pd
import os
import shutil
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor

def label_image(args):
    index, row, source_folder, destination_folder = args
    image_name = row['filename']
    species = row['label']
    
    # Create directory for the species if it doesn't exist
    species_folder = os.path.join(destination_folder, species)
    
    # Handle cases where the folder name already exists as a file
    if os.path.exists(species_folder) and not os.path.isdir(species_folder):
        new_species_folder = species_folder + "_folder"
        os.makedirs(new_species_folder)
        species_folder = new_species_folder
    
    if not os.path.exists(species_folder):
        os.makedirs(species_folder)
    
    # Copy the image to the species folder
    src_path = os.path.join(source_folder, image_name)
    dst_path = os.path.join(species_folder, image_name)
    
    shutil.copy(src_path, dst_path)

def main():
    # Read the CSV file
    data = pd.read_csv('D:/Youtube chanel/Project-butterfly/archive/Training_set.csv')

    # Your image folders (remove the extra double quote from the source folder)
    source_folder = 'D:/Youtube chanel/Project-butterfly/archive/train'
    destination_folder = 'D:/Youtube chanel/Project-butterfly/archive/labelled'

    # Ensure destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Process in parallel
    with ProcessPoolExecutor() as executor:
        args_list = [(index, row, source_folder, destination_folder) for index, row in data.iterrows()]
        list(tqdm(executor.map(label_image, args_list), total=data.shape[0]))

if __name__ == '__main__':
    main()
