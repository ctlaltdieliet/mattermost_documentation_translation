.. _bulk-laden-gegevens:

De opdracht bulkladen uitvoeren
== == == == == == == == == == == == == == == ==

Voordat u de opdracht bulkladen uitvoert, moet u eerst een 'JSONL' maken
<https://jsonlines.org> ` __ bestand dat de gegevens bevat die u wilt importeren. Nadat u het bestand hebt gemaakt, voert u de opdracht bulkload uit in de validatiemodus. In deze modus worden de gegevens gecontroleerd op juistheid, maar niet naar de database geschreven. Na het valideren voert u de opdracht in de werkstand Toepassen uit, waardoor de gegevens worden opgeslagen in de database.

** Voor het laden van gegevens in bulk * *:

1. Maak de ` JSONL
<https://jsonlines.org> ` __ gegevensbestand in de meest overeenkomende directory. Het bestand kan elke naam hebben, maar in deze procedure heet het ` `data.jsonl ` `. De indeling van het bestand wordt beschreven in de sectie :ref: ` data-format `.

2. Controleren of het bestand juist is:

  a. Ga naar de meest overeenkomende directory.

    ` ` cd /opt/matterbest ` ` (de locatie kan anders zijn op je systeem)

  b. Voer de volgende opdracht uit:

    ` ` sudo -u matterbest bin/matterbest import bulk data.jsonl -- validate ` `

3. Opgelost eventuele fouten die worden gemeld, en controleer het bestand opnieuw. Ga niet naar de volgende stap totdat u de validatieopdracht zonder fouten kunt uitvoeren.

4. Voer de opdracht bulkload uit in de werkstand toepassen:

  ` ` sudo -u mattermeest bin/matterbest import bulk data.jsonl -- apply ` `

5. Als de opdracht voor bulkload is voltooid, maakt u alle caches leeg. Open de System Console en klik op ** General > Configuration > Purge All Caches * * in eerdere versies of ** Systeemconsole * * > ** Omgeving ** > ** Webserver * * in versies na 5.12. .. Belangrijk:
  Eigenaar van ` ` data ` ` directory en al zijn inhoud moet veranderen naar Matterbest gebruiker om het correct te laten werken. Anders kan Matterbest de bestanden niet ophalen die zijn gemaakt in ` ` data ` ` dir nadat het importtool is uitgevoerd, omdat alle bestanden die zijn gemaakt in ` ` data ` ` dir eigendom zijn van ` ` root ` ` ` als het gereedschap werd uitgevoerd als ` ` sudo ` ` `.
