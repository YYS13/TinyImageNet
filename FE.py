import cv2

class Features:
    def __init__(self, imgs):
        self.imgs = imgs
    
    def colorHistogram(self):
        hist = cv2.calcHist(self.imgs, [0], None, [256], [0, 256])
        return hist
        
    def SIFT():
        return 0
    def HOG():
        return 0