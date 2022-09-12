def increment(n):
    try:
        return int(n)+1
    except:
        raise ValueError("This is value error")
a=increment("yash")
print(a)