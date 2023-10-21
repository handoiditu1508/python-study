customer = {
    "name": "John Smith",
    "age": 30,
    "age": 40,
    "is_verified": True,
}

print(customer["age"])

print("-" * 10)
print("get not existed key")
print("-" * 10)

# print(customer["test"]) # will throw error since "test" not exist
print(customer.get("test"))
print(customer.get("test", "hello"))

print("-" * 10)
print("update value")
print("-" * 10)

customer["age"] = 50
customer["male"] = True
print(customer)
