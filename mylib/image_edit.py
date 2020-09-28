import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

class ImageEdit:

    def __init__(self, work_dir_path, blocksize = 5, adptc = 1):
        self.work_home = work_dir_path
        self.adapt_block_size = blocksize
        self.adapt_c = adptc

    # グレイアウト ヒストグラム平坦化
    def convert_greyscale(self, image_path):
        img = cv2.imread(image_path)
        grayscale_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # tmp_image = grayscale_image
        tmp_image = cv2.equalizeHist(grayscale_image)

        # 適応閾値処理(検証) http://opencv.jp/opencv-2svn/cpp/miscellaneous_image_transformations.html
        # tmp_image_adapt = cv2.adaptiveThreshold(tmp_image, 255, 
        #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 
        #     self.adapt_block_size, self.adapt_c)

        # グレイアウト 中間ファイル作成
        file_name = os.path.basename(image_path)
        tmp_dir = os.path.join(self.work_home, "COLOR_BGR2GRAY")

        tmp_file = os.path.join(tmp_dir, "gray_" + file_name)
        cv2.imwrite(tmp_file, grayscale_image)
        self.last_image = tmp_file

        # ヒストグラム平坦化 中間ファイル作成
        tmp_file = os.path.join(tmp_dir, "hist_" + file_name)
        # 保存
        cv2.imwrite(tmp_file, tmp_image)
        self.last_image = tmp_file

        # tmp_file = os.path.join(tmp_dir, "binari_" + file_name)
        # cv2.imwrite(tmp_file, tmp_image_adapt)
        

