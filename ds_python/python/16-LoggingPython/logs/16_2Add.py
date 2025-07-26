from logger import logging

def Add(a,b):
    logging.debug("now adding two number")
    return a+b

c=Add(4,5)
logging.info("this info for printing")
print(c)