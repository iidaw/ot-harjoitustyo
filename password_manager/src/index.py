from tkinter import Tk
from repositories.info_repo import InfoRepo
from repositories.user_repo import UserRepo
from service.service import Service
from ui.ui import UI


def main():
    window = Tk()
    window.title("Password manager")

    user_repo = UserRepo()
    info_repo = InfoRepo()
    service = Service(user_repo)

    ui_view = UI(window, user_repo, service, info_repo)
    ui_view.start()

    window.mainloop()


if __name__ == '__main__':
    main()
