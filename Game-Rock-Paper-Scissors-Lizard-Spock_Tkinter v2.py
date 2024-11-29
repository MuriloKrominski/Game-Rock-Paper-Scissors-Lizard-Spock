import tkinter as tk
from tkinter import messagebox
from enum import Enum
import random
import webbrowser


class Idioma(Enum):
    PT = 'pt'
    EN = 'en'


# Traduções
TRADUCOES = {
    Idioma.PT: {
        "titulo": "Pedra, Papel, Tesoura, Lagarto e Spock - By Murilo Krominski",
        "escolha_jogada": "Escolha sua jogada:",
        "placar": "Placar - Você: {} | Dr. Sheldon Lee Cooper: {} | Empates: {}",
        "resultado": "Você jogou {}. \nDr. Sheldon Lee Cooper jogou {}.\n{}",
        "estatisticas": "Estatísticas:\nRodadas: {}\nVitórias: {:.1f}%\nDerrotas: {:.1f}%\nEmpates: {:.1f}%",
        "vencer": "\n\n'Você venceu! Isso é altamente ilógico!' – Dr. Sheldon Lee Cooper",
        "perder": "\n\n'Você perdeu! Bazinga!' – Dr. Sheldon Lee Cooper",
        "empatar": "\n\n'Empate! Um empate estatístico? Fascinante!' – Dr. Sheldon Lee Cooper",
        "idioma_titulo": "Escolha o idioma/Choose language",
        "idioma_botao": "Confirmar/Confirm",
        "jogadas": {
            "PAPEL": "Papel",
            "PEDRA": "Pedra",
            "TESOURA": "Tesoura",
            "LAGARTO": "Lagarto",
            "SPOCK": "Spock",
        },
        "estatisticas_botao": "📊 Estatísticas",
        "github": "Visite meu GitHub: https://murilokrominski.github.io",
    },
    Idioma.EN: {
        "titulo": "Rock, Paper, Scissors, Lizard, Spock",
        "escolha_jogada": "Choose your move:",
        "placar": "Score - You: {} | Dr. Sheldon Lee Cooper: {} | Draws: {}",
        "resultado": "You played {}. \nDr. Sheldon Lee Cooper played {}.\n{}",
        "estatisticas": "Statistics:\nRounds: {}\nWins: {:.1f}%\nLosses: {:.1f}%\nDraws: {:.1f}%",
        "vencer": "\n\n'You won! This is highly illogical!' – Dr. Sheldon Lee Cooper",
        "perder": "\n\n'You lost! Bazinga!' – Dr. Sheldon Lee Cooper",
        "empatar": "\n\n'Draw! A statistical tie? Fascinating!' – Dr. Sheldon Lee Cooper",
        "idioma_titulo": "Choose language",
        "idioma_botao": "Confirm",
        "jogadas": {
            "PAPEL": "Paper",
            "PEDRA": "Rock",
            "TESOURA": "Scissors",
            "LAGARTO": "Lizard",
            "SPOCK": "Spock",
        },
        "estatisticas_botao": "📊 Statistics",
        "github": "Visit my GitHub: https://murilokrominski.github.io",
    },
}


class Jogada(Enum):
    PAPEL = 0
    PEDRA = 1
    TESOURA = 2
    LAGARTO = 3
    SPOCK = 4




# Regras de vitória com emojis
regras_vitoria = {
    (Jogada.TESOURA, Jogada.PAPEL): "✂️ cut/corta 📄",
    (Jogada.PAPEL, Jogada.PEDRA): "📄 covers/cobre 🪨",
    (Jogada.PEDRA, Jogada.LAGARTO): "🪨 crushes/esmaga 🦎",
    (Jogada.LAGARTO, Jogada.SPOCK): "🦎 poisons/envenena 🖖",
    (Jogada.SPOCK, Jogada.TESOURA): "🖖 smashes/esmaga ✂️",
    (Jogada.TESOURA, Jogada.LAGARTO): "✂️ decapitate/decapita 🦎",
    (Jogada.LAGARTO, Jogada.PAPEL): "🦎 eats/come 📄",
    (Jogada.PAPEL, Jogada.SPOCK): "📄 disproves/refuta 🖖",
    (Jogada.SPOCK, Jogada.PEDRA): "🖖 vaporizes/vaporiza 🪨",
    (Jogada.PEDRA, Jogada.TESOURA): "🪨 crushes/quebra ✂️",
}


