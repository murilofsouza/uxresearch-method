# Verificação de entregável
Updated: 2026-08-25

Como se **confere** um entregável construído — wireframe, protótipo, tela. Não é sobre a documentação
nem sobre a camada do cliente: é o que a spec pode prometer e o que só a coisa construída responde.

Estas regras estavam enterradas numa página de convenções de front-end, entre gotchas de framework. São
método: valem para qualquer stack.

> **O *como* medir é do stack** (subir o build, qual ferramenta) e mora na wiki do cliente. Aqui está
> **o que** se mede, **o que invalida a medição** e **o que não se contorna**.

**Quase tudo aqui vale para qualquer coisa construída** — inclusive um layout que é o entregável
final, sem produto depois. As exceções são **discriminador** e **estado global**, que são regras de
código: num projeto que entrega layout elas não têm alvo, e o que não tem alvo se remove. *(A lista se
nomeia, não se conta: "as quatro primeiras" apodrece na primeira regra que entra no meio.)* A página
inteira **não se aplica** a projeto que termina em pesquisa e escopo — ver
[SCHEMA](SCHEMA.md#o-que-vale-em-todo-projeto-e-o-que-depende-de-haver-construção).

**Se o construído é descartável, isto continua valendo e a verificação de drift não.** Medir densidade
e dobra é o que dá valor ao descartável — é para isso que ele existe. Hashear spec contra código que vai
ser jogado fora, não. Ver
[fases-e-agentes](fases-e-agentes.md#e-declare-se-o-construído-sobrevive-ao-projeto).

## O que trava a medição não se contorna — se remove

Se existe qualquer coisa entre o construído e o navegador, **ela é dívida de método, não
inconveniência**: um método que mede em vez de presumir para de medir quando medir dá trabalho.

O caso: o entregável ficava atrás de um **gate de senha**, que rodava também no servidor de
desenvolvimento. A wiki do projeto documentava **dois contornos** — servir o HTML pré-renderizado do
build num estático, e subir o servidor de produção com um segredo de sessão descartável para assinar o
cookie do gate. Os dois funcionavam, e ficaram escritos como procedimento por semanas.

**O tell de que era contorno e não solução:** o procedimento pedia **manipular segredo de sessão para
medir a altura de uma página**. Quando a saída "barata" exige tocar em credencial, quase sempre existe
uma mais barata que não exige.

A solução foi uma linha — o gate deixou de rodar em modo desenvolvimento, e só ele; qualquer build
deployado continua atrás da senha, com uma variável para religar. **O que ela custou até ser
escrita:** uma rodada de validação inteira fechou com **três números marcados "remedir"**, porque a
medição dependia de alguém digitar senha, e a propagação desses três números para os documentos que os
citam teve de ser refeita depois.

**A regra, generalizada:** proteção de acesso, dado de fixture, ambiente que só sobe com credencial de
terceiro — tudo isso é legítimo em produção e **candidato a desligar em desenvolvimento**, porque em
`localhost` a ameaça que justificava a proteção não existe. O gate protege contra a internet; não há
internet chegando na sua máquina.

## Densidade não se valida em texto

**Estrutura e escopo fecham em Markdown; densidade percebida só no HTML renderizado.** O orçamento de
primeira dobra parte das **alturas medidas** na página construída, no viewport real do público, com
folga declarada — nunca do diagrama ASCII.

**E calibrar por padding é proibido.** Se o orçamento só fecha raspando 2 px de espaçamento, **o alvo
está errado** — o número foi ajustado para caber, o que o torna inútil como régua. O padding é a última
coisa que se mexe, não a primeira.

## Conteúdo de exemplo plausível, nunca lorem ipsum

Título curto demais **mente a favor** do layout; longo demais, contra. Texto de exemplo tem de vir do
domínio real — nomes, lugares e comprimentos que o produto vai receber.

Corolário: **reticências ficam proibidas** (alinham destruindo informação) e **limite rígido de
caracteres no painel também** — briga com quem publica em dia de fechamento. Contador, se entrar, é
orientação.

**Se o produto já existe, o conteúdo de exemplo é o conteúdo publicado dele** — título real, foto
real, comprimento real, na proporção real de tema. Inventar plausível quando o publicado está a uma
leitura de distância troca a régua por uma estimativa, e é o publicado que o cliente reconhece na
apresentação. Duas notas de campo: o que responde `403` para linha de comando costuma abrir num
navegador de verdade, e imagem de lista quase sempre chega em atributo de *lazy load*, não no `src`.

⚠️ **Mas conteúdo publicado carrega data, e data envelhece na peça.** Se o card não exibe data, a
idade do texto não vaza e a escolha é livre; se exibe, ou o recorte é recente ou a peça mente. Confira
qual dos dois é o caso **antes** de escolher os itens, não depois de preencher.

## A resposta da ferramenta não é prova — a prova é a peça exportada

> Dono: `UX`

Preencher conteúdo **fora do navegador** — layout dirigido por automação numa ferramenta de design —
tem uma classe de falha que a página construída não tem: a escrita **reporta sucesso e não muda nada**.
Num único bloco de quatro cards, três formas apareceram na mesma sessão:

- **texto exposto como propriedade do componente** não se escreve no nó de texto; e o inverso também é
  verdade — texto que *não* é propriedade só aceita a escrita no nó. As duas trocadas retornam sucesso;
- **preenchimento de imagem que não alcança filho de instância** — a imagem sobe, o identificador dela
  volta preenchido, e a aplicação acontece em **zero nós**;
- **variante que renderiza invisível** — rótulo branco em card branco: o conteúdo entrou, ninguém vê.

**A regra:** depois de escrever, **exporte a peça e olhe**. Retorno de ferramenta, contagem de nós
tocados e ausência de erro no console **não são prova de pixel** — é a mesma tese do critério de aceite
que passa por inspeção e nunca por execução, um andar antes. Um bloco preenchido às cegas passa em
qualquer revisão que só leia o log.

**E rótulo invisível é variante, não conteúdo.** A tentação é corrigir a cor ali mesmo; o jeito de
decidir sem inventar design é **copiar a peça irmã que a mesma tela já usa** — se um chip equivalente
existe em outro bloco, a variante dele é a resposta, e a divergência entre os dois é que era o defeito.

## Recorte sem interseção é regra de conteúdo — e não se herda de camada para camada

> Dono: `UX`

Quando duas peças da mesma tela bebem da mesma lista, o recorte de cada uma **não pode se cruzar**: sem
isso a tela mostra o mesmo item duas vezes e a contagem de conteúdo infla. Isso já estava resolvido — e
voltou a acontecer quando a mesma tela foi reconstruída na camada seguinte, porque a regra vivia num
**comentário de código da camada descartável**. O comentário não viaja; o conteúdo, sim.

O resultado passou por revisão: dois cards do mesmo bloco com **nome, chapéu, título e foto idênticos**,
na tela que o cliente lê.

**Onde a regra mora:** junto do conteúdo — no doc que lista o conteúdo de exemplo —, nunca só na
camada que vai ser jogada fora
([fases-e-agentes](fases-e-agentes.md#e-declare-se-o-construído-sobrevive-ao-projeto)).
**Como se confere:** dois títulos iguais na mesma tela é defeito, e a varredura é literalmente essa. É
mais barata que a revisão que a deixou passar.

## Variante que muda de forma por breakpoint não aparece no ASCII

Um card que vira horizontal no mobile é **economia certa** numa faixa de 18 itens e **defeito** onde a
imagem é o argumento. As duas decisões parecem idênticas no diagrama. **Só a régua na página construída
pega.**

## Tipo novo é variante do template, não tela nova

Três tipos de arquivo diferentes saíram **do mesmo conjunto de componentes** — o que muda é quais
módulos têm dado.

**E componente novo ali é sinal de premissa errada, não de necessidade.** Das três variantes, a única
mudança em componente compartilhado foi **um rótulo opcional**. Quando a variante pede componente novo, o
que está errado costuma ser a premissa de que ela é uma tela.

Consequência prática no rastreio: **a variante não ganha arquivo, ganha linha** — ver
[fases-e-agentes](fases-e-agentes.md).

## Discriminador com um só valor é convite à regressão

Um `TipoMidia = "video" | "podcast"` sobreviveu a **três remodelagens do produto** porque "custa nada
deixar" — e cada rodada conservadora trouxe o `podcast` de volta, **com rota, copy e template**. O tipo
não era extensibilidade: era um convite escrito no código.

**Quando o segundo valor morre, o tipo morre com ele.** Se um dia houver outro, ele nasce como entidade
nova, não como string reaproveitada. Vale igualmente para taxonomia, tipo de conteúdo no CMS e union de
TypeScript.

## Um estado global, uma fonte — e uma implementação da peça que o mostra

O selo de "ao vivo" tinha **três implementações** (duas pastilhas inline e um componente) e **duas fontes
de verdade**: a tela lia a query string, a faixa e o cabeçalho liam um booleano fixo. Efeito:
`?estado=offline` **não apagava a faixa**.

E o ponto que generaliza:

> **Critério de aceite que passa por inspeção de código e nunca por verificação não é exercitável.**

O critério exigia que a faixa desaparecesse. Ele "passava" quando alguém lia o código e concluía que
passaria. Nunca foi executado, porque não *podia* ser.

**Estado que atravessa superfícies é lido do dado pelo próprio componente**, não recebido por prop de
cada tela. Uma fonte, uma implementação da peça — e aí o critério vira comando.

## Checklist

Antes de dar um entregável por conferido:

- [ ] densidade medida no **construído**, no viewport do público, sem calibrar por padding
- [ ] conteúdo de exemplo do domínio real — **o publicado, se o produto já existe**
- [ ] nenhum item repetido entre dois blocos da mesma tela (dois títulos iguais é defeito)
- [ ] o que foi preenchido por automação **conferido na peça exportada**, não no retorno da ferramenta
- [ ] cada variante de breakpoint aberta na régua, não só no ASCII
- [ ] nenhum componente novo entrou por causa de variante
- [ ] nenhum discriminador com um valor só
- [ ] todo critério de aceite **executável** — existe um passo que o faz falhar
- [ ] **nada entre o construído e o navegador** — nenhum passo de medição pede senha ou segredo

---

← [SCHEMA](SCHEMA.md) · [fases-e-agentes](fases-e-agentes.md) · [fonte-canonica](fonte-canonica.md)
