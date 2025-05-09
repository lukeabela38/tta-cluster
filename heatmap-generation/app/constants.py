from enum import Enum

class HeatMapGeneratorConfigs(Enum):
    CHECKPOINT: str = "google/owlv2-base-patch16-ensemble"
    TASK: str = "zero-shot-object-detection"
    LABELS: list[str] = ["ball", "net", "table", "person"]