# Challenges

## Frequentie-sturing met data
 - Met name bij hoogfrequente dienstregelingen is er vanuit reizigersperspectief steeds minder behoefte aan een vaste dienstregeling en steeds meer behoefte aan een betrouwbare, vaste frequentie.
 - Bij verstoringen in de dienstuitvoering ontstaat er al heel snel een situatie waarin de opvolgtijd niet evenredig wordt verdeeld tussen trams en bussen op de dezelfde lijn/richting; het kan soms voorkomen dat twee voertuigen vlak achter elkaar rijden omdat het achterste voertuig zich volgens instructie aan de vaste dienstregeling houdt.
 - Met behulp van de realtime open source OV data is het mogelijk om aan de bestuurder informatie te bieden over de positie van de voorganger en de achterligger op de lijn. Met deze informatie kan de bestuurder vervolgens zelf de beslissing nemen om sneller te rijden, mogelijk eerder te vertrekken of juist langzamer te rijden of langer te halteren.
 - De informatie is aan de bestuurder aan te bieden mbv een app op een telefoon of tablet.
 - **Propositie:** Een uitbreiding van dit idee zou kunnen zijn om de ideale verdeling van de voertuigen op de lijn dynamisch te optimaliseren door een algoritme dat aan ieder bestuurder een specifieke versnelling- of vertraging-suggestie kan doen.

## Klantinteracties in het voertuig
 - Openbaar vervoerbedrijven hebben (net als in andere branches) behoefte aan frequente en effectieve klanttevredenheidsmetingen. Uitdaging hierbij is vaak dat er niet altijd een goede match te maken is tussen de specifieke OV rit en de perceptie hiervan door de reiziger. Met andere woorden: hoe waarderen reizigers specifiek OV verplaatsingen.
 - Het praktisch 100% bezit van smartphones door reizigers biedt hierbij kansen.
 - **Propositie:** Voorgesteld wordt om een app te ontwikkelen die reizigers de mogelijkheid biedt om laagdrempelig een waardering af te geven. Met input van één waarde: namelijk het duidelijk zichtbare voertuignummer of het scannen van een qr code wordt dan automatisch de match gemaakt met een specifieke OV voertuigrit. Hiervoor is Open OV koppelvlak data noodzakelijk. Het zou natuurlijk mooi zijn als reizigers met de app in staat zijn om direct foto’s te delen als er een defect of een misstand is.  
  
## Toedeling van reizigersritten aan voertuigritten
 - Het in- en uitchecken binnen stedelijke tram- en bus systemen, vindt meestal plaats binnen het voertuig. De datakwaliteit die hierdoor ontstaat is vrij hoog, omdat hierbij niet alleen de verplaatsing herleidbaar wordt, maar ook de verbinding gelegd kan worden met specifieke voertuigritten, waardoor bezettingen inzichtelijk worden.
 - HTM overweegt om het in- en uitchecken plaats te laten vinden op de halte. Hierdoor is niet meer een één-op-één relatie te leggen met de voertuigritten. Er is behoefte aan een methode om de in- en uitchecktransacties toe te delen aan de voertuigritten. Uitdaging hierbij is het gedrag van reizigers en de effecten van overstappen van de ene naar de andere rit.
 - Voor de oplossing is enerzijds een set ov-chipkaarttranacties beschikbaar en anderzijds een set met operationele gegevens (open data)
 - **Propositie:** Deliverable zou zijn: een script dat de toedeling uitvoert.  

## Aanrijdingen voorkomen uit open data
 - De positie van andere railvoertuigen is voor trambestuurders betrekkelijk voorspelbaar in normale omstandigheden; vaak is er vrij zicht en een grote mate van voorspelbaarheid in de dienstregeling. Toch zijn er situaties waarbij er railvoertuigen onverwacht stil staan in een bocht of in een keerlus zonder dat een naderende bestuurder dit kan voorzien.
 - De actuele positie van railvoertuigen wordt redelijk actueel gedeeld in het open data domein (iedere halteringen en iedere  seconden). Deze data is geschikt om met een zekere mate van nauwkeurigheid (die past bij deze uitdaging) vast te stellen of zich een voertuig bevindt binnen de nabijheid van een ander naderend voertuig die dit mogelijk niet voorziet.
 - **Propositie:** Voorgesteld wordt om deze informatie als waarschuwing te tonen aan bestuurders als extra beveiliging tegen aanrijdingen.  

## Real-time low-cost voertuigtelemetrie
 - Railvoertuigen van HTM zijn naargelang het type uitgerust met (legacy) systemen om voertuiggegevens te loggen en soms ook te delen. Voorbeelden zijn de boorcomputer die zich bevindt in de nieuwere Avenio voertuigen of de hardware noodzakelijk voor het voertuigbeheerssysteem EBS.
 - Tegelijkertijd zien we dat allerlei technologie beschikbaar wordt om goedkoop een eigen IoT keten vorm te geven. Toepassingen zijn dan dat het makkelijk wordt om zelf metingen te verrichten aan de operationele prestaties, zoals bijvoorbeeld rijcomfort aan boord door optrekken en afremmen.
 - **Propositie:** Een concrete toepassing zou kunnen zijn: een smartphone als online ‘multisensor device’ verbinden met een Cloud IoT Hub om met een dashboard realtime de sensors in het voertuig te kunnen uitlezen en te loggen. Een relatie zou gelegd kunnen worden met open source OV verplaatsingsinformatie, zodat de events kunnen worden gekoppeld aan specifieke halteringen en voertuigritten.  

## Verbeteren voorspellingsalgoritme
 - Als reizigers op het haltebord kijken, zien ze hoeveel minuten het nog duurt voordat de tram of bus arriveert. Deze waarde wordt dynamisch bepaald op basis van de dienstregeling en de actuele afwijking daarop van de realisatie. De voorspelling vindt plaats in het voertuigbeheersysteem (EBS) en is ooit ontwikkeld door de leverancier. Het voorspellen van de realisatie vindt dus niet plaats in het openbare domein van de koppelvlakdata.
 - **Propositie:** Voorgesteld wordt om een voorspellingsalgoritme te maken op basis van (ruim aanwezige) historische data. Hiermee raken vervoerders meer in control over de actuele voorspelling die zij afgeven aan hun reizigers.  
