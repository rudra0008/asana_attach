#!/usr/bin/python -tt
#Command:   python attach_file.py
#Description: The script is used to attach leave and attendence data to respective users asana task
#Author:    Rudra Narayan Singh <rudran@one.com>
#Project:   one.com-internalit-tools
#Dependencies:

#!/usr/bin/python -tt
import os
import requests
import shutil
import json

class Asana_attach:

        def __init__(self,auth_key,task_id_location,attachment_location,uploaded_dir):
                self.auth_key = auth_key
                self.task_id_location = task_id_location
                self.attachment_location = attachment_location
                self.uploaded_dir = uploaded_dir

        def find_attachment_dir(self):
                if os.path.exists(self.attachment_location) and os.path.isdir(self.attachment_location):
                        if not os.listdir(self.attachment_location):
                                print("Directory is empty")
                                exit(1)
                        else:
                                print("Found files to attach")
                else:
                        print("Given Directory dosn't exists")
                        exit(0)


        def user_task_id(self):
            userlist = {}
            with open(self.task_id_location) as user_file:
                data=json.load(user_file)
                for key, value in data.items():
                    userlist[key] = int(value)
                return userlist

        def fetch_username_from_file():
                
if __name__ =="__main__":
        auth_key = '0/cd7654a9c9124d76c56c24059845b2b9'
        task_id_location = r'/home/rudran/script/user_task_id.json'
        attachment_location = r'/home/rudran/script/arlr_files'
        uploaded_dir = r'/home/rudran/script/uploaded'
        attach_files = Asana_attach(auth_key,task_id_location,attachment_location,uploaded_dir)
        attach_files.find_attachment_dir()
        user_task = attach_files.user_task_id()
        print "done"

