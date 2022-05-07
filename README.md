# DB with update all feature

#Class: 
##EfficientDB
Constructor optionally accepts an initial value for all elements, even if the DB is empty.
e.g:
database = EfficientDB("initial str")

Properties:
last_update - returns the value of the last update_all method.

#Methods: 
set(key, value) \\O(1)
update_all(value) \\O(1)
timestamp(Optinal : key) \\O(1)
set_all(value) \\ the diamond of the DB, updates all keys to the given value in O(1)
value_of(key) \\ returns the value of the given key, unless set_all has been called before, done in O(1)
set_and_get_dict \\ return python dictionary with keys and their correct values according to update_all method. 

