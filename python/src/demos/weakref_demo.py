import weakref
import gc


class MyClass:
    pass


obj = MyClass()
r = weakref.ref(obj)

print(r)
del obj
print(r)


class ExpensiveObject:
    def __init__(self, name):
        self.name = name
        

_cache = weakref.WeakValueDictionary()


def get_object(name):
    if name in _cache:
        return _cache[name]
    else:
        obj = ExpensiveObject(name)
        _cache[name] = obj
        return obj


obj = get_object("BigData")
print(obj.name)

del obj
gc.collect()

print(_cache.get("BigData"))
