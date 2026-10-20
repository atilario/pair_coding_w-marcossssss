def validar_email(email: str) -> bool:
    """Valida um endereço de e-mail de acordo com as regras de aceite:
    - Deve ser texto (str)
    - Não pode conter espaços
    - Deve conter exatamente um '@'
    - Usuário (antes do '@') não pode ser vazio
    - Domínio deve ter pelo menos duas partes não vazias separadas por ponto
    - Rejeita None e domínio terminado em ponto
    """
    if not isinstance(email, str):
        return False

    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    usuario, dominio = email.split("@")

    if not usuario:
        return False

    partes_dominio = dominio.split(".")
    if len(partes_dominio) < 2:
        return False

    if not all(partes_dominio):
        return False

    return True