from pathlib import Path
from src.datasets import CrossDockDataset
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

train_dataset = CrossDockDataset(
                data_path="data/single_backup",
                prefix='crossdocksingle_train.full',
                device=device,
            )




