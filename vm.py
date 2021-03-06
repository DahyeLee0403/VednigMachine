#프로덕션 코드
change = 0

class VendingMachine:
    #class의 인스턴스가 무조건 이 과정을 밟게  끔초기화 시켜준다
    def __init__(self):
        self._change = 0

    def run(self, raw):
        tokens = raw.split(" ")
        cmd, params = tokens[0], tokens[1:]

        if cmd == "잔액" :
            return "잔액은 " + str(self._change) + "원입니다"
        elif cmd == "동전":
            coin = params[0]
            self._change += int(coin)
            return coin + "원을 넣었습니다"
        else:
            return "알 수 없는 명령입니다"


#
# def init():
#     global change
#     change = 0
#
# def run(raw):
#     global change
#
#     tokens = raw.split(" ")
#     cmd, params = tokens[0], tokens[1:]
#
#     if cmd == "잔액" :
#         return "잔액은 " + str(change) + "원입니다"
#     elif cmd == "동전":
#         coin = params[0]
#         change += int(coin)
#         return coin + "원을 넣었습니다"
#     else:
#         return "알 수 없는 명령입니다"
