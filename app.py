from registrar_notas import RegistroNotas

def main():
    registro = RegistroNotas()
    registro.limpar_tela()
    materias = {
        "1": "Arquitetura de Computadores",
        "2": "Desenvolvimento em python",
        "3": "Banco de dados",
        "4": "Segurança cibernetica",
        "5": "Desenvolvimento web",
        "6": "Lógica de computadores",
        "7": "Linguagem orientada objetos em java"
    }

    while True:
        registro.limpar_tela()
        print("\n1. Adicionar Notas em Lote")
        print("2. Exibir Notas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                notas_lote = []
                while True:
                    matricula = input("Número de matrícula (ou deixe vazio para sair): ").strip()
                    if not matricula:
                        break
                    if not matricula.isdigit():
                        print("Número de matrícula inválido. Use apenas números.")
                        continue

                    aluno = input("Nome do aluno: ").strip()
                    if not aluno or aluno.isdigit():
                        print("Nome do aluno inválido. Não pode ser apenas números.")
                        continue

                    semestre = input("Semestre: ").strip()
                    if not semestre:
                        print("O semestre não pode estar vazio.")
                        continue

                    print("Escolha a matéria:")
                    for num, nome in materias.items():
                        print(f"{num}. {nome}")

                    materia_opcao = input("Número da matéria: ").strip()
                    match materia_opcao:
                        case _ if materia_opcao in materias:
                            materia = materias[materia_opcao]
                        case _:
                            print("Matéria inválida, tente novamente.")
                            continue

                    try:
                        nota = float(input("Nota (0 a 10): ").strip())
                        if not (0 <= nota <= 10):
                            print("A nota deve ser entre 0 e 10.")
                            continue
                    except ValueError:
                        print("Por favor, insira um valor numérico válido para a nota.")
                        continue

                    notas_lote.append((matricula, aluno, semestre, materia, nota))
                    registro.adicionar_notas_em_lote(notas_lote)
            case "2":
                registro.exibir_notas()
                input("Pressione Enter para continuar...")
            case "3":
                print("Saindo...")
                break
            case _:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
