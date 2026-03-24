# 1. 讓使用者輸入
a = int(input("請輸入第一個整數: "))
b = int(input("請輸入第二個整數: "))

# 2. 找出範圍並判斷 17 的倍數
start, end = min(a, b), max(a, b)
multiples = [i for i in range(start, end + 1) if i % 17 == 0]

# 3. 印出結果
print(f"範圍內 17 的倍數有: {multiples}")
print(f"總和 (Sum) = {sum(multiples)}")
