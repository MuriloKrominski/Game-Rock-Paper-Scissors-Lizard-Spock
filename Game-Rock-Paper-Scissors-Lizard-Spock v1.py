import random  # Para gerar jogadas aleatórias para o computador
import os  # Para limpar o terminal entre rodadas
from enum import Enum  # Para criar enumeradores (Jogada, Resultado, Idioma)
from typing import Optional, Dict  # Para anotações de tipo
from collections import defaultdict  # Para contadores automáticos de valores

# Enumeração para os idiomas suportados
class Idioma(Enum):
    PT = 'pt'  # Português
    EN = 'en'  # Inglês

# Classe para armazenar e acessar as traduções
class Traducoes:
    TEXTOS = {
        Idioma.PT: {  # Traduções em Português
            'titulo': 'Bem-vindo ao jogo Pedra, Papel, Tesoura, Lagarto e Spock',
            'escolha_idioma': 'Escolha o idioma / Choose language:\n1 - Português\n2 - English',
            'placar': 'PLACAR',
            'voce': 'Você',
            'computador': 'Computador',
            'empates': 'Empates',
            'escolha_lance': 'Escolha seu lance:',
            'opcoes_jogada': '0 - Papel | 1 - Pedra | 2 - Tesoura | 3 - Lagarto | 4 - Spock',
            'jogada_invalida': 'Jogada inválida! Escolha 0, 1, 2, 3 ou 4',
            'digite_numero': 'Por favor, digite um número (0, 1, 2, 3 ou 4)',
            'sua_jogada': 'Sua jogada',
            'jogada_computador': 'Jogada do computador',
            'voce_venceu': 'Você venceu! 🎉',
            'voce_perdeu': 'Você perdeu! 😢',
            'empate': 'Empate! 🤝',
            'jogar_novamente': 'Jogar novamente? 0 - Sim | 1 - Não',
            'escolha_sim_nao': 'Por favor, digite 0 para Sim ou 1 para Não',
            'stats_titulo': '🤓 ESTATÍSTICAS PARA NERDS 🤓',
            'total_rodadas': 'Total de rodadas',
            'taxa_vitoria': 'Taxa de vitória',
            'taxa_derrota': 'Taxa de derrota',
            'taxa_empate': 'Taxa de empate',
            'jogadas_frequentes': 'Suas jogadas mais frequentes',
            'maior_sequencia': 'Maior sequência de vitórias',
            'sequencia_atual': 'Sequência atual de vitórias',
            'papel': 'PAPEL',
            'pedra': 'PEDRA',
            'tesoura': 'TESOURA',
            'lagarto': 'LAGARTO',
            'spock': 'SPOCK',
            # Descrições das interações
            'descricoes_interacoes': {
                (0, 2): "Tesoura corta Papel",
                (2, 0): "Tesoura corta Papel",
                (0, 1): "Papel cobre Pedra",
                (1, 0): "Papel cobre Pedra",
                (1, 3): "Pedra esmaga Lagarto",
                (3, 1): "Pedra esmaga Lagarto",
                (3, 4): "Lagarto envenena Spock",
                (4, 3): "Lagarto envenena Spock",
                (4, 2): "Spock esmaga Tesoura",
                (2, 4): "Spock esmaga Tesoura",
                (2, 3): "Tesoura decapita Lagarto",
                (3, 2): "Tesoura decapita Lagarto",
                (3, 0): "Lagarto come Papel",
                (0, 3): "Lagarto come Papel",
                (0, 4): "Papel refuta Spock",
                (4, 0): "Papel refuta Spock",
                (4, 1): "Spock vaporiza Pedra",
                (1, 4): "Spock vaporiza Pedra",
                (1, 2): "Pedra quebra Tesoura",
                (2, 1): "Pedra quebra Tesoura",
            }
        },
        Idioma.EN: {  # Traduções em Inglês
            'titulo': 'Welcome to Rock, Paper, Scissors, Lizard, Spock game',
            'escolha_idioma': 'Choose language / Escolha o idioma:\n1 - Portuguese\n2 - English',
            'placar': 'SCORE',
            'voce': 'You',
            'computador': 'Computer',
            'empates': 'Draws',
            'escolha_lance': 'Choose your move:',
            'opcoes_jogada': '0 - Paper | 1 - Rock | 2 - Scissors | 3 - Lizard | 4 - Spock',
            'jogada_invalida': 'Invalid move! Choose 0, 1, 2, 3 or 4',
            'digite_numero': 'Please enter a number (0, 1, 2, 3 or 4)',
            'sua_jogada': 'Your move',
            'jogada_computador': 'Computer move',
            'voce_venceu': 'You won! 🎉',
            'voce_perdeu': 'You lost! 😢',
            'empate': 'Draw! 🤝',
            'jogar_novamente': 'Play again? 0 - Yes | 1 - No',
            'escolha_sim_nao': 'Please enter 0 for Yes or 1 for No',
            'stats_titulo': '🤓 NERD STATS 🤓',
            'total_rodadas': 'Total rounds',
            'taxa_vitoria': 'Win rate',
            'taxa_derrota': 'Loss rate',
            'taxa_empate': 'Draw rate',
            'jogadas_frequentes': 'Your most frequent moves',
            'maior_sequencia': 'Longest win streak',
            'sequencia_atual': 'Current win streak',
            'papel': 'PAPER',
            'pedra': 'ROCK',
            'tesoura': 'SCISSORS',
            'lagarto': 'LIZARD',
            'spock': 'SPOCK',
            # Descrições das interações
            'descricoes_interacoes': {
                (0, 2): "Scissors cuts Paper",
                (2, 0): "Scissors cuts Paper",
                (0, 1): "Paper covers Rock",
                (1, 0): "Paper covers Rock",
                (1, 3): "Rock crushes Lizard",
                (3, 1): "Rock crushes Lizard",
                (3, 4): "Lizard poisons Spock",
                (4, 3): "Lizard poisons Spock",
                (4, 2): "Spock smashes Scissors",
                (2, 4): "Spock smashes Scissors",
                (2, 3): "Scissors decapitates Lizard",
                (3, 2): "Scissors decapitates Lizard",
                (3, 0): "Lizard eats Paper",
                (0, 3): "Lizard eats Paper",
                (0, 4): "Paper disproves Spock",
                (4, 0): "Paper disproves Spock",
                (4, 1): "Spock vaporizes Rock",
                (1, 4): "Spock vaporizes Rock",
                (1, 2): "Rock crushes Scissors",
                (2, 1): "Rock crushes Scissors",
            }
        }
    }

    def __init__(self, idioma: Idioma):
        self.idioma = idioma  # Define o idioma selecionado

    def get(self, chave: str) -> str:
        return self.TEXTOS[self.idioma][chave]  # Retorna a tradução correspondente

