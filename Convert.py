from PIL import Image
from pyffmpeg import FFmpeg

def CheckSupport(Extension : str, SupportList : list):
    if Extension not in SupportList:
        return False
    return True

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

def ConvertImageWithoutRGB(Source : str, Destination : str):
    with Image.open(Source) as File:
        File.save(Destination)

def ConvertImage(Source : str, Destination : str):
    SourceExtension = Source.split(".")[-1]
    DestinationExtension = Destination.split(".")[-1]

    if not CheckImageSupport(SourceExtension): return
    if not CheckImageSupport(DestinationExtension): return
    
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

    if not CheckAudioSupport(SourceExtension): return
    if not CheckAudioSupport(DestinationExtension): return

    FFmpegClient.convert(Source, Destination)

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

    if not CheckVideoSupport(SourceExtension): return
    if not CheckVideoSupport(DestinationExtension): return

    FFmpegClient.convert(Source, Destination)
