import Convert
def Convert():
    file_name = input("Enter the file name: ")
    output_format = input("Enter the desired format (e.g., jpg, pdf, etc.): ")
    print("Option 1: Convert selected")
def Transcribe():
    print("Option 2: Transcribe selected")

def Download():
    print("Option 3: Download selected")

selection = True
while selection:
    print("Menu:")
    print("1. Convert")
    print("2. Transcribe")
    print("3. Download")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == '1':
        (Convert())
    elif choice == '2':
        (Transcribe())
    elif choice == '3':
        (Download())
    else:
        print("Exiting the program.")
        selection = False