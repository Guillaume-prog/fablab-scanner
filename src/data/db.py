from tinydb import TinyDB, Query
import os.path as path
import time

class DB:

    def __init__(self, tables_dir):
        self.db = TinyDB(path.join(tables_dir, "data.json"))
        self.entry_db = self.db.table("entries")
        self.user_db = self.db.table("users")

    def user_registered(self, uid):
        User = Query()
        res = self.user_db.search(User.uid == uid)
        return len(res) > 0

    def register_user(self, uid, name, mail, status):
        self.user_db.insert({
            'uid': uid,
            'name': name,
            'mail': mail,
            'status': status
        })

    def add_user_entry(self, uid):
        User = Query()
        res = self.user_db.search(User.uid == uid)

        print(res)

        if len(res) == 0:
            return
        
        user = res[0]
        self.add_visit_entry(uid, user['name'], user['mail'], user['status'])
        

    def add_visit_entry(self, uid, name, mail, status):
        self.entry_db.insert({
            'timestamp': time.time(),
            'uid': uid,
            'name': name,
            'mail': mail,
            'status': status
        })

