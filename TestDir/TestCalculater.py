from SourceDir.Calculater import Cal
import pytest

def test_add():
    cal = Cal()
    assert 8 == cal.add(4, 4)

if __name__ == '__main__':
    pytest.main()
