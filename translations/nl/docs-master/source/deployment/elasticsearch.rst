Elasticsearch (E20)
== == == == == == == == == =

*Beschikbaar in Enterprise Edition E20 .*

Elasticsearch biedt grootschalige implementaties met geoptimaliseerde zoekprestaties en voorkomt degradatie van prestaties en timeouts.

De implementatie gebruikt ` Elasticsearch <https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html> ` __ als een gedistribueerde, RESTful zoekmachine die zeer efficiënte databasezoekopdrachten ondersteunt in een ` clusteromgeving <https://docs.mattermost.com/deployment/cluster.html> ` __. .. tocboom::
    :maxdepth: 2
    
Implementatiehandleiding
----------------

Overzicht
~ ~ ~ ~ nten

Met behulp van elasticsearch kunt u snel, in de buurt van real time, grote hoeveelheden gegevens doorzoeken door een index van post-gegevens te maken en te beheren. Het indexeringsproces kan worden beheerd vanaf de systeemconsole na het instellen en aansluiten van een Elasticsearch-server. De post-index wordt opgeslagen op de Elasticsearch-server en wordt voortdurend bijgewerkt nadat nieuwe posts zijn gemaakt. Om bestaande berichten te indexeren, moet er een bulkindex van de volledige post database worden gegenereerd. .. Belangrijk:
    De standaard Matterendste database-zoekopdracht begint met prestatievermindering op ongeveer 2,5 miljoen posts, afhankelijk van de specificaties voor de databaseserver. Als u verwacht dat uw Matterste server meer dan 2,5 miljoen berichten heeft, raden wij u aan Elasticsearch te gebruiken voor optimale zoekprestaties. Voor implementaties met meer dan 5 miljoen posten, is Elasticsearch vereist om significante prestatieproblemen (zoals timeouts) te vermijden met zoeken en op-vermeldingen.

Elasticsearch v5.x, v6.x en v7.x worden ondersteund. 

... Opmerking:
    Vanaf Matterbest v5.26 kunt u inactieve gebruikers filteren, zoeken op gebruikersrol en ook zoeken naar termen binnen links. Deze update introduceert een wijziging die de "van" deel van de zoekopdracht beïnvloedt. Om dit te voorkomen, moet u uw Elasticsearch-instance/cluster opnieuw indexeren voordat u een upgrade uitvoert.
    
Een Elasticsearch-server instellen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Het ingestelde proces voor de Elasticsearch-server is gedocumenteerd in de ` officiële Elasticsearch-documentatie <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html> ` __. .. Opmerking:
  U moet de 'ICU Analyzer Plugin <https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu.html>' __ installeren bij het instellen van Elasticsearch voor Mattermost.

Elasticsearch in Matterbest configureren
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Voer de volgende stappen uit om uw Elasticsearch-server aan Matterbest te koppelen en de post-index te genereren.

1. Open ** System Console > Environment > Elasticsearch * * (of ** System Console > Advanced > Elasticsearch * * in versies ouder dan 5.12).
2. Set ** enable elasticsearch indexing * * to ` ` true ` ` om de andere instellingen op de pagina in te schakelen. Zodra de configuratie is opgeslagen, worden nieuwe posts die naar de database worden gemaakt automatisch geïndexeerd op de Elasticsearch-server.
3. Stel de verbindingsgegevens van de Elasticsearch-server in:
  a) Enter ** Serververbindingsadres * * voor de Elasticsearch-server die u eerder hebt ingesteld.
  b) (facultatief) Ent
** Servergebruikersnaam * * voor toegang tot de Elasticsearch-server.
    -Opmerking: Voor AWS Elasticsearch laat dit veld leeg.
  c) (Optioneel) Enter ** Server-wachtwoord * * behorend bij de gebruikersnaam.
    -Opmerking: Voor AWS Elasticsearch laat dit veld leeg.
  d) Set ** Enable Cluster Sniffing * * (Optioneel). Hiermee wordt gezocht en wordt automatisch verbinding gemaakt met alle gegevensknooppunten in uw cluster.
    -Opmerking: Voor AWS Elasticsearch moet dit veld worden ingesteld op ` ` false ` `.
