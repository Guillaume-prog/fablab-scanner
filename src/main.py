from ui import Site
from data import DB
from io import Screen, RFID


def main():
    running = True

    site = Site()
    db = DB('./assets/tables/')
    screen = Screen()
    reader = RFID()

    site.launch()
    while running:
        uid = reader.wait_for_card()

        if not db.user_registered(uid):
            screen.display_code(uid)

            payload = site.wait_for_register()

            if not payload == None:
                wants_to_register, name, mail, status = payload

                if(wants_to_register):
                    db.register_user(uid, name, mail, status)
                
                db.add_visit_entry(uid, name, mail, status)
        else:
            db.add_user_entry(uid)
            screen.display_message("Bienvenue !", 5)


if __name__ == "__main__":
    main()