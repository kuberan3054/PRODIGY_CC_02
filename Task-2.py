import cv2
import numpy as np
import copy

plain_img = cv2.imread("dog1.jpg")
x,y,_=plain_img.shape



#Key generation
key = np.empty((x, y), dtype=object)
for i in range(x):
    for j in range(y):
        key[i, j] = list(np.random.randint(0, 256, size=3))

#Encryption of the plain image
enc_img = copy.deepcopy(plain_img)
for i in range(x):
    for j in range(y):
        enc_img[i][j][0] = (key[i][j][0]+plain_img[i][j][0])%255
        enc_img[i][j][1] = (key[i][j][1] + plain_img[i][j][1]) % 255
        enc_img[i][j][2] = (key[i][j][2] + plain_img[i][j][2]) % 255

#Decryption of the plain image
dec_img = copy.deepcopy(enc_img)
for i in range(x):
    for j in range(y):
        dec_img[i][j][0] = (enc_img[i][j][0]-key[i][j][0])%255
        dec_img[i][j][1] = (enc_img[i][j][1]-key[i][j][1])% 255
        dec_img[i][j][2] = (enc_img[i][j][2]-key[i][j][2])% 255

#scaling for visual convenience
scale_factor = 0.3
new_width = int(plain_img.shape[1] * scale_factor)
new_height = int(plain_img.shape[0] * scale_factor)

original_image = cv2.resize(plain_img, (new_width, new_height))
encrypted_image = cv2.resize(enc_img, (new_width, new_height))
decrypted_image = cv2.resize(dec_img,(new_width,new_height))

cv2.imshow("original",original_image)
cv2.imshow("encrypted",encrypted_image)
cv2.imshow("decrypted",decrypted_image)
cv2.waitKey(0)
