Bleve Search (Experimental)
== == == == == == == == == == == == == =

Bleve is een zoekmachine die gebruik maakt van Lucene-stijl full-text zoeken en indexeren. Deze stijl van zoeken en indexeren helpt bij het overwinnen van beperkingen van de standaard database-zoekfunctie, zoals uitdagingen met tekens en geavanceerde zoekmogelijkheden.

De Bleve zoekmachine werkt als een bibliotheek geïntegreerd in de Matterendste codebase. Omdat het indexen genereert op het bestandssysteem van de server waarop het actief is, heeft het geen externe server nodig om te functioneren. Hierdoor kan Bleve niet ingeschakeld worden in High Availability-implementaties.

Bleve in Matterbest configureren
-------------------------------

Voer de volgende stappen uit om de Matterigste server te configureren voor het gebruik van Bleve en het genereren van vereiste indexen. Als de configuratie eenmaal is opgeslagen, worden nieuwe posts die naar de database worden gemaakt automatisch geïndexeerd met Bleve.

** Note:** Tijdens het indexeren kunnen de zoekresultaten onvolledig zijn totdat de indexeertaak is voltooid.

1. Open ** System Console > Experimental > Bleve * *.
2. Set ** Schakel Bleve Indexing * * * naar ** true** in om de andere instellingen op de pagina in te schakelen.
3. Stel het pad in dat wordt gebruikt voor het opslaan van bleve-indexen (bijvoorbeeld: ` ` /var/opt/mattermost/bleveindexes ` ` `). De gebruiker die Matterbest uitvoert, moet gemachtigd zijn voor toegang tot de directory.
4. Sla de configuratie op.
5. Klik op de knop ** Index Nu * *. Alle gebruikers, kanalen en berichten in de database zullen de oudste worden geïndexeerd.
6. Instellen ** Activeer Bleve voor zoekopdrachten * * naar ** true**.
7. Set ** Enable Bleve for autocomplete queries * * to ** true**.

Het gebruik van Bleve Search
------------

De volgende voorwaarden worden toegepast bij het gebruik van Bleve zoeken:

* ** Niet-aangehaalde termen: ** Zoektermen die niet-alfanumerieke tekens/speciale tekens buiten aanhalingstekens bevatten, worden verwijderd. Als u bijvoorbeeld ` ` abcd '**' & & abc ` ` gebruikt als zoekterm, worden er resultaten geretourneerd voor een zoekopdracht naar ` ` abcd "**" abc ` ` omdat de ` ` & & ` ` tekens niet binnen de aanhalingstekens stonden.
* ** Wildcard search: ** Wildcard search (bijv. ` ` abc * ` `) wordt ondersteund.