class JogoInterface:
    def __init__(self, root, idioma=Idioma.PT):
        self.root = root
        self.idioma = idioma
        self.textos = TRADUCOES[self.idioma]
        self.placar_jogador = 0
        self.placar_computador = 0
        self.placar_empates = 0
        self.total_rodadas = 0

        # Configurar a janela
        self.root.title(self.textos["titulo"])

        self.label_titulo = tk.Label(root, text=self.textos["escolha_jogada"], font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        self.botoes = []
        for jogada in Jogada:
            texto_botao = self.textos["jogadas"][jogada.name]
            btn = tk.Button(root, text=texto_botao, width=15, command=lambda j=jogada: self.jogar(j))
            btn.pack(pady=5)
            self.botoes.append(btn)

        self.label_placar = tk.Label(root, text=self.textos["placar"].format(0, 0, 0), font=("Arial", 12))
        self.label_placar.pack(pady=20)

        self.label_resultado = tk.Label(root, text="", font=("Arial", 14))
        self.label_resultado.pack(pady=10)

        self.botao_estatisticas = tk.Button(
            root, text=self.textos["estatisticas_botao"], command=self.mostrar_estatisticas
        )
        self.botao_estatisticas.pack(pady=5)

        # Link para o GitHub
        self.label_github = tk.Label(
            root, text=self.textos["github"], fg="blue", cursor="hand2", font=("Arial", 10, "italic")
        )
        self.label_github.pack(side="bottom", pady=10)
        self.label_github.bind("<Button-1>", self.abrir_github)

    def jogar(self, jogada_jogador):
        jogada_computador = random.choice(list(Jogada))
        resultado_texto, vencedor = self.determinar_vencedor(jogada_jogador, jogada_computador)

        self.total_rodadas += 1
        if vencedor == "Jogador":
            self.placar_jogador += 1
        elif vencedor == "Dr. Sheldon Lee Cooper":
            self.placar_computador += 1
        else:
            self.placar_empates += 1

        self.label_placar.config(
            text=self.textos["placar"].format(self.placar_jogador, self.placar_computador, self.placar_empates)
        )
        jogada_jogador_texto = self.textos["jogadas"][jogada_jogador.name]
        jogada_computador_texto = self.textos["jogadas"][jogada_computador.name]
        self.label_resultado.config(
            text=self.textos["resultado"].format(jogada_jogador_texto, jogada_computador_texto, resultado_texto)
        )

    def determinar_vencedor(self, jogada_jogador, jogada_computador):
        if jogada_jogador == jogada_computador:
            return self.textos["empatar"], "Empate"
        elif (jogada_jogador, jogada_computador) in regras_vitoria:
            return f"{regras_vitoria[(jogada_jogador, jogada_computador)]}. {self.textos['vencer']}", "Jogador"
        else:
            return f"{regras_vitoria[(jogada_computador, jogada_jogador)]}. {self.textos['perder']}", "Dr. Sheldon Lee Cooper"

    def mostrar_estatisticas(self):
        if self.total_rodadas == 0:
            messagebox.showinfo(self.textos["titulo"], "Sem rodadas ainda!")
            return

        porcentagens = {
            "vitorias": (self.placar_jogador / self.total_rodadas) * 100,
            "derrotas": (self.placar_computador / self.total_rodadas) * 100,
            "empates": (self.placar_empates / self.total_rodadas) * 100,
        }
        estatisticas = self.textos["estatisticas"].format(
            self.total_rodadas, porcentagens["vitorias"], porcentagens["derrotas"], porcentagens["empates"]
        )
        messagebox.showinfo(self.textos["titulo"], estatisticas)

    def abrir_github(self, event):
        webbrowser.open("https://murilokrominski.github.io/autor.htm")


def escolher_idioma():
    def confirmar_idioma():
        idioma_selecionado = Idioma.PT if idioma_var.get() == "PT" else Idioma.EN
        root.destroy()
        iniciar_jogo(idioma_selecionado)

    root = tk.Tk()
    root.title("Idioma / Language")

    idioma_var = tk.StringVar(value="PT")
    label = tk.Label(root, text=TRADUCOES[Idioma.PT]["idioma_titulo"], font=("Arial", 16))
    label.pack(pady=10)

    tk.Radiobutton(root, text="Português", variable=idioma_var, value="PT").pack(anchor="w")
    tk.Radiobutton(root, text="English", variable=idioma_var, value="EN").pack(anchor="w")

    botao_confirmar = tk.Button(root, text=TRADUCOES[Idioma.PT]["idioma_botao"], command=confirmar_idioma)
    botao_confirmar.pack(pady=10)

    root.mainloop()


def iniciar_jogo(idioma):
    root = tk.Tk()
    JogoInterface(root, idioma)
    root.mainloop()


if __name__ == "__main__":
    escolher_idioma()
