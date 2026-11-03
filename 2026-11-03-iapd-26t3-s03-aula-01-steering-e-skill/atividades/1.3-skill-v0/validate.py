#!/usr/bin/env python3
"""Valida o frontmatter de um ou mais SKILL.md contra a spec Agent Skills (agentskills.io).

Uso: python validate.py caminho/da/skill [outra/skill ...]
     python validate.py --all <pasta-com-skills>/suite-referencia

Regras checadas:
- frontmatter YAML delimitado por --- na primeira linha
- name: obrigatório, 1 a 64 caracteres, só [a-z0-9-], sem começar/terminar com hífen,
  sem hífens consecutivos, igual ao nome da pasta
- description: obrigatório, 1 a 1024 caracteres
- compatibility: opcional, até 500 caracteres
- metadata: opcional, mapa chave: valor com valores string
- license, allowed-tools: opcionais
- aviso se o corpo passar de 500 linhas
Sai com código 1 se alguma skill for inválida.
"""
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
CONHECIDOS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}


def parse_frontmatter(text: str):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "frontmatter ausente: a primeira linha deve ser ---"
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None, "frontmatter não fechado com ---"
    fm: dict = {}
    mode, cur = None, None          # mode: None | "map" | "fold"
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):   # vazio ou comentário YAML
            continue
        if raw.startswith(" ") and mode:
            if mode == "map":
                k, _, v = raw.strip().partition(":")
                fm[cur][k.strip()] = v.strip().strip('"').strip("'")
            else:
                fm[cur] = (fm[cur] + " " + raw.strip()).strip()
            continue
        mode = None
        k, sep, v = raw.partition(":")
        if not sep:
            return None, f"linha inválida no frontmatter: {raw!r}"
        k, v = k.strip(), v.strip()
        if v in {"", ">", ">-", "|", "|-"}:
            cur = k
            if k == "metadata":
                mode, fm[k] = "map", {}
            else:
                mode, fm[k] = "fold", ""
            continue
        fm[k] = v.strip('"').strip("'")
    body = "\n".join(lines[end + 1:])
    return (fm, body), None


def validate_skill(path: Path) -> list[str]:
    errors = []
    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        return [f"{path}: SKILL.md não encontrado"]
    parsed, err = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    if err:
        return [f"{path}: {err}"]
    fm, body = parsed
    name = fm.get("name")
    if not name:
        errors.append("name ausente")
    else:
        if not 1 <= len(name) <= 64:
            errors.append(f"name com {len(name)} caracteres (limite 64)")
        if not NAME_RE.match(name):
            errors.append(f"name '{name}' fora de [a-z0-9-] ou com hífen mal posicionado")
        if name != path.name:
            errors.append(f"name '{name}' diferente do nome da pasta '{path.name}'")
    desc = fm.get("description")
    if not desc:
        errors.append("description ausente")
    elif not 1 <= len(desc) <= 1024:
        errors.append(f"description com {len(desc)} caracteres (limite 1024)")
    comp = fm.get("compatibility")
    if comp and len(comp) > 500:
        errors.append(f"compatibility com {len(comp)} caracteres (limite 500)")
    meta = fm.get("metadata")
    if meta is not None:
        if not isinstance(meta, dict):
            errors.append("metadata deve ser um mapa chave: valor")
        else:
            for k, v in meta.items():
                if not isinstance(v, str) or not v:
                    errors.append(f"metadata.{k} deve ser string não vazia")
    extras = set(fm) - CONHECIDOS
    if extras:
        print(f"  aviso: campos fora da spec (ignorados por outros agentes): {sorted(extras)}")
    n_lines = len(body.splitlines())
    if n_lines > 500:
        print(f"  aviso: corpo com {n_lines} linhas (recomendado < 500)")
    return [f"{path}: {e}" for e in errors]


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    paths = []
    if args[0] == "--all":
        for root in args[1:]:
            paths += sorted(p.parent for p in Path(root).rglob("SKILL.md"))
    else:
        paths = [Path(a) for a in args]
    failed = 0
    for p in paths:
        print(f"[{p}]")
        errs = validate_skill(p)
        if errs:
            failed += 1
            for e in errs:
                print("  ERRO:", e.split(": ", 1)[1])
        else:
            print("  OK")
    print(f"\n{len(paths) - failed}/{len(paths)} skills válidas")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
