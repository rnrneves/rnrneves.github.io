def verificar_acesso(cargo, dia_da_semana):
    dias_uteis = ["segunda", "Terça", "Quarta", "Quinta", "Sexta"]

#Regra de acesso
    if cargo == "gerente":  
        permissao = True
    elif cargo == "Analista"  and dia_da_semana in dias_uteis:
        permissao = True
    elif cargo == "estagiario" and dia_da_semana in dias_uteis:
        permissao = True
    elif cargo == "Supervisor" and dia_da_semana in dias_uteis:
        permissao = True
    else:
        permissao = False
#Exebindo resultado
    if permissao:
        print("Acesso permitido.")
    else:
        print("Acesso negado")

#Uso
cargo = input("Digite seu cargo: ")
verificar_acesso(cargo, "segunda")
