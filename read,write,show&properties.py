import cv2
import imutils
img = cv2.imread("gratisography-funflower-800x525.jpg")
cv2.imwrite("FunFlower.jpg",img)
cv2.imshow("Flower",img)
resizeImg = imutils.resize(img, width = 200)
cv2.imwrite("resizedImage.jpg",resizeImg)
cv2.imshow("resizeImg",resizeImg)
print(img.size)
print(img.shape)
print(img.dtype)
GrayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("GrayFlower.jpg",GrayImg)
cv2.imshow("GrayFunFlower",GrayImg)
ThresImg = cv2.threshold(GrayImg,130,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("ThresholdImg.jpg",ThresImg)
cv2.imshow("ThresholdImg",ThresImg)
GaussBlur = cv2.GaussianBlur(img,(21,21),0) #kernel always be in odd value for gaussian blur
cv2.imwrite("GaussBlurImg.jpg",GaussBlur)
cv2.imshow("GaussBlur",GaussBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()
