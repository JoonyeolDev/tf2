
import re
import customer_func1 as cf
custlist = [{'name': 'i1', 'gender': 'M', 'email': 'raoneli1@naver.com', 'birthday': '1991'},
            {'name': 'i2', 'gender': 'M', 'email': 'raoneli2@naver.com', 'birthday': '1991'},
            {'name': 'i3', 'gender': 'M', 'email': 'raoneli3@naver.com', 'birthday': '1991'},
            {'name': 'i4', 'gender': 'M', 'email': 'raoneli4@naver.com', 'birthday': '1991'},]
page= len(custlist) - 1


while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()  

    if choice=="I":  
        page = cf.insertData(custlist)
    elif choice=="C": 
        cf.curData(custlist,page)
    elif choice == 'P':
        cf.preData(custlist,page)
    elif choice == 'N':
        cf.nextData(custlist,page)
    elif choice=='D':
        cf.delData()
    elif choice=="U": 
        cf.updateData()
    elif choice=="Q":
        break
    