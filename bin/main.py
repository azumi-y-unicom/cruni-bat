""" This program is starting. """
import sys
import os
import pathlib
import logging.config
from logging import getLogger
import click

# システムパスの設定
APP_HOME = os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)), ".."  ))
print("APP_HOME:", APP_HOME)
APP_CONF = os.path.join(APP_HOME, "conf")
print("APP_CONF:", APP_CONF)

sys.path.append(os.path.join(APP_HOME))

from mylib.ocr import MyOcr
from mylib.image_edit import ImageEdit

logging.config.fileConfig(os.path.join(APP_CONF, "logging.conf"))
logger = getLogger(__name__)


# コマンドラインの引数を設定
@click.command()
@click.option('--must_arg', '-m', required=True, help="解析画像のファイルパス")
@click.option('--option_arg', '-o', default='', help="解析結果の出力パス")

def cmd(must_arg, option_arg):
    logger.info("START cmd")
    try:
        image_file = must_arg

        image_edit = ImageEdit()
        # image_edit.hoge(image_file)

        my_ocr = MyOcr()
        text = my_ocr.recognize_image(image_file)

        # 解析結果の出力
        if(option_arg == ""):
            print(text)
        else:
            if(Exists_dir(option_arg)):
                # 新規上書き
                with open(option_arg, mode='w', encoding='UTF-8') as f:
                    f.write(text)
    except Exception as ex:
        logger.fatal(ex)

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
