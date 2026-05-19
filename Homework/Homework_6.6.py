from faker import Faker

fake = Faker()

print("Случайное имя:", fake.name())
print("Случайный адрес:", fake.address())

print("\n--- Two Sum ---")

nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print("Ответ:", [i, j])