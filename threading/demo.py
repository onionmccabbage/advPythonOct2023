import sys

# tuples
t = (1,2,3)
t = (1) # not a tuple
t = (1,) # a one-member tuple
print(type(t))

# we can introspect the system and infer capabilities
print(sys.maxsize ) # the largest size object that python can exist in memory
print(sys.version_info)
print(sys.platform)
print(sys.base_prefix) # the location of python on this o/s