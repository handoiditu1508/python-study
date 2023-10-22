customer = {
    "name": "John Smith",
    "age": 30,
    "age": 40,
    "is_verified": True,
}

print(customer["age"])

print("-" * 10, "get not existed key", "-" * 10)

# print(customer["test"]) # will throw error since "test" not exist
print(customer.get("test"))
print(customer.get("test", "hello"))

print("-" * 10, "update value", "-" * 10)

customer["age"] = 50
customer["male"] = True
print(customer)
