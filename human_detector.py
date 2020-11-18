import cv2
import numpy as np
import file_operation
import configg
import picfilter
import os

url_config = './yolofile/yolov3.cfg'
url_weights = './yolofile/yolov3.weights'
url_classes = './yolofile/yolov3.txt'

# get file path list
filepathlist = file_operation.get_filelist(configg.prepare_folder)


def get_output_layers(nets):
    layer_names = nets.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in nets.getUnconnectedOutLayers()]
    return output_layers


def human_classify():
    net = cv2.dnn.readNet(url_weights, url_config)

    for url_image in filepathlist:
        image = cv2.imread(url_image)
        scale = 0.00392
        blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(get_output_layers(net))
        class_ids = []
        confidences = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    class_ids.append(class_id)
                    confidences.append(float(confidence))

        if class_ids.__contains__(0):
            picfilter.movesiglefile(url_image, configg.storage_folder + 'human\\' + os.path.basename(url_image))
        else:
            picfilter.movesiglefile(url_image, configg.storage_folder + 'noman\\' + os.path.basename(url_image))
