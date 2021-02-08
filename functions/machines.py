def sampling (text, startPos, endPos, samplingStep):
    return text[startPos:endPos:samplingStep]

def histogramRed (image):
    return image[0:len(image):3]

def histogramGreen (image):
    return image[1:len(image):3]

def histogramBlue (image):
    return image[2:len(image):3]