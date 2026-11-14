# Year 2 practice sets — MA203 · EC2A1 · EC2B1 · EC2C1

Unofficial. Written by a student with AI assistance. Not affiliated with LSE, and not produced, checked or endorsed by LSE or any course teacher. Errors are possible.

Site: https://ruiqichenbiec.github.io/lse-y2-practice/

## What is here

- `index.html` — the page: practice sets listed by round, course and chapter.
- `pdf/<course>/<course>-ch<nn>.pdf` — the practice sets, one chapter per teaching week, numbered separately for each course. Problems are numbered `Q<chapter>.<k>`. Each problem is followed by its hints and a full solution. The sets are self-contained: definitions and results they use are stated in the set itself.
- `checks/<course>-ch<nn>/` — the machine checks behind the labels on the page, and `report.md`, a per-part summary.

Only chapters that have gone through every check are published; the others are listed as "in preparation".

## How the checks work

Each part of each problem falls under one of these labels. `checks/<course>-ch<nn>/report.md` lists every part and its check, using short codes: `lean` = statement formally verified, `sympy` = answer recomputed, `numeric` = numerically checked, `reviewed-only` = reviewed by a model only, `na` = definition recall.

| Label | What was checked | What was not checked |
|---|---|---|
| Statement formally verified | The conclusion of that part has a proof that compiles in Lean 4 with Mathlib (`checks/<course>-ch<nn>/Q….lean`). | Each step of the written solution in the PDF. The Lean proof may take a different route. |
| Answer recomputed | An independent SymPy script derives the final value or expression from the problem's data and matches the printed answer (`checks/<course>-ch<nn>/Q….py`). | The wording of the intermediate steps. |
| Numerically checked | The identity holds on random numerical examples. | The general case. |
| Reviewed by a model only | An AI model reviewed the part; there is no machine check (explanations, discussion, diagrams). | — |
| Definition recall | Nothing: the part asks for a definition or a statement from memory. | — |

A second AI model compared every Lean statement and every script with the printed problem, to confirm that what was checked is the problem as printed. No teacher has reviewed this material.

## Reporting an error

Open an issue: https://github.com/ruiqichenbiec/lse-y2-practice/issues — say which course and which problem (for example `MA203 Q2.7(b)`).

## Licence

Practice sets, page, and the problem text quoted at the top of each check file: CC BY-NC-SA 4.0. Everything else under `checks/` (Lean and Python code, reports): MIT. See `LICENSE.md`.
