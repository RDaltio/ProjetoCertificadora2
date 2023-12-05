from matplotlib import pyplot as plt
from gui import PrintGraficoMovimento

class Menu:
    def __init__(self):
        self.particulas = []

    def apresentar_menu(self):
        while True:
            print("\nEscolha uma opção:")         
            print("\n1. Simular movimento retilíneo uniforme.")         
            print("\n2. Simular movimento retilíneo uniformemente variado.")       
            print("\n3. Simular movimento vertical.")       
            print("\n4. Visualizar resultados antigos.")
            print("\n5. Sair.")
            opcao = int(input("\nDigite o número da opção desejada: "))

            if opcao in [1, 2, 3]:
                resultados = self.simular_movimento(opcao)
                self.adicionar_particula(resultados)
            elif opcao == 4:
                self.visualizar_resultados_antigos()
            elif opcao == 5:
                break
            else:
                print("\nOpção inválida. Por favor, escolha uma opção válida.")

            resposta = input("\nDeseja realizar nova operação? (S para Sim/ N para Não): ")
            if resposta.lower() != 's':
                break

    def simular_movimento(self, tipo_movimento):
        posicao_inicial = float(input("\nDigite a posição inicial da partícula em metros: "))
        velocidade_inicial = float(input("\nDigite a velocidade da partícula em metros por segundo: "))
        tempo = float(input("\nDigite o tempo em segundos: "))

        if tipo_movimento == 1:
            aceleracao = 0
        elif tipo_movimento == 2:
            aceleracao = float(input("\nDigite a aceleração da partícula em metros por segundo ao quadrado: "))
        elif tipo_movimento == 3:
            aceleracao = -9.81
        else:
            aceleracao = 0

        output = PrintGraficoMovimento(posicao_inicial, velocidade_inicial, aceleracao, tempo)
        output.printGrafico()

        return {
            "posicao": output.posicao_tempo,
            "velocidade": output.velocidade_tempo,
            "aceleracao": output.aceleracao_tempo,
            "tempo": output.tempo_list
        }

    def adicionar_particula(self, resultados):
        self.particulas.append(resultados)

    def visualizar_resultados_antigos(self):
        if not self.particulas:
            print("\nNenhuma simulação foi realizada ainda.")
        else:
            fig, axs = plt.subplots(len(self.particulas), 3, figsize=(16, 4 * len(self.particulas)), dpi=100)
            fig.suptitle("Resultados Antigos")

            for idx, resultados in enumerate(self.particulas):
                axs[idx, 0].plot(resultados['tempo'], resultados['posicao'], label=f'Simulação {idx + 1}')
                axs[idx, 0].set_xlabel("Tempo - t(s)")
                axs[idx, 0].set_ylabel("Posição - S (m)")
                axs[idx, 0].axhline(0, color='black', linewidth=1)
                axs[idx, 0].axvline(0, color='black', linewidth=1)

                axs[idx, 1].plot(resultados['tempo'], resultados['velocidade'], label=f'Simulação {idx + 1}', color="green")
                axs[idx, 1].set_xlabel("Tempo - t(s)")
                axs[idx, 1].set_ylabel("Velocidade - v (m/s)")
                axs[idx, 1].axhline(0, color='black', linewidth=1)
                axs[idx, 1].axvline(0, color='black', linewidth=1)

                axs[idx, 2].plot(resultados['tempo'], resultados['aceleracao'], label=f'Simulação {idx + 1}', color="red")
                axs[idx, 2].set_xlabel("Tempo - t(s)")
                axs[idx, 2].set_ylabel("Aceleração - a (m/s²)")
                axs[idx, 2].axhline(0, color='black', linewidth=1)
                axs[idx, 2].axvline(0, color='grey', linewidth=1)

            plt.show()
