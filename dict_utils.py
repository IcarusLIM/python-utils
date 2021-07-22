def get_recursion(o, paths):
    tmp = o
    try:
        for p in paths:
            if p in tmp:
                tmp = tmp[p]
        return tmp
    except:
        pass
    return None
