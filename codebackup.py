# import cv2
#
# faceClassifier = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
# objImage = cv2.imread('C:\\Users\\2002251505\\Desktop\\pictrain\\psn\\psn10248.jpg')
# cvtImage = cv2.cvtColor(objImage, cv2.COLOR_BGR2GRAY)
# foundFaces = faceClassifier.detectMultiScale(cvtImage, scaleFactor=1.3, minNeighbors=9, minSize=(50, 50))
# print(" There are {} faces in the input image".format(len(foundFaces)))
# for (x, y, w, h) in foundFaces:
#     cv2.rectangle(objImage, (x, y), (x + w, y + h), (0, 0, 255), 2)
# cv2.namedWindow("xx", 0)
# cv2.imshow("xx", objImage)
# cv2.waitKey(0)
####################################################################################################################
# import cv2
# import numpy as np
# import file_operation
# import configg
# import picfilter
# import os
#
# url_config = './yolofile/yolov3.cfg'
# url_weights = './yolofile/yolov3.weights'
# url_classes = './yolofile/yolov3.txt'
#
# # get file path list
# filepathlist = file_operation.get_filelist(configg.prepare_folder)
#
#
# def get_output_layers(nets):
#     layer_names = nets.getLayerNames()
#     output_layers = [layer_names[i[0] - 1] for i in nets.getUnconnectedOutLayers()]
#     return output_layers
#
#
# net = cv2.dnn.readNet(url_weights, url_config)
#
# for url_image in filepathlist:
#     image = cv2.imread(url_image)
#     scale = 0.00392
#     blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop=False)
#     net.setInput(blob)
#     outs = net.forward(get_output_layers(net))
#     class_ids = []
#     confidences = []
#
#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.5:
#                 class_ids.append(class_id)
#                 confidences.append(float(confidence))
#
#     if class_ids.__contains__(0):
#         picfilter.movesiglefile(url_image, configg.storage_folder + 'human\\' + os.path.basename(url_image))
#     else:
#         picfilter.movesiglefile(url_image, configg.storage_folder + 'noman\\' + os.path.basename(url_image))
####################################################################################################################


####################################################################################################################


####################################################################################################################


####################################################################################################################


####################################################################################################################


####################################################################################################################


####################################################################################################################


####################################################################################################################


####################################################################################################################

