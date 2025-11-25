# simple_calculator.py
import math

import sentry_sdk

sentry_sdk.init(
    dsn="https://e581abe209b42a851a9b765860f70648@sentry.hamravesh.com/9405",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)
# -------- عملیات اصلی --------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        err = ValueError("Cannot divide by zero")
        if sentry_sdk:
            sentry_sdk.capture_exception(err)
        return None     # IMPORTANT: DO NOT RAISE ERROR
    return a / b

def sine(x):
    return math.sin(x)

def tangent(x):
    try:
        return math.tan(x)
    except Exception as e:
        if sentry_sdk:
            sentry_sdk.capture_exception(e)
        raise

# -------- اجرای ساده --------
if __name__ == "__main__":
    print("Simple Python Calculator\n")

    print("2 + 3 =", add(2, 3))
    print("5 - 1 =", subtract(5, 1))
    print("4 * 6 =", multiply(4, 6))
    print("8 / 2 =", divide(8, 2))
    print("sin(1) =", sine(1))
    print("tan(1) =", tangent(1))

    print("\nAll operations executed successfully!")
