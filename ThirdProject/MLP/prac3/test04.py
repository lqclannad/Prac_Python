import torch
from torch.nn.functional import one_hot

a = torch.Tensor([1,3,5]).long()
print(a)
y = label = one_hot(a,num_classes=10)
print(y)
a = torch.Tensor([123])
a[0] = 1
print(a)
'''
out = torch.Tensor([[0.2568, 0.0754, 0.0918, 0.0561, 0.0490, 0.0610, 0.0539, 0.1002, 0.1203,
         0.1353],
        [0.0655, 0.0251, 0.1420, 0.1169, 0.1309, 0.1335, 0.1323, 0.1524, 0.0504,
         0.0508],
        [0.2443, 0.0693, 0.0998, 0.0602, 0.0590, 0.0700, 0.0635, 0.1045, 0.1098,
         0.1195],
        [0.0285, 0.0101, 0.1480, 0.1553, 0.1543, 0.1627, 0.1343, 0.1499, 0.0304,
         0.0264],
        [0.1139, 0.2049, 0.0285, 0.0449, 0.0141, 0.0198, 0.0187, 0.0562, 0.2252,
         0.2737],
        [0.2216, 0.0505, 0.1148, 0.0649, 0.0675, 0.0818, 0.0776, 0.1246, 0.0905,
         0.1062],
        [0.1102, 0.0525, 0.1252, 0.0903, 0.1104, 0.1103, 0.1241, 0.1268, 0.0740,
         0.0761],
        [0.1059, 0.2131, 0.0242, 0.0411, 0.0116, 0.0167, 0.0158, 0.0513, 0.2314,
         0.2888],
        [0.0426, 0.0194, 0.1413, 0.1398, 0.1519, 0.1525, 0.1387, 0.1337, 0.0432,
         0.0369],
        [0.0971, 0.2189, 0.0190, 0.0354, 0.0084, 0.0127, 0.0119, 0.0451, 0.2390,
         0.3124],
        [0.1106, 0.2075, 0.0257, 0.0421, 0.0122, 0.0176, 0.0164, 0.0534, 0.2295,
         0.2850],
        [0.0721, 0.0465, 0.1258, 0.1136, 0.1399, 0.1308, 0.1371, 0.1097, 0.0675,
         0.0571],
        [0.0944, 0.0628, 0.1198, 0.0971, 0.1257, 0.1133, 0.1280, 0.1102, 0.0775,
         0.0712],
        [0.1641, 0.0533, 0.1207, 0.0760, 0.0865, 0.0977, 0.1023, 0.1237, 0.0836,
         0.0922],
        [0.1973, 0.1292, 0.0638, 0.0559, 0.0336, 0.0434, 0.0394, 0.0820, 0.1679,
         0.1876],
        [0.1431, 0.1772, 0.0374, 0.0483, 0.0182, 0.0252, 0.0230, 0.0653, 0.2107,
         0.2517],
        [0.1501, 0.0607, 0.1179, 0.0795, 0.0927, 0.1003, 0.1075, 0.1159, 0.0862,
         0.0895],
        [0.1013, 0.0653, 0.1187, 0.0928, 0.1205, 0.1095, 0.1260, 0.1115, 0.0795,
         0.0747],
        [0.0223, 0.0066, 0.1510, 0.1632, 0.1525, 0.1661, 0.1293, 0.1636, 0.0240,
         0.0214],
        [0.0834, 0.0596, 0.1203, 0.1044, 0.1340, 0.1211, 0.1329, 0.1040, 0.0757,
         0.0648],
        [0.0608, 0.0347, 0.1321, 0.1230, 0.1450, 0.1391, 0.1388, 0.1186, 0.0584,
         0.0496],
        [0.1232, 0.0406, 0.1313, 0.0869, 0.0991, 0.1108, 0.1195, 0.1429, 0.0683,
         0.0774],
        [0.0631, 0.0374, 0.1305, 0.1209, 0.1442, 0.1374, 0.1388, 0.1158, 0.0606,
         0.0512],
        [0.2070, 0.1033, 0.0851, 0.0625, 0.0514, 0.0615, 0.0579, 0.0914, 0.1364,
         0.1434],
        [0.0503, 0.0235, 0.1393, 0.1322, 0.1457, 0.1448, 0.1369, 0.1372, 0.0477,
         0.0424],
        [0.0576, 0.0296, 0.1355, 0.1258, 0.1435, 0.1399, 0.1371, 0.1299, 0.0537,
         0.0475],
        [0.1848, 0.1419, 0.0546, 0.0531, 0.0275, 0.0366, 0.0329, 0.0774, 0.1820,
         0.2091],
        [0.1131, 0.0302, 0.1400, 0.0892, 0.0979, 0.1139, 0.1205, 0.1649, 0.0587,
         0.0716],
        [0.1305, 0.1568, 0.0693, 0.0749, 0.0538, 0.0595, 0.0632, 0.0806, 0.1583,
         0.1532],
        [0.1511, 0.1671, 0.0475, 0.0554, 0.0258, 0.0338, 0.0318, 0.0723, 0.1949,
         0.2202],
        [0.0712, 0.0459, 0.1259, 0.1142, 0.1405, 0.1316, 0.1376, 0.1093, 0.0671,
         0.0565],
        [0.0504, 0.0182, 0.1455, 0.1298, 0.1379, 0.1439, 0.1339, 0.1566, 0.0425,
         0.0412],
        [0.0298, 0.0108, 0.1476, 0.1536, 0.1536, 0.1613, 0.1345, 0.1499, 0.0314,
         0.0274],
        [0.0393, 0.0169, 0.1431, 0.1431, 0.1524, 0.1547, 0.1378, 0.1381, 0.0401,
         0.0345],
        [0.0314, 0.0120, 0.1465, 0.1520, 0.1546, 0.1610, 0.1360, 0.1446, 0.0332,
         0.0286],
        [0.0479, 0.0211, 0.1411, 0.1342, 0.1455, 0.1461, 0.1362, 0.1422, 0.0451,
         0.0406],
        [0.0422, 0.0190, 0.1417, 0.1402, 0.1517, 0.1526, 0.1384, 0.1349, 0.0427,
         0.0367],
        [0.1067, 0.2136, 0.0258, 0.0432, 0.0129, 0.0182, 0.0175, 0.0529, 0.2287,
         0.2806],
        [0.0150, 0.0036, 0.1529, 0.1755, 0.1518, 0.1725, 0.1229, 0.1734, 0.0171,
         0.0153],
        [0.1426, 0.0609, 0.1181, 0.0814, 0.0959, 0.1024, 0.1111, 0.1156, 0.0849,
         0.0871],
        [0.0429, 0.0160, 0.1457, 0.1378, 0.1438, 0.1491, 0.1344, 0.1544, 0.0393,
         0.0366],
        [0.0394, 0.0141, 0.1471, 0.1412, 0.1447, 0.1513, 0.1337, 0.1578, 0.0366,
         0.0342],
        [0.0257, 0.0083, 0.1498, 0.1585, 0.1522, 0.1632, 0.1313, 0.1597, 0.0271,
         0.0242],
        [0.1375, 0.0265, 0.1407, 0.0799, 0.0875, 0.1080, 0.1129, 0.1721, 0.0580,
         0.0769],
        [0.0714, 0.0460, 0.1259, 0.1141, 0.1404, 0.1315, 0.1375, 0.1094, 0.0672,
         0.0566],
        [0.1642, 0.1395, 0.0699, 0.0660, 0.0453, 0.0537, 0.0528, 0.0831, 0.1602,
         0.1653],
        [0.0563, 0.0215, 0.1435, 0.1248, 0.1360, 0.1399, 0.1339, 0.1527, 0.0463,
         0.0451],
        [0.0511, 0.0262, 0.1370, 0.1316, 0.1491, 0.1462, 0.1394, 0.1259, 0.0505,
         0.0430],
        [0.1277, 0.1707, 0.0603, 0.0708, 0.0438, 0.0504, 0.0527, 0.0771, 0.1730,
         0.1735],
        [0.0969, 0.2125, 0.0166, 0.0316, 0.0066, 0.0105, 0.0094, 0.0425, 0.2429,
         0.3304],
        [0.0719, 0.0467, 0.1255, 0.1137, 0.1402, 0.1311, 0.1375, 0.1088, 0.0677,
         0.0569],
        [0.0555, 0.0300, 0.1348, 0.1276, 0.1473, 0.1430, 0.1393, 0.1224, 0.0541,
         0.0460],
        [0.0584, 0.0327, 0.1332, 0.1250, 0.1462, 0.1408, 0.1392, 0.1200, 0.0566,
         0.0480],
        [0.0963, 0.2156, 0.0172, 0.0327, 0.0071, 0.0111, 0.0101, 0.0432, 0.2419,
         0.3247],
        [0.0417, 0.0186, 0.1420, 0.1406, 0.1517, 0.1529, 0.1383, 0.1357, 0.0422,
         0.0363],
        [0.1035, 0.2162, 0.0236, 0.0408, 0.0114, 0.0164, 0.0157, 0.0504, 0.2320,
         0.2899],
        [0.0648, 0.0386, 0.1299, 0.1196, 0.1432, 0.1362, 0.1383, 0.1155, 0.0616,
         0.0523],
        [0.0742, 0.0491, 0.1246, 0.1117, 0.1389, 0.1290, 0.1366, 0.1080, 0.0693,
         0.0585],
        [0.0974, 0.0267, 0.1433, 0.0931, 0.1059, 0.1137, 0.1220, 0.1781, 0.0537,
         0.0661],
        [0.1125, 0.2006, 0.0221, 0.0368, 0.0092, 0.0141, 0.0124, 0.0501, 0.2353,
         0.3068],
        [0.1260, 0.1925, 0.0346, 0.0493, 0.0177, 0.0243, 0.0228, 0.0624, 0.2159,
         0.2544],
        [0.0668, 0.0392, 0.1302, 0.1179, 0.1409, 0.1334, 0.1365, 0.1193, 0.0619,
         0.0538],
        [0.0573, 0.0291, 0.1358, 0.1260, 0.1432, 0.1397, 0.1367, 0.1315, 0.0533,
         0.0473],
        [0.1432, 0.1717, 0.0491, 0.0585, 0.0285, 0.0363, 0.0350, 0.0729, 0.1927,
         0.2123],
        [0.1643, 0.0462, 0.1248, 0.0755, 0.0854, 0.0991, 0.1039, 0.1322, 0.0782,
         0.0905],
        [0.1322, 0.0659, 0.1160, 0.0843, 0.1009, 0.1044, 0.1150, 0.1109, 0.0859,
         0.0845],
        [0.0309, 0.0113, 0.1473, 0.1522, 0.1531, 0.1603, 0.1348, 0.1495, 0.0323,
         0.0283],
        [0.0972, 0.2048, 0.0147, 0.0283, 0.0053, 0.0087, 0.0074, 0.0404, 0.2458,
         0.3473],
        [0.1591, 0.1611, 0.0486, 0.0544, 0.0257, 0.0339, 0.0315, 0.0733, 0.1929,
         0.2197],
        [0.1632, 0.0403, 0.1283, 0.0754, 0.0846, 0.1003, 0.1048, 0.1412, 0.0735,
         0.0885],
        [0.0340, 0.0135, 0.1455, 0.1488, 0.1536, 0.1586, 0.1365, 0.1433, 0.0354,
         0.0306],
        [0.0742, 0.0105, 0.1610, 0.0970, 0.0980, 0.1189, 0.1149, 0.2426, 0.0335,
         0.0494],
        [0.1049, 0.0432, 0.1311, 0.0921, 0.1110, 0.1118, 0.1244, 0.1415, 0.0673,
         0.0728],
        [0.0605, 0.0280, 0.1379, 0.1226, 0.1388, 0.1373, 0.1352, 0.1383, 0.0526,
         0.0488],
        [0.0561, 0.0230, 0.1416, 0.1257, 0.1382, 0.1403, 0.1347, 0.1472, 0.0478,
         0.0454],
        [0.0435, 0.0141, 0.1489, 0.1354, 0.1388, 0.1480, 0.1326, 0.1652, 0.0371,
         0.0364],
        [0.0270, 0.0090, 0.1492, 0.1568, 0.1525, 0.1625, 0.1323, 0.1569, 0.0284,
         0.0252],
        [0.0789, 0.0430, 0.1298, 0.1083, 0.1315, 0.1244, 0.1321, 0.1258, 0.0651,
         0.0610],
        [0.1001, 0.0356, 0.1363, 0.0935, 0.1108, 0.1131, 0.1242, 0.1557, 0.0613,
         0.0695],
        [0.0646, 0.0389, 0.1297, 0.1197, 0.1436, 0.1363, 0.1386, 0.1146, 0.0618,
         0.0522],
        [0.1307, 0.0408, 0.1303, 0.0844, 0.0967, 0.1090, 0.1175, 0.1419, 0.0694,
         0.0794],
        [0.0403, 0.0173, 0.1430, 0.1420, 0.1512, 0.1534, 0.1375, 0.1394, 0.0406,
         0.0353],
        [0.0501, 0.0238, 0.1389, 0.1325, 0.1468, 0.1455, 0.1375, 0.1345, 0.0481,
         0.0423],
        [0.0297, 0.0110, 0.1472, 0.1540, 0.1548, 0.1622, 0.1353, 0.1467, 0.0317,
         0.0273],
        [0.0487, 0.0104, 0.1572, 0.1238, 0.1222, 0.1408, 0.1261, 0.2008, 0.0325,
         0.0375],
        [0.0512, 0.0257, 0.1375, 0.1315, 0.1483, 0.1458, 0.1388, 0.1281, 0.0500,
         0.0430],
        [0.1981, 0.0869, 0.0983, 0.0678, 0.0676, 0.0759, 0.0742, 0.0978, 0.1160,
         0.1174],
        [0.2500, 0.1103, 0.0549, 0.0425, 0.0215, 0.0313, 0.0253, 0.0781, 0.1715,
         0.2146],
        [0.0405, 0.0175, 0.1429, 0.1418, 0.1513, 0.1533, 0.1376, 0.1389, 0.0408,
         0.0354],
        [0.1771, 0.1367, 0.0665, 0.0614, 0.0392, 0.0484, 0.0460, 0.0825, 0.1653,
         0.1769],
        [0.1481, 0.1693, 0.0475, 0.0561, 0.0263, 0.0342, 0.0324, 0.0722, 0.1950,
         0.2190],
        [0.1046, 0.2120, 0.0220, 0.0384, 0.0100, 0.0148, 0.0137, 0.0492, 0.2349,
         0.3004],
        [0.0908, 0.0470, 0.1285, 0.1000, 0.1239, 0.1174, 0.1287, 0.1279, 0.0684,
         0.0674],
        [0.0736, 0.2144, 0.0081, 0.0197, 0.0025, 0.0046, 0.0039, 0.0284, 0.2525,
         0.3922],
        [0.1830, 0.0536, 0.1184, 0.0723, 0.0798, 0.0919, 0.0929, 0.1233, 0.0872,
         0.0975],
        [0.0526, 0.0157, 0.1497, 0.1255, 0.1309, 0.1413, 0.1311, 0.1719, 0.0398,
         0.0416],
        [0.0448, 0.0186, 0.1429, 0.1369, 0.1458, 0.1481, 0.1356, 0.1466, 0.0423,
         0.0384],
        [0.0979, 0.2145, 0.0179, 0.0335, 0.0075, 0.0116, 0.0105, 0.0441, 0.2410,
         0.3217],
        [0.1038, 0.2120, 0.0213, 0.0375, 0.0095, 0.0142, 0.0131, 0.0484, 0.2360,
         0.3042],
        [0.0323, 0.0127, 0.1456, 0.1510, 0.1552, 0.1608, 0.1370, 0.1415, 0.0344,
         0.0293]])

label = torch.Tensor([[0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
        [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.]])

print(torch.argmax(out,dim=1))
print(torch.argmax(label,dim=1))
print(torch.sum(torch.eq(out,label)).item())
'''

