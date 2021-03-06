# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/15 22:58
# 文件名称: utils.py
# 开发工具: Pycharm
import cv2
import numpy as np
import torch


def iou(box, boxes, isMin=False):
    # 计算面积[x1,y1,x2,y2]
    box_area = (box[2] - box[0]) * (box[3] - box[1])
    boxes_area = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])

    x1 = torch.maximum(box[0], boxes[:, 0])
    y1 = torch.maximum(box[1], boxes[:, 1])
    x2 = torch.minimum(box[2], boxes[:, 2])
    y2 = torch.minimum(box[3], boxes[:, 3])

    w = torch.maximum(torch.Tensor([0]), (x2 - x1))
    h = torch.maximum(torch.Tensor([0]), (y2 - y1))
    inter = w * h

    if isMin:
        ovr = torch.true_divide(inter, torch.minimum(box_area, boxes_area))
    else:
        ovr = torch.true_divide(inter, (box_area + boxes_area - inter))
    return ovr


def nms(boxes, thresh=0.3, isMin=False):
    _boxes = boxes
    if boxes.shape[0] == 0:
        return torch.Tensor([])
    # 根据置信度从大到小对标签重新排序
    _boxes = _boxes[(-_boxes[:, 4]).argsort()]
    # 存储需保留的框
    r_boxes = []
    while _boxes.shape[0] > 1:
        a_box = _boxes[0]
        b_boxes = _boxes[1:]
        r_boxes.append(a_box)
        # 将其他框与最大置信度框的iou小于阈值的索引保留
        index = torch.where(iou(a_box, b_boxes) < thresh)
        # 根据索引覆盖原来的盒子，再进行下次循环
        _boxes = b_boxes[index]
    if _boxes.shape[0] == 1:
        r_boxes.append(_boxes[0])
    return torch.stack(r_boxes)


def convert_to_square(box):
    # numpy.copy  tensor.clone
    square_box = box.clone()
    if box.shape[0] == 0:
        return torch.Tensor([])
    h = box[:, 3] - box[:, 1]
    w = box[:, 2] - box[:, 0]
    max_side = torch.maximum(h, w)
    square_box[:,0] = box[:,0] + w*0.5 - max_side*0.5
    square_box[:,1] = box[:,1] + h*0.5 - max_side*0.5
    square_box[:,2] = box[:,2] - w*0.5 + max_side*0.5
    square_box[:,3] = box[:,3] - h*0.5 + max_side*0.5
    index = torch.nonzero(torch.lt(square_box,0))
    for i in index:
        i0 = i[0].item()
        i1 = i[1].item()
        if i1 == 0:    # x1<0
            square_box[i0,2] = square_box[i0,2].item() - square_box[i0,i1].item()
            square_box[i0,i1] = 0
        elif i1 == 1:   # y1<0
            square_box[i0,3] = square_box[i0,3].item() - square_box[i0,i1].item()
            square_box[i0,i1] = 0
    return square_box


