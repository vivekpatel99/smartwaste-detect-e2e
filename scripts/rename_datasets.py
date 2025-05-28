from pathlib import Path
import rootutils
rootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)

def rename_images_in_directory(base_dir_str: str):
    base_dir = Path(base_dir_str)

    for image_path in base_dir.iterdir():
        class_name = image_path.stem
        print(f'[INFO]: Renaming images in {class_name}')
        for idx, image in enumerate(image_path.iterdir()):
            new_image_name = f"{class_name}_{idx}.jpg"
            new_image_path = image_path / new_image_name
            print(f'[INFO]: Renaming {image.name} to {new_image_name}')
            image.rename(new_image_path)



if __name__ == "__main__":
    rename_images_in_directory("data/waste_segregation_datasets/V1/val")