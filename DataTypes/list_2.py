nums = [1,2,3]

nums.append(4)
print(f"Append-{nums}")
nums.insert(1,100)
print(f"Insert-{nums}")
nums.remove(2)
print(f"Remove-{nums}")
nums.pop()
print(f"pop-{nums}")
nums.sort()
print(f"Sort-{nums}")
nums.reverse()
print(f"Reverse-{nums}")

print(max(nums))
print(min(nums))
print(sum(nums))