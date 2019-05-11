from member.model import MemberDAO

if __name__ == '__main__':
    dao = MemberDAO()
    dao.create()
    dao.insert_many()