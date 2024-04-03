# PASS IN

![thumbnail](./.github/thumbnail.png)

>> An app to handle event check-in's easily.

O pass.in é uma aplicação de **gestão de participantes em eventos presenciais**.

A ferramenta permite que o organizador cadastre um evento e abra uma página pública de inscrição.

Os participantes inscritos podem emitir uma credencial para check-in no dia do evento.

O sistema fará um scan da credencial do participante para permitir a entrada no evento.

## Requisitos

### Requisitos funcionais

- [X]  O organizador deve poder cadastrar um novo evento;
- [X]  O organizador deve poder visualizar dados de um evento;
- [X]  O organizador deve poder visualizar a lista de participantes;
- [X]  O participante deve poder se inscrever em um evento;
- [x]  O participante deve poder visualizar seu crachá de inscrição;
- [ ]  O participante deve poder realizar check-in no evento;

### Regras de negócio

- [X]  O participante só pode se inscrever em um evento uma única vez;
- [ ]  O participante só pode se inscrever em eventos com vagas disponíveis;
- [ ]  O participante só pode realizar check-in em um evento uma única vez;

### Requisitos não-funcionais

- [ ]  O check-in no evento será realizado através de um QRCode;

## Especificações da API

[Swagger UI](./swagger.json)

## Banco de dados

Nessa aplicação vamos utilizar banco de dados relacional (SQL). Para ambiente de desenvolvimento seguiremos com o SQLite pela facilidade do ambiente.

### Diagrama ERD

![erd.svg](./.github/erd.svg)
