from . import rectify
from . import matching

import cv2

def process(img1, img2):

    # 转为灰度图
    img1 = cv2.cvtColor(img1_rectified, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2_rectified, cv2.COLOR_BGR2GRAY)

    # 直方图均衡
    img1 = cv2.equalizeHist(im1)
    img2 = cv2.equalizeHist(im2)

    return img1, img2

def distance(img1, img2):

    # 获取图片大小
    size = img1.shape[::-1]

    # 立体校正及畸变校正, Q 为投影矩阵
    img1, img2, Q = rectify.stereo(img1, img2, size)

    # 图像预处理
    img1, img2 = process(img1, img2)

    # 立体匹配, 获取视差图
    disp = matching.disparity_BM(img1, img2)
    
    # 计算 3D 坐标, z 轴即为深度
    threeD = cv2.reprojectImageTo3D(disp, Q)
