import torch

print("torch 版本：", torch.__version__)
print("CUDA 版本：", torch.version.cuda)
print("GPU 是否可用：", torch.cuda.is_available())

if torch.cuda.is_available():
    print("显卡名称：", torch.cuda.get_device_name(0))
else:
    print("当前只能用 CPU")