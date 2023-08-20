import random

############################### 환경 : 에이전트의 액션을 받아 상태변이를 일으키고, 보상을 줌
class GridWorld():
    def __init__(self):
        self.x=0
        self.y=0
    

    # 액션 받아 상태변이 일으키고, 보상 반환하는 함수
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

    # 에피소드가 끝났는지 판별해주는 함수
    def is_done(self):
        if self.x == 3 and self.y == 3:
            return True
        else :
            return False

    def get_state(self):
        return (self.x, self.y)

    # 에이전트가 종료 상태에 도달하면 다시 처음 상태로 초기화하는 함수
    def reset(self):
        self.x = 0
        self.y = 0
        return (self.x, self.y)







############################### 에이전트 : 4방향 랜덤 정책을 따라 움직임
class Agent():
    def __init__(self):
        pass        

    def select_action(self):    # 모든 액션이 각 1/4 확률
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
    env = GridWorld()
    agent = Agent()
    # 각 상태 밸류 0으로 초기화
    data = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    gamma = 1.0
    reward = -1
    alpha = 0.001

    for k in range(50000):  # 50000번의 에피소드
        done = False
        history = []

        ######### 에이전트가 경험 쌓는 부분(에피소드 생성) : 에이전트가 환경과 상호작용하며 데이터를 축적
        while not done:
            action = agent.select_action()
            (x,y), reward, done = env.step(action)
            history.append((x,y,reward))
        env.reset()
        ######### 에피소드 끝난 후 학습하는 부분 : 쌓인 경험을 통해 테이블을 업데이트
        cum_reward = 0   # 리턴
        for transition in history[::-1]:
            x, y, reward = transition
            data[x][y] = data[x][y] + alpha*(cum_reward-data[x][y])
            cum_reward = reward + gamma*cum_reward 
            
    for row in data:
        print(row)

if __name__ == '__main__':
    main()
