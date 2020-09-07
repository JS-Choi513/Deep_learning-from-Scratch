import numpy as np
import matplotlib.pyplot as plt
# 교차 엔트로피 오차도 마찬가지로 추정치와 정답을 통해 
# 신경망의 성능을 나타내는 지표이다.
# 교차 엔트로피 오차는 주로 분류문제에서 많이 사용되는데 
# 예측값이 참과 거짓 둘중 하나로 결정될(이산적) 때 주로 쓴다 
# 밑이 자연상수 e인 로그를 사용하여 계산한다, 이는 자연로그에 쓰이는 상수e 가 가장 많은 값을 표현해주기 때문

x = np.arange(0, 1, 0.01)
y = np.log(x)
 
plt.plot(x, y)
plt.show()

def CEE(y, t):
    delta = 1e-10 # 값이 0이 되는것을 방지하기 위해 매우 작은 값을 더한다. 
    return -np.sum(t*np.log(y+delta))
t = np.array([0, 0, 0, 0.5, 0.5, 0, 0, 0, 0, 0])
y0 = [0, 0, 0, 0.5, 0.5, 0, 0, 0, 0, 0]
y1 = [0.01, 0.01, 0.1, 0.3, 0.33, 0.04, 0.02, 0.05, 0.01, 0.1]
y2 = np.array([0.3, 0.01, 0.1, 0.01, 0.04, 0.02, 0.05, 0.33, 0.01, 0.1])
print(CEE(t,y0)) # 0.6931471803599453
print(CEE(t,y1)) # 8.265472039806522
print(CEE(t,y2)) # 21.21844021456322