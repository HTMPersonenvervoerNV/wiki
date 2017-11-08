# Groeperen alle maatregelen in 1 bestand

```bash
cd maatregelen; ls -1 | sort -n | while read i; do echo "[Maatregel" `basename $i .md`"]($i)"; done > index.md
```
