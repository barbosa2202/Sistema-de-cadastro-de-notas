import json
import os


class RegistroNotas:
    def __init__(self, arquivo="notas.json"):
        self.arquivo = arquivo
        self.notas = self.carregar_notas()

    def carregar_notas(self):
        if os.path.exists(self.arquivo):
            try:
                with open(self.arquivo, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                print("Erro ao carregar o arquivo de notas. Criando um novo arquivo.")
                return {}
        else:
            return {}

    def salvar_notas(self):
        try:
            with open(self.arquivo, "w") as f:
                json.dump(self.notas, f, indent=4)
        except IOError:
            print("Erro ao salvar o arquivo de notas.")

    def validar_nome(self, nome):
        if nome.isdigit():
            print("Nome invalido. Nao use apenas numeros.")
            return False
        return True

    def validar_matricula(self, matricula):
        if not matricula.isdigit():
            print("Numero de matrícula invalido. Deve conter apenas numeros.")
            return False
        return True

    def adicionar_notas_em_lote(self, notas_lote):
        for matricula, aluno, semestre, materia, nota in notas_lote:
            self.notas[matricula] = {"aluno": aluno, "semestres": {}}

            self.notas[matricula]["semestres"][semestre] = {}

            self.notas[matricula]["semestres"][semestre][materia] = nota

            self.salvar_notas()

    def exibir_notas(self):
        if not self.notas:
            print("Nenhuma nota registrada ainda.")
            return

        print("\nRegistro de Notas:")
        for matricula, dados in self.notas.items():
            print(f"Matrícula: {matricula} | Aluno: {dados['aluno']}")
            for semestre, materias in dados["semestres"].items():
                print(f"  Semestre: {semestre}")
                for materia, nota in materias.items():
                    print(f"    Matéria: {materia} | Nota: {nota}")
    
    def limpar_tela(self):
        os.system('clear')