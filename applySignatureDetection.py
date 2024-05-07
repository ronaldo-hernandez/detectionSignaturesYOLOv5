import os
# pip install pysqlite3
import cv2
from signature_detector import *
import re
import time
from saveImgData import saveDataIntoSQLite

path_to_model = {"path_to_model" : "modelTrained/best.pt"}
signature_detector = YoloSignatureDetector(**path_to_model)

def truncateExtension(nameImg):
    PATRON = re.findall(".*(.[a-z]{3})",nameImg)[0]
    nameImg = nameImg.replace(PATRON,"")
    return nameImg


def detectOneImg(nameImg):
    start = time.time()
    print("1). Se empezo a leer la imagen. | 'tiempo':", time.time() - start)
    picture = cv2.imread(nameImg)
    start = time.time()
    print("1.1). Se terminó de leer la imagen. | 'tiempo':", time.time() - start)
    start = time.time()
    predicted = signature_detector.predict(images=[picture])
    print("3). Se implementó el modelo. | 'tiempo':", time.time() - start)
    confidenceList = []
    count = 1
    for image in predicted:
        for signature in image:
            confidenceList.append({f"firmaN_{count}":signature.confidence})
            picture = cv2.rectangle(picture,
                                    (int(signature.x_min), int(signature.y_min)),
                                    (int(signature.x_max), int(signature.y_max)),(255, 0, 0),2)
            count += 1
    signaturesDetected = len(confidenceList)
    status, encodeImg = cv2.imencode(".png",picture)
    imgInBytes = ""
    if status:
        imgInBytes = encodeImg.tobytes()
        with open(f"{truncateExtension(nameImg)}_ImgSD.png","wb") as file:
            file.write(imgInBytes)
    context = {}
    context.update({"firmasDetectadas":signaturesDetected})
    context.update({"modelResult":str(predicted)})
    context.update({"confidenceBySign":str(confidenceList)})
    context.update({"nameImage":nameImg})
    collectionToSave = []
    for row in context:
        collectionToSave.append(context[row])
    resultSaved = saveDataIntoSQLite(tuple(collectionToSave))
    if resultSaved["status"] ==200:
        context.update({"savedInSQL":True})
    else:
        context.update({"savedInSQL":False})
    return context

