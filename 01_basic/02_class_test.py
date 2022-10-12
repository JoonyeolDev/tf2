from ast import Num


class Calculator: #값 + 함수
    sum = 100
    def __init__(self): # 인스턴스 변수 :self는 객채별로 따로 저장가능
        self.result = 0
        
    def add(self,num):
        self.result += num
        return self.result


cal1 = Calculator() # 주소 설정
cal2 = Calculator()
# cal1.result =2
# cal2.result =9


# print(cal1.result)
# print(cal2.result)
# print(Calculator.sum)
# Calculator.sum = 200 # 클래스 변수 : 클래스당 하나
# print(cal1.sum)
# print(cal2.sum)

cal1.add(3)
cal1.add(4)
print(cal1.result)
print(cal2.result)

class FourCal(Calculator):
    def sub(self,num):
        self.result -= num
        return self.result

cal3 = FourCal(5)
cal4 = FourCal(3)

cal3.add(5)
print(cal3.result)