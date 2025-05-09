import os
from constants import HeatMapGeneratorConfigs
from zero_shot_object_detection import HeatMapGenerator

def create_folder(location: str) -> None:
    if not os.path.exists(location):
        os.makedirs(location)

def main() -> int:

    current_working_directory: str = os.getcwd()

    folders: list[str] = [
        f"{current_working_directory}/app/inputs",
        f"{current_working_directory}/app/outputs",
    ]

    for folder in folders:
        create_folder(folder)

    HeatMapGenerator(folders[0], HeatMapGeneratorConfigs)
    return 0

if __name__ == "__main__":
    main()