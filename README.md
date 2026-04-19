[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/KQahFieU)

# ICE Middleware — Exemplo 3.21

Baseado no livro Distributed Systems de Maarten van Steen, Capítulo 3, Exemplo 3.21.

## Métodos adicionados

Além do `printString` original, foram adicionados dois novos métodos à interface `Printer`:

- **`countWords(string s) → int`**: retorna o número de palavras da string
- **`reverseString(string s) → string`**: retorna a string invertida

## Instalação (Amazon Linux)
sudo dnf install https://download.zeroc.com/ice/3.7/amzn2023/ice-repo-3.7.amzn2023.noarch.rpm
sudo dnf install python3-ice ice-compilers
## Como executar

Após clonar, rode em ambas as máquinas:
slice2py Printer.ice
Na máquina servidor:
python3 server.py

Na máquina cliente:
python3 client.py
