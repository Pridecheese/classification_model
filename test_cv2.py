# 비디오프레임 (배경 제거)cv.BackgroundSubtractor.apply( image[, fgmask[, learningRate]] ) ->
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from rembg import remove
import os
#https://github.com/xuebinqin/U-2-Net
#https://github.com/xuebinqin/DIS
# rpath=r"d:\imgs"
def removeBackgroundFolder(rpath):
    f_lists = os.listdir(rpath)

    print(f_lists)
    for folder in f_lists:
        f_names = os.listdir(rpath+"\\"+folder)
        print(folder,":",end="")
        for f_name in f_names:
            ori_img = cv.imread(rpath+"\\"+folder+"\\"+f_name)
            ori_img = cv.resize(ori_img,(256,256))
            # cv.imshow("ori img",ori_img)
            rmbg_img = remove(ori_img)
            cv.imwrite(rpath+"\\"+folder+"\\"+f_name,rmbg_img)
            # cv.imshow("rmbg img",rmbg_img)
            # cv.waitKey(0)
            # cv.destroyAllWindows()
            print(".",end="")
        print()
def singleRemoveBackground(imagePathName):
    ori_img = cv.imread(imagePathName)
    ori_img = cv.resize(ori_img, (256, 256))
    # cv.imshow("ori img",ori_img)
    rmbg_img = remove(ori_img)
    cv.imwrite(imagePathName)
    print("배경이미지 제거가 완료 되었습니다.")
if __name__=="__main__":
    pass # 이 파일을 직접 실행했을때 작동되는 코드
else:
    pass # 다른 파일에서 import 시 작동되는 코드
#grabCut