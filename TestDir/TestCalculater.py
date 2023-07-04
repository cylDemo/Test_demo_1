from SourceDir.Calculater import Cal
import pytest

def test_add():
    cal = Cal()
    assert 6 == cal.add(2, 4)

if __name__ == '__main__':
    pytest.main()
