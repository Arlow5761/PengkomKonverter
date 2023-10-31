import Convert
import transcribe
import Downloader as Downloader
def Converter():
    print("Option 1: Convert selected")
    file_name = input("Enter the file name: ")
    output_format = input("Enter the desired format (e.g., jpg, pdf, etc.): ")
    output_file = file_name.split(".") [0] + "." + output_format
    file_group = Convert. GetFileGroup (file_name)
    if file_group == Convert. GetFileGroup (output_file):
        if file_group == "Image":
            Convert. ConvertImage (file_name, output_file)
        elif file_group  == "Audio":
            Convert. ConvertAudio (file_name, output_file)
        elif file_group  == "Video":
            Convert. ConvertVideo (file_name, output_file)
    else:
        if file_group == "Video" and Convert. GetFileGroup (output_file) == "Audio":
            Convert. ConvertVideoToAudio (file_name, output_file)
        elif file_group == "Image" and Convert. GetFileGroup (output_file) == "PDF":
            Convert. ConvertImageToPdf (file_name, output_file)
        elif file_group == "Docx" and Convert. GetFileGroup (output_file) == "PDF":
            Convert. ConvertDocxtoPdf (file_name, output_file)
        else:
            print("File type not supported!")
            return
    print("Convert finished")

def Transcribe():
    print("Option 2: Transcribe selected")
    file_name = input("Enter the file name: ")
    output_format = input("Enter the desired output file name: ")
    transcribe. transcribe (file_name, output_format)
    print("Transcribe finished")

def Download():
    print("Option 3: Download selected")
    Downloader.Download ()
    print("Download finished")

selection = True
while selection:
    print("Menu:")
    print("1. Convert")
    print("2. Transcribe")
    print("3. Download")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == '1':
        (Converter())
    elif choice == '2':
        (Transcribe())
    elif choice == '3':
        (Download())
    elif choice == '4':
        print("Exiting the program.")
        selection = False