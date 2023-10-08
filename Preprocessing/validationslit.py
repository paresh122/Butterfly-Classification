import os
import shutil
from sklearn.model_selection import train_test_split

# Define paths
base_path = 'D:/Youtube chanel/Project-butterfly/archive/labelled'
validation_path = 'D:/Youtube chanel/Project-butterfly/archive/validation'

# Get all the species names (folder names in your training directory)
species_names = os.listdir(base_path)

# A list to keep track of all images and their labels
all_images = []
all_labels = []

species_counts_before = {}  # Dict to store counts before splitting
species_counts_after = {}   # Dict to store counts after splitting to validation

for species in species_names:
    species_folder = os.path.join(base_path, species)
    species_images = [os.path.join(species_folder, img) for img in os.listdir(species_folder)]
    
    species_counts_before[species] = len(species_images)
    
    all_images.extend(species_images)
    all_labels.extend([species] * len(species_images))

# Split the data into training and validation sets
train_images, validation_images, _, _ = train_test_split(all_images, all_labels, test_size=0.1, stratify=all_labels)

# Now, move the validation images to the validation folder, retaining their species-specific folder structure
for image_path in validation_images:
    species = os.path.basename(os.path.dirname(image_path))
    dest_folder = os.path.join(validation_path, species)
    
    # Create species folder in validation path if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    dest_path = os.path.join(dest_folder, os.path.basename(image_path))
    shutil.move(image_path, dest_path)
    
    # Count the moved images for each species
    species_counts_after[species] = species_counts_after.get(species, 0) + 1

print("Moved validation images!")

print("\nSpecies Counts Before Splitting:")
for species, count in species_counts_before.items():
    print(f"{species}: {count} images")

print("\nSpecies Counts After Moving to Validation:")
for species, count in species_counts_after.items():
    print(f"{species}: {count} images")