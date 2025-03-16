import logging

def add(a,b):
    try:
        result = a + b
    except TypeError as e:
        logging.warning(f"Du bist ein lappen. Gib was gscheids ein!")
    else:
        logging.info("Wir haben a und b addiert")
        return result
def sub(a,b):
    try:
        result = a - b
    except TypeError as e:
        logging.warning(f"Du sollst immer Zahlen eingeben du lappen")
    else:
        logging.info(f"b wurde von a subtrahiert!")
        return result