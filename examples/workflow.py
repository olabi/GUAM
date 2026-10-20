import os
from glob import glob

import cudf as cd
from omegaconf import OmegaConf

from guam.datalibs import DataLoader


CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "workflow_config.yaml")

cfg = OmegaConf.load(CONFIG_PATH)

df = cd.DataFrame({
    "name":  [1.0, None, 3.0, 4.0, None],
    "name2": [10.0, 20.0, 30.0, 40.0, 50.0],
})

dataset = DataLoader(df, output_path=cfg.data.output_path)
workflow, output_path = dataset(cfg.workflow)

print(cd.read_parquet(sorted(glob(os.path.join(output_path, "*.parquet")))))
