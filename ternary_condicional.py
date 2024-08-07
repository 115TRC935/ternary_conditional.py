
#   _______  _______  ____
#  |__   __||  __ \ / ____|
#     | |   | |__) | |     
#     | |   |  _  /| |     
#     | |   | | \ \| |____ 
#     |_|   |_|  \_\\_____| 
#This library is a simple condition, with a short sintax than common ternary operators.
#You can use it with any variable, because is a lambda function.

hi = lambda var, comparator, true, false: true if var >= comparator else false 
lo = lambda var, comparator, true, false: true if var <= comparator else false
eq = lambda var, comparator, true, false: true if var == comparator else false
