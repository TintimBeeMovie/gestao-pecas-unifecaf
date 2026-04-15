# Sistema de Gestão de Peças - UNIFECAF

## 📋 Descrição
Sistema desenvolvido em Python para automação do controle de qualidade
de peças industriais. O sistema avalia, armazena e gera relatórios
das peças produzidas em linha de montagem.

## ✅ Critérios de Aprovação
- Peso entre 95g e 105g
- Cor: azul ou verde
- Comprimento entre 10cm e 20cm

## 🚀 Como rodar o programa

### Requisitos
- Python 3.x instalado

### Passo a passo
1. Baixe ou clone o repositório
2. Abra o terminal na pasta do projeto
3. Execute o comando:
python main.py
4. Use o menu interativo para operar o sistema

## 📱 Menu do Sistema
- Opção 1: Cadastrar nova peça
- Opção 2: Listar peças aprovadas/reprovadas
- Opção 3: Remover peça cadastrada
- Opção 4: Listar caixas fechadas
- Opção 5: Gerar relatório final
- Opção 0: Sair

## 💡 Exemplos de entrada e saída

### Peça APROVADA:
ID da peça: 001
Peso (g): 100
Cor: azul
Comprimento (cm): 15
✅ Peça 001 APROVADA!

### Peça REPROVADA:
ID da peça: 002
Peso (g): 50
Cor: vermelho
Comprimento (cm): 5
❌ Peça 002 REPROVADA! Motivos: Peso fora do padrão, Cor inválida, Comprimento fora do padrão
## 📦 Armazenamento em Caixas
- Cada caixa comporta até 10 peças aprovadas
- Ao atingir 10 peças, a caixa é fechada automaticamente
- Uma nova caixa é aberta para as próximas peças

## 👨‍💻 Desenvolvido por
Rodrigo Valentin Costa - UNIFECAF - Algoritmos e Lógica de Programação.