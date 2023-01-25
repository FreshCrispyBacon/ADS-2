import time
import matplotlib.image as mpimg
import pandas as pd
import numpy as np
import math
import torch
from yolov5 import detect
import glob
import os
import shutil
import matplotlib.pyplot as plt
import plotly.express as px
import string
import warnings
warnings.filterwarnings('ignore')

def rd_to_wgs(x, y):
    X0 = 155000
    Y0 = 463000

    pqk = [
        (0, 1, 3235.65389),
        (2, 0, -32.58297),
        (0, 2, -0.24750),
        (2, 1, -0.84978),
        (0, 3, -0.06550),
        (2, 2, -0.01709),
        (1, 0, -0.00738),
        (4, 0, 0.00530),
        (2, 3, -0.00039),
        (4, 1, 0.00033),
        (1, 1, -0.00012)]

    pql = [
        (1, 0, 5260.52916),
        (1, 1, 105.94684),
        (1, 2, 2.45656),
        (3, 0, -0.81885),
        (1, 3, 0.05594),
        (3, 1, -0.05607),
        (0, 1, 0.01199),
        (3, 2, -0.00256),
        (1, 4, 0.00128),
        (0, 2, 0.00022),
        (2, 0, -0.00022),
        (5, 0, 0.00026)]

    dx = 1E-5 * (x - X0)
    dy = 1E-5 * (y - Y0)

    lat = 52.15517440
    lon = 5.38720621

    for p, q, k in pqk:
        lat += k * dx ** p * dy ** q / 3600

    for p, q, l in pql:
        lon += l * dx ** p * dy ** q / 3600

    return lat, lon
pd.set_option('display.max_columns', None)
pd.options.display.max_colwidth = 1000
j = 1

# NDW dataset inlezen
NDW = pd.read_csv("C:/Users/davka/Downloads/ads2/verkeersborden_actueel_beeld.csv")
NDW = NDW.drop(
    columns=['type.1', 'number', 'type', 'schemaVersion', 'validated', 'validatedOn', 'userId', 'organisationId',
             'textSigns', 'wvk_id', 'name.1', 'code', 'image', 'firstSeen', 'lastSeen', 'removed',
             'publicationTimestamp'])

# df filteren op alleen Haarlem
NDW = NDW[NDW['townname'] == 'Haarlem']

# type bord fixen
names = ['A1-30', 'A1-30-ZB', 'A1-50', 'A1-70', 'A4-30', 'AB10', 'B1', 'B2', 'B2', 'B3', 'B5', 'B6', 'B6', 'B7', 'BB12',
         'BB15', 'BB35', 'BW3', 'BW207', 'C1', 'C2', 'C3', 'C4', 'C4L', 'C7', 'C9', 'C12', 'C15', 'C20', 'Camping',
         'D1', 'D2', 'D3', 'D5', 'D6', 'E1', 'E1', 'E1-ZB', 'E1-ZE', 'E2', 'E2-ZE', 'E3', 'E4', 'E6', 'E7', 'E101',
         'F10-B', 'G7', 'G11', 'G11', 'G12', 'G12-A', 'J2', 'J3', 'J11', 'J15', 'J15', 'J16', 'J20', 'J22', 'J22',
         'J23', 'J23', 'J24', 'J32', 'J37', 'J38', 'J38', 'K6', 'K7', 'K8', 'K10', 'K10', 'K11', 'K14', 'L2', 'L4',
         'L4', 'L05', 'L8', 'L8', 'L9', 'L10', 'L1002-A', 'OB70', 'OB703', 'VR9', 'flits camera']

