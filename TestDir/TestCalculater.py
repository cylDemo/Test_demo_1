from SourceDir.Calculater import Cal
import pytest

def test_add():
    cal = Cal()
    assert 9 == cal.add(5, 4)

if __name__ == '__main__':
    pytest.main()