# Enumeração para as jogadas possíveis
class Jogada(Enum):
    PAPEL = 0
    PEDRA = 1
    TESOURA = 2
    LAGARTO = 3
    SPOCK = 4

    @classmethod
    def from_int(cls, valor: int) -> Optional['Jogada']:
        try:
            return Jogada(valor)  # Converte o número inteiro para a jogada correspondente
        except ValueError:
            return None

# Enumeração para os resultados possíveis
class Resultado(Enum):
    VITORIA_JOGADOR = 'p'  # Vitória do jogador
    VITORIA_COMPUTADOR = 'c'  # Vitória do computador
    EMPATE = 'd'  # Empate

# Classe para armazenar e calcular estatísticas do jogo
class Estatisticas:
    def __init__(self):
        self.total_rodadas = 0  # Total de rodadas jogadas
        self.jogadas_jogador = defaultdict(int)  # Contador de jogadas do jogador
        self.jogadas_computador = defaultdict(int)  # Contador de jogadas do computador
        self.resultados = defaultdict(int)  # Contador de resultados
        self.sequencia_vitorias = 0  # Sequência atual de vitórias
        self.maior_sequencia_vitorias = 0  # Maior sequência de vitórias

    def registrar_rodada(self, jogada_jogador: Jogada, jogada_computador: Jogada, resultado: Resultado):
        self.total_rodadas += 1  # Incrementa o total de rodadas
        self.jogadas_jogador[jogada_jogador] += 1  # Conta a jogada do jogador
        self.jogadas_computador[jogada_computador] += 1  # Conta a jogada do computador
        self.resultados[resultado] += 1  # Registra o resultado

        if resultado == Resultado.VITORIA_JOGADOR:
            self.sequencia_vitorias += 1  # Incrementa a sequência de vitórias
            self.maior_sequencia_vitorias = max(self.maior_sequencia_vitorias, self.sequencia_vitorias)
        else:
            self.sequencia_vitorias = 0  # Reseta a sequência se não for vitória

    def calcular_porcentagens(self) -> Dict[str, float]:
        if self.total_rodadas == 0:
            return {'vitorias': 0.0, 'derrotas': 0.0, 'empates': 0.0}
        return {
            'vitorias': (self.resultados[Resultado.VITORIA_JOGADOR] / self.total_rodadas) * 100,
            'derrotas': (self.resultados[Resultado.VITORIA_COMPUTADOR] / self.total_rodadas) * 100,
            'empates': (self.resultados[Resultado.EMPATE] / self.total_rodadas) * 100
        }

