cases=32
main="int main(){"
for i in  range(cases):
    main+='\nif(omit['+str(i)+']==0){'
    main+="\n\tcout<<\"Running Case"+str(i)+"\"<<endl;"
    main+="\n\tCase"+str(i)+"();"
    main+='\n\tfout.open("marks.txt",ios::out | ios::trunc);fout<<marks<<","<<'+str(i)+';fout.close();'
    main+="}"
    main+='else\n\tfout.open("marks.txt",ios::out | ios::trunc);fout<<marks<<","<<'+str(i)+';fout.close();'
main+="}"
f=open("main.cpp",'w+')
f.write(main)