4. Klik op ** Test Connection * * and ** Save** de configuratie.
  -Als de serververbinding mislukt, kunt u de configuratie niet opslaan of zoeken met Elasticsearch.
5. Bouw de post-index van bestaande berichten door te klikken op ** Build Index * *.
  -Dit proces kan tot een paar uur duren, afhankelijk van de grootte van de post-database en het aantal berichten. Het voortgangspercentage kan worden gezien als de index wordt gemaakt. Om te voorkomen dat uitvaltijd is ingesteld ** Schakel Elasticsearch for search query's * * in op ` ` false ` ` zodat de databasezoekfunctie beschikbaar is tijdens het indexeringsproces.
6. Elasticsearch inschakelen door instelling ** Elasticsearch inschakelen voor zoekopdrachten * * in ` ` true ` ` `.
  -Opmerking: Het is raadzaam om bulkindexering te voltooien voordat Elasticsearch wordt ingeschakeld, anders zijn de zoekresultaten onvolledig. Als deze instelling ` ` false ` ` is, wordt databasezoekopdracht gebruikt voor alle zoekopdrachten.
7. Start de Matterigste server opnieuw. Opmerking:
    Aanvullende geavanceerde Elasticsearch-instellingen voor grote implementaties kunnen buiten de systeemconsole worden geconfigureerd in het bestand ` `config.json ` `. Lees de ` documentatie voor meer informatie <https: //docs.mattermost.com/administration/config-settings.html#elasticsearch> ` __. .. Opmerking:
    Als uw inzet een groot aantal posten heeft (meestal meer dan 1 miljoen maar niet strikt gedefinieerd), kan het percentage van de herindexering voor een lange tijd bij 99% blijven.

1. Elasticsearch maakt gebruik van een standaard selectie van "stop woorden" om de zoekresultaten relevant te houden. Resultaten voor de volgende woorden worden niet geretourneerd:
  -"a", "an", "en", "zijn", "als", "als", "be", "maar", "maar", "voor", "als", "in", "in", "in", "nee", "niet", "niet", "dat", "of", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", "
2. Het zoeken van stopwoorden in aanhalingstekens levert meer resultaten op dan alleen de zoektermen (` ticket <https://mattermost.atlassian.net/browse/MM-7216> ` __).
3. AWS Elasticsearch implementaties hebben een limiet van 1000 dagen na de geschiedenis die doorzoekbaar is.
4. De zoekresultaten zijn beperkt tot het team van een gebruiker en het kanaal lidmaatschap. Dit wordt afgedwongen door de Matterendste server. De entiteiten worden geïndexeerd in Elasticsearch op een manier die Matterbest toestaat om ze te filteren bij het uitvoeren van een query, dus de Mattermeeste server vernauwt de resultaten op elke Elasticsearch aanvraag die deze filters toepassen.

Veelgestelde vragen (FAQ)
--------------------------------

Moet ik Elasticsearch gebruiken?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Vragen

De Elasticsearch engine is ontworpen voor grote Enterprise-implementaties die zeer efficiënte databasezoekopdrachten willen uitvoeren in een clusteromgeving. De standaard Matterendste database-zoekopdracht begint met prestatievermindering op ongeveer 2,5 miljoen posts, afhankelijk van de specificaties voor de databaseserver. Als u verwacht dat uw Matterste server meer dan 2,5 miljoen berichten heeft, raden wij u aan Elasticsearch te gebruiken voor optimale zoekprestaties.

Welke typen indexen worden gemaakt?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Matterbest maakt drie soorten indexen: gebruikers, kanalen en berichten. Gebruikers en kanalen hebben elk één index. Posts worden op datum geaggregeerd in meerdere indexen.

Kan een beleid voor de rollover van de index worden gedefinieerd?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

De instelling ` AggregatePostsAfterDays <https: //docs.mattermost.com/administration/config-settings.html#aggregate-search-indexes> ` __ configuratie-instelling definieert een sluitingswaarde. Alle posten die aan deze waarde voorafgaan, worden opnieuw geïndexeerd en samengevoegd in nieuwe en grotere indexen. De standaardinstelling is 365 dagen.

Zijn er nieuwe zoekfuncties aangeboden met Elasticsearch?
~ ~ ~ ~ > ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~

