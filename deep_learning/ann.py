# artificial neural network, ANN
import torch
x = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])

print(x) # tensor([[1,2,3],[4,5,6],[7,8,9]])
print(x.size()) # torch.Size([3,3])
print(x.shape) # torch.Size([3,3])
print(x.ndimension()) # 2


# 랭크 늘리기
x = torch.unsqueeze(x, 0)

print(x) # tensor([[[1,2,3],
         #          [4,5,6],
         #          [7,8,9]]])
print(x.size()) # torch.Size([1, 3, 3])
print(x.ndimension()) # 3

# 랭크 줄이기
x = torch.squeeze(x)

# view() - 쉽게 원소 생성가능하나
x = x.view(9)
print(x) # tensor([1,2,3,4,5,6,7,8,9])
print(x.size()) # torch.Size([9])

# 텐서의 원소 개수를 변경할 수는 없음
try:
    x = x.view(2,4)
except Exception as e:
    print(e) # shape '[2, 4]' is invalid for input of size 9

# 행렬 곱 torch.mm
w = torch.randn(5,3, dtype=torch.float)
x = torch.tensor([[1.0, 2.0], [3.0,4.0], [5.0,6.0]])
print(w.size()) # torch.Size([5, 3])
print(x.size()) # torch.Size([3, 2])
print(w)
print(x)

b = torch.randn(5,2, dtype=torch.float)
print(b.size())
print(b)

wx = torch.mm(w,x) 
print(wx.size()) # torch.Size([5, 2])

result = wx + b
print(result.size()) # torch.Size([5, 2])
print(result)