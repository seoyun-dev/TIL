import random

############################### 환경 : 에이전트의 액션을 받아 상태변이를 일으키고, 보상을 줌
class GridWorld():
    def __init__(self):
        self.x=0
        self.y=0
    
    def step(self, a):
        # 0번 액션: 왼쪽, 1번 액션: 위, 2번 액션: 오른쪽, 3번 액션: 아래쪽
        if a==0:
            self.move_left()
        elif a==1:
            self.move_up()
        elif a==2:
            self.move_right()
        elif a==3:
            self.move_down()

        reward = -1 # 보상은 항상 -1로 고정
        done = self.is_done()
        return (self.x, self.y), reward, done

    def move_right(self):
        self.y += 1  
        if self.y > 3:
            self.y = 3
    
    def move_left(self):
        self.y -= 1
        if self.y < 0:
            self.y = 0
    
    def move_up(self):
        self.x -= 1
        if self.x < 0:
            self.x = 0

    def move_down(self):
        self.x += 1
        if self.x > 3:
            self.x = 3

    def is_done(self):
        if self.x == 3 and self.y == 3:
            return True
        else :
            return False

    def get_state(self):
        return (self.x, self.y)
    
    def reset(self):
        self.x = 0
        self.y = 0
        return (self.x, self.y)




############################### 에이전트 : 4방향 랜덤 정책을 따라 움직임
class Agent():
    def __init__(self):
        pass        

    def select_action(self):
        coin = random.random()
        if coin < 0.25:
            action = 0
        elif coin < 0.5:
            action = 1
        elif coin < 0.75:
            action = 2
        else:
            action = 3
        return action





############################### 학습을 하는 메인 함수
def main():
    #TD
    env = GridWorld()
    agent = Agent()
    # 각 상태 밸류 0으로 초기화
    data = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    gamma = 1.0
    reward = -1
    # MC보다 큰 알파 값 이유 : TD가 MC보다 학습의 변동성이 작기 때문
    alpha = 0.01

    for k in range(50000):   # 50000번의 에피소드
        done = False
        ########## 경험 쌓는 부분(에피소드 생성) : 에이전트가 환경과 상호작용하며 데이터 축적
        while not done:
            x, y = env.get_state()
            action = agent.select_action()
            (x_prime, y_prime), reward, done = env.step(action)
            ####### 에피소드 내부에서 학습하는 부분 : 상태전이 일어나자마자 테이블 값 업데이트
            data[x][y] = data[x][y] + alpha*(reward+gamma*data[x_prime][y_prime]-data[x][y])
        env.reset()
            
    for row in data:
        print(row)

if __name__ == '__main__':
    main()