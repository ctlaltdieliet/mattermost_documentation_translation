FAQ voor gegevensopslag op client
== == == == == == == == == == == == == ==

Mobiele webervaring
---------------------

** 1. Welke gegevens worden opgeslagen? **
  Net als bij een desktopwebbrowser kunnen gegevens worden opgeslagen in de cache van de mobiele webbrowser die zich bevindt op het opslagsysteem van het besturingssysteem dat wordt beschermd door beveiligingsmaatregelen in het fysieke apparaat en het besturingssysteem.
** 2. Hoe worden de gegevens beschermd? **
  Beveiliging voor mobiele web-ervaring is vergelijkbaar met de beveiliging voor een desktop web-ervaring.
** 3. Wanneer worden de gegevens gewist? **
  Als u zich afmeldt of uw account gedeactiveerd is, kunnen de gegevens in de browsercache zich bevinden totdat de cache vervalt of de tijdelijke bestandssysteemopslag op het besturingssysteem wordt gewist, afhankelijk van het besturingssysteem.


Mobiele app-ervaring
----------------------------------

Om de initiële laadtijd te versnellen, worden de gegevens van Matterbest mobiele apps lokaal op het apparaat opgeslagen voor v1.1 en hoger. Hieronder vindt u algemene vragen over cachegegevens: 

** 1. Welke gegevens worden lokaal opgeslagen met de nieuwe mobiele apps op een mobiel apparaat? **

  De gegevens die op het apparaat kunnen worden gevonden, zijn alleen afhankelijk van de vraag of de gebruiker al dan niet is aangemeld bij de Matterendste server, en is onafhankelijk van de status van de verbinding van het apparaat of de status van de app. Tijdens het aanmelden is alles wat de gebruiker normaal mag laten zien in aanmerking voor opslag op het apparaat, met daarin de volgende inhoud:

  -berichten
  -bestanden en afbeeldingen die zijn gekoppeld aan berichten
  -avatars, gebruikersnamen en e-mailadressen van personen in het huidige open kanaal

  Bovendien worden metagegevens die de app gebruikt voor het bijhouden van de bewerkingen ook in de cache opgeslagen. De metagegevens bevatten gebruikers-ID 's, kanaal-ID' s, team-ID 's en bericht-ID' s. Momenteel kan de cache niet op afstand opnieuw worden ingesteld op verbonden mobiele apparaten.

** 2. Hoe zit het met push-berichten? **
  Het geheugen van de push-berichten wordt beheerd door het besturingssysteem op het apparaat. Matterbest kan worden geconfigureerd voor het verzenden van beperkte hoeveelheden informatie die niet de berichttekst of de kanaalnaam bevatten, en het kan ook worden geconfigureerd om geen push-berichten te verzenden.

** 3. Waar zijn de opgeslagen gegevens en hoe wordt die gegevens beschermd? **
  De gegevens worden opgeslagen in de lokale opslag van de app. Het wordt beschermd door de beveiligingsmaatregelen die een apparaat meestal biedt aan de apps die zijn geïnstalleerd op het.

** 4. Hoe lang zijn de gegevens opgeslagen? **
  Gegevens worden opgeslagen totdat de gebruiker zich afmeldt, of totdat deze wordt verwijderd tijdens het normale cachebeheer. Als u een gebruikersaccount deactiveert, wordt er een afmelding en het verwijderen van gegevens van het apparaat uitgevoerd.

** 5. Zijn berichten vooraf geladen? **
  Nee. Berichten worden verzonden naar het apparaat op aanvraag. Ze zijn niet vooraf geladen in afwachting van de gebruikers scrollen of schakelen van kanalen.

** 6. Wat gebeurt er met berichten die op de server worden gewist nadat een gebruiker ze heeft gezien? **
  De berichten worden gewist van de client.

** 7. Welke gegevens worden opgeslagen op een mobiel apparaat nadat een account is gedeactiveerd in de volgende gevallen: **
  1. *Het mobiele apparaat is verbonden met running.*
    A
de in de vragen 1 en 2 vermelde gegevens, maar binnen 60 seconden nadat een account op de server is gedeactiveerd, worden alle appgegevens uit de cache verwijderd.
  2. *Het mobiele apparaat wordt afgesloten met de app-running.*
    Alle gegevens in de vragen 1 en 2, maar binnen 60 seconden nadat het apparaat opnieuw is verbonden, worden alle appgegevens uit de cache verwijderd.
  3. *Het mobiele apparaat is verbonden met de app niet running.*
    Alle gegevens in de vragen 1 en 2, maar binnen 60 seconden nadat de app is gestart, worden alle appgegevens uit de cache verwijderd.
  4. *Het mobiele apparaat is niet verbonden en de app is niet running.*
    Alle gegevens in de vragen 1 en 2, maar binnen 60 seconden nadat het apparaat opnieuw is verbonden en de app is gestart, worden alle appgegevens uit de cache verwijderd.

** 8. Welke gegevens kunnen op het apparaat staan nadat een gebruikersaccount is gedeactiveerd en alle gegevens uit de cache worden verwijderd? **
  Als bestandsbijlagen zijn ingeschakeld op de server, kunnen gebruikers bestanden downloaden die zijn gekoppeld aan berichten en deze opslaan op hun lokale bestandssysteem. Nadat ze zijn gedownload, staan de bestanden buiten de controle van de app en kunnen ze voor onbepaalde tijd op het apparaat blijven.