'''
out = torch.Tensor([[0.5211],
        [0.5211],
        [0.5211],
        [0.5211],
        [0.5211],
        [0.5211],
        [0.5211],
        [0.5210],
        [0.5211],
        [0.5211],
        [0.5211],
        [0.5210],
        [0.5211],
        [0.5211],
        [0.5211],
        [0.5211],
        [0.5211],
        [0.4999],
        [0.5211]])
for item in out:
        item[0] = 1 if item[0] > 0.5 else 0

print(out)
'''

out = torch.Tensor([[0.4848],
        [0.4964],
        [0.4891],
        [0.4881],
        [0.4935],
        [0.4877],
        [0.4863],
        [0.4876],
        [0.4848],
        [0.5013],
        [0.4863],
        [0.4940],
        [0.4886],
        [0.4847],
        [0.4847],
        [0.4926],
        [0.4881],
        [0.4912],
        [0.4845],
        [0.4843],
        [0.4991],
        [0.4899],
        [0.4957],
        [0.4988],
        [0.4980],
        [0.4972],
        [0.4891],
        [0.4907],
        [0.4866],
        [0.4974],
        [0.5003],
        [0.4875],
        [0.4904],
        [0.4880],
        [0.5019],
        [0.4846],
        [0.4888],
        [0.4838],
        [0.4975],
        [0.4902],
        [0.4883],
        [0.4980],
        [0.4872],
        [0.4847],
        [0.4847],
        [0.4871],
        [0.4873],
        [0.4933],
        [0.4923],
        [0.4863],
        [0.4854],
        [0.4976],
        [0.4837],
        [0.5126],
        [0.4844],
        [0.4985],
        [0.4955],
        [0.4839],
        [0.4845],
        [0.4894],
        [0.4884],
        [0.4863],
        [0.5040],
        [0.4836],
        [0.4886],
        [0.4858],
        [0.4871],
        [0.4908],
        [0.4885],
        [0.4844],
        [0.4922],
        [0.4844],
        [0.4887],
        [0.4862],
        [0.4979],
        [0.4840],
        [0.4851],
        [0.4959],
        [0.4986],
        [0.5015],
        [0.4876],
        [0.4883],
        [0.4921],
        [0.4848],
        [0.4890],
        [0.4839],
        [0.4836],
        [0.5009],
        [0.4844],
        [0.4863],
        [0.4895],
        [0.4888],
        [0.4959],
        [0.4966],
        [0.4957],
        [0.4844],
        [0.4931],
        [0.4921],
        [0.4848],
        [0.5100]])

