# Pele de wireframe
Updated: 2026-08-28

Como o wireframe se **parece**: a escala, a tipografia, a grade, o kit mínimo de peças e as armadilhas
que produzem pixel errado com o build verde. Só a camada visual — o que se **mede** nele é
[verificacao-de-entregavel](verificacao-de-entregavel.md), e o que ele deve **conter** é a spec de tela
do projeto.

> **Capacidade opcional.** Só liga em projeto que constrói wireframe ou layout navegável. Projeto que
> termina em pesquisa e escopo não tem alvo aqui — ver
> [SCHEMA](SCHEMA.md#o-que-vale-em-todo-projeto-e-o-que-depende-de-haver-construção).

As regras vêm de um wireframe navegável de ~26 telas, e os números são medidos, não estimados. O
exemplo de stack é Tailwind v4 + React, mas só o §6 depende disso: a classe de defeito é de qualquer
CSS em camadas.

---

## 1. O princípio, e o que ele proíbe

**O wireframe existe para ser lido como comportamento, não como proposta visual.** No momento em que
ele tem cor de marca, a conversa com o cliente vira *"não gostei desse azul"* e a revisão de estrutura
morre.

Daí a régua central: **nunca cor de marca no wireframe.** Destaque é **peso, tom e traço** — negrito,
um cinza mais escuro, sublinhado, borda. Nada de verde/âmbar/vermelho para estado, nada de gradiente,
nada de hex solto no markup.

**E o low-fi rabiscado também sai.** Fonte manuscrita, tracejado, caixa cinza sem rótulo: parecem
wireframe, mas custam legibilidade e fazem o cliente descontar o que lê — *"é só um rascunho"*. O que
fica é uma **pele tipográfica sóbria com conteúdo real**: escala de cinza, uma família sans,
hierarquia por tamanho e peso. O cliente lê o site; o que ele não vê é uma decisão de marca disfarçada
de wireframe.

🔴 **A exceção declarada: documento que se encaminha ao cliente.** Um resumo executivo em PDF ou HTML
**não é interface** — chega sozinho, sem a moldura que o contextualiza, e a marca é o que diz de quem
ele é. Ali a paleta oficial entra. A régua vale para o **protótipo** e para a **casca** que o
hospeda; não para a peça que viaja.

⚠️ **Sem tema escuro.** Uma escala só. Variante escura num wireframe dobra a superfície de erro de
contraste, dobra o custo de cada tela nova e não responde nenhuma pergunta do cliente.

---

## 2. A escala

Cinza-azulada, 10 tons. É a paleta canônica: nenhum cinza fora dela.

```
F0F4F8   E9EDF2   D7DCE0   C3CAD4   939BAE   646E82   454F62   2E3646   252B37   1E232E
```

**A página é branca** — o fundo mais leve possível. A escala entra nas **superfícies rebaixadas** e
nas **linhas**, nunca no fundo geral.

```css
:root {
  --canvas:         #ffffff;   /* fundo da página */
  --surface:        #ffffff;   /* card, caixa que sobe */
  --surface-sunken: #f0f4f8;   /* faixa alternada, thead, blockquote, placeholder */
  --ink:            #1e232e;   /* título, texto forte */
  --ink-soft:       #2e3646;   /* corpo de texto */
  --ink-faint:      #646e82;   /* metadado, eyebrow, legenda */
  --line:           #d7dce0;   /* borda padrão */
  --line-strong:    #c3cad4;   /* borda que precisa aparecer */
  --realce:         #1e232e;   /* link, foco, item ativo — tom, não cor */
  --realce-suave:   #e9edf2;

  --coluna-leitura: 680px;
}
```

**Contraste medido — o número que decide onde o texto fraco pode pousar:**

| Fundo | `--ink-faint` sobre ele | Veredito |
|---|---|---|
| `--canvas` (#ffffff) | 5,13:1 | ✅ |
| `--surface-sunken` (#f0f4f8) | **4,64:1** | ✅ AA |
| `--realce-suave` (#e9edf2) | **4,36:1** | 🔴 reprova |

⚠️ **É por isso que o rebaixado é `F0F4F8` e não o tom seguinte.** Escurecer a superfície rebaixada um
degrau derruba **todo metadado da página** abaixo de AA de uma vez, e nada no build avisa. Se a escala
mudar, este é o par que se remede primeiro.

### Selos: tom e forma, nunca semáforo

```css
--selo-forte-bg: #2e3646;  --selo-forte-ink: #f0f4f8;
--selo-medio-bg: #d7dce0;  --selo-medio-ink: #1e232e;
--selo-contorno-ink: #454f62;
```

**Selo é sempre texto.** Um estado que muda o que o item promete — *esgotado*, *inscrições abertas*,
*já realizado* — tem de existir para quem não distingue cor e para quem lê por leitor de tela. A
escala cinza já força isso; mantenha a régua mesmo quando houver cor.

### 🔴 A armadilha de nome de token

**Se o sistema de UI que o projeto usa já tem um token com esse nome, o nome está queimado.**

O caso: o destaque da casca chamava-se `--accent`, o kit de componentes declara `--accent` em `:root`,
os dois arquivos são importados no mesmo documento e **quem vem depois vence**. O destaque resolveu
para um cinza quase branco. **Todo link de conteúdo, o item ativo da navegação e o anel de foco
ficaram em 1,09:1 sobre branco, com o build passando verde.**

**Solução por construção: prefixo em outra língua.** `--realce`, `--selo-*`, `--linha-*`. Os selos
nunca tiveram o problema justamente por isso.

A mesma família de defeito no eixo global: **regra nova que toque `html`, `body` ou `:root` precisa de
escopo de pele** (`html:has([data-skin="…"])`). Sem escopo ela vaza para a outra pele, e o sintoma só
aparece medindo o estilo computado — não no build, não no lint.

---

## 3. Tipografia

**Uma família só.** Sans do sistema ou uma neutra de projeto. Sem fonte de display, sem segunda
família para títulos: a variação é tamanho, peso e cor.

| Papel | Tamanho | Peso | Cor |
|---|---|---|---|
| `h1` do herói | 1,875rem → 3rem no wide | 600 | `ink` |
| Promessa (linha sob o `h1`) | 1,125rem → 1,25rem | 400 | `ink` |
| `h2` de bloco | 1,25rem → 1,5rem | 600 | `ink` |
| Eyebrow (rótulo curto acima do título) | 0,75rem, caixa alta, `tracking` largo | 600 | `ink-faint` |
| Apoio do bloco | 0,875rem | 400 | `ink-soft` |
| `h3` de card | 1rem | 600 | `ink` |
| Corpo | 1rem, entrelinha 1,7 | 400 | `ink-soft` |
| Metadado, legenda | 0,75rem | 400/500 | `ink-faint` |

**Título ganha `tracking` apertado; eyebrow ganha `tracking` largo.** É o par que separa os dois
papéis sem usar cor.

### A coluna de leitura: 680px, medida

Era 720px. Com o corpo em ~19px a linha dava **92,7 caracteres** — teto prático ~85. Medido com
`measureText` no estilo real, não estimado por `ch`:

| Coluna | Corpo 19px | Texto de aprofundamento 21px |
|---|---|---|
| 720 | 83,6 | 77,7 ← colado no teto |
| 700 | 81,3 | 75,5 |
| **680** | **79,0** | **73,3** ← escolhido |
| 660 | 76,7 | 71,2 ← estreita demais para o ganho |

Em 680 o corpo fecha em 79 (faixa boa, com folga) e o texto maior em 73 (faixa *confortável*, 45–75) —
a hierarquia sai de graça: o especial lê melhor que o comum, que é o que a variante promete. Custo:
+1,4% de altura de página, e **zero no mobile**, porque o teto só existe do breakpoint largo para
cima.

⚠️ **O valor mora num token, nunca escrito à mão na tela.** Dois consumidores do mesmo valor de
leitura em dois literais é como eles divergem na primeira correção. E **não mantenha um segundo
mecanismo em paralelo** (`max-w-prose` e afins): dois tokens de coluna concorrentes é o defeito, não a
solução — apareceu quando uma onda de nove telas nasceu sem herdar a peça.

### Hierarquia por proximidade, não por enfeite

Um `h3` a 2px do corpo (18 contra 16), separado só por peso, lê como parágrafo em negrito. O conserto
barato é **mais respiro acima e menos abaixo**: é o que diz *"este título pertence à seção de cima e
manda no que vem embaixo"* — o sinal mais forte de hierarquia, e o mais barato.

E **um device por elemento**: se o `h2` já usa filete (borda no topo) e o `blockquote` usa barra
lateral, o `h3` não ganha filete lateral. Dois elementos com barra competem.

---

## 4. A grade

**Contêiner de 1200px, faixa full-bleed por fora.** O arranjo é sempre o mesmo: `<section>` full-bleed
com a cor de fundo → contêiner centrado dentro → conteúdo. **A faixa atravessa a viewport; só o
conteúdo afunila.**

O erro que isso corrige não é ter coluna estreita — coluna estreita é acerto para texto corrido. O
erro é a **faixa** ser estreita junto: a página perde a borda que atravessa, o fundo alternado e o
alinhamento com cabeçalho e rodapé.

⚠️ **A tela usa um fragmento na raiz, não um `<div>` com largura** — qualquer wrapper com largura
máxima estrangula as faixas e o breadcrumb.

**Ritmo vertical:**

| Bloco | Padding |
|---|---|
| Herói | 3,5rem → 5rem no wide |
| Seção de conteúdo | 3rem → 4rem no wide |
| Bloco dentro de coluna (layout de 2 colunas) | 2,5rem + borda de topo |

**Separação entre blocos vizinhos: alternar `canvas` / `sunken`** — não borda dupla, não linha
decorativa. ⚠️ **Dentro de uma coluna estreita as faixas alternadas somem**: viram retângulo cinza
solto ao lado de um trilho branco. Ali a separação é a linha de topo. É divergência declarada, e o
motivo é o trabalho de cada tela — uma home apresenta assuntos lado a lado; uma página de produto
acompanha uma decisão, com algo fixo ao lado.

**Grade de itens — o que de fato se repete (33 ocorrências do primeiro caso):**

```
gap 1rem  ·  2 colunas a partir de sm      /* cards, o caso comum        */
gap 1rem  ·  3 colunas a partir de lg      /* três destaques             */
gap 0,75rem · 2 → 4 colunas                /* selos, itens curtos        */
```

**Raio: 0,25rem para tudo** — card, botão, caixa. Raio maior lê como UI acabada, que é a leitura que o
wireframe não quer.

**Foco visível, sempre:**

```css
:focus-visible { outline: 2px solid var(--realce); outline-offset: 2px; border-radius: 2px; }
```

---

## 5. O kit mínimo — nove peças

O erro que custa mais caro no meio do caminho é **não ter peça e deixar o padrão para a disciplina de
quem constrói.**

A medição: o literal do contêiner apareceu **35 vezes** no projeto — cabeçalho e rodapé inclusos — e o
arranjo de herói foi copiado **17 vezes** à mão. **Não havia peça para herdar**, e foi exatamente por
isso que uma onda de nove telas novas nasceu com a largura errada e com um segundo token de coluna de
leitura. Peça faltando não produz erro: produz cópia divergente.

**Construa estas nove antes da segunda tela.**

| Peça | O que é | A régua que ela carrega |
|---|---|---|
| `Heroi` | faixa de abertura, `<h1>` | o `<h1>` mora aqui e em nenhum outro lugar; o eyebrow é `<p>`, fora do heading |
| `Secao` | invólucro de todo bloco, `<h2>` | **bloco vazio não renderiza** |
| `Medida` | a coluna de leitura dentro da faixa larga | consome o token, não um literal |
| `Faixa` | o contêiner sem herói nem título | para paginação e chrome |
| `Card` | item de lista | o **link é o título**, não o card |
| `ImagemPlaceholder` | espaço reservado de imagem | rótulo e proporção **obrigatórios** |
| `Migalha` | breadcrumb + `BreadcrumbList` | markup e dado estruturado saem do **mesmo array** |
| `Prova` | credencial ou número com fonte | sem ano **ou** sem fonte ⇒ o item não renderiza |
| `AcaoPrimaria` | o CTA | o rótulo segue o **estado do dado**, não o tipo do produto |

### 5.1 `Secao` — a régua que ela torna impossível quebrar

**"Bloco com título e sem conteúdo não renderiza."** O defeito que ela mata é o **rótulo órfão**:
título com nada embaixo, *em breve*, placeholder. Numa revisão de arquitetura, rótulo órfão é ruído
que o cliente lê como promessa.

⚠️ **O guarda é uma prop explícita, não `!children`.** `children` vindo de um `.map()` sobre array
vazio é `[]`, que é **truthy** — testar `children` renderiza o título com o nada embaixo, que é
exatamente o defeito. Contrato se cumpre no **valor**, não no tipo. E quem decide é quem chama, porque
só quem chama sabe o que "vazio" significa ali.

```jsx
function Secao({ id, eyebrow, titulo, apoio, vazio = false, fundo = "canvas", acao, children }) {
  if (vazio) return null;
  return (
    <section id={id} aria-labelledby={`${id}-titulo`}
             className={fundo === "sunken" ? "bg-sunken" : "bg-canvas"}>
      <div className="mx-auto max-w-[1200px] px-4 py-12 lg:px-6 lg:py-16">
        <div className="flex flex-wrap items-end justify-between gap-x-6 gap-y-2">
          <div>
            {eyebrow && <p className="mb-2 text-xs font-semibold uppercase tracking-widest
                                      text-ink-faint">{eyebrow}</p>}
            <h2 id={`${id}-titulo`}
                className="text-xl font-semibold tracking-tight text-ink lg:text-2xl">{titulo}</h2>
            {apoio && <p className="mt-1.5 max-w-2xl text-sm text-ink-soft">{apoio}</p>}
          </div>
          {acao}
        </div>
        <div className="mt-8">{children}</div>
      </div>
    </section>
  );
}
```

⚠️ **`aria-labelledby` apontando para o `<h2>`, nunca `aria-label`.** Uma `<section>` com heading
visível e `aria-label` tem dois nomes para a mesma região, e eles divergem na primeira edição.

⚠️ **O eyebrow fica FORA do `<h2>`.** Dentro, o nome acessível da região vira *"Educação Comece pelo
nível certo"* — o rótulo curto colado no título, anunciado a cada entrada na região. Fora, ele é
visual para quem vê e silencioso para quem ouve.

⚠️ **A cor de fundo é ternário, nunca duas classes do mesmo eixo na string.** Ver §6.3.

### 5.2 `Card` — o card inteiro não é link

Card-inteiro-clicável quebra três coisas de uma vez: o nome acessível do link vira o parágrafo
inteiro, o texto de dentro deixa de ser selecionável, e link dentro de link é HTML inválido —
*controle dentro de controle*.

**O link é o título, e o alvo de toque não sofre:**

```jsx
<article className="relative flex h-full flex-col rounded border border-line bg-surface p-5
                    transition-colors hover:border-line-strong">
  <h3 className="text-base font-semibold text-ink">
    <a href={rota} className="underline-offset-2 hover:underline after:absolute after:inset-0">
      {titulo}
    </a>
  </h3>
  {resumo && <p className="mt-2 text-sm text-ink-soft">{resumo}</p>}
  {metadados?.length > 0 && (
    <ul className="mt-4 flex flex-wrap gap-x-3 gap-y-1 text-xs text-ink-faint">
      {metadados.map((m) => (
        <li key={m} className="after:ml-3 after:text-line-strong after:content-['·']
                               last:after:content-['']">{m}</li>
      ))}
    </ul>
  )}
</article>
```

O pseudo-elemento absoluto sobre o card inteiro estende a **área clicável** sem estender o **nome
acessível**. O `relative` no `<article>` ancora isso, e o anel de foco fica no link — que é o que
realmente recebeu foco.

**Destino que ainda não existe: o item renderiza completo e SEM link**, com aviso visível. As duas
alternativas são piores — sumir com o item esconde conteúdo que existe, e linkar entrega um 404 a quem
clicou. É o par visual do 404 na rota: o card impede o clique, a rota impede o endereço colado.

⚠️ **Aviso que é estado do ambiente de revisão, e não do site, leva um atributo que o marque** — sem
isso ele entra nas medições de densidade como conteúdo do cliente.

### 5.3 `ImagemPlaceholder` — a decisão que quase ninguém acerta de primeira

**Fundo e borda dependem de sobre o que ele está:**

| Contexto | Fundo | Borda | Por quê |
|---|---|---|---|
| Sobre superfície rebaixada (slot no herói) | `surface` | sólida | precisa **subir** |
| Sobre a página branca, ou dentro de card | `sunken` | `line-strong` | precisa **afundar** |

Três precedentes contraditórios apareceram no mesmo projeto antes de a peça existir, e a contradição
era **legítima** — é a regra acima. Sem a peça, o quarto lugar inventa um quarto vocabulário.

**Duas props obrigatórias, sem default:**

1. **`rotulo`** — num wireframe o placeholder tem de **se anunciar como placeholder**. Caixa cinza sem
   rótulo lê como foto que não carregou, que é um defeito de site real.
2. **`proporcao`** — `aspect-ratio` **zera CLS por construção**. Reservar a caixa é requisito, não
   estética; default silencioso aqui é o mesmo que não ter.

```jsx
<div role="img" aria-label={`${rotulo} — espaço reservado, a arte entra na fase de UI`}
     className="flex items-end rounded border border-line-strong bg-sunken p-3 aspect-[16/9]">
  <p aria-hidden="true" className="text-xs font-medium text-ink-faint">{rotulo}</p>
</div>
```

🔴 **A régua não é "wireframe sem imagem": é "foto que não é dado é decoração que finge ser
conteúdo".** A distinção é se a imagem é **campo na fonte**. O post tem capa e o evento tem banner —
reservar o espaço deles mostra o peso real da página. A pessoa não tem campo de foto no cadastro: ali
continua sem, e nada nesta peça autoriza o contrário.

⚠️ **Rótulo fraco sobre a superfície `realce-suave` é proibido** — 4,36:1 (§2).

### 5.4 `AcaoPrimaria` — o CTA é um, e o rótulo segue o dado

```jsx
<a href="#interesse" className="inline-flex min-h-11 items-center rounded bg-ink px-6 text-sm
                                font-semibold text-canvas hover:opacity-90">{texto}</a>
```

`min-h-11` (44px) é o alvo de toque. **`<a>` para uma âncora na própria página, não `<button>`:**
funciona sem JS, é anunciado como link e entra na ordem de tabulação sozinho — o que uma `<div>`
estilizada de botão não faz, e era o que existia antes.

**A precedência do rótulo é pelo estado do dado, nunca pelo tipo do produto:** nenhuma oferta aberta →
*avise-me quando abrir* · sem preço → *solicitar proposta* · caso contrário → o rótulo do nível. O
texto de "não dá para se inscrever agora" é o mesmo para o produto caro e para o barato.

---

## 6. Armadilhas de camada

CSS-first, sem arquivo de config: a configuração são blocos de tema no próprio CSS. Isso muda quem
vence. **Nenhuma das quatro quebra build, lint ou checagem de tipo** — as quatro produzem pixel errado
com tudo verde, e três apareceram na mesma sessão.

1. **Regra de estado fora da camada base vence variante responsiva.** Um seletor de atributo +
   classe é (0,2,0) e bate o utilitário responsivo (0,1,0): o botão de menu aparecia **no desktop**,
   ao lado da navegação inteira. **Regra de estado — tem JS, tem tema, gaveta aberta — vai dentro da
   camada base**, para utilitário vencer por ordem de camada e o responsivo voltar a mandar.

2. **E o inverso morde igual: utilitário vence a camada base.** Um `flex` na string de classes anula
   o `display: none` declarado na base, e as duas variantes do mesmo componente aparecem juntas.
   **Se o `display` é decidido por classe de estado, não ponha utilitário de display no elemento.**

3. **Duas utilities do mesmo eixo na mesma string são resolvidas pela ordem no CSS, não na string.**
   Fundo claro + fundo escuro juntos não dão erro — dão a cor errada. Aparece ao expandir um
   utilitário composto sobre um override. **Ternário sempre.**

4. **Ler o estilo computado no mesmo tick em que a cor muda devolve o valor antigo** em qualquer
   elemento com transição de cor. Já custou um diagnóstico errado — *"o token não vira"* num card que
   virava. Meça depois da transição, ou tire a transição antes de medir.

**E as âncoras:** desconte o chrome com **`scroll-padding-top` no `html`** — um valor, um lugar —,
nunca com `scroll-margin-top` em cada heading. Com os dois valendo eles **somam**, e a âncora aterrissa
ao dobro da folga: medido em 240px de deslocamento para um chrome de 105px. O desconto é a soma de
todas as barras grudadas, não de uma; quando duas deixam de se sobrepor, um valor fixo que "funcionava"
passa a errar por acidente.

---

## 7. Checklist visual de tela

Passa/falha, com número medido — não impressão. Complementa a lista de
[verificacao-de-entregavel](verificacao-de-entregavel.md), que cobre densidade, dobra e conteúdo de
exemplo.

- [ ] **Zero cor de marca.** Nenhum hex fora da escala, nenhum gradiente, nenhum semáforo.
- [ ] **Todo texto passa AA** — com atenção ao texto fraco sobre superfície rebaixada.
- [ ] **Um `<h1>` por página**, no herói, e hierarquia de heading sem pulo.
- [ ] **Um `banner`, um `main`, um `contentinfo`, uma marca** por página.
- [ ] **Todo bloco com imagem ou embed tem dimensão reservada** — CLS zero por construção.
- [ ] **Todo placeholder tem rótulo em texto.**
- [ ] **Nenhum bloco com título e sem conteúdo.**
- [ ] **Nenhum estado comunicado só por cor.**
- [ ] **Alvo de toque ≥ 44px** em todo controle.
- [ ] **`Tab` uma vez e olhar**: o atalho de salto aparece, e não atrás de chrome grudado.
- [ ] **Sem JavaScript a página continua legível** — abas abertas, navegação como lista, formulário
      com destino.
- [ ] **A página não rola na horizontal** na menor largura; tabela rola dentro do próprio wrapper.
- [ ] **Nenhuma string de classes com duas utilities do mesmo eixo.**

---

## 8. Ordem de construção

1. **Tokens e tema** — a escala, os semânticos, a coluna de leitura. Antes de qualquer tela.
2. **A moldura global** — cabeçalho, rodapé, atalhos de salto, `main`. É onde os landmarks nascem, e
   onde a altura do chrome vira variável (§6).
3. **As nove peças do §5.** Não pule: elas existem para a *segunda* tela, e a segunda tela sempre vem.
4. **Uma tela de referência, completa** — a mais densa do projeto. O que se decide nela vira o default
   das ondas seguintes, então ela se revisa antes de escalar.
5. **As demais telas, compondo.** Se uma tela precisa de markup novo, a primeira pergunta é se não é
   peça faltando.

---

← [SCHEMA](SCHEMA.md) · [verificacao-de-entregavel](verificacao-de-entregavel.md) ·
[fases-e-agentes](fases-e-agentes.md)
