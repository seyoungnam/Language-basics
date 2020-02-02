# Assert
def check_assert():
    a = 3
    b = 2
    assert a < b, "False: 'a'가 'b'보다 크다."
    print("a=" + str(a) + " b=" + str(b))

try:
    check_assert()
except Exception as e:
    print("Exception: check_asset", e)