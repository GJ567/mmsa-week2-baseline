from MMSA import get_config_regression

config = get_config_regression('lmf', 'mosi')

for k, v in config.items():
    print(k, ":", v)