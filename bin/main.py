import sys
import os 
import click
import logging.config

app_home = os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)) , ".." ))
sys.path.append(os.path.join(app_home))
print("app_home:",  app_home)

app_conf =os.path.join(app_home, "conf")
print("app_conf:",  app_conf)

logging.config.fileConfig(os.path.join(app_conf, "logging.conf"))

from logging import getLogger
logger = getLogger(__name__)

# コマンドラインの引数を設定
@click.command()
@click.option('--must_arg', '-m', required=True, help="解析画像のファイルパス")
@click.option('--option_arg', '-o', default='', help="任意引数")

def cmd(must_arg, option_arg):
    logger.info("START cmd")
    try:
        print("hoge")
    except Exception as ex:
        print(ex)
        pass
    logger.info("End cmd")

# 起点とイメージしやすくするため
def main():
    # エディタ次第でエラー扱いされるが@clickで対応しているので問題なし
    cmd()

if __name__ == "__main__":
    main()
