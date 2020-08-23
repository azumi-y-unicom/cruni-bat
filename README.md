# cruni-bat
バージョンを上げるにつれて独自性を上げる。  
1st：まずはOSSでもなんでも使って動くものを  
2nd：手書き、写真などを認識できるように  
3rd：Webカメラで認識できるように  

# note
## インストール落ち着いたら別途まとめる
tesseract-ocr-win64 v5.0.0 (最新版はα版だったからこちらを使用）使ってもつまらんから様子見て削除  
https://qiita.com/henjiganai/items/7a5e871f652b32b41a18    

## 開発環境
VSCodeを使用

## PowerShellのポリシー変更
事前にPowerShellを起動し、VSCodeでvenvを実行できるようにしておく  

☆実行ポリシーを変える  
```
Set-ExecutionPolicy RemoteSigned
```
  
　備考：開いたPowerShellだけ、実行ポリシーを変える  
```
Set-ExecutionPolicy RemoteSigned -Scope Process
```
  
## コーディング規約
コメント：  Docstringに準拠
参考：
［Python入門］docstringの書き方  
https://www.atmarkit.co.jp/ait/articles/1912/06/news025.html

Google Python Style Guide  
https://google.github.io/styleguide/pyguide.html

## その他参考資料
click（バッチオプション設定）  
https://blog.amedama.jp/entry/2015/10/14/232045

ロガー（logging）基礎  
https://docs.python.org/ja/3/howto/logging.html

Python Logging Best Practices  
https://pieces.openpolitics.com/2012/04/python-logging-best-practices/

log設定ファイルの書式解説  
https://docs.python.org/ja/3/library/logging.config.html#logging-config-fileformat


