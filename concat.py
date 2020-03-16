import os
def main():
    ls=(os.listdir())
    head=""
    errors=""
    functions=[]
    prototypes=[]
    config_file=open("config.txt")
    lines=config_file.readlines()
    for l in lines:
        print(l);
        functions.append(l.split(":")[0])
        prototypes.append(l.split(":")[1])
    found=False;
    bracket=False;
    count=0
    for f in ls:
        head+='\n';
        if(f.find(".cpp")!=-1 and f.find("test")==-1) and os.system("g++ -c "+f)!=0 :
                found=True;
                print(f+" has compilation errors")
                errors+=f+" has compilation errors "
                continue;
        if(f.find(".cpp")!=-1 and f.find("test")==-1):
            
            found=True;
            print("Reading "+f+".........")
            f1=open(f,'r');
            lines=f1.readlines()
            #print(lines)
            
            for l in range(len(lines)):
                line=lines[l]
                if(line.find("main")==-1):
                    head+=line;
                else:
                    line=line.replace("main","main"+str(count));
                    head+=line
                    count+=1
                    
                
                    

            f1.close();
    if found==True:
        f=open("master.h",'w+')
        #checking for functions.....
        #print(head)
        #h=head.split('\n');
        marks=5*len(functions);
        for i in range(len(functions)):
            f1=functions[i]
            if(head.find(f1)==-1):
                print("Missing function:"+f1);
                head+=prototypes[i]+'\n';
                marks-=5;

            

        m=open('attempt.txt','w+')
        m.write(errors+',')

        f.write(head)

                
            
main()