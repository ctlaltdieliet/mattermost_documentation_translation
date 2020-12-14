Gegevensbewaarbeleid
== == == == == == == == == == =

Standaard slaat Matterbest alle berichthistorie op met een onbeperkte zoekhistorie voor beheerders en eindgebruikers.

Met een gegevensretentiebeleid kunt u een aangepast beleid instellen om te beheren hoe lang berichten en uploads worden bewaard in de meeste kanalen en directe berichten. .. waarschuwing: als een bericht of bestand eenmaal is gewist, is de actie onomkeerbaar. Wees voorzichtig bij het instellen van een aangepast gegevensretentiebeleid. .. tocboom::
    :maxdepth: 2

Een beleid voor gegevensbewaring configureren
-----------------------------------

U stelt als volgt een aangepast bewaarbeleid voor gegevens in:

1. Ga naar ** System Console > Compliance > Data Retention Policy * *.
2. Selecteer een optie ** Bericht bewaren * *. Wanneer een tijd is opgegeven, worden berichten, inclusief bestandsbijlagen, ouder dan de tijdsduur die u instelt op het opgegeven tijdstip gewist. De minimale bewaartermijn is één dag.
3. Selecteer een optie ** Bestand Retention * *. Wanneer een tijd is opgegeven, zullen geüploade bestanden die ouder zijn dan de tijdsduur die u instelt worden verwijderd op het opgegeven tijdstip. De minimale bewaartermijn is één dag.
4. Stel de begintijd van de dagelijkse geplande bewaartermijn voor gegevens in. Kies een tijd waarin minder mensen uw systeem gebruiken. Moet een tijdsaanduiding van 24 uur zijn in de notatie UU:MM.

Sla de instellingen op en start de server opnieuw. Berichten en bestanden die ouder zijn dan de duur die u hebt ingesteld, worden op de opgegeven servertijd gewist, indien van toepassing.

U kunt de wistaak ook op elk moment handmatig uitvoeren door te klikken op ** Run Wissen Job Now * * in ** System Console > Compliance > Data Retention Policy * *.

Veelgestelde vragen (FAQ ' s)
---------------------------------

Wat gebeurt er wanneer een bericht wordt gewist?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Het bericht wordt verwijderd uit de interface Matterendste en wordt permanent verwijderd uit de database. Het bericht is niet meer doorzoekbaar en kan niet worden opgehaald in vastgezette posts of gemarkeerde lijsten.

Antwoorden die de berichtduur niet overschrijden, worden nog steeds afgebeeld in de gebruikersinterface. Verdere antwoorden zijn echter niet meer mogelijk.

Wat gebeurt er als een bestand wordt gewist?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

De bestandsbijlage wordt verwijderd uit de interface Matterendste en wordt permanent verwijderd.

Waarom is een oud bestand niet verwijderd na het uitvoeren van de wisopdracht?
~ ~ ~ ~ ~ > ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~

Controleer eerst of de verwijdering van de gegevens is geslaagd in de tabel voor wisopdracht in ** System Console > Compliance > Data Retention Policy * *.

Waarom zie ik ` ` In behandeling ` ` in de tabel met wisopdracht zonder details?
~ ~ ~ ~ ~ > ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~

Dit betekent meestal dat er een andere taak voor het bewaren van gegevens wordt uitgevoerd. U kunt dit controleren in de wisopdracht in ** System Console > Compliance > Data Retention Policy * *.

Als er geen taken in uitvoering zijn en de taak ` ` In behandeling 'is gebleven' voor meer dan een uur, neem dan contact op met ondersteuning

Hoe stel ik een aangepast beleid in per team of kanaal?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ nten

Het instellen van aangepaste beleidsdefinities voor elk team en elk kanaal zijn in de roadmap, maar nog niet ondersteund.

Als u geïnteresseerd bent in deze functie, overweeg dan het ` bestaande featurevoorstel <https://mattermost.uservoice.com/forums/306457-general/suggestions/31731844-ee-data-retention-policy-for-individual-teams-and> ` __ en deel uw feedback in de reacties.

Hoe wordt de bewaring van gegevens verwerkt in de mobiele apps?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Wanneer berichten of bestanden worden gewist, zijn ze niet meer doorzoekbaar in de Mattermeeste mobiele apps.

Hoe weet ik of een gegevensbewaartaak mislukt?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Matterit biedt de status van elke gegevenstentietaak in ** Systeemconsole * * > ** Compliance** > * * Het beleid voor gegevensbewaring * *. Hier kunt u zien of de taak is geslaagd of mislukt, inclusief de details van de fout.

Wat gebeurt er als de bewaartermijn voor gegevens wordt gewijzigd?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Het bewaren van gegevens wordt eenmaal per dag uitgevoerd op het moment dat in de instellingen is opgegeven. Het wijzigen van de bewaartermijn maakt niet automatisch een planning voor een extra uitvoering van de data retention job-het werkt alleen hoe lang de gegevens worden bewaard in Matterbest.

Krijgt de systeembeheerder een bericht wanneer de bewaartermijn voor gegevens wordt gewijzigd?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden

Nee, de instelling wordt bijgewerkt, maar de systeembeheerder ontvangt geen feedback over wat de effecten zullen zijn (bijvoorbeeld rapportage van hoeveel berichten moeten worden verwijderd).

Bevat de gegevensretentietaak gearchiveerde kanalen? 
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Posts en bijlagen in gearchiveerde kanalen worden beïnvloed door de functie voor het bewaren van gegevens. Als een post de leeftijd overschrijdt die is geconfigureerd voor de functie voor het bewaren van gegevens, wordt deze verwijderd uit de database.

Hoe lang duurt het voor het uitvoeren van een wisquery en beïnvloedt het de prestaties van de server?
~ ~ ~ ~ > ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~ ~

Gegevensopslag voert de feitelijke wisquery in batches uit, waarbij gegevens worden gewist in blokken van 1000 records per query. Dit is zo dat de database niet wordt vergrendeld voor langere perioden met langdurige query's. Als u aan deze limiet houdt, wordt de query beperkt tot een paar milliseconden ' uitvoeringstijd op de database zelf.

Elke batch van gegevens wordt verwijderd op basis van indexen-het maken van de vragen snel uit te voeren op kleine batches. Dit helpt de server volledig responsief te blijven tijdens het uitvoeren van het proces.
