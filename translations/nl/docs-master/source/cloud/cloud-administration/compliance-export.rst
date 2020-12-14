Nalevingsexportbèta
== == == == == == == == == == ==

Deze functie maakt het mogelijk dat de nalevingsexport wordt geproduceerd vanuit de systeemconsole, waarin alle berichten zijn opgenomen, waaronder:

-Die zijn gemaakt in directe berichtkanalen
-Bestandsuploads
-Posts van plugins
-Posts van bots/webhaken

De export bevat informatie over de historie van kanaalleden op het moment dat het bericht werd gepost.

Items voor gewiste berichten en bestanden worden opgenomen in CSV-en actierapporten. De gewiste content wordt opgenomen in de nalevingsexport. Algemene relay-rapporten bevatten items voor het wissen van bestanden, maar items voor het wissen van berichten zijn uitgesloten.

Standaard slaat Matterbest alle berichthistorie op met een onbeperkte zoekhistorie voor beheerders en eindgebruikers. U kunt een ` aangepast gegevensretentiebeleid ' instellen voor de manier waarop lange berichten en bestandsuploads worden bewaard in de meeste kanalen en directe berichten.

Bedrijfsimplementaties met een vereiste om historie te archiveren buiten de bewaartermijn van gegevens kunnen deze addon inschakelen om nalevingsrapporten te exporteren naar systemen van derden. Integratie met Actiance Vantage en Global Relay worden momenteel ondersteund, met integraties met andere systemen in de roadmap. .. tocboom::
    :maxdepth: 2

Handleiding instellen
------------

Gebruik de volgende handleidingen voor het configureren van exports voor CSV, Actiance XML of Global Relay EML. 

... Opmerking:
  De nalevingsexporten bevatten geen posts die zijn verzonden voordat de functie is ingeschakeld.

1. Ga naar ** System Console > Compliance > Compliance Export (Beta) * *.
2. Set ** Enable Compliance Exports * * to ** true**.
3. Stel de ** Compliance Export time * * in. Dit is de begintijd van de taak voor het uitvoeren van de dagelijkse geplande nalevingsexport en moet een tijdsaanduiding van 24 uur zijn in de notatie UU:MM. Kies een tijd waarin minder mensen uw systeem gebruiken.
4. Stel de indeling van het exportbestand in op **CSV* *.
5. Kies ** Save**.

U kunt de CSV-indeling gebruiken om de export eenvoudig te transformeren in een gewenste indeling voor uw externe archiefsysteem. Voor een voorbeeld-CSV-uitvoer, ` download hier een CSV-exportbestand <https://github.com/mattermost/docs/blob/master/source/samples/csv_export.zip> ` __.

Actieteit ~ ~ ~ ~ g ~ ~ g ~ ~ g ~ ~ g

1. Ga naar ** System Console > Compliance > Compliance Export (Beta) * *.
2. Set ** Enable Compliance Exports * * to ** true**.
3. Stel de ** Compliance Export time * * in. Dit is de begintijd van de taak voor het uitvoeren van de dagelijkse geplande nalevingsexport en moet een tijdsaanduiding van 24 uur zijn in de notatie UU:MM. Kies een tijd waarin minder mensen uw systeem gebruiken.
4. Stel de indeling van het exportbestand in op ** Actiance XML* *.
5. Kies ** Save**.

Als u Actiance XML als bestandsformaat hebt geselecteerd, kunt u een integratie met Actiance Vantage Archive-systeem instellen. Voor meer informatie, zie ` hun homepage <https://www.actiance.com/products/vantage/> ` __. Voor een voorbeeld van Actiance output, ` download een Actiance XML export bestand hier <https://github.com/mattermost/docs/blob/master/source/samples/actiance_export.xml> ` __. .. Opmerking:
  In de XML-export van Actiance wordt het kanaaltype voorafgegaan door de kanaalnamen.

Algemene rela
y EML ~ ~ ~ ~ ~ ~ ng ~ ~ ~ ~ n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

