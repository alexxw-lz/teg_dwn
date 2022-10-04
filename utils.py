import json
import os
from pyrogram import Client
import cfg

def dict2json(file_name,the_dict):
    '''
    将字典文件写如到json文件中
    :param file_name: 要写入的json文件名(需要有.json后缀),str类型
    :param the_dict: 要写入的数据，dict类型
    :return: 1代表写入成功,0代表写入失败
    '''
    try:
        json_str = json.dumps(the_dict,indent=4,ensure_ascii=False)
        #print(json_str)
        with open(file_name, 'w') as json_file:
            json_file.write(json_str)
        print('下载记录写入成功')
        return 1
    except:
        print('下载记录写入失败')
        return 0

def json2dict(file_name):
    with open(file_name,'r', encoding='UTF-8') as f:
     load_dict = json.load(f)
     # print('加载下载记录')
     return load_dict
# 创建下载记录文件
def create_his_file(file_path):
    with open(file_path,'w') as f:
        his_dict = '{"photo":[],"video":[],"document":[]}'
        f.write(his_dict)

def load_history(file_name):
    if os.path.exists(file_name):
        his_dict = json2dict(file_name)
    else:
        his_dict={"photo":[],"video":[],"document":[]}
    return his_dict

# def get_chat_history(file_name):
#     if json2dict(file_name)[chat_id]:
#         his_dict = json2dict(file_name)[chat_id]
#     else:
#         his_dict={"photo":[],"video":[],"document":[]}
#     return his_dict

def store_chat_history(file_name,chat_his_dict):
    dict2json(file_name,chat_his_dict)

def is_exists(his_file,file_name,file_type):
    his_dict = load_history(his_file)
    if file_name in his_dict[file_type]:
        print(file_name+':文件已下载')
        return True
    return False

# 需要先下载OneDriveUploader 和对应的配置文件
# wget https://raw.githubusercontent.com/MoeClub/OneList/master/OneDriveUploader/amd64/linux/OneDriveUploader
# wget https://raw.githubusercontent.com/donfo22/mdowm/main/auth2.json
def uploadfile(sour_path,tar_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print('Current_Dir:'+current_dir)
    if not os.path.exists(current_dir+'/OneDriveUploader'):
        os.system('wget https://raw.githubusercontent.com/MoeClub/OneList/master/OneDriveUploader/amd64/linux/OneDriveUploader -P '+current_dir)
        os.system('wget https://raw.githubusercontent.com/donfo22/mdowm/main/auth2.json -P '+current_dir)
        os.system('chmod +x '+current_dir+'/OneDriveUploader')
    if os.path.exists(sour_path):
        os.system(current_dir+"/OneDriveUploader -f -c auth2.json -skip -s "+ sour_path+ " -r "+tar_path)

def get_client():
    app = Client(
	session_name = 'user',
	api_id = cfg.API_ID,
	api_hash = cfg.API_HASH,
	phone_number = cfg.PHONE_NUMBER,
	# proxy = dict(hostname = cfg.HOST,port = cfg.PORT),
	# bot_token = cfg.BOT_TOKEN,
    )
    return app

# 获取频道群组（ID,Name）字典
def get_channel(app):
	channel_dict = {}
	#app.start()
	for dialog in app.iter_dialogs():
		#print((dialog.chat.first_name+' '+dialog.chat.last_name if dialog.chat.last_name else dialog.chat.first_name)or dialog.chat.title, dialog.chat.id)
		#print(dialog.chat.title,dialog.chat.id)
		channel_dict[dialog.chat.id] = dialog.chat.title
	return channel_dict

def get_channel_name(app,chat_id):
    channel_dict = get_channel(app)
    return channel_dict[chat_id]

if __name__ == "__main__":
    app = get_client()
    app.start()
    chat_id = -1001544078753
    channel_name = get_channel_name(app,chat_id)
    print(channel_name)

