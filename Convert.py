from PIL import Image
from pyffmpeg import FFmpeg

SupportedImageFiles = [
    "jpg",
    "png",
    "bmp",
    "gif",
    "webp"
]

def CheckImageSupport(Extension : str):
    if Extension not in SupportedImageFiles:
        return False
    return True

def ConvertImageWithRGB(Source : str, Destination : str):
    with Image.open(Source) as File:
        RGB_File = File.convert("RGB")
        RGB_File.save(Destination)

def ConvertImageWithoutRGB(Source : str, Destination : str):
    with Image.open(Source) as File:
        File.save(Destination)

def ConvertImage(Source : str, Destination : str):
    SourceExtension = Source.split(".")[-1]
    DestinationExtension = Source.split(".")[-1]

    if not CheckImageSupport(SourceExtension): return
    if not CheckImageSupport(DestinationExtension): return

    if (DestinationExtension == "jpg"):
        return ConvertImageWithRGB(Source, Destination)
    
    return ConvertImageWithoutRGB(Source, Destination)

