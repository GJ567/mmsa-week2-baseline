import pickle

path = r'F:\Code\Study\MMSA_Week2\data\MOSI\Processed\unaligned_50.pkl'

with open(path, "rb") as f:
    data = pickle.load(f)

print("最外层 keys：", data.keys())

train = data["train"]

print("train 里的 keys：", train.keys())

print("训练样本数量：", len(train["raw_text"]))

print("第一个文本：", train["raw_text"][0])
print("文本特征 shape：", train["text"][0].shape)
print("音频特征 shape：", train["audio"][0].shape)
print("视觉特征 shape：", train["vision"][0].shape)
print("回归标签：", train["regression_labels"][0])