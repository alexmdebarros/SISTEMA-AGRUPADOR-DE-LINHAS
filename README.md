Aqui está o modelo de um `README.md` em Markdown para o sistema que você desenvolveu:


# Agrupador de Linhas 1.0

Este é um sistema desenvolvido com Python e Tkinter para processar arquivos CSV. O programa agrupa os dados por "ID DO PEDIDO MAGAZINE", realiza somas de duas colunas específicas e salva o resultado em um novo arquivo CSV.

## Funcionalidades

- **Agrupamento e Somas**: O sistema agrupa os dados com base no campo "ID DO PEDIDO MAGAZINE" e calcula as somas das colunas "VALOR TOTAL BRUTO ESTORNADO EM REPASSE" e "VALOR DE COMISSÃO RESSARCIDA".
- **Processamento de Arquivos CSV**: O arquivo CSV de entrada deve estar no formato esperado, com as colunas devidamente separadas por ponto e vírgula (`;`) e codificação `latin1`.
- **Interface Gráfica**: O programa conta com uma interface simples desenvolvida com Tkinter, onde o usuário pode selecionar o arquivo CSV e processá-lo com facilidade.
- **Formatação de Valores**: As somas realizadas nas colunas "VALOR TOTAL BRUTO ESTORNADO EM REPASSE" e "VALOR DE COMISSÃO RESSARCIDA" são formatadas com duas casas decimais, usando a vírgula como separador decimal.

## Pré-requisitos

Antes de executar o programa, certifique-se de ter o Python 3 instalado, juntamente com a biblioteca Tkinter e Pandas.

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- Tkinter: Geralmente vem instalado com o Python.
- Pandas: Instale a biblioteca utilizando o comando:

   ```bash
   pip install pandas
   ```

## Como Usar

1. **Instalar Dependências:**
   
   Caso o Pandas não esteja instalado, instale-o com o seguinte comando:

   ```bash
   pip install pandas
   ```

2. **Executar o Sistema:**
   
   Execute o script `main.py` no seu terminal ou IDE de preferência:

   ```bash
   python main.py
   ```

3. **Selecionar o Arquivo:**
   
   Clique no botão **"Selecionar Arquivo"** e escolha o arquivo CSV que deseja processar.

4. **Processar o Arquivo:**
   
   Após selecionar o arquivo, clique no botão **"Processar"** para realizar o processamento. O arquivo resultante será salvo no mesmo diretório com o sufixo `_processado` no nome.

5. **Resultado:**
   
   O programa irá exibir uma mensagem informando o sucesso ou falha no processamento, e o novo arquivo será salvo com o nome formatado.

## Estrutura do Código

### Funções Importantes:

- **`process_csv(input_file, output_file)`**: Função principal que processa o arquivo CSV, realizando as somas necessárias e formatando os valores.
  
- **`select_file()`**: Função que abre a janela para o usuário selecionar o arquivo CSV.
  
- **`show_processing_message()`**: Exibe uma mensagem de processamento com pontos piscando enquanto o arquivo está sendo processado.

- **`save_file()`**: Função que executa o processamento do arquivo e salva o resultado.

### Componentes da Interface Gráfica:

- **Entrada de Arquivo**: Campo onde o caminho do arquivo selecionado é mostrado.
- **Botão "Selecionar Arquivo"**: Abre uma janela para selecionar o arquivo CSV.
- **Botão "Processar"**: Inicia o processamento do arquivo selecionado.
- **Rótulo de Processamento**: Exibe uma mensagem animada enquanto o arquivo está sendo processado.

## Exemplo de Uso

### Arquivo de Entrada (Exemplo):
```csv
ID DO PEDIDO MAGAZINE;PARCELA ATUAL;VALOR TOTAL BRUTO ESTORNADO EM REPASSE;VALOR DE COMISSÃO RESSARCIDA
1234;1;100,00;10,00
1234;2;200,00;20,00
5678;1;150,00;15,00
5678;2;50,00;5,00
```

### Arquivo de Saída (Exemplo):
```csv
ID DO PEDIDO MAGAZINE;PARCELA ATUAL;VALOR TOTAL BRUTO ESTORNADO EM REPASSE;VALOR DE COMISSÃO RESSARCIDA
1234;2;300,00;30,00
5678;2;200,00;20,00
```

## Contribuições

Se você tem sugestões ou melhorias para este sistema, sinta-se à vontade para abrir uma **issue** ou fazer um **pull request**.
