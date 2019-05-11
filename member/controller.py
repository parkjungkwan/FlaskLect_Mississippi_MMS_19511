from member.model import MemberDAO

class MemberController:
    def __init__(self):
        self._dao = MemberDAO()
        # self._dao.create()
        # self._dao.insert_many()



    def login(self, userid, password):
        row = self._dao.login(userid, password)
        view = ''
        if row is None:
            view = 'index.html'
        else:
            view = 'home.html'

        return view
