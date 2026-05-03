from colorama import Fore, Style

def cor_mensagem(nivel):
    match nivel:
        case "nivel_1":
            return Fore.LIGHTRED_EX + "Muito baixo (crítico)."
        case "nivel_2":
            return Fore.LIGHTYELLOW_EX + "Baixo."
        case "nivel_3":
            return Fore.LIGHTGREEN_EX + "Médio."
        case "nivel_4":
            return Fore.LIGHTCYAN_EX + "Alto."
        case "nivel_5":
            return Fore.LIGHTBLUE_EX + "Muito alto (alerta)."
        case _:
            # Caso o nível não seja reconhecido
            return Fore.WHITE + "Nível desconhecido."


# Lista com os níveis dos reservatórios
reservatorio_niveis = ["nivel_1", "nivel_2", "nivel_3", "nivel_4", "nivel_5"]

# Quantidade de reservatórios que serão analisados
qtd_reservatorios = 1

# Loop para percorrer os reservatórios
for i in range(qtd_reservatorios):
    nivel = reservatorio_niveis[i]  # Seleciona o nível atual da lista
    
    mensagem = cor_mensagem(nivel)  # Chama a função e recebe a mensagem
    
    # Exibe o resultado formatado
    print(f"Nível do Reservatório: {nivel}. Situação: {mensagem}")

# Reseta as configurações de cor no terminal
print(Style.RESET_ALL)
