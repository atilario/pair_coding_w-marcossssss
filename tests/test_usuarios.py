from usuarios import validar_email


def test_valido():
    assert validar_email("ana@empresa.com") is True


def test_valido_com_subdominio():
    assert validar_email("ana@empresa.com.br") is True


def test_sem_arroba():
    assert validar_email("ana.exemplo.com") is False


def test_multiplos_arrobas():
    assert validar_email("ana@@empresa.com") is False


def test_usuario_vazio():
    assert validar_email("@empresa.com") is False


def test_dominio_vazio():
    assert validar_email("ana@") is False


def test_dominio_terminado_em_ponto():
    assert validar_email("ana@empresa.") is False


def test_dominio_iniciado_com_ponto():
    assert validar_email("ana@.empresa.com") is False


def test_dominio_sem_ponto():
    assert validar_email("ana@empresa") is False


def test_com_espaco():
    assert validar_email("ana @empresa.com") is False
    assert validar_email("ana@ empresa.com") is False


def test_entrada_none():
    assert validar_email(None) is False


def test_tipo_nao_str():
    assert validar_email(123) is False
    assert validar_email(["ana@empresa.com"]) is False