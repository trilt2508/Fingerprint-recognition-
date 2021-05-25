import cv2 as cv
from glob import glob
import os
import numpy as np
from utilss.poincare import calculate_singularities
from utilss.segmentation import create_segmented_and_variance_images
from utilss.normalization import normalize
from utilss.gabor_filter import gabor_filter
from utilss.frequency import ridge_freq
from utilss import orientation
from utilss.crossing_number import calculate_minutiaes
from tqdm import tqdm
from utilss.skeletonize import skeletonize


def fingerprint_pipline(input_img):
    block_size = 16

    # pipe line picture re https://www.cse.iitk.ac.in/users/biometrics/pages/111.JPG
    # normalization -> orientation -> frequency -> mask -> filtering

    # normalization - removes the effects of sensor noise and finger pressure differences.
    normalized_img = normalize(input_img.copy(), float(100), float(100))
    # cv.imshow('image', input_img)
    # cv.waitKeyEx()
    # cv.imshow('image', normalized_img)
    # cv.waitKeyEx()
    # color threshold
    # threshold_img = normalized_img
    # _, threshold_im = cv.threshold(normalized_img,127,255,cv.THRESH_OTSU)
    # cv.imshow('color_threshold', normalized_img); cv.waitKeyEx()

    # ROI and normalisation
    (segmented_img, normim, mask) = create_segmented_and_variance_images(normalized_img, block_size, 0.2)

    # print(normim)
    # print(mask)
    # orientations
    angles = orientation.calculate_angles(normalized_img, W=block_size, smoth=False)
    # print(angles.shape)

    orientation_img = orientation.visualize_angles(segmented_img, mask, angles, W=block_size)

    # find the overall frequency of ridges in Wavelet Domain
    freq = ridge_freq(normim, mask, angles, block_size, kernel_size=5, minWaveLength=5, maxWaveLength=15)
    # create gabor filter and do the actual filtering
    gabor_img = gabor_filter(normim, angles, freq)
    # cv.imshow('image', gabor_img)
    # cv.waitKeyEx()
    # thinning oor skeletonize
    thin_image = skeletonize(gabor_img)

    # minutias
    minutias = calculate_minutiaes(thin_image)

    # singularities
    singularities_img = calculate_singularities(thin_image, angles, 1, block_size, mask)

    # visualize pipeline stage by stage
    output_imgs = [normalized_img, segmented_img, orientation_img, gabor_img, thin_image, minutias,singularities_img]
    # for i in range(len(output_imgs)):
    #     if len(output_imgs[i].shape) == 2:
    #         output_imgs[i] = cv.cvtColor(output_imgs[i], cv.COLOR_GRAY2RGB)
    # results = np.concatenate([np.concatenate(output_imgs[:4], 1), np.concatenate(output_imgs[4:], 1)]).astype(np.uint8)
    # cv.imshow('image', results)
    # cv.waitKeyEx()
    return output_imgs


if __name__ == '__main__':
    # open images
    # img_dir = './sample_inputs/*'
    # img_dir = './input/*'
    # # output_dir = './output/'
    # output_dir = './out/'
    # def open_images(directory):
    #     images_paths = glob(directory)
    #     return np.array([cv.imread(img_path,0) for img_path in images_paths])
    #
    # images = open_images(img_dir)
    #
    # # image pipeline
    # os.makedirs(output_dir, exist_ok=True)
    # for i, img in enumerate(tqdm(images)):
    #     results = fingerprint_pipline(img)
    #     cv.imwrite(output_dir+str(i)+'.png', results)
    #     cv.imshow('image pipeline', results); cv.waitKeyEx()
    image = cv.imread("D:\\ATTT\\test1.tif",cv.IMREAD_GRAYSCALE)
    list_images = fingerprint_pipline(image)
    print(list_images[5].shape)
    cv.imshow('image', list_images[5])
    cv.waitKeyEx()