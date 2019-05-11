from member.model import MemberDAO

if __name__ == '__main__':
    dao = MemberDAO()
    dao.create()
    dao.insert_many()
    # print('로그인 정보 테스트')
    # print(dao.login('lee','1'))