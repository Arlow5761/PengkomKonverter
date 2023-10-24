from PIL import Image
from pyffmpeg import FFmpeg
from docx2pdf import convert as Convert2PDF

def CheckSupport(Extension : str, SupportList : list):
    if Extension not in SupportList:
        return False
    return True

def GetExtension(File : str):
    return File.split(".")[-1]

def GetFileGroup(File : str):
    Extension = GetExtension(File)

    if Extension in SupportedImageFiles:
        return "Image"
    
    if Extension in SupportedAudioFiles:
        return "Audio"
    
    if Extension in SupportedVideoFiles:
        return "Video"
    
    return "Unknown"

SupportedImageFiles = [
    "jpg",
    "png",
    "bmp",
    "gif",
    "webp"
]

def CheckImageSupport(Extension : str):
    return CheckSupport(Extension, SupportedImageFiles)

def ConvertImageWithRGB(Source : str, Destination : str):
    with Image.open(Source) as File:
        RGB_File = File.convert("RGB")
        RGB_File.save(Destination)
    
    return True

def ConvertImageWithoutRGB(Source : str, Destination : str):
    with Image.open(Source) as File:
        File.save(Destination)
    
    return True

def ConvertImage(Source : str, Destination : str):
    SourceExtension = Source.split(".")[-1]
    DestinationExtension = Destination.split(".")[-1]

    if not CheckImageSupport(SourceExtension): return False
    if not CheckImageSupport(DestinationExtension): return False
    
    if (DestinationExtension == "jpg"):
        return ConvertImageWithRGB(Source, Destination)
    
    return ConvertImageWithoutRGB(Source, Destination)

SupportedAudioFiles = [
    "mp2",
    "mp3",
    "wav"
]

FFmpegClient = FFmpeg()

def CheckAudioSupport(Extension : str):
    return CheckSupport(Extension, SupportedAudioFiles)

def ConvertAudio(Source : str, Destination : str):
    SourceExtension = Source.split(".")[-1]
    DestinationExtension = Source.split(".")[-1]

    if not CheckAudioSupport(SourceExtension): return False
    if not CheckAudioSupport(DestinationExtension): return False

    FFmpegClient.convert(Source, Destination)

    return True

SupportedVideoFiles = [
    "mp4",
    "mkv",
    "mov"
]

def CheckVideoSupport(Extension : str):
    return CheckSupport(Extension, SupportedVideoFiles)

def ConvertVideo(Source : str, Destination : str):
    SourceExtension = Source.split(".")[-1]
    DestinationExtension = Source.split(".")[-1]

    if not CheckVideoSupport(SourceExtension): return False
    if not CheckVideoSupport(DestinationExtension): return False

    FFmpegClient.convert(Source, Destination)

    return True

def ConvertImageToPdf(Source : str, Destination : str):
    SourceExtension = GetExtension(Source)
    DestinationExtension = GetExtension(Destination)

    if not CheckImageSupport(SourceExtension): return False
    if (DestinationExtension != "pdf"): return False

    ConvertImageWithRGB(Source, Destination)

    return True

def ConvertVideoToAudio(Source : str, Destination : str):
    SourceExtension = GetExtension(Source)
    DestinationExtension = GetExtension(Destination)

    if not CheckVideoSupport(SourceExtension): return False
    if not CheckAudioSupport(DestinationExtension): return False

    FFmpegClient.convert(Source, Destination)

    return True

def ConvertDocxtoPdf(Source : str, Destination : str):
    SourceExtension = GetExtension(Source)
    DestinationExtension = GetExtension(Destination)

    if (SourceExtension != "docx"): return
    if (DestinationExtension != "pdf"): return

    Convert2PDF(Source, Destination)

    return True