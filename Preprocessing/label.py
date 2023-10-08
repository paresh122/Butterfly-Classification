import os

base_dir = "D:/Youtube chanel/Project-butterfly/archive/labelled"  # replace with the path to the directory containing the 30 folders

for category_folder in os.listdir(base_dir):
    category_path = os.path.join(base_dir, category_folder)
    
    if os.path.isdir(category_path):  # ensures it's a folder
        count = 1
        for filename in os.listdir(category_path):
            file_path = os.path.join(category_path, filename)
            
            # Construct new filename
            new_filename = f"{category_folder.lower()}_{str(count).zfill(3)}.jpg"  # Assuming all images are .jpg
            new_file_path = os.path.join(category_path, new_filename)
            
            os.rename(file_path, new_file_path)
            
            count += 1
