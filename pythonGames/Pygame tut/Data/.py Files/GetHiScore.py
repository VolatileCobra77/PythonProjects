import pickle as pkl
hiScore = pkl.load(open("Data/hiScore.Txt", 'rb'))
print(f"current Hi Score {hiScore}")