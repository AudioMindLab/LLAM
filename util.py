import os
import shutil
def filter_dubplicate():
    jzwang_dir='content/publication/jzwang'
    exist_title=''
    for item in range(2007,2023):
        other_dir=os.path.join('content/publication/',str(item))
        if os.path.isdir(other_dir):
            for root,dirs,names in os.walk(other_dir):
                for file_name in names:
                    file_path=os.path.join(root,file_name)
                    if 'index.md' in file_path:
                        with open(file_path) as f_p:
                            all_lines=f_p.readlines()
                            for line in all_lines:
                                if 'title' in line:
                                    line=line.replace(':',"").replace('-',"")
                                    exist_title+=line.lower()
    count=0
    for root,dirs,names in os.walk(jzwang_dir):
        for file_name in names:
                    file_path=os.path.join(root,file_name)
                    if 'index.md' in file_path:
                        with open(file_path) as f_p:
                            all_lines=f_p.readlines()
                            for line in all_lines:
                                if 'title' in line:
                                     the_title=line.split('"')[1].lower().replace(':',"").replace('-',"")
                                     if the_title in exist_title:
                                            count+=1
                                            print("%02d   %s"%(count,the_title))
                                            print(root)
                                            shutil.rmtree(root)


    return 0

if __name__ == '__main__':
    filter_dubplicate()
    