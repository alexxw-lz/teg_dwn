import utils


def get_channel(app):
	channel_dict = {}
	app.start()
	for dialog in app.iter_dialogs():
		#print((dialog.chat.first_name+' '+dialog.chat.last_name if dialog.chat.last_name else dialog.chat.first_name)or dialog.chat.title, dialog.chat.id)
		#print(dialog.chat.title,dialog.chat.id)
		channel_dict[dialog.chat.id] = dialog.chat.title
	return channel_dict

if __name__=="__main__":
	app = utils.get_client()
	channel_dict = get_channel(app)
	print(channel_dict)