## loop starts here ##
for i in range(0,len(glob.glob('C:/Users/davka/Downloads/ads2/resizedfinal/*')),2):

    shutil.rmtree("C:/Users/davka/PycharmProjects/pythonProject/yolov5/runs/detect/a")
    shutil.rmtree("C:/Users/davka/PycharmProjects/pythonProject/yolov5/runs/detect/b")

    foto1 = glob.glob('C:/Users/davka/Downloads/ads2/resizedfinal/*')[i]
    foto1_name = 'a'
    foto2 = glob.glob('C:/Users/davka/Downloads/ads2/resizedfinal/*')[i+1]
    foto2_name = 'b'

    # optional: locatie bord berekenen op beide fotos en gemiddelde nemen

    # #foto1 = "C:/Users/davka/Downloads/ads2/resized/20221005112857432_360_01.jpg"
    # #foto1 = "C:/Users/davka/Downloads/ads2/resized/20221005113402003_360_01.jpg" #tijdelijk bord
    # #foto1 = 'C:/Users/davka/Downloads/ads2/resized/20221005113444641_360_01.jpg'
    # #foto1 = 'C:/Users/davka/Downloads/ads2/resized/20221005112557143_360_01.jpg' #foto2 is accurater in dit geval
    # #foto1 = 'C:/Users/davka/Downloads/ads2/resized/20221005112618203_360_01.jpg'
    # #foto1 = 'C:/Users/davka/Downloads/ads2/resized/20221005112848700_360_01.jpg'
    # foto1 = 'C:/Users/davka/Downloads/ads2/clean folder/20221005112638232_360_01.jpg' #veel verkeerborden
    # foto1_name = 'a'
    # #foto2 = "C:/Users/davka/Downloads/ads2/resized/20221005112857944_360_01.jpg"
    # #foto2 = "C:/Users/davka/Downloads/ads2/resized/20221005113402518_360_01.jpg" #tijdelijk bord
    # #foto2 = 'C:/Users/davka/Downloads/ads2/resized/20221005113445155_360_01.jpg'
    # #foto2 = 'C:/Users/davka/Downloads/ads2/resized/20221005112557655_360_01.jpg' #foto2 is accurater in dit geval
    # #foto2 = 'C:/Users/davka/Downloads/ads2/resized/20221005112618716_360_01.jpg'
    # #foto2 = 'C:/Users/davka/Downloads/ads2/resized/20221005112849215_360_01.jpg'
    # foto2 = 'C:/Users/davka/Downloads/ads2/clean folder/20221005112638744_360_01.jpg' #veel verkeersboden
    # foto2_name = 'b'

    # foto 1 yolo runnen
    detect.run(weights="C:/Users/davka/PycharmProjects/pythonProject/yolov5/runs/train/exp13/weights/best.pt",
                      source=foto1,
                      data="C:/Users/davka/PycharmProjects/pythonProject/yolov5/data.yaml",
                      imgsz=(640, 640),
                      conf_thres=0.7,
                      save_txt=True,
                      name=foto1_name)

    # foto 2 yolo runnen
    detect.run(weights="C:/Users/davka/PycharmProjects/pythonProject/yolov5/runs/train/exp13/weights/best.pt",
                      source=foto2,
                      data="C:/Users/davka/PycharmProjects/pythonProject/yolov5/data.yaml",
                      imgsz=(640, 640),
                      conf_thres=0.7,
                      save_txt=True,
                      name=foto2_name)

    #time.sleep(5)

    foto1_strip = foto1[43:]
    foto1_txt_path = 'C:/Users/davka/PycharmProjects/pythonProject/yolov5/runs/detect/'+foto1_name+'/labels/'+foto1_strip[:-3]+'txt'
    foto2_strip = foto2[43:]
    foto2_txt_path = 'C:/Users/davka/PycharmProjects/pythonProject/yolov5/runs/detect/'+foto2_name+'/labels/'+foto2_strip[:-3]+'txt'

    if glob.glob(foto1_txt_path) and glob.glob(foto2_txt_path):

        foto1_img_path = 'C:/Users/davka/PycharmProjects/pythonProject/yolov5/runs/detect/' + foto1_name + '/' + foto1_strip
        foto2_img_path = 'C:/Users/davka/PycharmProjects/pythonProject/yolov5/runs/detect/' + foto2_name + '/' + foto2_strip
        sign_folder = 'C:/Users/davka/PycharmProjects/pythonProject/borden/'
        shutil.copy(foto1_img_path, sign_folder + foto1_strip)
        shutil.copy(foto2_img_path, sign_folder + foto2_strip)

        # foto1 txt bestand van yolo uitlezen voor plek van de bounding box
        df_txt1 = pd.read_csv(foto1_txt_path, sep=' ', names=['type', 'cx', 'cy', 'w', 'h'])
        df_txt2 = pd.read_csv(foto2_txt_path, sep=' ', names=['type', 'cx', 'cy', 'w', 'h'])

        #


        # txt bestanden sorteren
        df_txt1 = df_txt1.sort_values(by=['type', 'cy', 'cx'])
        df_txt2 = df_txt2.sort_values(by=['type', 'cy', 'cx'])

        # txt bestanden vergelijken
        for k in range(len(df_txt1.index)):
            print(df_txt1.index, df_txt2.index)
            if k+1 > len(df_txt2.index):
                break
            if df_txt1.iloc[k,0] == df_txt2.iloc[k,0]:

                foto1_type_bord = float(df_txt1.iloc[k,0])
                foto1_x_anno = float(df_txt1.iloc[k,1])
                print('Foto 1 type bord:', foto1_type_bord)
                print('Foto 1 X-coordinaat annotitie:', foto1_x_anno)

                foto2_type_bord = float(df_txt2.iloc[k,0])
                foto2_x_anno = float(df_txt2.iloc[k,1])
                print('Foto 2 type bord:', foto2_type_bord)
                print('Foto 2 X-coordinaat annotitie:', foto2_x_anno)

                ### Foto1 ####
                # if bounding box links van foto (<0.5)
                if foto1_x_anno < 0.5:
                    hoek1 = (1 - (foto1_x_anno / 0.5)) * 70

                # if bounding box rechts van foto (>0.5)
                else:
                    hoek1 = (foto1_x_anno - 0.5) * 70 * 2

                ### Foto2 ###
                # if bounding box links van foto (<0.5)
                if foto2_x_anno < 0.5:
                    hoek2 = (1 - (foto2_x_anno / 0.5)) * 70

                # if bounding box rechts van foto (>0.5)
                else:
                    hoek2 = (foto2_x_anno - 0.5) * 70 * 2

                print('Hoek 1 = ', hoek1)
                print('Hoek 2 = ', hoek2)

                # naam van foto 1 en 2 strippen en opzoeken in de iv infra dataset voor RD coordinaten
                ivinfra = pd.read_csv(
                    "C:/Users/davka/Downloads/ads2/IN__220025 De_Haagse_Hogeschool_360 foto_Orbit generic traject.csv", sep="\t")

                foto1_ivinfra = ivinfra[(ivinfra['Fotonaam'] == str(foto1_strip[:-7]))]
                foto1_ivinfra_X = float(foto1_ivinfra['X'].values)
                foto1_ivinfra_Y = float(foto1_ivinfra['Y'].values)
                print('Foto 1 coordinaten auto: ', foto1_ivinfra_X, foto1_ivinfra_Y)

                foto2_ivinfra = ivinfra[(ivinfra['Fotonaam'] == str(foto2_strip[:-7]))]
                foto2_ivinfra_X = float(foto2_ivinfra['X'].values)
                foto2_ivinfra_Y = float(foto2_ivinfra['Y'].values)
                print('Foto 2 coordinaten auto: ', foto2_ivinfra_X, foto2_ivinfra_Y)

                # afgelegde afstand tussen twee fotos = sqrt((x1-x2)^2+(y1-y2)^2)
                afgelegde_afstand = math.sqrt((foto1_ivinfra_X - foto2_ivinfra_X) ** 2 + (foto1_ivinfra_Y - foto2_ivinfra_Y) ** 2)
                print('Afgelegde afstand van auto:', afgelegde_afstand)

                ## afstand in de richting van de heading
                ## ((-tan(hoek foto2) * afstand) / (tan(hoek foto1)-tan(hoek foto2)))
                # hoeft mss niet -Bram

                # functie afstand bepalen van auto naar bord
                # ((-tan(hoek foto2) * afstand) / (tan(hoek foto1)-tan(hoek foto2))) / cos(hoek foto1)
                hoek1radialen = hoek1 * math.pi / 180
                hoek2radialen = hoek2 * math.pi / 180

                if hoek1radialen == hoek2radialen:
                    break

                afstand_tot_bord = (((math.tan(hoek2radialen) * -1) * afgelegde_afstand) / (
                            math.tan(hoek1radialen) - math.tan(hoek2radialen))) / math.cos(hoek1radialen)
                print('Afstand van auto tot bord foto1:', afstand_tot_bord)

                afstand_tot_bord2 = ((math.tan(hoek1radialen) * afgelegde_afstand) / (
                            math.tan(hoek2radialen) - math.tan(hoek1radialen))) / math.cos(hoek2radialen)
                print('Afstand van auto tot bord foto2:', afstand_tot_bord2)

                # heading uit df halen van foto1
                heading1 = float(ivinfra[ivinfra['Fotonaam'] == foto1_strip[:-7]]['Heading'].values)
                print('Heading: ', heading1)

                heading2 = float(ivinfra[ivinfra['Fotonaam'] == foto2_strip[:-7]]['Heading'].values)
                print('Heading: ', heading2)

                # buitenhoek = 360 - heading - hoek foto1
                buitenhoek1 = (360 - heading1 - hoek1) % 90
                print('Buitenhoek 1: ', buitenhoek1)

                buitenhoek2 = (360 - heading2 - hoek2) % 90
                print('Buitenhoek 2: ', buitenhoek2)

                # afgelegde afstand in Y = cos(buitenhoek) * afstand tot bord
                afgelegde_afstand_Y = abs(math.cos(buitenhoek1 * math.pi / 180) * afstand_tot_bord)
                print('Afgelegde afstand in Y foto1: ', afgelegde_afstand_Y)

                afgelegde_afstand_Y2 = abs(math.cos(buitenhoek2 * math.pi / 180) * afstand_tot_bord2)
                print('Afgelegde afstand in Y foto2: ', afgelegde_afstand_Y2)

                # afgelegde afstand in X = cos(90-buitenhoek) * afstand naar bord
                afgelegde_afstand_X = abs(math.cos((90 - buitenhoek1) * math.pi / 180) * afstand_tot_bord)
                print('Afgelegde afstand in X foto1: ', afgelegde_afstand_X)

                afgelegde_afstand_X2 = abs(math.cos((90 - buitenhoek2) * math.pi / 180) * afstand_tot_bord2)
                print('Afgelegde afstand in X foto2: ', afgelegde_afstand_X2)

                # nieuwe coordinaten bepalen

                # nieuw X = oud X + afgelegde afstand in X
                if (heading1 + hoek1) % 360 <= 90:
                    nieuw_X = foto1_ivinfra_X + afgelegde_afstand_X
                    nieuw_Y = foto1_ivinfra_Y + afgelegde_afstand_Y
                elif heading1 + hoek1 <= 180:
                    nieuw_X = foto1_ivinfra_X + afgelegde_afstand_X
                    nieuw_Y = foto1_ivinfra_Y - afgelegde_afstand_Y
                elif heading1 + hoek1 <= 270:
                    nieuw_X = foto1_ivinfra_X - afgelegde_afstand_X
                    nieuw_Y = foto1_ivinfra_Y - afgelegde_afstand_Y
                elif heading1 + hoek1 <= 360:
                    nieuw_X = foto1_ivinfra_X - afgelegde_afstand_X
                    nieuw_Y = foto1_ivinfra_Y + afgelegde_afstand_Y

                if (heading2 + hoek2) % 360 <= 90:
                    nieuw_X2 = foto2_ivinfra_X + afgelegde_afstand_X2
                    nieuw_Y2 = foto2_ivinfra_Y + afgelegde_afstand_Y2
                elif heading2 + hoek2 <= 180:
                    nieuw_X2 = foto2_ivinfra_X + afgelegde_afstand_X2
                    nieuw_Y2 = foto2_ivinfra_Y - afgelegde_afstand_Y2
                elif heading2 + hoek2 <= 270:
                    nieuw_X2 = foto2_ivinfra_X - afgelegde_afstand_X2
                    nieuw_Y2 = foto2_ivinfra_Y - afgelegde_afstand_Y2
                elif heading2 + hoek2 <= 360:
                    nieuw_X2 = foto2_ivinfra_X - afgelegde_afstand_X2
                    nieuw_Y2 = foto2_ivinfra_Y + afgelegde_afstand_Y2

                print('Berekend coordinaat X van bord foto1: ', nieuw_X)
                print('Berekend coordinaat X van bord foto2: ', nieuw_X2)

                # nieuw Y = oud Y + afgelegde afstand in Y

                print('Berekend coordinaat Y van bord foto1: ', nieuw_Y)

                # nieuw_Y2 = foto2_ivinfra_Y + afgelegde_afstand_Y2
                print('Berekend coordinaat Y van bord foto2: ', nieuw_Y2)

                avg_X = (nieuw_X + nieuw_X2) / 2
                avg_Y = (nieuw_Y + nieuw_Y2) / 2

                foto1_type_bord_clean = names[int(foto1_type_bord)]

                # filteren voor alle verkeersborden van dat type in straal van 5-10m staan van berekende bord locatie
                NDW1 = NDW[(NDW['rvvCode'] == foto1_type_bord_clean) & (NDW['x'] <= nieuw_X + 40) & (NDW['x'] >= nieuw_X - 40)
                           & (NDW['y'] <= nieuw_Y + 40) & (NDW['y'] >= nieuw_Y - 40)]

                NDW2 = NDW[(NDW['rvvCode'] == foto1_type_bord_clean) & (NDW['x'] <= nieuw_X2 + 40) & (NDW['x'] >= nieuw_X2 - 40)
                           & (NDW['y'] <= nieuw_Y2 + 40) & (NDW['y'] >= nieuw_Y2 - 40)]
                print(NDW1)
                if len(NDW1.index) == 0 or len(NDW2.index) == 0:
                    print('Geen verkeersborden gedetecteerd\n')
                    continue
                # if aantal gevonden borden >1
                if len(NDW1.index) > 1 and len(NDW2.index) > 1:
                    # afstand bepalen van de auto naar elk bord
                    # pythagoras coordinaten van NDW en onze eigen berekende coordinaten

                    NDW1['afstand1'] = 0
                    NDW2['afstand2'] = 0

                    for i in range(len(NDW1.index)):
                        NDW1.iloc[i, -1:] = math.sqrt((nieuw_X - NDW1.iloc[i, 4]) ** 2 + (nieuw_Y - NDW1.iloc[i, 5]) ** 2)

                    for i in range(len(NDW2.index)):
                        NDW2.iloc[i, -1:] = math.sqrt((nieuw_X - NDW2.iloc[i, 4]) ** 2 + (nieuw_Y - NDW2.iloc[i, 5]) ** 2)

                    # neem dichtsbijzijnde bord
                    NDW1 = NDW1[NDW1['afstand1'] == NDW1['afstand1'].min()]
                    NDW2 = NDW2[NDW2['afstand2'] == NDW2['afstand2'].min()]
                # coordinaten (afstand) vergelijken
                print('NDW1: ', NDW1)
                print('\n\nNDW2: ', NDW2)

                NDWlat = NDW1['latitude'].values[0]
                NDWlong = NDW1['longitude'].values[0]

                # punt1 = rd_to_wgs(nieuw_X, nieuw_Y)
                # punt2 = rd_to_wgs(nieuw_X2, nieuw_Y2)

                f = open("C:/Users/davka/Downloads/ads2/punten.txt", 'a')
                f.write(str(j) + ', ' + str(NDWlat) + ', ' + str(NDWlong) + ', ' + str(NDW1['rvvCode'].values[0]) + ', 10000' + '\n')
                f.close()
                j+=1

df = pd.read_csv("C:/Users/davka/Downloads/ads2/punten.txt")
df.columns = ['id', 'latitude', 'longitude', 'type', 'size']
# print('DF BELOW\n')
# print(df)
# print('\n')
color_scale = [(0, 'orange'), (1, 'red')]

fig = px.scatter_mapbox(df,
                        lat="latitude",
                        lon="longitude",
                        hover_name='type',
                        # hover_data=["Address", "Listed"],
                        # color="Listed",
                        color_continuous_scale=color_scale,
                        size='size',
                        zoom=13,
                        height=1080,
                        width=1920)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()

# print('\nRD coordinaten 1: ', punt1)
# print('RD coordinaten 2: ', punt2)
