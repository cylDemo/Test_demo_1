from SourceDir.Calculater import Cal
import pytest

def test_add():
    cal = Cal()
    assert 4 == cal.add(2, 2)

if __name__ == '__main__':
    pytest.main()
