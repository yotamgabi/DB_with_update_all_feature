# DB with update all feature

## Class: EfficientDB
#####   Constructor optionally accepts an initial value for all elements, even if the DB is empty.
#####   e.g:
```Python
database = EfficientDB( Optinal : initial_value )
```
### Properties:
```Python
last_update #retrns the value of the last set_all method, regardles if some keys had another update afterwards
```
### Methods: 
``` Python
set(key, value)   # O(1)
timestamp(Optinal : key) # O(1)
set_all(value) # the diamond of the DB, updates all keys to the given value in O(1)
value_of(key) # returns the value of the given key,
              # if set_all has been called after the value was declared, returns last_update. done in O(1)
set_and_get_dict() # return python dictionary with keys and their correct values according to update_all method, θ(n) 
isEmpty() 
```
