# mypkg
このリポジトリはROS 2で使えるリポジトリであり、talkeとlistenerのノードでメッセージの送受信を行い、ノード間の通信をすることができる。

![test](https://github.com/EbisawaRyota/mypkg/actions/workflows/test.yml/badge.svg)

## ROS 2の'talker'と'listener'ノード間の通信
端末1でtalkerのプログラムを立ち上げる
```
端末1$　ros2 run demo_nodes_py talker
・・・
[INFO] [1660366971.132536000] [talker]:Publishing:"Hello World: 79"
[INFO] [1660366972.132853800] [talker]:Publishing:"Hello World: 80"
[INFO] [1660366973.132538200] [talker]:Publishing:"Hello World: 81"
・・・
```
talkerがプログラムを立ち上げトピックにメッセージを送信する。
次に、端末2の方でtalkerのプログラムを立ち上げる
```
端末2$　ros2 run demo_nodes_py listener
・・・
[INFO] [1660366971.133705900] [listener]:I heard:"Hello World: 79"
[INFO] [1660366972.133861900] [listener]:I heard:"Hello World: 80"
[INFO] [1660366973.133210800] [listener]:I heard:"Hello World: 81"
・・・
```
listenerがプログラムを立ち上げトピックを受け取り、ノードからメッセージを受け取る。

## talker
* talkerはトピックに継続的にメッセージを送信する。
## listener
* listenerはトピックを受け取りtalkerからのメッセージを受け取りコンソールに表示させる。
## メッセージ型
* talkerのノードから/countupのトピックを通じて送信され、メッセージ型は16ビット符号付き整数で文字列は送ることができない。

## 必要なソフト
* Python
* ROS 2(Foxy Fitzroy)

## テスト環境
* Ubuntu 20.04

## ライセンス及び著作権
* このソフトウェアパッケージは３条項BSDライセンスの下、再頒布および使用が許可されます.
* このパッケージのコードの一部は、下記のスライド(CC-BY-SA 4.0 by Ryuihi Ueda)のものを、本人の許可を得て自身の著作としたものです. 
    * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2023 Ryota Ebisawa
