from PIL import Image
from pyffmpeg import FFmpeg
from docx2pdf import convert as Convert2PDF

#KAMUS:
#SupportedImageFiles, SupportedAudioFiles, SupportedVideoFiles : string array
#FFmpegClient : FFmpegObject

SupportedImageFiles = [
    "jpg",
    "png",
    "bmp",
    "gif",
    "webp"
]

SupportedAudioFiles = [
    "mp2",
    "mp3",
    "wav"
]

SupportedVideoFiles = [
    "mp4",
    "mkv",
    "mov"
]

def CheckSupport(Extension : str, SupportList : list):

    #KAMUS LOKAL
    #Extension, SupportList : string

    if Extension not in SupportList:
        return False
    return True

def GetExtension(File : str):

    #KAMUS LOKAL
    #File : string

    return File.split(".")[-1].lower()

def GetFileGroup(File : str):

    #KAMUS LOKAL
    #File, Extension : string

    Extension = GetExtension(File)

    if Extension in SupportedImageFiles:
        return "Image"
    
    if Extension in SupportedAudioFiles:
        return "Audio"
    
    if Extension in SupportedVideoFiles:
        return "Video"
    
    if (Extension == "pdf"):
        return "PDF"
    
    if (Extension == "docx"):
        return "Docx"
    
    return "Unknown"

def CheckImageSupport(Extension : str):

    #KAMUS LOKAL
    #Extension : string

    return CheckSupport(Extension, SupportedImageFiles)

def ConvertImageWithRGB(Source : str, Destination : str):

    #KAMUS LOKAL
    #Source, Destination : string
    #File, RGB_File : Image

    try:
        with Image.open(Source) as File:
            RGB_File = File.convert("RGB")
            RGB_File.save(Destination)

        return True
    except:
        return False

def ConvertImageWithoutRGB(Source : str, Destination : str):

    #KAMUS LOKAL
    #Source, Destination : string
    #File : Image

    try:
        with Image.open(Source) as File:
            File.save(Destination)

        return True
    except:
        return False

def ConvertImage(Source : str, Destination : str):

    #KAMUS LOKAL
    #Source, Destination : string

    if (GetFileGroup(Source) != "Image"): return False
    if (GetFileGroup(Destination) != "Image"): return False
    
    if (GetExtension(Destination) == "jpg"):
        return ConvertImageWithRGB(Source, Destination)
    
    return ConvertImageWithoutRGB(Source, Destination)

FFmpegClient = FFmpeg(enable_log=False)

def CheckAudioSupport(Extension : str):

    #KAMUS LOKAL
    #Extension : string

    return CheckSupport(Extension, SupportedAudioFiles)

def ConvertAudio(Source : str, Destination : str):

    #KAMUS LOKAL
    #Source, Destination : string

    if (GetFileGroup(Source) != "Audio"): return False
    if (GetFileGroup(Destination) != "Audio"): return False

    try:
        FFmpegClient.convert(Source, Destination)
        return True
    except:
        return False

def CheckVideoSupport(Extension : str):

    #KAMUS LOKAL
    #Extension : string

    return CheckSupport(Extension, SupportedVideoFiles)

def ConvertVideo(Source : str, Destination : str):

    #KAMUS LOKAL
    #Source, Destination : string

    if (GetFileGroup(Source) != "Video"): return False
    if (GetFileGroup(Destination) != "Video"): return False

    try:
        FFmpegClient.convert(Source, Destination)
        return True
    except:
        return False

def ConvertImageToPdf(Source : str, Destination : str):

    #KAMUS LOKAL
    #Source, Destination : string

    if (GetFileGroup(Source) != "Image"): return False
    if (GetFileGroup(Destination) != "PDF"): return False

    try:
        ConvertImageWithRGB(Source, Destination)
        return True
    except:
        return False

def ConvertVideoToAudio(Source : str, Destination : str):

    #KAMUS LOKAL
    #Source, Destination : string

    if (GetFileGroup(Source) != "Video"): return False
    if (GetFileGroup(Destination) != "Audio"): return False

    try:
        FFmpegClient.convert(Source, Destination)
        return True
    except:
        return False

def ConvertDocxtoPdf(Source : str, Destination : str):

    #KAMUS LOKAL
    #Source, Destination : string

    if (GetFileGroup(Source) != "Docx"): return False
    if (GetFileGroup(Destination) != "PDF"): return False

    try:
        Convert2PDF(Source, Destination)
        return True
    except:
        return False