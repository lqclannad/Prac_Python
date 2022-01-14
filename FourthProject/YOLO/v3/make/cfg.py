
IMG_HEIGHT = 416
IMG_WIDTH = 416

CLASS_NUM = 4

CLASS_NAME = ["人", "红绿灯", "手机", "苹果"]

ANCHORS_GROUP = {
    13: [[87, 346], [149, 227], [105, 358]],
    26: [[82, 165], [85, 237], [160, 163]],
    52: [[19, 64], [52, 30], [49, 252]]
}

ANCHORS_GROUP_AREA = {
    13: [x * y for x, y in ANCHORS_GROUP[13]],
    26: [x * y for x, y in ANCHORS_GROUP[26]],
    52: [x * y for x, y in ANCHORS_GROUP[52]],
}
