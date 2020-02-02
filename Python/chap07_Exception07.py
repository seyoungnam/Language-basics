# unittest
import unittest

def custom_function():
    pass

# TestCase를 작성
class CustomTests(unittest.TestCase):
    def test_runs(self):
        """ 단순 실행 여부 판별하는 테스트 메소드"""
        custom_function() # 해당 메소드가 정의되지 않으면 unittest.main()을 통해 NameError 발생

# unittest를 실행
if __name__ == '__main__':
    unittest.main()