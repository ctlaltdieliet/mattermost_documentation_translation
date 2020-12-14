.. _about-bulk-loading-opdracht:

Over de opdracht voor bulkladen
== == == == == == == == == == == == == == ==

Het bulk laden van de opdracht is onderbreekbaar en idempotent Als de import wordt onderbroken om welke reden dan ook, het blijft van waar het uit de volgende keer dat u het uitvoeren. U kunt de opdracht herhaaldelijk uitvoeren met hetzelfde gegevensbestand en de gegevens worden slechts één keer geïmporteerd. Vanaf v5.20 worden de bijlagen vervangen door de inkomende gegevens vanaf v5.20. Vóór v5.20 werden updates van berichten met overeenkomende tijdstempels toegevoegd aan oudere posten. 

U kunt de bulk laden commando uitvoeren op een live systeem Hoewel u niet hoeft te sluiten Matterbest om de opdracht uit te voeren, kunnen wijzigingen door gebruikers van het systeem tussen de uitvoeringen worden overschreven als de corresponderende velden aanwezig zijn in het gegevensbestand.

Sommige gegevensvelden zijn optioneel Niet alle velden zijn verplicht. Als er een optioneel veld ontbreekt in het object dat wordt geïmporteerd, wordt de huidige waarde van het veld in de database niet gewijzigd.

De opdracht voor bulkladen is geen synchronisatietool. U kunt de opdracht voor het laden van bulkgoederen niet gebruiken om objecten of hun velden te verwijderen uit de database van Matterit. Met de opdracht worden alleen velden gemaakt of overschreven. .. Belangrijk:
  De opdracht voor bulkladen wordt uitgevoerd in de CLI en wordt uitgevoerd in de beveiligingscontext van de CLI. Dit betekent dat het volledige permissies heeft om alles in de Matterendste database te benaderen en te wijzigen.
