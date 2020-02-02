# https://wikidocs.net/16107
import unittest
import os

def custom_function(file_name):
    with open(file_name, 'rt') as f:
        return sum(1 for _ in f) # 파일 내 몇줄인지 카운팅, '_'은 특정값을 skip할 때 쓰임

# TestCase를 작성
class CustomTests(unittest.TestCase):
    def setUp(self):
        """테스트 시작되기 전 파일 작성"""
        self.file_name = 'test_file.txt'
        with open(self.file_name, 'wt') as f:
            f.write("""
            파이썬에선 정말 단위테스트 모듈이 기본적으로 포함되어 있나요? 진짜?
            멋지군요!
            단위테스트를 잘 수행해보고 싶습니다!
            """.strip())

    def tearDown(self):
        """테스트 종료 후 파일 삭제"""
        try:
            os.remove(self.file_name)
        except:
            pass

    def test_runs(self):
        """단순 실행여부 판별하는 테스트 메소드"""

        custom_function(self.file_name)

    def test_line_count(self):
        self.assertEqual(custom_function(self.file_name), 3) # self.assertEqual(a,b) => a와 b가 같은지 확인 후 메세지 리턴

    def test_no_file(self):
        with self.assertRaises(IOError):
            custom_function('abc.txt')

# unittest를 실행
if __name__ == '__main__':
    unittest.main() # test_로 시작하는 2개의 테스트가 실행되어 성공되었음이 표시.