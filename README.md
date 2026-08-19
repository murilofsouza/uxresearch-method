# Método de UX Research

O método que uma entrega de UX Research segue: como o projeto se organiza, por onde entra coisa nova,
o que é fonte única, como o material do cliente fala, o que a publicação recusa publicar e como se
confere um entregável.

**Leia [`SCHEMA.md`](SCHEMA.md) primeiro** — é o mapa. As demais páginas se abrem sob demanda.

Cada regra aqui foi paga por um defeito real e **chega com o bug que a originou**. Isso não é anedota:
regra sem razão o próximo dilui, porque não sabe o que ela custou.

---

## De onde veio, e por quê

Este repo saiu de `metodo/` no [`llm-wiki-daedalus`](https://github.com/murilofsouza/llm-wiki-daedalus),
**com os 15 commits de história preservados**. O motivo da saída: aquele repo é o padrão da
wiki-curadora — inglês, público, audiência externa —, e este é o método de entrega de um projeto de
UX Research. Dois assuntos e duas audiências no mesmo remote custavam controle de tráfego em toda
página, que abria dizendo quando ela não valia.

O critério que autorizou a fusão era *"o que o artefato é, não o assunto"*. Ele separa prosa de código
e **é cego para separar prosa de prosa**. O critério que faltava: **quem lê, e do que aquilo é fonte.**

**O Obsidian é o ambiente de trabalho; o UX Research é o entregável do cliente.** Dois donos, dois
repos.

---

## ⚠️ Estado de transição — este repo carrega as duas metades

Hoje ele tem **as nove páginas**, e três delas não são de UX Research: `estrutura-de-projeto`,
`regra-de-chegada` e `fonte-canonica` são regras do **vault** e voltam para o repo público. A divisão
por regra é a Fase B do `PLAN-006` (vault: `5. Work/Studio Visual/Método de Projeto/Plans/open/`), e
ela espera o FIA e o Jornal da Orla fecharem — **desenhar a fronteira antes dos dois consumidores
terminarem é adivinhar o que é invariante**, o mesmo argumento que já adiou o pacote e o gerador.

**Isto está escrito porque a mistura é transitória, não deliberada.** Sem esta seção, a próxima sessão
lê as nove páginas como decisão e a Fase B nunca acontece.

### Duas regras enquanto ele estiver assim

**1. Regra nova nasce com o dono marcado.** Uma palavra, no momento de escrever, quando o bug está na
frente e a classificação é óbvia:

| Marca | Quem é o dono | Vai para |
|---|---|---|
| `BRAIN` | regra do vault — pastas, rota de entrada, fonte única, divisão de doc | o repo público |
| `UX` | regra de entrega — camada do cliente, specs, wireframe, portal, fases | fica aqui |
| `eng` | engenharia geral — não é método de nenhum dos dois | `~/.claude/CLAUDE.md` |

Sem isso, a Fase B vira reler ~1.600 linhas frias adivinhando de quem é cada regra. Com isso, vira uma
varredura de marcas.

**2. O bug continua entrando sem nome, mesmo com o repo privado.** A regra vinha de o repo ser público,
e a tentação agora é relaxar — mas **um terço destas páginas volta para o público na Fase B**. Nome de
cliente escrito aqui hoje é sanitização retroativa depois, num corpus maior. A prova é a situação e o
número — *"a contagem chegou a viver em 11 arquivos"* —, nunca o cliente, a cidade ou o concorrente.

---

## O que este método não é

- **Não é o escopo nem o estado de um projeto** — isso é a spec de escopo e o `roadmap`.
- **Não é a wiki de um cliente** — ela guarda `client` · `stack` · `conventions` e **linka** este método.
  Regra cross-cliente duplicada numa wiki de cliente é bug.
- **Não é o padrão da wiki-curadora** — isso é o
  [`llm-wiki-daedalus`](https://github.com/murilofsouza/llm-wiki-daedalus): como a documentação se
  mantém enxuta. Este método é o que se documenta.
- **Não é código.** O sync, a casca do portal e as invariantes executáveis vivem em
  `@studiovisual/hub-sync` e no template. **O agente escreve, o sync verifica.**

## O gargalo

Prosa depende de leitura, e o que depende de leitura volta sempre. O que cobra este método na prática
são as invariantes do `hub-sync`, que **abortam a publicação** no gargalo por onde todo conteúdo passa.
Regra que nenhum gargalo pode cobrar é candidata a apagar, não a mudar de pasta.

---

*Referenciado, nunca copiado.*
