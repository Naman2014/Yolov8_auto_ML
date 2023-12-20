import os
import random
import shutil

def split_dataset(dataset_path, train_ratio=0.8, seed=42):
    # Set random seed for reproducibility
    random.seed(42)

    # Define paths for images and labels
    images_path = os.path.join(dataset_path, "images")
    labels_path = os.path.join(dataset_path, "labels")

    # Get the list of filenames in the dataset
    filenames = os.listdir(images_path)

    # Shuffle the filenames randomly
    random.shuffle(filenames)

    # Calculate the split index based on the train_ratio
    split_index = int(train_ratio * len(filenames))

    # Split the dataset into training and validation sets
    train_filenames = filenames[:split_index]
    val_filenames = filenames[split_index:]

    # Create train and val folders
    train_path = os.path.join(dataset_path, "train")
    val_path = os.path.join(dataset_path, "val")

    os.makedirs(train_path, exist_ok=True)
    os.makedirs(val_path, exist_ok=True)

    # Move images and labels to the respective folders
    for filename in train_filenames:
        image_src = os.path.join(images_path, filename)
        label_src = os.path.join(labels_path, filename.replace(".jpg", ".txt"))

        shutil.move(image_src, os.path.join(train_path, filename))
        shutil.move(label_src, os.path.join(train_path, filename.replace(".jpg", ".txt")))

    for filename in val_filenames:
        image_src = os.path.join(images_path, filename)
        label_src = os.path.join(labels_path, filename.replace(".jpg", ".txt"))

        shutil.move(image_src, os.path.join(val_path, filename))
        shutil.move(label_src, os.path.join(val_path, filename.replace(".jpg", ".txt")))

# Specify the path to the dataset folder
dataset_path = "editing yaml file\data"

# Call the function to split the dataset
split_dataset(dataset_path)
