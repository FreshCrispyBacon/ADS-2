import cv2
from datetime import datetime

counter = 0
now = datetime.now()
print('Starting time: ', datetime.now())

for filename in glob.glob('alles/20221005_selectie_360_5/*'):
    
    # read image
    img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    #print('Original Dimensions of image number ', counter, ' is: ',img.shape)
 
    # new dimensions
    width = 640
    height = 640
    dim = (width, height)
 
    # resize image
    resized = cv2.resize(img, dim)
 
    #print('Resized Dimensions : ',resized.shape)
    
    # save new image
    if filename[-5:-4] == '1':
        cv2.imwrite('resizedfinal/'+filename[-28:] ,resized)
        print(filename[-28:])
        print('Image number: ', counter)
    
        counter += 1

print('Finished time: ', datetime.now())
print('Total time: ', datetime.now()-now)
