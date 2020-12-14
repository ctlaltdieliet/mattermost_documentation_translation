Gegevensretentiebeleid (E20)
== == == == == == == == == == == == == == == == =

Beschikbaar in ` Enterprise Edition E20 <https://mattermost.com/pricing-self-managed/> ` __.

Standaard slaat Matterbest alle berichthistorie op met een onbeperkte zoekhistorie voor beheerders en eindgebruikers.

In Enterprise Edition E20 kunt u een aangepast beleid instellen om te beheren hoe lang berichten en uploads worden bewaard in de meeste kanalen en directe berichten. .. waarschuwing: als een bericht of bestand eenmaal is gewist, is de actie onomkeerbaar. Wees voorzichtig bij het instellen van een aangepast gegevensretentiebeleid. .. tocboom::
    :maxdepth: 2

Een beleid voor gegevensbewaring configureren
------------------------------------

U stelt als volgt een aangepast bewaarbeleid voor gegevens in:

1. Ga naar ** System Console > Compliance > Data Retention Policy * * (of ** System Console > Advanced > Data Retention Policy * * in versies prior to 5.12).
2. Selecteer een optie ** Bericht bewaren * *. Wanneer een tijd is opgegeven, worden berichten, inclusief bestandsbijlagen, ouder dan de tijdsduur die u instelt op het opgegeven tijdstip gewist. De minimale bewaartermijn is één dag.
3. Selecteer een optie ** Bestand Retention * *. Wanneer een tijd is opgegeven, zullen geüploade bestanden die ouder zijn dan de tijdsduur die u hebt ingesteld worden verwijderd uit uw bestandssysteem (van uw lokale schijf of uw Amazon S3 service zoals gespecificeerd in ** Systeemconsole > Milieu > Bestand Opslag * * (of ** Systeemconsole > Bestanden > Opslag * * in versies ouder dan 5.12)) op het opgegeven tijdstip. De minimale bewaartermijn is één dag.
4. Stel de begintijd van de dagelijkse geplande bewaartermijn voor gegevens in. Kies een tijd waarin minder mensen uw systeem gebruiken. Moet een tijdsaanduiding van 24 uur zijn in de notatie UU:MM.

Sla de instellingen op en start de server opnieuw. Berichten en bestanden die ouder zijn dan de duur die u hebt ingesteld, worden op de opgegeven servertijd gewist, indien van toepassing.

U kunt de wistaak ook op elk moment handmatig uitvoeren door te klikken op ** Run Wissen Job Now * * in ** System Console > Compliance > Data Retention Policy * * (of ** System Console > Advanced > Data Retention Policy * * in versies prior to 5.12). .. Opmerking:
  Als u de gegevensbewaartermijn en ` ElasticSearch <https://docs.mattermost.com/deployment/elasticsearch.html> ' _ gebruikt, zorg er dan voor dat de instelling ` ElasticSearch aggregate search indexes <https: //docs.mattermost.com/administration/config-settings.html#aggregate-search-indexes> ` _ is ingesteld op een waarde die groter is dan uw gegevensbewaarbeleid in dagen.

