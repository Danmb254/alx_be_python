#scope

x = "global_scope"

def test():
    y = "local_scope"
    print(y)
    
test()
print(y)