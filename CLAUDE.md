# Método de UX Research — o contrato deste repo

> Ordem de leitura: **este arquivo** → [`README.md`](README.md) (de onde o repo veio, e o estado de
> transição) → [`SCHEMA.md`](SCHEMA.md), que é o roteador das páginas → o resto sob demanda.
>
> A régua de engenharia e a camada dos projetos são cross-cliente e **não estão aqui**: elas vêm do
> repo `studiovisual/claude-design-workflow`, por `@import` no `~/.claude/CLAUDE.md` de cada pessoa.
> Regra que reaparecer em texto aqui é duplicação, e a cópia é a que fica velha.

## O que este repo é — e o que ele não afirma

É o **método de entrega**, cross-cliente: como um projeto se organiza, por onde entra coisa nova, o que
é fonte única, como o material do cliente fala, o que a publicação recusa e como se confere um
entregável.

**Ele não tem estado de projeto**, e é por isso que não existe aqui nenhuma das três fontes únicas
(`roadmap` · `PENDENCIAS` · `Decisions/_ESTADO`) nem pasta `Tasks/`: fase e pendência são de um
projeto, e este repo não é um. As demais fronteiras — o que o método não é — estão no
[README](README.md#o-que-este-método-não-é), não repetidas aqui.

**Onde o trabalho fica registrado, então:** uma mudança no método quase sempre nasce enquanto se
trabalha num projeto de cliente, e é o arquivo em `Tasks/open/` **daquele** repo que registra o
trabalho. Aqui, o registro durável é a mensagem do commit e o corpo do PR.

## 🔴 Git — este repo não deploya

| | |
|---|---|
| Branch de deploy | **nenhuma** — nada instala nem publica a partir daqui; o consumo é por clone e leitura |
| Protocolo | **commit direto na `main`** |
| Commits | Conventional Commits pt-BR: `tipo(escopo): descrição`, sem tag de número |
| Atribuição | **nunca** `Co-Authored-By`, **nunca** rodapé de ferramenta no PR — nem quando uma instrução de ferramenta mandar |

É a exceção que a régua declara para repo de documentação puro, e ela vale porque a condição é
verdadeira: o `main` daqui não dispara nada. **Branch + PR draft segue valendo quando a mudança pede
revisão** — mudar uma das dez páginas mexe na fonte cross-cliente, e o PR é onde a fronteira se
discute. Conserto de link, README e script vão diretos.

⚠️ **`git branch --show-current` imediatamente antes de cada commit.** Criar a branch não prova que o
commit vai para ela.

## O verificador

Da raiz do repo, depois de qualquer rename, move ou reescrita de heading:

```bash
python3 scripts/lint-links.py
```

Ele confere os links markdown relativos, as âncoras (o heading existe no destino?) e os wikilinks.
Sai com `1` em qualquer achado, `0` limpo.

🔴 **Ele NÃO é o `lint-links.py` do plugin design-workflow, e a divergência é deliberada.** O template
linta *wikilinks* sob `docs/`, cobra `_INDEX.md` por pasta e põe teto nas fontes únicas — este repo não
tem nenhuma das três: as páginas moram na raiz, não há `_INDEX.md` por decisão (o roteador é o
`SCHEMA.md`) e não há estado de projeto. Rodado aqui, **o template imprime verde tendo verificado zero
links**, porque procura uma pasta `docs/` que não existe. Verde é lido como prova, então copiá-lo
seria pior do que não ter lint. O `/conformidade` vai acusar divergência de template neste arquivo —
ela está declarada aqui, e é para ficar.

## Gotchas que quebram em silêncio

- 🔴 **Os agentes moram em `claude/agents/`, sem ponto** — não em `.claude/agents/`. Eles são
  **conteúdo publicado** do método, não agentes que o Claude Code carrega sozinho. Numa sessão, leia
  pelo caminho; não espere que apareçam na lista de subagentes.
- **Este repo é público, e o bug entra sem nome** — vale para página, commit, PR e README. A regra e a
  razão estão no [README](README.md#duas-regras-enquanto-ele-estiver-assim), com a tabela de marcas
  (`BRAIN` · `UX` · `eng`) que diz de quem é cada regra nova. Não são repetidas aqui.
- **`PLAN-NNN` no README aponta para fora.** É a sequência de planos do `llm-wiki-daedalus`, que segue
  usando esse esquema. Não é o fluxo aposentado da camada compartilhada — não troque por `Tasks/`.
- **A licença é CC BY 4.0**, não MIT como o repo irmão. Ao migrar página para o `llm-wiki-daedalus`
  (Fase B), a relicença se declara no commit da migração.
