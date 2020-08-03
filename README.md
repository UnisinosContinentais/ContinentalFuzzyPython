# ContinentalFuzzy

## Controlador de Lógica Fuzzy que possui os seguintes tipos de inferência:

- Mamdani (scikit-fuzzy);
- Takagi-Sugeno.

## Rodar o Console Integração

No diretório raiz do projeto digitar:

```
$ python consoleIntegracao.py
```

## Rodar o Console

Para testar o controlador Mamdani, no diretório raiz do projeto digitar:

```
$ python -m continentalfuzzy.console.console test_mamdani.fis 0.8 0.025 100
```

Para testar o controlador Sugeno, no diretório raiz do projeto digitar:

```
$ python -m continentalfuzzy.console.console test_sugeno.fis 0.8 0.025 100
```
