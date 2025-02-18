# lqm-file-extractor

Ferramenta Python para extrair conteúdo de texto de arquivos .lqm e .jlqm (QuickMemo+).

→ [Projeto Original](https://github.com/pporadzisz/lqm-file-extractor) ←

## Funcionalidades
- **Extração:** Extrai os arquivos do .lqm para suas respectivas pastas.
- **Arquivos .txt:** Cria arquivos .txt do conteudo escrito de cada arquivo .jlqm extraido
- **Organiza a saída:** Todos os arquivos .txt extraídos são salvos em uma pasta única chamada **extracted_texts**.
- **Inclui metadados:** Adiciona data de criação, categoria e ID do memo aos arquivos de texto extraídos.
- **Tratamento de erros:** Continua o processamento mesmo que alguns arquivos falhem na extração e lista os erros ao final.

## Instalação

### Linux

1. Baixe o arquivo extract.py:

```
wget [https://raw.githubusercontent.com/pporadzisz/lqm-file-extractor/master/extract.py](https://github.com/Jhonatafs/lqm-file-extractor/blob/master/extract.py)
```

2. Certifique-se de que o Python 3 está instalado:

```
python3 --version
```

## Como Usar

Execute o script passando o caminho da pasta que contém os arquivos .lqm:

```
python3 extract.py caminho_para_arquivos_lqm
```

### Exemplo

#### Entrada

```
python3 extract.py /home/user/Downloads/quickmemo_plus
```

#### Saída

```
##### QuickMemo+\_190212_021335(1).lqm

Data de Criação: 2019-02-12 02:13:35
Categoria: My memos
ID do Memo: 123

Texto:
EU AMO LINUX

##### QuickMemo+\_190212_021340(1).lqm

Data de Criação: 2019-02-12 02:13:40
Categoria: My memos
ID do Memo: 124

Texto:
Meu segundo texto
```

## Passo a Passo

1. Use a opção Compartilhar no QuickMemo+ no seu dispositivo Android.
2. Selecione todas as notas e clique no botão Compartilhar.
3. Escolha a opção Arquivo QuickMemo+ (.lqm).
4. Salve os arquivos .lqm no Google Drive ou no armazenamento local.
5. Baixe os arquivos .lqm para uma única pasta no seu computador.
6. Baixe o script extract.py.
7. Execute o script no terminal:

```
python3 extract.py /caminho/para/seu/arquivos_lqm
```

8. Verifique a pasta extracted_texts para ver os arquivos .txt extraídos.

## Contribuindo

Sinta-se à vontade para fazer um fork deste projeto e enviar pull requests com melhorias. Para mudanças significativas, abra uma issue primeiro para discutir as alterações.
Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](/LICENSE) para detalhes.

## Versão em Inglês

Para a versão em inglês deste README, consulte [README.md](/README.md).
