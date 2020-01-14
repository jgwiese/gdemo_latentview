import sys
import argparse

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from ui_mainwindow import Ui_MainWindow

import numpy as np
import torch
import Autoencoder as Autoencoder

parser = argparse.ArgumentParser()
parser.add_argument('--model', default='./model/model-checkpoint.pt', type=str, help='path to ml model')

class Model(QObject):
    inferred = Signal()

    def __init__(self, ml_model_path):
        super().__init__()
        checkpoint = torch.load(ml_model_path, map_location='cpu')
        self.autoencoder = Autoencoder.VariationalAutoencoder(imageShape=(1, 128, 128),
                                                          firstFilterCount=16,
                                                          act=torch.nn.functional.elu, layerwise=False)
        self.autoencoder.load_state_dict(checkpoint['model_state_dict'])

        # providing a vector z from one sample of the validation set
        self.z = torch.from_numpy(np.asarray([-8.8492e-01,  3.2924e-01,  1.6989e+00, -1.1646e+00, -6.7215e-01,
         -8.3765e-01,  1.0475e+00, -7.6167e-01,  1.5044e+00, -2.0770e+00,
         -8.9687e-01, -1.5045e+00,  1.8635e-01,  2.8085e-01,  1.4227e-01,
         -1.1353e+00, -6.4419e-01,  1.3345e+00,  5.4033e-02, -4.6920e-01,
         -6.1643e-01,  1.7381e+00, -3.0586e-01, -2.5329e-01,  3.1175e+00,
         -1.0362e+00, -1.3935e+00,  1.0158e+00,  6.3395e-01, -6.8531e-02,
         -1.1117e+00, -3.7122e-01, -3.5248e-01,  1.7212e-01,  1.2474e+00,
         -6.1144e-01, -7.1520e-01, -1.0144e+00, -1.4054e+00,  5.7090e-01,
         -1.0911e+00,  3.9517e-01,  1.2465e+00, -1.9319e-01, -5.3027e-01,
         -5.3061e-01, -6.7704e-01,  8.0270e-02,  4.9083e-02,  1.0887e-01,
          2.8546e-03, -7.6487e-01,  6.9228e-01,  1.3604e+00, -6.7222e-01,
          5.9886e-03,  7.5945e-01,  5.2745e-02,  1.9323e+00,  4.1338e-01,
         -1.1450e+00,  7.0341e-01, -4.3833e-01,  3.2049e-01], dtype=np.float32)).unsqueeze(0)

        self.infer()
        self.image = np.zeros((1, 64, 64), dtype=np.float32)
        self.image_segmentation = np.zeros((1, 64, 64), dtype=np.float32)

    def infer(self):
        self.image = torch.sigmoid(self.autoencoder.decoder.forward(self.z, 4, (1, 256, 2, 2))).detach()
        self.image = self.image.squeeze(0).permute(1, 2, 0)
        self.image = (self.image.numpy() * 255).astype(np.ubyte)
        self.image = np.stack([self.image] * 3, axis=2).squeeze()

        self.image_segmentation = torch.sigmoid(self.autoencoder.decoder_segmentation.forward(self.z, 4, (1, 256, 2, 2))).detach()
        self.image_segmentation = self.image_segmentation.squeeze(0).permute(1, 2, 0)
        self.image_segmentation = self.image_segmentation.numpy().astype(np.float32)
        binary_map = self.image_segmentation[..., 0] > 0.1
        self.image[binary_map] = self.image_segmentation[binary_map] * np.array([0, 255, 127])

        self.inferred.emit()

class View(QMainWindow):
    slider_moved = Signal(int, int)

    def __init__(self):
        super(View, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('latent space viewer')
        self.setWindowFlag(Qt.Dialog, True)
        self.imageSize = QSize(512, 512)
        self.pixmap = QPixmap(self.imageSize)

        self.sliders = [self.ui.horizontalSlider_1, self.ui.horizontalSlider_2, self.ui.horizontalSlider_3,
                                 self.ui.horizontalSlider_4, self.ui.horizontalSlider_5, self.ui.horizontalSlider_6,
                                 self.ui.horizontalSlider_7, self.ui.horizontalSlider_8, self.ui.horizontalSlider_9,
                                 self.ui.horizontalSlider_10, self.ui.horizontalSlider_11, self.ui.horizontalSlider_12,
                                 self.ui.horizontalSlider_13, self.ui.horizontalSlider_14, self.ui.horizontalSlider_15,
                                 self.ui.horizontalSlider_16]

        self.signalMapper = QSignalMapper()
        self.signalMapper.mapped.connect(self.on_sliderMoved)
        for slider in self.sliders:
            self.signalMapper.setMapping(slider, int(slider.objectName().split('_')[-1]) - 1)
            slider.valueChanged.connect(self.signalMapper.map)

    def on_sliderMoved(self, id):
        value = self.sliders[id].value()
        self.slider_moved.emit(id, value)

    def draw_image(self, image):
        self.pixmap = QPixmap().fromImage(image.copy()).scaled(self.imageSize)
        self.ui.canvas.setPixmap(self.pixmap)

class Controller():
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Connections
        self.model.inferred.connect(self.on_inferred)
        self.view.slider_moved.connect(self.on_sliderMoved)

        self.on_sliderMoved(0, 0)

    def on_inferred(self):
        image = QImage(self.model.image, self.model.image.shape[0], self.model.image.shape[1], QImage.Format_RGB888)
        self.view.draw_image(image)

    def on_sliderMoved(self, id, value):
        self.model.z[0, id] = value / 1.0
        self.model.infer()

class Program():
    def __init__(self, argv):
        args = parser.parse_args(argv[1:])
        self.model = Model(args.model)
        self.view = View()
        self.controller = Controller(self.model, self.view)
        self.view.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = Program(sys.argv)
    sys.exit(app.exec_())
