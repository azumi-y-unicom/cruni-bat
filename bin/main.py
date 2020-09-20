import sys
import os 
import click
import pathlib
import logging.config

app_home = os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)) , ".." ))
sys.path.append(os.path.join(app_home))
print("app_home:",  app_home)

app_conf =os.path.join(app_home, "conf")
print("app_conf:",  app_conf)

logging.config.fileConfig(os.path.join(app_conf, "logging.conf"))

from logging import getLogger
from mylib.ocr import MyOcr

logger = getLogger(__name__)

# コマンドラインの引数を設定
@click.command()
@click.option('--must_arg', '-m', required=True, help="解析画像のファイルパス")
@click.option('--option_arg', '-o', default='', help="解析結果の出力パス")

def cmd(must_arg, option_arg):
    logger.info("START cmd")
    try:
        image_file = must_arg
        myOcr = MyOcr()
        text = myOcr.recognize_image(image_file)

        # 解析結果の出力
        if(option_arg == ""):
            print(text)
        else:
            if(Exists_dir(option_arg)):
                # 新規上書き
                with open(option_arg, mode='w') as f:
                    f.write(text)
    except Exception as ex:
        logger.fatal(ex)
        pass
    logger.info("End cmd")

def Exists_dir(file_path):
    obj_path = pathlib.Path(file_path)
    return os.path.exists(str(obj_path.parent))


# 起点とイメージしやすくするため
def main():
    # エディタ次第でエラー扱いされるが@clickで対応しているので問題なし
    cmd()

if __name__ == "__main__":
    main()
