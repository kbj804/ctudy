import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
from sklearn.datasets import load_boston

boston = load_boston()
bostonDF = pd.DataFrame(boston.data, columns=boston.feature_names)
bostonDF['PRICE'] = boston.target
print(bostonDF.shape)
bostonDF.head(10)

# gradient_descent()함수에서 반복적으로 호출되면서 update될 weight/bias 값을 계산하는 함수. 
# rm은 RM(방 개수), lstat(하위계층 비율), target은 PRICE임. 전체 array가 다 입력됨. 
# 반환 값은 weight와 bias가 update되어야 할 값과 Mean Squared Error 값을 loss로 반환.
def get_update_weights_value(bias, w1, w2, rm, lstat, target, learning_rate=0.01):
    
    # 데이터 건수
    N = len(target)
    
    predicted = w1 * rm + w2 * lstat + bias
    diff = target - predicted
    bias_factor = np.ones((N,))
    
    # T는 ㅡ 를 ㅣ 로 바꾸는거
    w1_update = -(2/N)*learning_rate*(np.dot(rm.T, diff))
    w2_update = -(2/N)*learning_rate*(np.dot(lstat.T, diff))
    bias_update = -(2/N)*learning_rate*(np.dot(bias_factor.T, diff))
    
    # 제곱의 평균
    mse_loss = np.mean(np.square(diff))
    
    return bias_update, w1_update, w2_update, mse_loss

    # RM, LSTAT feature array와 PRICE target array를 입력 받아서 iter_epochs수만큼 반복적으로 Weight와 Bias를 update적용. 
def gradient_descent(features, target, iter_epochs=1000, verbose=True):
    # w1, w2는 numpy array 연산을 위해 1차원 array로 변환하되 초기 값은 0으로 설정
    # bias도 1차원 array로 변환하되 초기 값은 1로 설정. 
    w1 = np.zeros((1,))
    w2 = np.zeros((1,))
    bias = np.ones((1, ))
    print('최초 w1, w2, bias:', w1, w2, bias)
    
    # learning_rate와 RM, LSTAT 피처 지정. 호출 시 numpy array형태로 RM과 LSTAT으로 된 2차원 feature가 입력됨.
    learning_rate = 0.01
    rm = features[:, 0]
    lstat = features[:, 1]
    
    # iter_epochs 수만큼 반복하면서 weight와 bias update 수행. 
    for i in range(iter_epochs):
        # weight/bias update 값 계산 
        bias_update, w1_update, w2_update, loss = get_update_weights_value(bias, w1, w2, rm, lstat, target, learning_rate)
        # weight/bias의 update 적용. 
        w1 = w1 - w1_update
        w2 = w2 - w2_update
        bias = bias - bias_update
        if verbose:
            print('Epoch:', i+1,'/', iter_epochs)
            print('w1:', w1, 'w2:', w2, 'bias:', bias, 'loss:', loss)
        
    return w1, w2, bias


# 위에서 한거 밑에 이거 한번 사용하면 끝.. 그래서 라이브러리를 쓰는거다

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaled_features = scaler.fit_transform(bostonDF[['RM', 'LSTAT']])
print(scaled_features[:10])

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
# fit_transform: 원래 있던 값을 정규화 시켜주는 값
scaled_features = scaler.fit_transform(bostonDF[['RM', 'LSTAT']])

# .values: numpy(array)로 변경
w1, w2, bias = gradient_descent(scaled_features, bostonDF['PRICE'].values, iter_epochs=1000, verbose=True)
print('##### 최종 w1, w2, bias #######')
print(w1, w2, bias)


###### 최종 w1, w2, bias ####### 1000번 돌렸을때
# [18.54730416] [-13.01074165] [16.77763613]
# scaled_features(RM) ㅣ 506개 * 18.54730416  +  scaled_features(LTSTE) 506개 * -13.01074165 + 16.77763613
predicted = scaled_features[:, 0]*w1 + scaled_features[:, 1]*w2 + bias
predicted


# 실제값이랑 예측값 붙여서 비교해봄
predicted = scaled_features[:, 0]*w1 + scaled_features[:, 1]*w2 + bias
bostonDF['PREDICTED_PRICE'] = predicted
bostonDF.head(10)