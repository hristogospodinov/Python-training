def myfunc(word):    
    result = ''
    for each,case in enumerate(word):
        if each % 2 == 0:
            result += case.upper()
        else:
            result += case.lower()
    return result