1. Ga naar ** System Console > Compliance > Compliance Export (Beta) * *.
2. Set ** Enable Compliance Exports * * to ** true**.
3. Stel de ** Compliance Export time * * in. Dit is de begintijd van de taak voor het uitvoeren van de dagelijkse geplande nalevingsexport en moet een tijdsaanduiding van 24 uur zijn in de notatie UU:MM. Kies een tijd waarin minder mensen uw systeem gebruiken.
4. Stel de indeling van het exportbestand in op ** GlobalRelay EML* *.
5. Selecteer ` A9/Type 9 'of' A10/Type 10 ' voor de ** Global Relay Customer Account * *. Dit is het type Global Relay-klantenaccount dat uw organisatie heeft.
6. Stel de optie ** Global Relay SMTP username * *, ** Global Relay SMTP password * *, en ** Global Relay SMTP email address * * in, zoals geleverd door Global Relay.
7. Kies ** Save**.

Als u Global Relay EML hebt geselecteerd als bestandsindeling, kunt u een integratie met Global Relay-archiefsysteem instellen. Meer informatie vindt u in 'Global Relay Archive <https://www.globalrelay.com/gr-services/archive>' __. .. Opmerking:
  Berichten die groter zijn dan 250 MB hebben hun bijlagen verwijderd omdat ze te groot zijn om naar Global Relay te gaan. Er wordt een fout toegevoegd aan de serverlogboeken met ID ` ` global_relay_attachments_removed ` `. Deze bevat het post-ID waarvan de bijlagen zijn verwijderd, en de bijlage-ID ' s. Een ' ticket wordt in de wachtrij gezet om grote berichten beter af te handelen <https://mattermost.atlassian.net/browse/MM-10038> ` __.

Voor meer informatie over het Global Relay-archiefsysteem, zie "hun homepage <https://www.globalrelay.com/>" __.

Veelgestelde vragen (FAQ)
---------------------------------

Hoe exporteer ik de geschiedenis van het verleden?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Ng~

Voer de ` ` export ` ` :doc: ` command line tool <command-line-tools>` uit. U kunt een ` exportFrom ` optie opgeven om gegevens uit een bepaalde tijdsaanduiding te exporteren. Alle posts die na deze tijdsaanduiding zijn gemaakt, worden geëxporteerd.

Wat gebeurt er als ik handmatig gegevens exporteren?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Als de nalevingsuitvoertaak automatisch wordt uitgevoerd, handmatig via de systeemconsole, exporteert het alle posts die zijn gemaakt sinds de vorige post die de vorige keer werd uitgevoerd. Als dit de eerste keer is dat de taak wordt uitgevoerd, worden alle posten die zijn gemaakt nadat de functie is ingeschakeld, geëxporteerd.

Wanneer u handmatig wordt uitgevoerd via de System Console, worden de XML-bestanden van de System Console en Actiance weggeschreven naar de subdirectory ` export 'van de geconfigureerde ` Local Storage Directory <https: //docs.mattermost.com/administration/config-settings.html?#local-storage-directory>' __. Bestanden worden naar een map geschreven met namen op basis van een tijdbereik. Global Relay EML export formaat zal worden gemaild naar het geconfigureerde e-mailadres wanneer het handmatig wordt uitgevoerd.

Waarom wordt de nalevingsexport bèta?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Ng~

Deze functie wordt genoemd als bèta om de volgende redenen:

1. De taak voor het uitvoeren van een nalevingsexport is niet getest op een systeem met 10.000s van gelijktijdige actieve gebruikers.
2. De uitvoer bevat nog geen berichten met speciale typen, namelijk systeemberichten, webhook-berichten en aangepaste pluginberichten.
3. Er is nog geen manier om te onderscheiden wie een bericht bewerkt of verwijderd, noch welk bericht is een antwoord of een bewerking van een ander bericht.
4. Het QA-proces is nog in uitvoering.

Hoe weet ik of een nalevingsexporttaak mislukt?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Matterit biedt de status van elke nalevingsexporttaak in ** System Console > Compliance > Compliance Export (Beta) * *. Hier kunt u zien of de taak is geslaagd of mislukt, met inbegrip van het aantal geëxporteerde berichten en bestanden.
