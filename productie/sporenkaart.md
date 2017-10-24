# Productie Sporenkaart

1. Ontvangen SVG bestand Roland
2. Converteren TTF lettertypes naar WOFF formaat
3. Plaats lettertype in map fonts
4. Wijzigen header SVG bestand; hoogte en breedte aanpassen, `<style>` toevoegen.
```
<?xml version="1.0" encoding="UTF-8" ?>
<html>
<head>
</head>
<body>
<svg xmlns="http://www.w3.org/2000/svg" width="4096" height="2896" viewBox="0,0,1024,724" preserveAspectRatio="xMidYMid" zoomAndPan="magnify">
<style>
<![CDATA[
      @font-face { font-family: "INTL_ISO"; src: url('fonts/INTL_ISO.woff') format('woff'); text-rendering:optimizeLegibility; }
]]>
</style>
```
5. Wijzigen footer SVG bestand;
```
</svg></body></html>
```
6. Voeg links toe aan bestand via reguliere expressies
```
:%s/\(.*fuchsia.*\)>\([C]\?[0-9]\+\)<\/text>/\1 onclick="window.open('\/#!maatregelen\/\2.md', '_blank');">\2<\/text>/g
:%s/\(.*paleturquoise.*\)>\([C]\?[0-9]\+\)<\/text>/\1 onclick="window.open('\/#!maatregelen\/\2.md', '_blank');">\2<\/text>/g
:%s/\(.*deepskyblue.*\)>\([C]\?[0-9]\+\)<\/text>/\1 onclick="window.open('\/#!maatregelen\/\2.md', '_blank');">\2<\/text>/g
```
