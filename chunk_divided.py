#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import ijson
import json
import jsonlines
import os
from tqdm import tqdm


# In[3]:


json_data_dir = '/Users/一亩三分地/IT/corpus/webtext2019zh/'


# In[4]:


json_file_name = 'web_text_zh_train.json'


# In[16]:


full_file_name = json_data_dir + json_file_name


# In[69]:


def create_dir(folder_dir,folder_nam):
    full_folder_dir = folder_dir + '/' +folder_nam
    if not os.path.exists(full_folder_dir):
        os.makedirs(full_folder_dir)
        print('create folder %s done!' % full_folder_dir)
        return full_folder_dir + '/'
    else:
        print('folder %s existed!' % full_folder_dir)
        return full_folder_dir + '/'


# In[71]:


def json_file_divided(source_dir,source_file,target_dir,target_folder):
    
    source_file_with_dir = source_dir + '/' + source_file
    full_target_folfer_dir = create_dir(target_dir,target_folder)
    
    with open(source_file_with_dir) as reader:
        
        lines_count = 0
        file_count = 0
        json_list = []
        
        for line in tqdm(reader):

#             json_obj = json.loads(line)
#             print(json_obj)
            json_list.append(line)
            lines_count = lines_count + 1
            
            if lines_count % 6000 == 0:
                
                file_count = file_count + 1
                temp_file_name = 'divided_' + str(file_count) + '.json'
                temp_full_name = full_target_folfer_dir + temp_file_name
                
                with open(temp_full_name, 'w',encoding='utf8') as json_file:
                    json_file.write(''.join(json_list))
                    json_list.clear()
                
#                 break
        if json_list :
            
            file_count = file_count + 1
            temp_file_name = 'divided_' + str(file_count) + '.json'
            temp_full_name = full_target_folfer_dir + temp_file_name

            with open(temp_full_name, 'w',encoding='utf8') as json_file:
                json_file.write(''.join(json_list))
        
        print('totole lines : %s' % lines_count)

                
json_file_divided('/Users/一亩三分地/IT/corpus/webtext2019zh'
                  ,'web_text_zh_valid.json'
                  ,'/Users/一亩三分地/IT/corpus/webtext2019zh'
                  ,'divided_file')


# In[73]:


def json_file_divided_and_add_lines(source_dir,source_file,target_dir,target_folder):
    
    source_file_with_dir = source_dir + '/' + source_file
    full_target_folfer_dir = create_dir(target_dir,target_folder)
    
    with open(source_file_with_dir) as reader:
        
        lines_count = 0
        file_count = 0
        json_list = []
        
        for line in tqdm(reader):

#             json_obj = json.loads(line)
#             print(json_obj)
            json_list.append(line)
            lines_count = lines_count + 1
            
            if lines_count % 6000 == 0:
                
                file_count = file_count + 1
                temp_file_name = 'divided_' + str(file_count) + '.json'
                temp_full_name = full_target_folfer_dir + temp_file_name
                
                with open(temp_full_name, 'w',encoding='utf8') as json_file:
                    json_file.write('{"index":{}}\n' + '{"index":{}}\n'.join(json_list))
                    json_list.clear()
                
#                 break
        if json_list :
            
            file_count = file_count + 1
            temp_file_name = 'divided_' + str(file_count) + '.json'
            temp_full_name = full_target_folfer_dir + temp_file_name

            with open(temp_full_name, 'w',encoding='utf8') as json_file:
                json_file.write('{"index":{}}\n' + '{"index":{}}\n'.join(json_list))
        
        print('totole lines : %s' % lines_count)

                
json_file_divided_and_add_lines('/Users/一亩三分地/IT/corpus/webtext2019zh'
                                ,'web_text_zh_valid.json'
                                ,'/Users/一亩三分地/IT/corpus/webtext2019zh'
                                ,'divided_builk_file')


# In[ ]:


get_ipython().system(' curl -XPOST localhost:9200/index_bulk/_doc/_bulk --data-binary  @/Users/一亩三分地/IT/corpus/webtext2019zh//bulk_data.json; echo')
    
    


# In[ ]:


curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/_bulk --data-binary "@requests"; echo


# In[ ]:


curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/index_bulk/_doc/_bulk --data-binary "@/Users/一亩三分地/IT/corpus/webtext2019zh//bulk_data.json"; echo


# In[ ]:



curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/index_bulk2/_doc_bulk --data-binary "@/Users/一亩三分地/IT/corpus/webtext2019zh//bulk_data.json"; echo
      


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




