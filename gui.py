import numpy as np
import matplotlib.pyplot as plt

class PrintGraficoMovimento:
    def __init__(self, posicao_inicial, velocidade_inicial, aceleracao, tempo):
        self.posicao_inicial = posicao_inicial
        self.velocidade_inicial = velocidade_inicial
        self.aceleracao = aceleracao
        self.tempo = tempo

        self.tempo_list = None
        self.posicao_tempo = None
        self.velocidade_tempo = None
        self.aceleracao_tempo = None

    def printGrafico(self):
        self.tempo_list = np.linspace(0, self.tempo, 1000)

        self.velocidade_tempo = [self.velocidade_inicial + self.aceleracao * t for t in self.tempo_list]

        self.posicao_tempo = [
            self.posicao_inicial + self.velocidade_inicial * t + 0.5 * self.aceleracao * t**2
            for t in self.tempo_list
        ]

        self.aceleracao_tempo = [self.aceleracao for _ in self.tempo_list]

        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 4), dpi=100)

        ax1.plot(self.tempo_list, self.posicao_tempo)
        ax1.set_xlabel("Tempo - t(s)")
        ax1.set_ylabel("Posição - S (m)")
        ax1.axhline(0, color='black', linewidth=1)
        ax1.axvline(0, color='black', linewidth=1)

        ax2.plot(self.tempo_list, self.velocidade_tempo, color="green")
        ax2.set_xlabel("Tempo - t(s)")
        ax2.set_ylabel("Velocidade - v (m/s)")
        ax2.axhline(0, color='black', linewidth=1)
        ax2.axvline(0, color='black', linewidth=1)

        ax3.plot(self.tempo_list, self.aceleracao_tempo, color="red")
        ax3.set_xlabel("Tempo - t(s)")
        ax3.set_ylabel("Aceleração - a (m/s²)")
        ax3.axhline(0, color='black', linewidth=1)
        ax3.axvline(0, color='grey', linewidth=1)
        
        plt.show()
