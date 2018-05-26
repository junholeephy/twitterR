import os,sys
def str_list(filename):
    if(filename[0] == '/'):                 # 'filename' of absoulte location 
        filename = filename
    elif(filename[0] == '~'):
        filename = filename.replace("~",os.environ['HOME'])
    elif((filename[0]=="C")&(filename[1]==":")):
        filename = filename
    else:
        filename = os.getcwd() + "/" + filename

    loca = len(filename)
    for i in range(1,len(filename)+1):       # find the "/" location
        if(filename[-i] == '/'):
            loca = i-1
            break
    FILENAME = filename.replace(filename[:-loca],"")
    FILE = FILENAME.replace(".txt","")    #filetxt
    filename_NoRoot = filename.replace(filename[len(filename)-loca:len(filename)],"")

    filelist = [FILE, FILENAME, filename, filename_NoRoot]
    #[filename, filename.txt, absolute path filename.txt, absolute path]

    soo_file = open(filelist[2],"r")
    soo_list = []
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for line in soo_file:
        line = line.replace("\r\n","")
        line = line.replace("\n","")
        no_punct = ""
        for char in line:
            if char not in punctuations:
                no_punct = no_punct + char
        soo_list.append(no_punct)
    soo_file.close()
    return soo_list

def main():
    inputfile = "../python_positive.txt"
    ttt = str_list(inputfile)
    print(ttt)

if __name__=="__main__":
    main()

