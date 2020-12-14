.. _bulk-export:

== == == == == == == == = Bulk Export Tool
== == == == == == == == =

Het verplaatsen van gegevens van de ene Matterste-instance naar de andere begint met het exporteren van gegevens naar een ` JSONL <https://jsonlines.org> ` __ bestand met behulp van de 'bulklaadfunctie <https://docs.mattermost.com/deployment/bulk-loading.html>' __. Deze tool is handig als u een server hebt gemaakt voor een proof of concept, een andere server voor productiegebruik hebt gemaakt en nu de historie van het proof-of-concept-subsysteem wilt behouden.

U kunt de volgende gegevenstypen exporteren:

-Teams
-Kanalen (openbaar en privé)
-Gebruikers
-Teamlidmaatschappen van gebruikers
-Gebruikers ' Kanaal lidmaatschappen
-Posts (posten in de openbare/particuliere kanalen en ook antwoorden op deze posten) .. Inclusief: bulkexport-data.rst

De opdracht voor bulkexport uitvoeren
== == == == == == == == == == == == == == == =

Het exportcommando wordt uitgevoerd in de ` CLI <https://docs.mattermost.com/administration/command-line-tools.html> ` __. Het heeft permissies om toegang te krijgen tot alle informatie in de Matterendste database.

U voert de exportopdracht als volgt uit:

1. Navigeer naar de directory waar de Matterigste server is geïnstalleerd. Bij een standaardinstallatie van Matterbest is de directory ` ` /opt/matterbest ` `.
2. Voer de volgende opdracht uit om gegevens uit alle teams op de server te extraheren. U kunt de bestandsnaam wijzigen en een absoluut of relatief pad opgeven om te bepalen waar het bestand wordt geëxporteerd: ` ` sudo -u matterbest bin/matterbest export bulk file.json -- all teams ` `

  ` ` sudo -u mattermeest bin/mattermeest export bulk /home/user/bulk_data.json -- all teams ` `
  
3. Haal uw bestand op van de locatie die u hebt opgegeven.
