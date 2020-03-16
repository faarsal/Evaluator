import os
import shutil
import multiprocessing



def main():
    #Looping over all folders
    marksfile=open("marks.csv",'w+')
    folders=os.listdir()
    folders=[w for w in folders if w.find(".")==-1]
    print(folders)
    for i in folders:
        print("Folder start:"+i)
        for root, dirs, files in os.walk('./'+i):  # replace the . with your starting directory
            for file in files:
                path_file = os.path.join(root,file)
                print(path_file)
                try:
                    shutil.copy2(path_file,'./'+i) # change you destination dir
                except:
                    print("Same file"+path_file)
        try:
            shutil.copy2("concat.py","./"+i);
        except:
            print("Concat Already")
        try:
        
            shutil.copy2("test.cpp","./"+i+"/test.c");
            shutil.copy2("Compare.h","./"+i);
        except:
            print("Test Already")
        a=os.getcwd();
        os.chdir('./'+i);
        
        os.system("python "+"concat.py")
        #os.chdir(a);
        

        #os.chdir('./'+i);
        os.system("g++ test.c -std=c++11 -w")
        #os.system(".\\a.exe")
        p=multiprocessing.Process(target=Run)
        p.start()
        p.join(60)
        if p.is_alive():
            print("infinite loop")
            p.terminate();
        try:
            f=open("attempt.txt")
            marks=f.readline()
            f.close()
        except:
            marks="Attempt Not Generated,"
        try:
            f=open("marks.txt")
            marks+=f.readline();
            f.close();
        except:
            marks+='Compile Error'
        marksfile.write(i+","+marks+"\n")
        os.chdir(a)
def Run():
     print(os.getcwd())
     case=""
     while True:
        if(os.system(".\\a.exe"+case)==0):
            break;
        try:
            cse=open("marks.txt")
            case+=" "+str(int(cse.readline().split(",")[1])+1)
            print("omitting cases "+case)
        except:
            break

        


if __name__ == "__main__":
    main()