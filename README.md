# MMSA Week 2 Baseline Experiments

This repository contains my Week 2 experiments for multimodal sentiment analysis using MMSA.

## Environment

- Python 3.10
- PyTorch 2.0.1
- CUDA 11.8
- MMSA
- Dataset: CMU-MOSI

## Current Experiment

| Model | Dataset | Seed | MAE | Corr | Acc-2 | F1 |
|---|---|---:|---:|---:|---:|---:|
| LMF | MOSI | 1111 | 0.9841 | 0.6805 | 0.7881 | 0.7894 |

## Project Structure

```text
MMSA_Week2
├── run_lmf.py
├── test_env.py
├── test_mmsa.py
├── check_config.py
├── check_data.py
└── data
    └── MOSI
        └── Processed
            └── unaligned_50.pkl
Dataset

The dataset file is not included in this repository.

Please download the CMU-MOSI processed feature file and place it at:

data/MOSI/Processed/unaligned_50.pkl
Run
conda activate mmsa310
python run_lmf.py
Notes

LMF is used as the first baseline model to verify the MMSA experimental pipeline.
