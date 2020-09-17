from PIL import Image
import pyocr
import pyocr.builders

# logging確認する
from logging import getLogger
logger = getLogger(__name__)

class MyOcr:

    def recognize_image(self, in_path):
        logger.debug("START recognize_image")
        tools = pyocr.get_available_tools()
        
        # OCRツール確認　ツール無しなら終了
        if len(tools) == 0:
            raise Exception("There are no OCR tools.")
        
        # ツール取得
        tool = tools[0]
        print("use %s" % (tool.get_name()))

        # 画像読み取り
        logger.info("Recognize Image : " + in_path)
        img_org = Image.open(in_path)
        
        # ocr
        builder = pyocr.builders.TextBuilder()
        result = tool.image_to_string(img_org, lang="jpn", builder=builder)

        logger.debug("END recognize_image")
        return result

