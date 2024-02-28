#length 1  2  3  4  5  6  7  8  9  10
#price  1  5  8  9  10 17 17 20 24 30
#let n =4
#f(4,0) = 9+0 = 9
#f(1.3) = 1+8 = 9
#f(2,2) = 5+5 = 10 ->we want to return this
#f(3,1) = 8+1 = 9
#f(1,1,2) = 1+1+5 = 7
#f(2,1,1) = 5+1+1 = 7
#f(1,2,1) = 1+5+1 = 7
#f(1,1,1,1) = 1+1+1+1 = 4
#f(n) = min(f(n-1)+p(n),f(n-2)+p(n) . . .

#if n<=10: f(n) := max_i{price[n], f(n-1)+price[i]} //because we dont have len 0
#else: f(n) := max_i{f(n-i)+price[i]}

price_list = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
dp = [None] * (len(price_list)+1) #dynamic program array. 
#It stores results of subproblems to avoid recomputation

def f(n):
    global dp, price_list #calling global variables
    if n == 1: #if theres only one cut
        return n
    if dp[n] is not None: #if we already calculated this subproblem, return the result
        return dp[n] 
    max_price = price_list[n] #max price is the price of the last cut
    for i in range(1, n):
        sub_result = f(n - i) 
        if max_price < price_list[i] + sub_result: #if the price of the last cut is less than the price of the current cut + the price of the next cut, then
            max_price = price_list[i] + sub_result #update the max price
    dp[n] = max_price #store the result in the dynamic program array
    return dp[n] #return the result

for i in range(1, len(price_list)):
    result = f(i)
    print('Rope Length: {i} = {result}'.format(i=i, result=result))