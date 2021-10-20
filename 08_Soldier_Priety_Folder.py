
import os

def soldier_prettify(path, file, extn):

    os.chdir(path)
    folder_content = os.listdir()
    # jpg_files = [x for x in folder_content if x.split(".")[1]=="jpg"]
    # for i in range(len(jpg_files)):
    #     old_name = f"{path}\\{jpg_files[i]}"
    #     new_name = f"{path}\\{i+1}.jpg"
    #     os.rename(old_name, new_name)

    pdf_files = [x for x in folder_content if x.split(".")[1]=='pdf']

    for i in range(len(pdf_files)):
        old_name = f"{path}\\{pdf_files[i]}"
        new_name = f"{path}\\{pdf_files[i].split('.')[0].capitalize()}.pdf"
        os.rename(old_name,new_name)




if __name__ == '__main__':

    path = "F:\\dfp"
    file = 'h_file.txt'
    extn = 'jpg'

    soldier_prettify(path, file, extn)
    