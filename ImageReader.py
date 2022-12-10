from craft_hw_ocr import OCR
from transformers import  TrOCRProcessor, VisionEncoderDecoderModel

ocr = OCR.load_models()

def Image_To_text(image):
    
    img = OCR.load_image(image)
    
    processor = TrOCRProcessor.from_pretrained("microsoft/trocr-small-handwritten")
    model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-small-handwritten")

    img, results = OCR.detection(img, ocr[2])

    _ , text = OCR.recoginition(img, results, processor, model)

    return text