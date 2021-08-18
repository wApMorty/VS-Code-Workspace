import json, os, shutil

# Constants
InputFolder = os.path.join("D:\\Users","Paul","Documents","VS Code Workspace","btcDatas")
FileName  = "17_8_2021.txt"
FullInputFilePath = os.path.join(InputFolder, FileName)

file = open(FullInputFilePath, "r")

watchedValues = json.load(file)
btc = watchedValues["btc"]
ema5 = watchedValues["ema5"]
ema10 = watchedValues["ema10"]
ema15 = watchedValues["ema15"]
ema20 = watchedValues["ema20"]
ema50 = watchedValues["ema50"]
ema100 = watchedValues["ema100"]
ema200 = watchedValues["ema200"]
macdValue = watchedValues["macdValue"]
macdSignal = watchedValues["macdSignal"]
t = watchedValues["t"]

file.close()

inputBtc = btc[200:-30]
inputEma5 = ema5[200:-30]
inputEma10 = ema10[200:-30]
inputEma15 = ema15[200:-30]
inputEma20 = ema20[200:-30]
inputEma50 = ema50[200:-30]
inputEma100 = ema100[200:-30]
inputEma200 = ema200[200:-30]
inputMacdValue = macdValue[200:-30]
inputMacdSignal = macdSignal[200:-30]

expectedResult = []

inputs = []

for i in range(len(inputBtc)):
    inputs.append([inputBtc[i], inputEma5[i], inputEma10[i], inputEma15[i], inputEma20[i], inputEma50[i], inputEma100[i], inputEma200[i], inputMacdValue[i], inputMacdSignal[i]])

    delta = btc[i+230] - inputBtc[i]
    if delta > 0.005*inputBtc[i]:
        expectedResult.append([1, 0, 0])
    elif delta < -0.005*inputBtc[i]:
        expectedResult.append([0, 0, 1])
    else:
        expectedResult.append([0, 1, 0])

FileName = "Data_"+FileName
OutputFolder = os.path.join("D:\\Users","Paul","Documents","VS Code Workspace","btcTrainingDatasets")
FullDataPath = os.path.join(OutputFolder, FileName)

if not os.path.isfile(FullDataPath):
    shutil.copyfile(os.path.join(OutputFolder, "fileTemplate.txt"), FullDataPath)

file = open(FullDataPath, "r")
data = json.load(file)
data["inputs"] = inputs
data["outputs"] = expectedResult
file.close

file = open(FullDataPath, "w")
json.dump(data, file)
file.close()