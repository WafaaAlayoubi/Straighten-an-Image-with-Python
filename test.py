import cv2
import numpy as np

#---- 4 corner points of the bounding box
pts_src = np.array([[88.0,76.0], [410.0,96.0], [30.0, 500.0],[390.0, 544.0]])

#---- 4 corner points of the black image you want to impose it on
pts_dst = np.array([[0.0,0.0],[500.0, 0.0],[ 0.0,500.0],[500.0, 500.0]])

#---- forming the black image of specific size
im_dst = np.zeros((500, 500, 3), np.uint8)

#---- Framing the homography matrix
h, status = cv2.findHomography(pts_src, pts_dst)
 
im = cv2.imread('./image.png', cv2.IMREAD_COLOR)
#---- transforming the image bound in the rectangle to straighten
im_out = cv2.warpPerspective(im, h, (im_dst.shape[1],im_dst.shape[0]))
cv2.imwrite("im_out2.jpg", im_out)