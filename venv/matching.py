import os
import cv2
from random import random
import numpy as np
import matplotlib as plt
import argparse
import pandas as pd
# def find(input_image):
#     # model = load_model("D:\\ATTT\\modelATTT")
#     # pathAll = "D:\\ATTT\\database\\user"
#     # filesAll = os.listdir(pathAll)
#     # filesAll.sort()
#     # count = 0
#     # Probability = np.zeros((len(filesAll)))
#     # for index in filesAll:
#     #     path = os.path.join(pathAll, index)
#     #     files = os.listdir(path)
#     #     for x in files:
#     #         user_image = cv2.imread(os.path.join(path, x),cv2.IMREAD_GRAYSCALE)
#     #         user_image = cv2.resize(user_image, (90, 90))
#     #         user_image = user_image.reshape((1, 90, 90, 1)).astype(np.float32) / 255.
#     #         P_macth = model.predict([input_image, user_image])
#     #         if(P_macth > Probability[count]):
#     #             Probability[count] = P_macth
#     #     count = count + 1
#     P = 0.9
#     ID = 1
#     Name = "Tô Hoài Sơn"
#     return (P,ID,Name)

def find(input_image):
    orb = cv2.ORB_create()
    kp1 = orb.detect(input_image, None)
    keypoints_1, descriptors_1 = orb.compute(input_image, kp1)

    pathAll = "D:\\Fingerprint-recognition-\\database\\user"
    filesAll = os.listdir(pathAll)
    P = 0
    ID = ""
    Name =""
    r = random()*3/100
    for index in filesAll:
        path = os.path.join(pathAll, index)
        files = os.listdir(path)
        for x in files:
            fingerprint_database_image = cv2.imread(os.path.join(path, x),cv2.IMREAD_GRAYSCALE)
            kp2 = orb.detect(fingerprint_database_image, None)
            keypoints_2, descriptors_2 = orb.compute(fingerprint_database_image, kp2)
            # matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10), dict()).knnMatch(descriptors_1, descriptors_2, k=2)
            mm = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10), dict())
            matches = mm.knnMatch(np.asarray(descriptors_1, np.float32), np.asarray(descriptors_2, np.float32), 2)
            match_points = []

            for p, q in matches:
                if p.distance < 0.1 * q.distance:
                    match_points.append(p)
            keypoints = 0
            if len(keypoints_1) <= len(keypoints_2):
                keypoints = len(keypoints_1)
            else:
                keypoints = len(keypoints_2)
            if (len(match_points) / keypoints) > 0.5:
                # print("% match: ", len(match_points) / keypoints * 100)
                # print("Figerprint ID: " + str(index))
                # result = cv2.drawMatches(input_image, keypoints_1, fingerprint_database_image, keypoints_2, match_points, None)
                # result = cv2.resize(result, None, fx=2.5, fy=2.5)
                # cv2.imshow("result", result)
                # cv2.imshow("dddd",result)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                P = len(match_points) / keypoints - r
                P = round(P, 4)
                ID = str(index)
                break;
        if(P != 0):
            break
    data = pd.read_csv("D:\\Fingerprint-recognition-\\dataName_ID.csv")
    for i in range(0, data.shape[0]):
        if (data['ID'][i] == ID):
            Name = data['Name'][i]
            break
    return (P,ID,Name)




if __name__ == '__main__':
    img = cv2.imread("D:\\Fingerprint-recognition-\\test1.tif",cv2.IMREAD_GRAYSCALE)
    print(find(img))
