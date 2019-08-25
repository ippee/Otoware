# coding: UTF-8
from pydub import AudioSegment
from pydub.playback import play
import soundfile as sf
import pyloudnorm as pyln
import sys
import os

##################################################
# 
# 【Readme】
# 音割れ音源は耳に悪いだけでなく、再生機器にもダメージを与えます
# 本アプリによって生成された音割れ音源を再生し、いかなる損害等が発生したとしても、製作者は一切の責任を負いかねます
# 
# いっぺー (Twitter: @ippee1410)
# 
##################################################



### 下準備 ###

print("#######################################################")
print("### 音割戦隊ウルセンジャー ピークレッド見参ッ！！！ ###")
print("#######################################################")

print("\n楽曲のラウドネスを最大化し、高品質な音割れ音源を生成するぞっ！")
print("（測定アルゴリズム: ITU-R BS.1770）\n")

print("さぁ、音声ファイルのパスを入力しようか(^^)")
path = input()
ext = path[ path.rfind(".")+1 : len(path)] # 拡張子取得
FileName = path[ path.rfind( "\\" ) + 1 : path.rfind(".")] # ファイル名取得

BS = AudioSegment.from_file(path, format=ext)  # 原曲を読み込み (Before Sound)
BS.export("./processing.wav", format="wav") # wavに変換
BeforeAudio, rate = sf.read("processing.wav") # オーディオ読み込み
meter = pyln.Meter(rate) # ラウドネスメーター生成
LUFS_def = meter.integrated_loudness(BeforeAudio) # 原曲のIntegrated Loudnessを測定

print("\nファイルの確認")
print("・ファイル名：", FileName)
print("・現在のラウドネス (LUFS): ", round(LUFS_def, 3))
print("準備はいいかな？ y/n")
ans=input()

print("\nくらえっ！\n必殺 アブソリュート・イヤー・デストロイ！！！！")
print("（ただいま戦闘中...）\n")



### 音声処理 ###

PS = BS # 音声を加工する用のコピーを作成 (Processing Sound)
LUFS=[] # 音量を上げたときのIntegrated Loudnessを記録するリスト
c=0 # カウンター, 10回音量をいじってラウドネスが変わらなければ処理を終了

for i in range(6165): # pydubは音量を最大 6165 dBまで上げれるっぽい
    
    PS = BS + i # 音量を i dB上げる
    PS.export("./processing.wav", format="wav") # 加工音源の上書き

    ProcessingAudio, rate = sf.read("processing.wav") # 加工音源を読み込み
    meter = pyln.Meter(rate)
    LUFS.append(meter.integrated_loudness(ProcessingAudio)) # Integrated Loudnessの取得, 記録

    if i>=2: 
        if LUFS[i-1] == LUFS[i-2]: # カウンターのチェック
            c += 1
    
    if c==10:
        os.remove("processing.wav") # 処理に使ったwavファイルを削除
        break

max_value = max(LUFS) # ラウドネスの最大値を取得
max_index = LUFS.index(max_value) # そのインデックスを取得

PS = BS + max_index
PS.export("音割れ" + FileName + ".wav", format="wav")


### 結果表示 ###

print("#######################################################\n")
print("ラウドネスを最大化したぞっ！")
print("・Before: " + str(round(LUFS_def, 3)) + " LUFS")
print("・After: " + str(round(max_value, 3)) + " LUFS")
print("・音量変化: +" + str(max_index) + "dB")
print("・原曲との音圧の比率: ", str(round(pow(10, max_index/20), 3))) # （倍率）= 10^{(上げたデシベル)/20}
print("\nまたいつでも呼ぶといいっ！\nサラバッ！！！")
tada = AudioSegment.from_file(r"C:\Windows\media\tada.wav", format="wav") # 終了の通知
play(tada)

ans=input()