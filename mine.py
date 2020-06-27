import queue
import random


class Board:
    way = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
           (1, -1), (0, 1), (1, 0), (1, 1))

    def __init__(self, boardsize, bombnum):
        # 보드의 크기
        self.boardsize = boardsize
        # 지뢰가 설정되어 있는 테이블
        self.board = [['E'] * boardsize for _ in range(boardsize)]
        # 게임을 할 테이블
        self.findedbrd = [['A'] * boardsize for _ in range(boardsize)]
        # 폭탄 리스트
        self.bombpos = []
        # 깃발 리스트
        self.flag = []
        for _ in range(bombnum):
            # 무작위로 폭탄을 뽑아서 설정한다.
            bomb = [random.choice(range(boardsize)) for i in range(2)]
            self.board[bomb[0]][bomb[1]] = 'M'
            self.bombpos.append(bomb)
        self.bombpos.sort()

    # 이벤트가 발생했을때 폭탄을 밟았는지 확인하는 매서드
    def firstsearch(self, y, x):
        if self.board[y][x] == 'M':
            for ypos, xpos in self.bombpos:
                self.findedbrd[ypos][xpos] = 'M'
            self.findedbrd[y][x] = 'X'
            return True
        else:
            return False

    # 밟은 부분을 기준으로 폭탄이 없는 자리를 재귀로 탐색한다.
    def search_board(self, y, x):
        answer = 0
        if self.findedbrd[y][x] != 'A':
            return
        for ymove, xmove in self.way:
            xpos = x + xmove
            ypos = y + ymove
            if xpos < 0 or xpos >= self.boardsize \
                    or ypos < 0 or ypos >= self.boardsize:
                continue
            if self.board[ypos][xpos] == 'M':
                # self.findedbrd[ypos][xpos] = 'M'
                answer += 1
        if answer > 0:
            self.findedbrd[y][x] = str(answer)
        else:
            self.findedbrd[y][x] = 'E'
            for ymove, xmove in self.way:
                xpos = x + xmove
                ypos = y + ymove
                if xpos < 0 or xpos >= self.boardsize  \
                        or ypos < 0 or ypos >= self.boardsize:
                    continue
                if self.board[ypos][xpos] != 'M':
                    self.search_board(ypos, xpos)

    # 깃발 이벤트가 발생했을때 깃발이 있는지 없는지 확인해서 옳은 장소로 보낸다.
    def check_flag(self, y, x):
        if self.findedbrd[y][x] == 'F':
            return self.remove_flag(y, x)
        else:
            if self.findedbrd[y][x] == 'A':
                return self.Add_flag(y, x)
            return False

    # 깃발을 추가하는 매서드
    def Add_flag(self, y, x):
        self.flag.append([y, x])
        self.findedbrd[y][x] = 'F'
        if len(self.flag) == len(self.bombpos):
            self.flag.sort()
            for i in range(len(self.flag)):
                if self.flag[i] == self.bombpos[i]:
                    continue
                else:
                    # 만약 깃발이 하나라도 틀린게 있다면 False반환
                    return False
            # 전부 맞다면 True 반환
            return True

    # 깃발을 제거하는 매서드
    def remove_flag(self, y, x):
        self.flag.remove([y, x])
        self.findedbrd[y][x] = 'A'
        if len(self.flag) == len(self.bombpos):
            self.flag.sort()
            for i in range(len(self.flag)):
                if self.flag[i] == self.bombpos[i]:
                    continue
                else:
                    # 만약 깃발이 하나라도 틀린게 있다면 False반환
                    return False
            # 전부 맞다면 True 반환
            return True


def solution(brd, y, x):
    if brd.firstsearch(y, x):
        return True
    else:
        brd.search_board(y, x)
        return False


if __name__ == "__main__":
    brd = Board(4, 1)
    while True:
        command = int(input().strip())
        y, x = map(int, input().strip().split())
        if command == 1:
            happy = solution(brd, y, x)
            for item in brd.findedbrd:
                print(item)
            if happy:
                break
        else:
            happy = brd.check_flag(y, x)
            for item in brd.findedbrd:
                print(item)
            if happy:
                break
