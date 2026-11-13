import pytest
from app.classificacao import classificar_poder

def test_lendario():
    assert classificar_poder(680) == "lendário"

def test_lendario2():
    assert classificar_poder(600) == "lendário"

def test_forte():
    assert classificar_poder(500) == "forte"

def test_forte2():
    assert classificar_poder(590) == "forte"

def test_comum():
    assert classificar_poder(300) == "comum"

def test_comum2():
    assert classificar_poder(400) == "comum"

def test_negativo_levanta_erro():
    with pytest.raises(ValueError):
        classificar_poder(-1)