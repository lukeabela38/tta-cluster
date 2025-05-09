import enum
from transformers import pipeline

class HeatMapGenerator():
    def __init__(self, input_folder: str, config: enum.Enum):
        
        checkpoint = config.CHECKPOINT.value
        print(checkpoint)