De huidige implementatie van Elasticsearch komt overeen met de zoekfuncties die momenteel beschikbaar zijn in de databasezoekfunctie. Het Mattermeeste team werkt aan het uitbreiden van de Elasticsearch functie die is ingesteld met bestandsnaam en content search, datumfilters, en operators en modifiers.

Zijn mijn bestanden opgeslagen in Elasticsearch?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Nee, bestanden en bijlagen worden niet opgeslagen.

Hoe kan ik de systeemgezondheid van een Elasticsearch-server bewaken?
~ ~ ~ ~ > ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~

U kunt deze Prometheus-exporteur gebruiken voor het bewaken van ` diverse metrics <https: //github.com/justwatchcom/elasticsearch_exporter#metrics> ` __ over Elasticsearch: ` justwatchcom/elasticsearch_exporter <https://github.com/justwatchcom/elasticsearch_exporter> ` __.

U kunt ook verwijzen naar dit ` artikel over Elasticsearch performance monitoring <https: //www.datadoghq.com/blog/monitor-elasticsearch-performance-metrics/#key-elasticsearch-performance-metrics-to-monitor> ` __. Het is niet specifiek geschreven voor Prometheus, welke ` Matterbest's performance monitoring <https://docs.mattermost.com/deployment/metrics.html> ` __ system gebruikt, maar heeft verschillende tips en beste praktijken.

Waarom duurt een 25.000 post database een lange tijd om te indexeren in Elasticsearch?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden

Er zijn een aantal mogelijke redenen:

 -Een query op de berichten uit de database is een beperkte bron (d.w.z. de machine waarop de database zich bevindt is niet krachtig genoeg).
 -De Elasticsearch-cluster is de prestaties beperkt (d.w.z., de machines zijn niet krachtig genoeg).
 -De 25.000 berichten worden verspreid over een lange tijd venster, en de ` ` BulkIndexingTimeWindowSeconds ` ` configuratie waarde is te laag voor een efficiënte indexering van een dergelijke "sparse" database. De waarde van die configuratie moet idealiter zodanig worden vastgesteld dat het mediane aantal ambten binnen een bepaalde periode in de database daalt.
is ongeveer 700 tot 800. De standaardwaarde is 1 uur, dus als u veel minder dan 800 posten per uur doet, is de indexering veel trager in termen van "posts per tijdseenheid". Dit kan worden verhoogd door het verhogen van die tijd venster. Welke vorm van gegevens wordt verzonden naar Elasticsearch?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Matterbest communiceert met Elasticsearch via de REST API met behulp van JSON-berichten voor het indexeren en opvragen van entiteiten.

Hoeveel gegevens worden er verzonden naar Elasticsearch en wanneer?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Elke keer dat een bericht wordt gepubliceerd, wordt er een kanaal aangemaakt, of een gebruiker verandert, (hetzij omdat de eigenschappen veranderen, bijvoorbeeld: wijziging van de voornaam of omdat ze lid worden/verlaten van een kanaal), worden de gegevens gekoppeld aan die gebeurtenis naar Elasticsearch gestuurd.

Als zoeken via Elasticsearch is ingeschakeld, genereert elke zoekopdracht een query. Als automatisch aanvullen is ingeschakeld, genereert elke gebruiker of kanaal-automatisch aanvullen die is gekoppeld aan het schrijven van een bericht of een zoekopdracht naar de gebruiker een query.

Hoe weet ik of een Elasticsearch-taak mislukt?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Matterit biedt de status van elke Elasticsearch-indexeertaak in ** System Console > Environment > Elasticsearch * * (of ** System Console > Advanced > Elasticsearch * * in versies ouder dan 5.12). Hier kunt u zien of de taak is geslaagd of mislukt, inclusief de details van de fout.

Fouten worden geretourneerd in de serverlogboeken. Het foutenlogboek begint met de tekenreeks ` ` Failed job ` ` en bevat een job_id key/value pair. Functiefouten bij elasticsearch worden aangeduid met de naam van de werknemer ` ` EnterpriseElasticsearchAggregator ` ` ` en ` ` EnterpriseElasticsearchIndexer ` `. U kunt optioneel een script maken dat programmatisch query's voor dergelijke fouten en waarschuwt het juiste systeem.
