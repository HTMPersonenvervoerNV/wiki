# Groeperen alle maatregelen in 1 bestand

```bash
ls -1 | sort -n | while read i; do echo "[Maatregel" `basename $i .md`"](maatregelen/$i)"; done > ../winter2016.md
```
