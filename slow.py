import time


def slow():
    time.sleep(2)


def ans():
    slow()
    return {"a": "10"}