Veelgestelde vragen (FAQ ' s)
---------------------------------

Wat gebeurt er wanneer een bericht wordt gewist?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Het bericht wordt verwijderd uit de interface van Matterit en verwijderd uit de ` ` Posts ` ` tabel. Het bericht is niet meer doorzoekbaar en kan niet worden opgehaald in vastgezette posts of gemarkeerde lijsten.

Antwoorden die de berichtduur niet overschrijden, worden nog steeds afgebeeld in de gebruikersinterface. Verdere antwoorden zijn echter niet meer mogelijk.

Wat gebeurt er als een bestand wordt gewist?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

De bestandsbijlage wordt verwijderd uit de Mattermo
st gebruikersinterface, verwijderd uit de ` ` FileInfo ` ` tabel, en van uw lokale schijf of Amazon S3 service zoals opgegeven in ** System Console > Environment > File Storage * * (of ** System Console > Files > Storage * * in versies ouder dan 5.12).

Waarom is een oud bestand niet verwijderd na het uitvoeren van de wisopdracht?
~ ~ ~ ~ ~ > ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~

Eerst controleert u of de verwijdering van de gegevens is geslaagd in de tabel voor wisopdracht in ** System Console > Compliance > Data Retention Policy * * (of ** System Console > Advanced > Data Retention Policy * * in versies ouder dan 5.12).

Als de bestanden zijn geüpload voorafgaand aan Mattermeest v4.2, moet u de bestanden handmatig verwijderen uit uw lokale bestand opslag of Amazon S3 opslag:

1. Wacht totdat alle bestanden die zijn geüpload vóór Mattermeest v4.2, de duur van het bestand bewaarbeleid voorbij zijn.
2. Verwijder de ` ` teams/ ` ` map in de root van je Matterendste opslagdirectory.

Houd er rekening mee dat deze bestanden nog steeds worden verwijderd uit de interface Matterendste als ze zijn geüpload in Matterbest v3.5 of hoger, die de ` FileInfo-tabel <https: //docs.mattermost.com/administration/changelog.html#database-changes-from-v3-4-to-v3-5> ` __ bevatten. 

Waarom zie ik ` ` In behandeling ` ` in de tabel met wisopdracht zonder details?
~ ~ ~ ~ ~ > ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~

Dit betekent meestal dat er een andere taak voor het bewaren van gegevens wordt uitgevoerd. U kunt dit controleren in de wisopdracht in ** System Console > Compliance > Data Retention Policy * * (of ** System Console > Advanced > Data Retention Policy * * in versies ouder dan 5.12).

Als er geen taken in uitvoering zijn en de taak gedurende meer dan 2 minuten '` In behandeling' is gebleven, is het mogelijk dat u de server niet opnieuw hebt gestart nadat u het gegevensretentiebeleid hebt ingeschakeld. Start de server opnieuw op en probeer het opnieuw.

Hoe stel ik een aangepast beleid in per team of kanaal?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Het instellen van aangepaste beleidsdefinities voor elk team en elk kanaal zijn in de roadmap, maar nog niet ondersteund.

Als u geïnteresseerd bent in deze functie, overweeg dan het ` bestaande featurevoorstel <https://mattermost.uservoice.com/forums/306457-general/suggestions/31731844-ee-data-retention-policy-for-individual-teams-and> ` __ en deel uw feedback in de reacties.

Hoe wordt de bewaring van gegevens verwerkt in de mobiele apps?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Wanneer berichten of bestanden worden gewist, zijn ze niet meer doorzoekbaar in de Mattermeeste mobiele apps. 

In v1.5 en later van de iOS-en Android-apps worden berichten en bestanden in de volgende gevallen uit de lokale opslag verwijderd als ze de duur van het retentiebeleid overschrijden:

1. Wanneer de gebruiker de app opent.
2. Wanneer de gebruiker de app in de achtergrond plaatst.

In v1.4 en eerder van de mobiele apps worden berichten en bestanden niet uit de lokale opslag verwijderd als het gegevensretentiebeleid is ingeschakeld.

Hoe weet ik of een gegevensbewaartaak mislukt?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Matterit biedt de status van elke gegevenstentietaak in ** Systeemconsole * * > ** Compliance** > * * Gegevens Retention Policy * * (of ** System Console > Advanced > Data Retention Policy * * in versies ouder dan 5.12). Hier kunt u zien of de taak is geslaagd of mislukt, inclusief de details van de fout.

Bovendien worden alle fouten in de serverlogboeken geretourneerd. Het foutenlogboek begint met de tekenreeks ` ` Failed job ` ` en bevat een job_id key/value pair. Fouten bij het bewaren van gegevens worden geïdentificeerd met de naam van de werknemer ` ` EnterpriseDataRetention ` ` `. U kunt optioneel een script maken dat programmatisch query's voor dergelijke storingen en waarschuwt het juiste systeem.

Wat gebeurt er als de bewaartermijn voor gegevens wordt gewijzigd?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

De bewaartermijn van gegevens wordt eenmaal per dag uitgevoerd op het tijdstip dat is opgegeven in het bestand ` `config.json ` `. Het wijzigen van de bewaartermijn maakt niet automatisch een planning voor een extra uitvoering van de data retention job-het werkt alleen hoe lang de gegevens worden bewaard in Matterbest.

Krijgt de systeembeheerder een bericht wanneer de bewaartermijn voor gegevens wordt gewijzigd?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~

Nee, de nieuwe configuratie wordt bijgewerkt, maar de System Admin ontvangt geen feedback over wat de effecten zullen zijn (bijvoorbeeld rapportage van hoeveel berichten moeten worden verwijderd).

Heeft de gegevensbewaartaak invloed op de tabel met audits? 
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~

Voorafgaand aan v5.20 zou het bewaren van gegevens alle gebruikersactiviteiten wissen die overeenkomen met de configuratie van de gegevensbewaartijd. Vanaf v5.20 behoudt de audittabel de gebruikersactiviteit die overeenkomt met de configuratie van de gegevensbewaartijd. 

Bevat de gegevensretentietaak gearchiveerde kanalen? 
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~

Posts en bijlagen in gearchiveerde kanalen worden beïnvloed door de functie voor het bewaren van gegevens. Als een post de leeftijd overschrijdt die is geconfigureerd voor de functie voor het bewaren van gegevens, wordt deze verwijderd uit de database.

Hoe lang duurt het voor het uitvoeren van een wisquery en beïnvloedt het de prestaties van de server?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~

Gegevensopslag voert de feitelijke wisquery in batches uit, waarbij gegevens worden gewist in blokken van 1 000 records per query. Dit is zo dat de database niet wordt vergrendeld voor langere perioden met langdurige query's. Als u aan deze limiet houdt, wordt de query beperkt tot een paar milliseconden ' uitvoeringstijd op de database zelf.

Elke batch van gegevens wordt verwijderd op basis van indexen-het maken van de vragen snel uit te voeren op kleine batches. Dit helpt de server volledig responsief te blijven tijdens het uitvoeren van het proces.

Hoe weet ik of de gegevensbewaartaak wordt uitgevoerd/gepland?
~ ~ ~ ~ ~ > ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~

De taakplanner voert de gegevensbewaartaak uit op basis van de tijd die is opgegeven in de configuratie-instellingen. Op dit moment wordt een ` ` DEBUG ` `-level logregel afgedrukt: ` ` Scheduling data retention job ` `.

Wanneer een taak serv
er wordt opgehaald dat geplande taak voor uitvoering, een ` ` DEBUG ` ` `-level logregel wordt gegenereerd: ` ` Worker EnterpriseDataRetention: Received a new candidate job ` `.

Als de taak voltooid is, wordt er een ` ` INFO ` '-logregel gegenereerd: ` ` Worker EnterpriseDataRetention: Job is voltooid ` `.
