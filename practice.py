# def sum_mix(arr):
#     #your code here
#     new_arr = []
#     sum = 0 
#     for i in range(len(arr)):
#         if arr[i] == str(arr[i]):
#             arr[i] = int(arr[i])
#             new_arr.append(arr[i])
#         else :
#             new_arr.append(arr[i])
            
#     for i in range(0, len(new_arr),1):
#           sum = sum + arr[i]
        
#     return sum
# 
# should equal 15
# print(sum_mix([1,"2",3,4,"5"]))



# def solution(string):
#     new_str = ""
#     for i in range(len(string)-1,-1,-1):
#         new_str += string[i]
        
#     return new_str

# print(solution("hello"))


a = [7,9,5,8,4,3]

x = sorted(a,reverse=True)

print(x)
