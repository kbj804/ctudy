import os
import cv2
import numpy as np

def detect(image):
    

    gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    th1,img_bin = cv2.threshold(gray_scale,150,225,cv2.THRESH_BINARY)
    img_bin=~img_bin

    ### selecting min size as 15 pixels
    line_min_width = 15
    kernal_h = np.ones((1,line_min_width), np.uint8)
    kernal_v = np.ones((line_min_width,1), np.uint8)

    # Horizontal Kernel, Vertical Kernel
    img_bin_h = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_h)
    img_bin_v = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_v)

    # MIX Kernel
    img_bin_final=img_bin_h|img_bin_v


    final_kernel = np.ones((3,3), np.uint8)
    img_bin_final=cv2.dilate(img_bin_final,final_kernel,iterations=1)

    # connected~ 이웃연결관계
    # 어떤 객체가 연결되어 있을 때 두 개 픽셀이 상하좌우+대각선 으로 연결되어 있을 때
    """
    cv2.connectedComponentsWithStats(image, labels=None, stats=None, centroids=None, connectivity=None, ltype=None) -> retval, labels, stats, centroids

    • image: 8비트 1채널 영상
    • labels: 레이블 맵 행렬. 입력 영상과 같은 크기. numpy.ndarray.
    • stats: 각 객체의 바운딩 박스, 픽셀 개수 정보를 담은 행렬. numpy.ndarray. shape=(N, 5), dtype=numpy.int32.
    • centroids: 각 객체의 무게 중심 위치 정보를 담은 행렬 numpy.ndarray. shape=(N, 2), dtype=numpy.float64.
    • ltype: labels 행렬 타입. cv2.CV_32S 또는 cv2.CV_16S. 기본값은 cv2.CV_32S
    """
    _, labels, stats,_ = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)

    n1 = np.array(stats[2:])
    min_x, min_y, _, _, _ = np.min(n1, axis= 0)
    # print(n1)
    _, _, m_w_i, m_h_i, _= np.argmax(n1, axis= 0)
    _, _, m_w_i2, m_h_i2, _= np.argsort(n1, axis= 0)[0]
    ll = np.argsort(n1, axis= 0)
    # print(ll)
    # print(m_w_i, m_h_i)
    # print(m_w_i2, m_h_i2)
    
    s = n1[:, [1,3]].sum(axis=1).max()
    print(s)

    mm = n1[:, [1,3]].sum(axis=1).argmax()
    print(mm)


    max_x, _, max_w, _, _ = n1[m_w_i]
    _, max_y, _, max_h, _ = n1[m_h_i]

    max_x2, _, max_w2, _, _ = n1[m_w_i2]
    _, max_y2, _, max_h2, _ = n1[m_h_i2]

    # print(n1[m_w_i2])
    # print(n1[m_h_i2])

    x = n1[np.where(n1 >= max_y)]

    w = max_x + max_w
    h = max_y + max_h
    print(w,h)
    
    cv2.rectangle(image,(min_x, min_y),(w, 848),(0,255,0), 2)

    # for x,y,w,h,area in stats[2:]:
        # print(f"x: {x}, y: {y}, w: {w}, h: {h}, pixel: {area}, x+w: {x+w}, y+h: {y+h}")
        # cv2.rectangle(image,(x,y), (x+w, y+h),(0,255,0), 2)
        # cv2.rectangle(image,(28,75),(592,848),(0,255,0), 2)

    # re_image = cv2.resize(image, dsize=(0,0), fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
    
    
    cv2.imshow('detect', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_box(image, line_min_width=15):
    """
    labels is a GrayScale image with each connected Component getting assigned to a different value from its neighbor.
    stats is a tuple of lists with each tuple having (x,y,w,h,area) of the detected bounding boxes.
    """
    gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    th1,img_bin=cv2.threshold(gray_scale,150,225,cv2.THRESH_BINARY)
    kernal_h=np.ones((1,line_min_width), np.uint8)
    kernal_v=np.ones((line_min_width,1), np.uint8)
    img_bin_h=cv2.morphologyEx(~img_bin, cv2.MORPH_OPEN, kernal_h)
    img_bin_v=cv2.morphologyEx(~img_bin, cv2.MORPH_OPEN, kernal_v)
    img_bin_final=img_bin_h|img_bin_v
    final_kernel=np.ones((3,3), np.uint8)
    img_bin_final=cv2.dilate(img_bin_final,final_kernel,iterations=1)
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)
    return stats, labels


if __name__ == '__main__':
    
    image_path= './Scripts/cd/1.png'
    image=cv2.imread(image_path)

    detect(image)

    # state, label = detect_box(image)
    # print(state)