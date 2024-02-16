def memoizer(func):
    dict = {}
    
    def wrapper(*args):
        key = (args)
        if key in dict:
            print("запам'ятований результата:", key)
            return dict[key]
    
        result = func(*args)
        dict[key] = result
        return result
    return wrapper