# Otoware
**バージョンアップしました！！！**  
**https://github.com/ippee/Otoware-V2**  
  
「**音割戦隊ウルセンジャー - ピークレッド**」とは、入力した音源のラウドネスを強制的に最大化し、音割れさせるプログラムです  
好きに使ってください  
GUIはいつかつけようと思います、多分  
  
・**このアプリを使っていかなる損害が発生したとしても、私は一切の責任を負いかねます**  
耳とか再生機材は大切にね  
  
・Python 3.6.4で書いています  
pydub使っているので、ffmpegをインストールしておきましょう  
(pydub関係なしにffmpegは有能)  
  
・厳密にラウドネスを最大化しているわけではないです  
凄い数式いっぱい書いて厳密にやりたい人は各自で改良してください  
  
・91行目に、  
　　tada = AudioSegment.from_file(r"C:\Windows\media\tada.wav", format="wav")  
という記述がありますが、これはwindows 10に入っている効果音集みたいなところから引っ張ってきています  
もしMacとか別のOSでコレを動かしたい人がいた場合は注意です  
（処理が終わったことを知らせる効果音なので消しても問題ナシ）  
  
・私はDTMメインでやってるの人間なので、プログラミングの作法だか何だかというのはよくわかりません  
（動けばなんでもいい精神←）  
見にくかったらごめんさい  
　  
　  
　  
## 参考にしたサイト  
・【音割れ】うるさい音声を作ろう  
https://www.nicovideo.jp/watch/sm33239038  
  
・  小学生でも分かるデシベル(dB)の話  
https://macasakr.sakura.ne.jp/decibel.html  
  
・dB（デシベル）って何？音圧とは？【知っておくと便利な用語】  
https://info.shimamura.co.jp/digital/knowledge/2014/03/21161  
  
・dB（デシベル）とは  
https://www.onosokki.co.jp/HP-WK/c_support/newreport/decibel/dB.pdf  
  
・音響とか / Sound and Acoustics
https://www.geidai.ac.jp/~marui/dont_forget/node2.html#SECTION00023500000000000000  
  
・dB SPL ディービーエスピーエル とは  
https://www.g200kg.com/jp/docs/dic/dbspl.html
  
・dBFS ディービーエフエス とは  
https://www.g200kg.com/jp/docs/dic/dbfs.html  
  
・そのRMS値って、どっちのRMS？  
https://soundevotee.net/blog/2017/03/04/which_rms_value_are_you_refering/  
  
・LUFS/LKFS…ラウドネスメーターについて復習して理解を深めよう  
https://soundevotee.net/blog/2017/04/25/learning_about_loudness_meter/  
  
・pythonで音声処理  
https://qiita.com/nyancook/items/786cffd0b07bad8b4444  
  
・pyloudnorm  
https://pypi.org/project/pyloudnorm/
