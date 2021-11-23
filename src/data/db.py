from tinydb import TinyDB, Query
import os.path as path
from datetime import datetime

class DB:

    def __init__(self, tables_dir):
        self.entry_db = TinyDB(path.join(tables_dir, "entries.json"))
        self.user_db = TinyDB(path.join(tables_dir, "users.json"))

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

    def add_visit_entry(self, uid):
        User = Query()
        res = self.user_db.search(User.uid == uid)

        if len(res) == 0:
            return
        
        user = res[0]
        self.add_visit_entry(user.uid, user.name, user.mail, user.status)
        

    def add_visit_entry(self, uid, name, mail, status):
        self.entry_db.insert({
            'timestamp': datetime.today(),
            'uid': uid,
            'name': name,
            'mail': mail,
            'status': status
        })

