from member.model import MemberDAO

class MemberController:
    def __init__(self):
        self.dao = MemberDAO()


    def login(self, userid, password):
        pass
