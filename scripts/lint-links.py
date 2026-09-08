#!/usr/bin/env python3
"""Lint dos links do método — as páginas na raiz e os agentes em claude/agents/.

Rode da raiz do repo:  python3 scripts/lint-links.py
(No Windows use "python" ou "py": a instalação não cria python3.exe.)
Sai com 1 se houver link para arquivo que não existe, âncora para heading que
não existe, ou wikilink que não resolve. Sai com 0 quando tudo resolve.

⚠️ Este script NÃO é o template do plugin design-setup, e a divergência é
deliberada. O template linta *wikilinks* sob `docs/`, cobra `_INDEX.md` por
pasta e põe teto nas três fontes únicas — este repo não tem nenhuma das três
coisas: não tem `docs/` (as páginas moram na raiz), não tem `_INDEX.md` por
decisão (o roteador é o `SCHEMA.md`) e não tem estado de projeto. Rodar o
template aqui imprime **verde tendo verificado zero links**, porque ele procura
uma pasta `docs/` que não existe — e verde é lido como prova. Foi por isso que
ele não veio copiado.

O que este repo tem, e que o template não olha: ~96 links markdown relativos
com âncora. Eles já quebraram de verdade uma vez, na mudança de casa do repo
(commit 86b9d23) — é esse o defeito que este script existe para pegar.

Nada agenda este script: ele roda sob demanda, e depois de qualquer rename,
move ou reescrita de heading.
"""
import io
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
WIKILINK = re.compile(r"!?\[\[([^\]\[]+)\]\]")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
CODE_SPAN = re.compile(r"`+[^`]*`+")  # crase: exemplo de sintaxe, não link
SKIP_DIRS = {".git", ".obsidian", "scripts"}
EXTERNO = ("http://", "https://", "mailto:", "tel:", "#")

# Quebrados deliberados: pares (arquivo, alvo do link). Entrada nova aqui só
# com a justificativa escrita no doc que carrega o link.
DELIBERATE = set()  # CONFIG: pares (arquivo, alvo do link)


def slug(titulo):
    """Âncora no estilo do GitHub: minúscula, espaço vira hífen, acento fica.

    O acento FICA e isso não é detalhe: as âncoras vivas do repo dependem dele
    (`#2-achado-aponta-onde-dói-não-onde-termina`). `isalnum()` do Python é
    unicode-aware, então `ó` e `ã` sobrevivem — normalizar para ASCII aqui
    inventaria quebra em link que funciona.
    """
    t = re.sub(r"`|\*\*|\*|__|~~", "", titulo).strip()
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)  # link dentro do título
    return "".join(c for c in t.lower().replace(" ", "-") if c.isalnum() or c in "-_")


def index(root):
    """Mapeia os .md do repo: caminho relativo → conjunto de âncoras dele."""
    paginas = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for name in filenames:
            if not name.endswith(".md") or name.startswith("."):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, root).replace(os.sep, "/")
            ancoras, in_fence = set(), False
            with io.open(path, encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    if line.lstrip().startswith("```"):
                        in_fence = not in_fence
                        continue
                    if in_fence:
                        continue
                    m = HEADING.match(line)
                    if m:
                        ancoras.add(slug(m.group(2)))
            paginas[rel] = ancoras
    return paginas


def existe(root, alvo):
    """Arquivo apontado por link relativo — com ou sem .md."""
    caminho = os.path.normpath(os.path.join(root, alvo))
    return os.path.exists(caminho) or os.path.exists(caminho + ".md")


def main():
    paginas = index(ROOT)
    quebrados, ancoras_mortas, wiki_quebrados = [], [], []
    contados = ancoras_contadas = 0

    for rel in sorted(paginas):
        path = os.path.join(ROOT, rel)
        base = os.path.dirname(rel)
        in_fence = False
        with io.open(path, encoding="utf-8", errors="replace") as fh:
            for lineno, line in enumerate(fh, 1):
                if line.lstrip().startswith("```"):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                limpa = CODE_SPAN.sub("", line)

                for alvo in MD_LINK.findall(limpa):
                    if alvo.startswith(EXTERNO):
                        continue
                    if (rel, alvo) in DELIBERATE:
                        continue
                    contados += 1
                    arquivo, _, ancora = alvo.partition("#")
                    destino = (
                        os.path.normpath(os.path.join(base, arquivo)).replace(os.sep, "/")
                        if arquivo
                        else rel
                    )
                    if arquivo and not existe(ROOT, destino):
                        quebrados.append((rel, lineno, alvo))
                        continue
                    if not ancora:
                        continue
                    ancoras_contadas += 1
                    # Âncora só se confere quando o destino é .md deste repo:
                    # em binário ou pasta não há heading para conferir.
                    if destino in paginas and ancora not in paginas[destino]:
                        ancoras_mortas.append((rel, lineno, alvo))

                for body in WIKILINK.findall(limpa):
                    alvo = body.replace("\\|", "|").split("|")[0].split("#")[0].strip()
                    if not alvo or (rel, alvo) in DELIBERATE:
                        continue
                    contados += 1
                    if not any(
                        p == alvo or p == alvo + ".md" or p.endswith("/" + alvo + ".md")
                        for p in paginas
                    ):
                        wiki_quebrados.append((rel, lineno, alvo))

    for rel, lineno, alvo in quebrados:
        print("QUEBRADO  %s:%d  →  %s" % (rel, lineno, alvo))
    for rel, lineno, alvo in ancoras_mortas:
        print("ÂNCORA    %s:%d  →  %s  (o heading não existe no destino)" % (rel, lineno, alvo))
    for rel, lineno, alvo in wiki_quebrados:
        print("WIKILINK  %s:%d  →  [[%s]]" % (rel, lineno, alvo))

    if quebrados or ancoras_mortas or wiki_quebrados:
        print(
            "\n%d link(s) para arquivo inexistente, %d âncora(s) morta(s), %d wikilink(s) "
            "quebrado(s) — de %d links conferidos."
            % (len(quebrados), len(ancoras_mortas), len(wiki_quebrados), contados)
        )
        # Um código só, e de propósito: aqui todo achado é defeito introduzido
        # AGORA, não tarefa em curso. O template tem um exit 2 para "fonte acima
        # do teto", que é trabalho de dias; este repo não tem fonte única com
        # teto, então carregar o código 2 seria prescrever o que não se verifica.
        return 1

    print(
        "%d links relativos conferidos, 0 quebrados. Âncoras: %d conferidas, 0 apontando "
        "para heading inexistente." % (contados, ancoras_contadas)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
