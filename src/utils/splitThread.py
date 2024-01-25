from PyQt5.QtCore import QThread, pyqtSignal
from PIL import Image, ImageFilter



class SplitThread(QThread):
    updateSignal = pyqtSignal(int)
    def __init__(self, gifPath, outputPath, outputFolder, count):
        super().__init__()
        self.gifPath = gifPath
        self.outputFolder = outputFolder
        self.outputPath = outputPath

        with Image.open(self.gifPath) as image:
            self.frameCount = image.n_frames
            image.seek(0)
            frame = image.copy()
            convertedImage = frame.convert('RGB')
            bluredImage = convertedImage.filter(ImageFilter.GaussianBlur(10))
            bluredImage.save(f"{self.outputPath}/blur{count}.jpg", "JPEG")


    def run(self):
        with Image.open(self.gifPath) as image:
            self.frameCount = image.n_frames
            for i in range(self.frameCount):
                image.seek(i)
                frame = image.copy()
                frame.save(f"{self.outputPath}{self.outputFolder}/bg{i+1}.png", "PNG")
