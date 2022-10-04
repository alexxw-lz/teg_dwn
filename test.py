import os
import utils
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))

# his_dict = utils.load_history('/workspaces/113810007/tg_dwn_file/asd.json')

# for k,v in iter(his_dict):
#     print(k,v)

#his_dict = {"photo":[],"video":[],"document":[]}
# his_dict=utils.load_history('history.json')

# his_dict["photo"].append('55.jpg')
# his_dict["video"].append('55.mp4')

#print(his_dict["video"])

#new_dict = his_dict
#print(new_dict["video"])

# utils.store_history('history.json',his_dict)

# if utils.is_exists('4444.mp4','video'):
#     print('Yes')
# else:
#     print('No')

sour_path = '/workspaces/113810007/tg_dwn_file/downloads'
tar_path = '/cs50/test'
utils.uploadfile(sour_path,tar_path)
