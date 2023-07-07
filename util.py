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
    insert_str_content='''

corresponding_author:
    - ''
    - 'Corresponding author'
publication_short: In *IJCNN2023* (CCF-C)
abstract: ''
tags:
  - Other
links:
# - name: "arXiv"
#   url: 'https://arxiv.org/abs/2304.11547'
url_pdf: ''
url_code: ''
url_poster: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# image:
#   caption: 'The architecture of speech representation learning'
#   focal_point: ''
#   preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}



'''
    for root,dirs,names in os.walk(jzwang_dir):
        for file_name in names:
                    file_path=os.path.join(root,file_name)
                    if 'index.md' in file_path:
                        with open(file_path,'a') as f_p:
                             f_p.write(insert_str_content)

    return 0

if __name__ == '__main__':
    filter_dubplicate()
    