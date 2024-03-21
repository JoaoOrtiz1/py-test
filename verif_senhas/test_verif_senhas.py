import verif_senhas
def test_senha_curta():
    assert not verif_senhas.verificar_senha("Ab#2"), "A senha curta não deve ser considerada segura."

def test_falta_caractere_maiusculo():
    assert not verif_senhas.verificar_senha("senh@1234"), "A senha sem caractere maiúsculo não deve ser considerada segura."

def test_falta_caractere_minusculo():
    assert not verif_senhas.verificar_senha("SENH@1234"), "A senha sem caractere minúsculo não deve ser considerada segura."

def test_falta_numero():
    assert not verif_senhas.verificar_senha("SenhaSegura@"), "A senha sem número não deve ser considerada segura."

def test_falta_caractere_especial():
    assert not verif_senhas.verificar_senha("Senha1234"), "A senha sem caractere especial não deve ser considerada segura."

def test_senha_segura():
    assert verif_senhas.verificar_senha("SenhaForte@123"), "Esta senha deve ser considerada segura."

def test_senha_falha_multiplos_criterios():
    assert not verif_senhas.verificar_senha("senha"), "A senha que falha em múltiplos critérios não deve ser considerada segura."