lst = []

n = int(input("enter the number the elements : "))

for i in range(n):
   ele = int(input())

   lst.append(ele)

print("unsorted list", lst)


for i in range(len(lst)):
   min_ind = i

   for j in range(i+1, n-i-1):
      if lst[j]>lst[j+1]:
         lst[j], lst[j+1] = lst[j+1], lst[j]
      else:
         pass

print("sorted list: ", lst)
