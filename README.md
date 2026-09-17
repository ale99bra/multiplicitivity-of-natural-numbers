# Multiplicitivity of Natural Numbers

**Author:** Alessio Branda

## Abstract

We investigate the structural patterns formed by divisibility over finite sets of initial prime numbers. We define a discrete invariant, *multiplicitivity* µ(n), which counts how many fundamental primes from a fixed set divide n. Focusing on the set {2, 3, 5, 7} (with primorial 210), multiplicitivity partitions the natural numbers into six classes: Unico, Monome, Duome, Triome, Quadrome, and Pentanome. We prove this partition is strictly periodic with period 210 and exhibits reflection symmetry centered at 105. We then generalize the framework to the k-th primorial and connect it to the classical restricted prime-omega function.

→ [Read the paper (PDF)](releases/multiplicitivity.pdf) ←

## Repository structure

```
.
├── paper/
│   ├── main.tex          # paper source
│   ├── references.bib    # bibliography
│   └── figures/          # generated figures used in the paper
├── scripts/
│   └── generate_figures.py   # regenerates all figures in paper/figures
├── releases/
│   └── multiplicitivity.pdf  # pre-built PDF
└── README.md
```

## Building the paper

From `paper/`:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Regenerating the figures

From `scripts/`:

```bash
pip install -r requirements.txt
python generate_figures.py
```

This writes all five figures into `paper/figures/`, overwriting the existing ones.

## Citing this work

```bibtex
@misc{branda2026multiplicitivity,
  author = {Branda, Alessio},
  title  = {Multiplicitivity of Natural Numbers},
  year   = {2026},
  note   = {\url{https://github.com/ale99bra/multiplicitivity-of-natural-numbers}}
}
```

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](./LICENSE) (CC BY 4.0).