tag = torch.Tensor([[1.],
        [1.],
        [0.],
        [1.],
        [1.],
        [0.],
        [0.],
        [0.],
        [1.],
        [1.],
        [1.],
        [1.],
        [1.],
        [0.],
        [0.],
        [1.],
        [0.],
        [0.],
        [1.],
        [0.],
        [0.],
        [1.],
        [1.],
        [0.],
        [1.],
        [1.],
        [1.],
        [1.],
        [0.],
        [1.],
        [1.],
        [1.],
        [1.],
        [1.],
        [0.],
        [0.],
        [0.],
        [0.],
        [0.],
        [1.],
        [1.],
        [1.],
        [0.],
        [0.],
        [1.],
        [0.],
        [0.],
        [1.],
        [1.],
        [0.],
        [0.],
        [1.],
        [1.],
        [0.],
        [0.],
        [0.],
        [1.],
        [0.],
        [1.],
        [0.],
        [0.],
        [0.],
        [0.],
        [0.],
        [0.],
        [0.],
        [1.],
        [0.],
        [1.],
        [0.],
        [1.],
        [0.],
        [1.],
        [1.],
        [1.],
        [1.],
        [0.],
        [1.],
        [1.],
        [1.],
        [0.],
        [1.],
        [0.],
        [0.],
        [0.],
        [1.],
        [1.],
        [1.],
        [1.],
        [0.],
        [1.],
        [1.],
        [0.],
        [1.],
        [1.],
        [0.],
        [1.],
        [0.],
        [1.],
        [1.]])

out = torch.gt(out,0.5)
print(out)
score = torch.sum(torch.eq(out,tag).float())
print(score)