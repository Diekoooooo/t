import paramiko
import datetime
import telegram
import os

# connect to the server
ssh = paramiko.sshclient()
ssh.set_missing_host_key_policy(paramiko.autoaddpolicy())
ssh.connect('143.42.31.79', username='root', password='9171679772Mm*')

# set the file path and name
file_path = '/etc/x-ui/x-ui.db'

# get current hour
now = datetime.datetime.now()
current_hour = now.hour

# set the allowed hours to send
allowed_hours = [9, 13, 17, 20]

# check if the current hour is in the allowed hours
if current_hour in allowed_hours:
    # open the file on the server
    with ssh.open_sftp() as sftp:
        # download file
        if os.path.exists(file_path):
            os.remove(file_path)
        sftp.get(file_path, file_path)
        
    # send the file to telegram
    bot = telegram.bot(token='6179165578:AAFf9N3i-nuXV65vnHJeY0NNeo2JfXHRTgs')
    chat_id = '922379605'
    with open(file_path, 'rb') as f:
        bot.send_document(chat_id=chat_id, document=f)
