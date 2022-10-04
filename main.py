import os
from datetime import datetime as dt
import cfg
import utils

# chat_id 频道或者群组ID,可通过get_chat_id 来获取
# his_file_path 下载历史记录文件地址


def download(app,chat_id):
	# 启动应用
	app.start()
	# 下载文件目录
	PATH = os.path.dirname(os.path.abspath(__file__))+'/downloads/'
	#加载历史记录
	his_file_path = os.path.dirname(os.path.abspath(__file__))+'/logs/'+str(chat_id)+'_history.json'
	print(his_file_path)
	if not os.path.exists(his_file_path):
		print('创建历史记录')
		utils.create_his_file(his_file_path)
	his_dict = utils.load_history(his_file_path)

	# 文件集合
	chat_his = app.iter_history(chat_id)
	print('获取文件集合')
	print(chat_his)
	# 计数器
	msg_id = 1
	for msg in chat_his:
		try:
			if msg.photo and cfg.opts[1]=='photo':
				date = dt.utcfromtimestamp(msg.photo.date)
				file = 'photo_'+str(date)[:10]+'_'+msg.photo.file_unique_id+'.jpg'
				file_type = 'photo'
			elif msg.video and cfg.opts[2]=='video':
				date = dt.utcfromtimestamp(msg.video.date)
				file = 'video_'+str(date)[:10]+'_'+msg.video.file_unique_id+msg.video.file_name
				file_type = 'video'
			elif msg.document and cfg.opts[3]=='document':
				date = dt.utcfromtimestamp(msg.document.date)
				file = 'file_'+str(date)[:10]+'_'+msg.document.file_unique_id+msg.document.file_name
				file_type = 'document'

			print(file_type+':'+file)

			if not os.path.exists(PATH+file) and not utils.is_exists(his_file_path,file,file_type):
				print(app.download_media(msg,file_name=file))
				#下载记录写入
				his_dict[file_type].append(file)
				print(msg_id)
				msg_id = msg_id+1


			if msg_id > 10 :
				print("已经下载了10个文件,暂停下载")
				#将下载历史记录写入history.json
				utils.store_chat_history(his_file_path,his_dict)
				sour_path = PATH
				channel_name = utils.get_channel_name(app,chat_id)
				tar_path = '/tg/'+channel_name
				utils.uploadfile(sour_path,tar_path)
				print('文件上传成功')
				# 删除已上传的文件
				os.system('rm -f '+PATH+'*')
				print('删除已下载文件成功')
				#重置计数器
				msg_id = 1
				#return
		except Exception as err:
			print(err)
			# continue
	# 上传最后下载的文件
	utils.store_chat_history(his_file_path,his_dict)
	sour_path = PATH
	channel_name = utils.get_channel_name(app,chat_id)
	tar_path = '/tg/'+channel_name
	utils.uploadfile(sour_path,tar_path)
	print('文件上传成功')
	# 删除已上传的文件
	os.system('rm -f '+PATH+'*')
	print('删除已下载文件成功')
if __name__=="__main__":
	chat_id = -1001346475648
	app = utils.get_client()
	download(app,chat_id)