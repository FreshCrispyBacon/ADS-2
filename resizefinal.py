import numpy as np
import pandas as pd
from IPython.display import Image, display
import glob
import cv2

lijst = []
for filename in glob.glob("C:/Users/davka/Downloads/ads2/resized/*"):
    lijst.append(filename)
lijst = [[x[-28:-14],x[-14:-11],x[-5:-4]] for x in lijst]

df = pd.DataFrame(lijst, columns=['Tijd','MS','Nummer'])
df['Tijd'] = pd.to_datetime(df['Tijd'])
df = df.sort_values(['Tijd','MS','Nummer'])
df = df[df['Nummer']!='6']
df = df.reset_index()
print(df)