if __name__ == '__main__':
    # a = torch.Tensor([7, 7, 13, 13])
    # b = torch.Tensor([[7, 7, 13, 13], [8, 8, 14, 14], [9, 9, 15, 15]])
    # print(iou(a, b))  # tensor([1.0000, 0.5319, 0.2857])
    # c = torch.Tensor(
    #     [[7, 7, 13, 13, 0.9], [8, 8, 14, 14, 0.8], [9, 9, 15, 15, 0.7], [0, 0, 2, 2, 0.83], [1, 0, 3, 2, 0.6]])
    # print(nms(c, 0.1))
    t = torch.Tensor([[ 4.9069e+02,  2.2636e+02,  5.0435e+02,  2.4384e+02,  1.0000e+00],
        [ 4.7421e+02,  2.2686e+02,  4.8734e+02,  2.4251e+02,  1.0000e+00],
        [ 2.9135e+02,  2.3051e+02,  3.0313e+02,  2.4721e+02,  9.9996e-01],
        [ 6.6161e+02,  2.3075e+02,  6.8343e+02,  2.5897e+02,  9.9996e-01],
        [ 2.3085e+02,  2.4067e+02,  2.5147e+02,  2.6593e+02,  9.9991e-01],
        [ 5.2821e+02,  2.1602e+02,  5.5745e+02,  2.5103e+02,  9.9989e-01],
        [ 2.6686e+02,  2.2989e+02,  2.8741e+02,  2.5582e+02,  9.9983e-01],
        [ 1.7478e+02,  2.5283e+02,  1.9747e+02,  2.8197e+02,  9.9979e-01],
        [ 5.9270e+02,  2.3046e+02,  6.1669e+02,  2.6169e+02,  9.9974e-01],
        [ 3.1445e+02,  2.3074e+02,  3.2582e+02,  2.4448e+02,  9.9965e-01],
        [ 1.2116e+02,  2.6052e+02,  1.4602e+02,  2.9204e+02,  9.9955e-01],
        [ 6.9719e+02,  2.4001e+02,  7.3581e+02,  2.8924e+02,  9.9952e-01],
        [ 4.5513e+02,  2.7187e+02,  4.6804e+02,  2.8834e+02,  9.9934e-01],
        [ 3.4837e+02,  2.7028e+02,  3.5927e+02,  2.8418e+02,  9.9923e-01],
        [ 2.1841e+02,  2.5605e+02,  2.2869e+02,  2.6877e+02,  9.9873e-01],
        [ 6.4319e+02,  4.1584e+02,  6.5262e+02,  4.2846e+02,  9.9806e-01],
        [ 7.1103e+02,  3.3691e+02,  7.2709e+02,  3.5752e+02,  9.9751e-01],
        [ 7.2606e+02,  2.4860e+02,  7.4193e+02,  2.6939e+02,  9.9736e-01],
        [ 4.5540e+02,  2.3090e+02,  4.6876e+02,  2.4804e+02,  9.9719e-01],
        [ 3.2721e+02,  2.2609e+02,  3.3655e+02,  2.3767e+02,  9.9678e-01],
        [ 2.6147e+02,  4.7110e+01,  2.7232e+02,  6.1025e+01,  9.9670e-01],
        [ 3.4208e+02,  2.2131e+02,  3.5637e+02,  2.3990e+02,  9.9566e-01],
        [ 3.4478e+02,  5.6545e+01,  3.5481e+02,  6.9383e+01,  9.9507e-01],
        [ 7.0405e+02,  2.6286e+02,  7.1532e+02,  2.7771e+02,  9.9381e-01],
        [ 7.5185e+02,  2.4704e+02,  7.6198e+02,  2.6011e+02,  9.9372e-01],
        [ 4.6241e+02,  2.8871e+02,  4.7902e+02,  3.1037e+02,  9.9312e-01],
        [ 2.8662e+02,  2.4675e+02,  2.9662e+02,  2.5953e+02,  9.9305e-01],
        [ 6.7476e+02,  3.3092e+02,  6.8939e+02,  3.4990e+02,  9.9253e-01],
        [ 3.3052e+02,  5.3560e+01,  3.4125e+02,  6.7095e+01,  9.9187e-01],
        [ 4.1969e+02,  4.8312e+01,  4.3607e+02,  6.9508e+01,  9.9113e-01],
        [ 6.9350e+02,  2.4097e+02,  7.0514e+02,  2.5604e+02,  9.9013e-01],
        [ 3.5667e+02,  3.0821e+02,  3.6924e+02,  3.2485e+02,  9.8581e-01],
        [ 3.5186e+02,  2.8478e+02,  3.6203e+02,  2.9774e+02,  9.8387e-01],
        [ 2.8650e+02,  5.5123e+00,  2.9729e+02,  1.8881e+01,  9.8174e-01],
        [ 7.0586e+02,  2.4909e+02,  7.1727e+02,  2.6344e+02,  9.7909e-01],
        [ 2.6099e+00,  2.3862e+02,  1.9815e+01,  2.6109e+02,  9.7852e-01],
        [ -2.6099e+00,  -2.3862e+01,  1.9815e+01,  2.6109e+01,  9.7852e-01],
        [ 3.4783e+02,  2.9397e+02,  3.5918e+02,  3.0916e+02,  9.7766e-01],
        [ 6.4091e+02,  3.2299e+02,  6.5418e+02,  3.4015e+02,  9.7265e-01],
        [ 2.8717e+02,  5.2100e+01,  2.9959e+02,  6.8168e+01,  9.7258e-01],
        [ 2.9087e+02,  2.6457e+02,  3.1057e+02,  2.9029e+02,  9.6746e-01],
        [ 3.0633e+02,  2.2937e+02,  3.1666e+02,  2.4151e+02,  9.6676e-01],
        [ 2.9407e+02,  1.7865e+01,  3.0557e+02,  3.2794e+01,  9.6479e-01],
        [ 2.6034e+02,  3.7371e+02,  2.7938e+02,  3.9950e+02,  9.6139e-01],
        [ 2.4990e+02,  4.0288e+01,  2.6058e+02,  5.4658e+01,  9.6093e-01],
        [ 1.2377e+02,  2.8616e+02,  1.3521e+02,  3.0096e+02,  9.5558e-01],
        [ 2.2665e+02,  2.3176e+02,  2.3912e+02,  2.4722e+02,  9.5230e-01],
        [ 3.5728e+02,  2.6625e+02,  3.6811e+02,  2.8031e+02,  9.4978e-01],
        [ 7.0347e+02,  3.2500e+02,  7.1811e+02,  3.4372e+02,  9.4315e-01],
        [ 8.8094e+01,  2.6105e+02,  1.1078e+02,  2.8980e+02,  9.4021e-01],
        [ 4.6496e+02,  2.1748e+02,  4.7869e+02,  2.3497e+02,  9.3299e-01],
        [ 2.2807e+02,  5.5755e+02,  2.3767e+02,  5.7052e+02,  9.3129e-01],
        [ 2.9852e+02,  2.8713e+01,  3.0924e+02,  4.2548e+01,  9.2985e-01],
        [ 2.1240e+02,  3.9718e+01,  2.2364e+02,  5.4311e+01,  9.2678e-01],
        [ 6.5899e+02,  3.2023e+02,  6.6880e+02,  3.3334e+02,  9.2538e-01],
        [ 2.9585e+02,  4.2896e+01,  3.0876e+02,  5.9602e+01,  9.2535e-01],
        [ 4.7865e+02,  4.6718e+01,  4.9101e+02,  6.3018e+01,  9.2171e-01],
        [ 2.4607e+02,  2.6508e+02,  2.6065e+02,  2.8428e+02,  9.0896e-01],
        [ 1.6269e+02,  2.3403e+02,  1.8515e+02,  2.6359e+02,  9.0563e-01],
        [ 3.4721e+02,  8.4386e+01,  3.5904e+02,  9.9903e+01,  9.0300e-01],
        [ 5.5314e+02,  3.4576e+02,  5.6948e+02,  3.6701e+02,  9.0167e-01],
        [ 3.0375e+02,  2.1289e+02,  3.4191e+02,  2.6103e+02,  9.0153e-01],
        [ 4.1091e+02,  3.7684e+02,  4.2067e+02,  3.8979e+02,  8.9631e-01],
        [ 6.5772e+02,  3.3756e+02,  6.7519e+02,  3.6200e+02,  8.9563e-01],
        [ 5.7407e+02,  3.7116e+02,  6.0369e+02,  4.0996e+02,  8.9218e-01],
        [ 6.7703e+02,  2.4570e+02,  6.9973e+02,  2.7460e+02,  8.9146e-01],
        [ 1.4163e+02,  2.6295e+02,  1.4964e+02,  2.7322e+02,  8.8924e-01],
        [ 5.0539e+02,  2.2640e+02,  5.1683e+02,  2.4174e+02,  8.8725e-01],
        [ 2.3139e+02,  4.3972e+01,  2.4306e+02,  5.9027e+01,  8.8655e-01],
        [ 4.5891e+02,  4.1936e+01,  4.7161e+02,  5.8754e+01,  8.8589e-01],
        [ 7.1573e+02,  3.1403e+02,  7.2946e+02,  3.3217e+02,  8.7605e-01],
        [ 1.3218e+02,  2.9677e+02,  1.4395e+02,  3.1160e+02,  8.7599e-01],
        [ 5.1279e+02,  4.7070e+01,  5.2517e+02,  6.3484e+01,  8.7229e-01],
        [ 2.0031e+02,  6.1962e+01,  2.1103e+02,  7.5678e+01,  8.7023e-01],
        [ 2.7148e+02,  4.5156e+01,  2.8378e+02,  6.1316e+01,  8.6614e-01],
        [ 1.6745e+02,  4.3125e+01,  1.8005e+02,  5.9590e+01,  8.5210e-01],
        [ 2.6025e+02,  2.1789e+02,  2.7597e+02,  2.3792e+02,  8.4271e-01],
        [ 2.3718e+02, -6.3540e+00,  2.8867e+02,  6.2091e+01,  8.3281e-01],
        [ 4.3286e+02,  4.0888e+01,  4.4538e+02,  5.7510e+01,  8.2973e-01],
        [ 4.4501e+02,  4.3707e+01,  4.5692e+02,  5.9437e+01,  8.2430e-01],
        [ 1.4817e+02,  2.8122e+02,  1.5855e+02,  2.9355e+02,  8.1728e-01],
        [ 6.2324e+02,  3.6641e+02,  6.3699e+02,  3.8416e+02,  8.1670e-01],
        [ 1.9388e+02,  2.3485e+02,  2.1620e+02,  2.6429e+02,  8.1614e-01],
        [ 2.1548e+01,  4.9482e+02,  5.5592e+01,  5.3874e+02,  8.1350e-01],
        [ 4.9072e+02,  3.9781e+01,  5.0395e+02,  5.7551e+01,  8.1298e-01],
        [ 6.6588e+02,  2.6242e+02,  6.7936e+02,  2.7972e+02,  8.1042e-01],
        [ 7.4178e+02,  3.1551e+02,  7.5392e+02,  3.3232e+02,  8.0975e-01],
        [ 2.0168e+02,  5.7016e+00,  2.3631e+02,  5.0849e+01,  8.0702e-01],
        [ 5.4236e+02,  3.9220e+02,  5.5375e+02,  4.0694e+02,  7.9565e-01],
        [ 2.4248e+02,  3.1979e+02,  2.6792e+02,  3.5328e+02,  7.9534e-01],
        [ 6.4565e+02,  4.3460e+01,  6.5779e+02,  5.9049e+01,  7.9522e-01],
        [ 1.5770e+02,  2.4579e+01,  1.7651e+02,  4.9031e+01,  7.9025e-01],
        [ 4.1996e+01,  2.2586e+02,  1.2574e+02,  3.3391e+02,  7.8533e-01],
        [ 5.3453e+02,  2.4583e+02,  5.4424e+02,  2.5752e+02,  7.7879e-01],
        [ 5.7676e+02,  4.5764e+01,  5.8930e+02,  6.2096e+01,  7.7820e-01],
        [ 2.8334e+02,  1.3375e+01,  3.7926e+02,  1.3806e+02,  7.6914e-01],
        [ 1.5714e+02,  4.8631e+01,  1.6961e+02,  6.5183e+01,  7.6740e-01],
        [ 1.1706e+02,  2.5382e+02,  1.2928e+02,  2.6988e+02,  7.6222e-01],
        [ 2.5052e+02,  2.4275e+02,  2.6235e+02,  2.5811e+02,  7.5347e-01],
        [ 7.2240e+02,  3.9108e+02,  7.3297e+02,  4.0469e+02,  7.5185e-01],
        [ 2.2130e+02,  2.7107e+02,  2.3283e+02,  2.8536e+02,  7.3725e-01],
        [ 1.8308e+02,  4.3610e+01,  1.9548e+02,  6.0057e+01,  7.3570e-01],
        [ 3.1445e+02,  2.5512e+02,  3.6858e+02,  3.2607e+02,  7.3509e-01],
        [ 3.7482e+02,  2.3048e+02,  3.9796e+02,  2.5950e+02,  7.2621e-01],
        [ 3.0466e+02,  7.5177e+01,  3.2256e+02,  9.8410e+01,  7.2497e-01],
        [ 2.5040e+02,  2.8166e+02,  2.7213e+02,  3.0922e+02,  7.2448e-01],
        [ 1.7462e+02,  5.3788e+01,  1.9853e+02,  8.4653e+01,  7.2405e-01],
        [ 5.2466e+02,  3.7018e+01,  5.3682e+02,  5.3072e+01,  7.1140e-01],
        [ 6.1031e+02,  3.3659e+01,  6.2290e+02,  4.9898e+01,  7.0893e-01],
        [ 3.3859e+02,  2.8611e+02,  3.4847e+02,  2.9968e+02,  7.0625e-01],
        [ 5.4906e+02,  4.6421e+01,  5.6117e+02,  6.2338e+01,  7.0215e-01],
        [ 3.0911e+02,  2.5461e+02,  3.2073e+02,  2.6973e+02,  7.0144e-01],
        [ 2.0188e+02,  4.3760e+01,  2.1392e+02,  5.9422e+01,  6.9377e-01],
        [ 2.5471e+02,  3.5482e+02,  2.6824e+02,  3.7236e+02,  6.8891e-01],
        [ 6.9064e+02,  3.3476e+02,  7.1077e+02,  3.6147e+02,  6.7870e-01],
        [ 3.0628e+02,  4.8826e+01,  3.2556e+02,  7.4097e+01,  6.7760e-01],
        [ 4.2052e+02,  3.2629e+01,  4.3353e+02,  5.0132e+01,  6.7464e-01],
        [ 5.2750e+02,  2.8547e+02,  5.5356e+02,  3.1999e+02,  6.7203e-01],
        [ 4.1189e+02,  4.3741e+01,  4.2314e+02,  5.8359e+01,  6.6151e-01],
        [ 6.6762e+02,  3.7236e+02,  6.8519e+02,  3.9605e+02,  6.2168e-01],
        [ 3.0584e+01,  1.3545e+02,  4.4320e+01,  1.5306e+02,  6.1635e-01],
        [ 3.9446e+02,  2.4272e+02,  4.1557e+02,  2.6911e+02,  6.1528e-01],
        [ 4.2867e+02,  2.5989e+02,  4.9576e+02,  3.4914e+02,  6.1021e-01],
        [ 4.5289e+02,  2.9312e+02,  4.6477e+02,  3.0907e+02,  6.0930e-01],
        [ 4.8127e+02,  2.0292e+02,  5.2627e+02,  2.5795e+02,  6.0094e-01]])
    square, index = convert_to_square(t)
    print("square:", square[index])
    # img = cv2.imread("img/1.jpg")
    # for b in t:
    #     x1 = int(b[0])
    #     y1 = int(b[1])
    #     x2 = int(b[2])
    #     y2 = int(b[3])
    #     cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
    # cv2.imshow("img",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