# Classe principal do jogo
class JogoPPTLS:
    def __init__(self):
        self.placar_jogador = 0  # Placar do jogador
        self.placar_computador = 0  # Placar do computador
        self.placar_empates = 0  # Número de empates
        self.estatisticas = Estatisticas()  # Instância para gerenciar estatísticas
        self.traducoes = None  # Traduções serão definidas posteriormente

        # Regras de vitória
        self.regras_vitoria = {
            (Jogada.TESOURA, Jogada.PAPEL): Resultado.VITORIA_JOGADOR,
            (Jogada.PAPEL, Jogada.PEDRA): Resultado.VITORIA_JOGADOR,
            (Jogada.PEDRA, Jogada.LAGARTO): Resultado.VITORIA_JOGADOR,
            (Jogada.LAGARTO, Jogada.SPOCK): Resultado.VITORIA_JOGADOR,
            (Jogada.SPOCK, Jogada.TESOURA): Resultado.VITORIA_JOGADOR,
            (Jogada.TESOURA, Jogada.LAGARTO): Resultado.VITORIA_JOGADOR,
            (Jogada.LAGARTO, Jogada.PAPEL): Resultado.VITORIA_JOGADOR,
            (Jogada.PAPEL, Jogada.SPOCK): Resultado.VITORIA_JOGADOR,
            (Jogada.SPOCK, Jogada.PEDRA): Resultado.VITORIA_JOGADOR,
            (Jogada.PEDRA, Jogada.TESOURA): Resultado.VITORIA_JOGADOR,
        }

    def escolher_idioma(self) -> None:
        while True:
            print('\n=========================')
            print('Escolha o idioma / Choose language:')
            print('1 - Português')
            print('2 - English')
            escolha = input().strip()
            if escolha == '1':
                self.traducoes = Traducoes(Idioma.PT)
                break
            elif escolha == '2':
                self.traducoes = Traducoes(Idioma.EN)
                break
            else:
                print("Por favor escolha 1 ou 2 / Please choose 1 or 2")

    def traduzir_jogada(self, jogada: Jogada) -> str:
        return self.traducoes.get(jogada.name.lower())

    def mostrar_placar(self) -> None:
        print('========================')
        print(f'\n{self.traducoes.get("placar")}:')
        print(f'{self.traducoes.get("voce")}: {self.placar_jogador}')
        print(f'{self.traducoes.get("computador")}: {self.placar_computador}')
        print(f'{self.traducoes.get("empates")}: {self.placar_empates}')
        
        if self.estatisticas.total_rodadas > 0:
            print(f'\n{self.traducoes.get("stats_titulo")}')
            print(f'{self.traducoes.get("total_rodadas")}: {self.estatisticas.total_rodadas}')
            
            porcentagens = self.estatisticas.calcular_porcentagens()
            print(f'{self.traducoes.get("taxa_vitoria")}: {porcentagens["vitorias"]:.1f}%')
            print(f'{self.traducoes.get("taxa_derrota")}: {porcentagens["derrotas"]:.1f}%')
            print(f'{self.traducoes.get("taxa_empate")}: {porcentagens["empates"]:.1f}%')
            
            print(f'\n{self.traducoes.get("jogadas_frequentes")}:')
            total = sum(self.estatisticas.jogadas_jogador.values())
            for jogada, count in self.estatisticas.jogadas_jogador.items():
                percentual = (count / total) * 100 if total > 0 else 0
                print(f'{self.traduzir_jogada(jogada)}: {percentual:.1f}%')
            
            print(f'\n{self.traducoes.get("maior_sequencia")}: {self.estatisticas.maior_sequencia_vitorias}')
            print(f'{self.traducoes.get("sequencia_atual")}: {self.estatisticas.sequencia_vitorias}')
        
        print('\n')
        print(self.traducoes.get('escolha_lance'))
        print(self.traducoes.get('opcoes_jogada'))

    def obter_jogada_computador(self) -> Jogada:
        return random.choice(list(Jogada))

    def obter_jogada_jogador(self) -> Optional[Jogada]:
        while True:
            jogada = input().strip()
            if not jogada.isdigit():
                print(self.traducoes.get("digite_numero"))
                continue
            jogada_enum = Jogada.from_int(int(jogada))
            if jogada_enum is None:
                print(self.traducoes.get("jogada_invalida"))
                continue
            return jogada_enum

    def determinar_vencedor(self, jogada_jogador: Jogada, jogada_computador: Jogada) -> Resultado:
        if jogada_jogador == jogada_computador:
            self.placar_empates += 1
            return Resultado.EMPATE
        elif (jogada_jogador, jogada_computador) in self.regras_vitoria:
            self.placar_jogador += 1
            return Resultado.VITORIA_JOGADOR
        else:
            self.placar_computador += 1
            return Resultado.VITORIA_COMPUTADOR

    def mostrar_resultado(self, jogada_jogador: Jogada, jogada_computador: Jogada, resultado: Resultado) -> None:
        print('\n====================')
        print(f'{self.traducoes.get("sua_jogada")}: {self.traduzir_jogada(jogada_jogador)}')
        print(f'{self.traducoes.get("jogada_computador")}: {self.traduzir_jogada(jogada_computador)}')
        
        if resultado == Resultado.EMPATE:
            print(self.traducoes.get("empate"))
        else:
            # Obtém a descrição da interação do dicionário de traduções
            chave_interacao = (jogada_jogador.value, jogada_computador.value)
            descricao = self.traducoes.get('descricoes_interacoes').get(chave_interacao)
            if not descricao:
                # Tenta a chave inversa caso não encontre
                chave_interacao = (jogada_computador.value, jogada_jogador.value)
                descricao = self.traducoes.get('descricoes_interacoes').get(chave_interacao)
            if descricao:
                print(descricao)
            if resultado == Resultado.VITORIA_JOGADOR:
                print(self.traducoes.get("voce_venceu"))
            else:
                print(self.traducoes.get("voce_perdeu"))
        print('========================')

    def jogar_novamente(self) -> bool:
        while True:
            print(self.traducoes.get("jogar_novamente"))
            escolha = input().strip()
            if escolha == '0':
                return True
            elif escolha == '1':
                return False
            else:
                print(self.traducoes.get("escolha_sim_nao"))

    def iniciar(self) -> None:
        print('========================')
        self.escolher_idioma()
        print(self.traducoes.get("titulo"))
        
        while True:
            self.mostrar_placar()
            
            jogada_jogador = self.obter_jogada_jogador()
            if jogada_jogador is None:
                continue
                
            jogada_computador = self.obter_jogada_computador()
            resultado = self.determinar_vencedor(jogada_jogador, jogada_computador)
            
            self.estatisticas.registrar_rodada(jogada_jogador, jogada_computador, resultado)
            
            self.mostrar_resultado(jogada_jogador, jogada_computador, resultado)
            
            if not self.jogar_novamente():
                break
                
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal

if __name__ == "__main__":
    jogo = JogoPPTLS()
    jogo.iniciar()
