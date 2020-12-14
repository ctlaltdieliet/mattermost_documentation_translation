Configuratie-instellingen
== == == == == == == == == == .. Opmerking:
   De volgorde van de configuratie-instellingen hieronder is een weerspiegeling van een reorganisatie van de System Console in versie 5.12, uitgebracht op 16 juni 2019. Om de configuratie-instellingen te bekijken op basis van de organisatie van de systeemconsole in versies ouder dan versie 5.12, raadpleegt u "deze documentatie <https://docs.mattermost.com/administration/prev-config-settings.html>".

De meeste configuratie-instellingen worden bijgehouden in het configuratiebestand ` `config.json `, dat zich bevindt in de directory ` ` mattermost/config ` `. U kunt het configuratiebestand wijzigen met behulp van de systeemconsole, of door een teksteditor te gebruiken om deze rechtstreeks te wijzigen.

Mattermost moet schrijfmachtigingen hebben voor ` `config.json ` `, anders hebben wijzigingen in de systeemconsole geen effect.

Op nieuwe installaties vanaf versie 5.14 is het bestand ` `default.json ` ` dat wordt gebruikt om de oorspronkelijke ` `config.json ` ` te maken, verwijderd uit het binaire bestand en vervangen door een buildstap die een verse ` `config.json ` ` genereert. Dit is om ervoor te zorgen dat het oorspronkelijke configuratiebestand alle correcte standaardwaarden bevat die in de servercode worden opgegeven. De bestaande ` `config.json ` ` ` bestanden worden niet beïnvloed door deze wijziging.

** Configuratie in database * *

Het opslaan van de configuratie in de database wordt ondersteund in v5.10 en later.  Zie meer informatie over hoe u dit kunt instellen ` hier <https://docs.mattermost.com/administration/config-in-database.html> ` _.

** Omgevingsvariabelen * *

Vanaf Mattermeest versie 3.8 kunt u omgevingsvariabelen gebruiken om de configuratie te beheren. Omgevingsvariabelen vervangen instellingen in ` `config.json ` ` `. Als een wijziging in een instelling in ` `config.json ` ` een herstart vereist om effect te hebben, dan vereisen wijzigingen in de corresponderende omgevingsvariabele ook een herstart van de server.

De naam van de omgevingsvariabele voor elke instelling kan worden afgeleid van de naam van die instelling in ` `config.json ` `. Bijvoorbeeld, om de naam van de site URL-instelling af te leiden:

1. Zoek de instelling in ` `config.json ` `. In dit geval *ServiceSettings.SiteURL*.
2. Voeg ` ` MM_ ` ` toe aan het begin en converteer alle tekens in hoofdletters en vervang de ` `. ` ` met ` ` _ ` `. Bijvoorbeeld, *MM_SERVICESETTINGS_SITEURL*.
3. De instelling wordt ` ` export MM_SERVICESETTINGS_SITEURL="http://example.com ' ` ` `.

Als een instelling is geconfigureerd via een omgevingsvariabele, wordt deze gewijzigd in de systeemconsole uitgeschakeld.

Voor elke instelling die niet is ingesteld in ` `config.json ` ` ` of in omgevingsvariabelen, gebruikt de Mattermeeste server de standaardwaarde zoals hier gedocumenteerd. .. Opmerking:
   Als een instelling is ingesteld via een omgevingsvariabele en eventuele andere wijzigingen worden aangebracht in de systeemconsole, wordt de opgeslagen waarde van de omgevingsvariabele teruggeschreven naar ` `config.json ` ` als waarde van die instelling. .. waarschuwing:
   Omgevingsvariabelen voor Mattermeeste-instellingen die zijn ingesteld binnen de actieve shell worden van kracht bij het migreren van de configuratie. Meer informatie vindt u in ' Configuratie in database <https: //docs.mattermost.com/a
dministration/config-in-database.html> ` _. .. waarschuwing:
   Databaseverbindingen voor de database lezen en zoeken replica's moeten worden geformatteerd met behulp van ` URL-codering <https://www.w3schools.com/tags/ref_urlencode.asp> ` __. Incorrect ingedeelde tekenreeksen kunnen sommige tekens veroorzaken om de tekenreeks te vroeg te beëindigen, wat resulteert in problemen wanneer de verbindingsreeks wordt ontleed. .. Inhoud:
  :diepte: 2 :lokaal:
  :backlinks: item

Info
-----

Instellingen voor het beheren van de editie en licentie voor Mattermeeste Enterprise Edition.

Uitgave en licentie
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Uitgave ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Bekijk de editie van de Mattermeest implementatie.

Licentie ^ ^ ^ ^ ^ ^ ^ ^ ^

U kunt abonnementegegevens bekijken, inclusief het aantal gebruikers en de vervaldatum van uw Mattermeest licentie.

Licentiesleutel ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Licentiebestanden uploaden of verwijderen. Voor meer informatie over Mattermeeste Licenties, zie onze ` veelgestelde vragen over licenties <https: //docs.mattermost.com/overview/license-and-subscription.html#frequently-asked-questions> ` _.

Rapportage
---------

Bekijk de statistieken voor uw algemene implementatie en specifieke teams en voor toegang tot serverlogboeken.

Sitestatistieken
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Statistieken bekijken over actieve gebruikers, teams, kanalen, sessies, webhaken en verbindingen.

Teamstatistieken
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Bekijk de statistieken per team over het aantal actieve gebruikers en de publieke en private kanalen.

Serverlogboeken
~ ~ ~ ~ nopen ~ ~

Logboekregistratie van events op de server bekijken.

Gebruikersbeheer
---------------

Instellingen voor het beheren van gebruikers, gebruikerstoegang, groepen en machtigingen.

Gebruikers
~ ~ ~ geven

Actieve en inactieve gebruikers bekijken en beheren en alle gebruikerssessies intrekken. Toegang tot individuele gebruikers om hun gebruikers-ID te bekijken en de teams te bekijken die ze hebben en wat hun rol is in een team. Bovendien kunt u de gebruiker toevoegen aan andere teams zonder directe toegang tot het team.

Teams (Experimental)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

*Beschikbaar in Enterprise Edition E20 *

Groepsychronisatie beheren voor teams. Zie ` Met behulp van AD/LDAP Synchronized Groups to Manage Team or Private Channel Membership <https://docs.mattermost.com/deployment/ldap-group-constrained-team-channel.html> ` __ voor meer informatie.

Kanalen (Experimental)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

*Beschikbaar in Enterprise Edition E20 *

Groepssychronisatie op kanalen beheren. Zie ` Met behulp van AD/LDAP Synchronized Groups to Manage Team or Private Channel Membership <https://docs.mattermost.com/deployment/ldap-group-constrained-team-channel.html> ` __ voor meer informatie.

Groepen
~ ~ ~ geven

*Beschikbaar in Enterprise Edition E20 *

Groepen biedt beheerders een manier om standaardteams en -kanalen te beheren door de AD/LDAP-groepen te koppelen aan de meeste groepen. Zie de ` Groepen documentatie <https://docs.mattermost.com/deployment/ldap-group-sync.html> ` __ voor meer informatie.

Machtigingen
~ ~ ~ ~ nopen ~ ~

*Beschikbaar in Enterprise Edition E10 en hoger *

Geavanceerde machtigingen bieden Admins een manier om de acties in Matterbest te beperken tot alleen geautoriseerde gebruikers. Zie ` machtigingsdocumentatie <https://docs.mattermost.com/deployment/advanced-permissions.html> ` __ voor meer informatie.

Milieu
-----------

Instellingen voor het configureren van de netwerkomgeving waarin Matterbest in gebruik wordt genomen.

Webserver
~ ~ ~ ~ nopen ~ ~

Voor wijzigingen in de eigenschappen in deze sectie moet eerst een herstart van de server worden uitgevoerd.

Site-URL ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De URL die gebruikers gebruiken voor toegang tot Matterbest. Het poortnummer is vereist als het geen standaardpoort zoals 80 of 443 is.

** Dit veld is vereist in Mattermeest v3.8 en later. * *

In Mattermeest v5.1 en later kan de URL een subpad bevatten, zoals ` `"https: //example.com/company/mattermost " ` `.

Als de URL van de site niet is ingesteld, worden de volgende functies niet correct uitgevoerd:

 -E-mailmeldingen bevatten gebroken links, en e-mail batching zal niet werken.
 -Verificatie via OAuth 2.0, waaronder GitLab, Google en Office 365, zal mislukken.
 -Plugins werken mogelijk niet zoals verwacht. + -------------------------------------------------------------------------------------------------------------------
| De '` `config.json ` ` instelling van deze feature is ` `' "" SiteURL ":" " ` ` met reeksinvoer. |
+ -------------------------------------------------------------------------------------------------------------------

Test live-URL ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze knop bevestigt dat de waarde die is ingevoerd in de URL van de site geldig en live is.

Luisteradres ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het adres en de poort waarop zich moet binden en luisteren. Als u ": 8065" opgeeft, wordt een bind uitgevoerd op alle netwerkinterfaces. Als u '`127.0.0.1:8065' opgeeft, wordt alleen een bind uitgevoerd op de netwerkinterface met dat IP-adres.

Als u een poort kiest van een lager niveau ("systeempoorten" of "welbekende poorten" genoemd, in het bereik van 0-1023), moet u gemachtigd zijn om aan die poort te binden.

Op Linux kunt u gebruik maken van: ` ` sudo setcap cap_net_bind_service = + ep /opt/mattermost/bin/matterbest ` ` om Matterbest toe te staan aan bekende poorten te binden. + ------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is' ` ' "ListenAddress": ": 8065" ` ` met tekenreeksinvoer. |
+ ------------------------------------------------------------------------------------------- +

Poort 80 naar 443 ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Forwards al onveilig verkeer van poort 80 naar beveiligde poort 443.

** False**: Bij gebruik van een proxy zoals NGINX voor Matterit is deze instelling niet nodig en moet worden ingesteld op ` ` false ` `. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "Forward80To443": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Verbindingsbeveiliging ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** Geen **: Matterbest zal verbinding maken via een onbeveiligde verbinding.

**TLS* *: Versleutelde de communicatie tussen Matterclients en uw se
Rver. Raadpleeg 'documentatie <https://docs.mattermost.com/install/config-tls-mattermost.html>' __ voor meer informatie. + --------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is' ` ConnectionSecurity ': "" ` ` met opties ` ` ` ` ` ` en ` ` ` "TLS" ` `. |
+ --------------------------------------------------------------------------------------------------------------------------------------------- +

TLS-certificaatbestand ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het pad naar het certificaatbestand dat moet worden gebruikt voor de TLS-verbindingsbeveiliging. + ------------------------------------------------------------------------------------
| De instelling '`config.json' van deze feature is '`' "TLSCertFile": "" ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------ +

TLS-sleutelbestand ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het pad naar het te gebruiken TLS-sleutelbestand voor de TLS-verbindingsbeveiliging. + ----------------------------------------------------------------------------------- +
| De instelling '`config.json' van deze feature is '`' "TLSKeyFile": "" ` ` met reeksinvoer. |
+ ----------------------------------------------------------------------------------- +

Gebruik Laten We Versleutelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Het automatisch ophalen van certificaten van Let's Encrypt inschakelen. Het certificaat wordt opgehaald wanneer een client probeert verbinding te maken vanuit een nieuw domein. Dit werkt met meerdere domeinen. Zie :doc: ` ../install/config-tls-matterbest ` voor meer informatie over het instellen van Let's Encrypt.

** False**: Handmatige certificaatspecificatie op basis van het ** TLS-certificaatbestand * * en ** TLS-sleutelbestand * * hierboven opgegeven. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` ` instelling van deze feature is ` `' "UseLetsEncrypt": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------------------
   Als Let's Encrypt is ingeschakeld, stuur poort 80 door een firewall, met ` Forward80To443 <https: //docs.mattermost.com/administration/config-settings.html#forward-port-80-to-443 > ` __ ` `config.json ` ` instelling ingesteld op ` ` true ` ` om de Let's Encrypt-certificering te voltooien.

Laten We Het Versleutelingsbestand Versleutelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het pad naar het bestand waar certificaten en andere gegevens over de Versleutelde service van de Let worden opgeslagen. + ----------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "LetsEncryptCertificateCacheFile": "./config/letsencrypt.cache" ` ` met tekenreeksinvoer. |
+ ----------------------------------------------------------------------------------------------------------------------------------- +

Timeout voor lezen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Maximale tijd vanaf wanneer de verbinding wordt geaccepteerd tot wanneer de lopende tekst van de aanvraag volledig wordt gelezen. + ---------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is ` ` ReadTimeout': 300 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------- +

Schrijftimeout ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als u HTTP (onveilig) gebruikt, is dit de maximale toegestane tijd vanaf het einde van het lezen van de opdrachtheaders tot de respons is geschreven. Als u HTTPS gebruikt, is het de totale tijd vanaf het moment dat de verbinding wordt geaccepteerd totdat de respons is geschreven. + ----------------------------------------------------------------------------------------- +
| De ' `config.json ` ` instelling van deze feature is ` ` "WriteTimeout": 300 ` ` met numerieke invoer. |
+ ----------------------------------------------------------------------------------------- +

Timeout inactief (^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Stel een expliciete timeout in op de HTTP-server. Dit is de maximale tijd die is toegestaan voordat een niet-actieve verbinding wordt verbroken. + ----------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` 'IdleTimeout': 60 ` ` met numerieke invoer. |
+ ----------------------------------------------------------------------------------------- +

Gebruik van API v3 eindpunten toestaan ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juni 16, 2018 release *

Stel in op ` ` false ` ` om alle versie 3-eindpunten van de REST API uit te schakelen. Integraties die afhankelijk zijn van API v3 mislukken en kunnen vervolgens worden geïdentificeerd voor migratie naar API v4. API v3 is gedeprecieerd en wordt in de nabije toekomst verwijderd. Zie https://api.mattermost.com voor meer informatie. + --------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableAPIv3 ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ --------------------------------------------------------------------------------------------------------- +

Webservermodus ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ gzip-compressie is van toepassing op de HTML-, CSS-, Javascript-en andere statische contentbestanden die de Mattermost webclient vormen. Het wordt aanbevolen om gzip in te schakelen om de prestaties te verbeteren, tenzij uw omgeving specifieke beperkingen heeft, zoals een webproxy die gzip-bestanden slecht distribueert.

** gzip**: De Mattermeeste server zal statische bestanden gecomprimeerd met gzip dienen om de prestaties te verbeteren.

** Uncompressed**: De Mattermeeste server zal statische bestanden niet comprimeren.

** Disabled**: De meest overeenkomende server heeft geen statische bestanden. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` `-instelling van deze feature is ` ` WebserverMode': "gzip" ` ` met opties ` ` "gzip" ` `, ` ` "ongecomprimeerde" ` ` en ` ` "uitgeschakeld" ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Schakel Het Inschakelen Van Onbeveiligde Uitgaande Verbindingen In ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Uitgaande HTTPS-verzoeken kunnen niet-geverifieerde, zelf-ondertekende certificaten accepteren. Bijvoorbeeld, uitgaande webhooks naar een server met een zelf ondertekend TLS-certificaat, met behulp van een domein, zal worden toegestaan.

** False**: Alleen beveiligde HTTPS-aanvragen zijn toegestaan.

** Beveiligingsbericht: ** Deze functie maakt deze verbindingen gevoelig voor man-in-the-middle-aanvallen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "EnableInsecureOutgoingConnections": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Beheerde-resourcepaden ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Een door komma's gescheiden lijst van paden in het domein Matterit die worden beheerd door een service van derden in plaats van Matterbest zelf. Links naar deze paden worden geopend in een nieuw tabblad/venster door Mattermeeste apps. Als Matterbest bijvoorbeeld wordt uitgevoerd op ' `https: //mymattermost.com ` `, wordt het instellen van deze naar ` ` conference ` ` links zoals ` ` https: //mymattermost.com/conference ` ` ` die in een nieuw venster worden geopend.

Bij gebruik van de Mattermeeste Desktop App is extra configuratie nodig om de link te openen in de Desktop App in plaats van in een browser. Zie ` hier <https://docs.mattermost.com/install/desktop-managed-resources.html> ` _ voor meer informatie. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is ` ` ` ManagedResourcePaths': "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Configuratie opnieuw laden van schijf ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

De werkstroom voor failover zonder downing van de server is het wijzigen van de databaseregel in het ` `config.json ` ` bestand, klik op ** Reload Configuration from Disk * * en klik op ** Recycle Database Connections * * in de sectie ** Geavanceerd > Database * *.

Alle Caches opschonen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Met deze knop worden alle caches voor sessies, accounts en kanalen verwijderd. Implementaties met behulp van hoge beschikbaarheid proberen alle servers in de cluster te wissen. Het verwijderen van de caches kan een negatieve invloed hebben op de prestaties.

Database
~ ~ ~ ~ nten

Voor wijzigingen in de eigenschappen in deze sectie is een restar van de server vereist
t voor het van kracht worden.

Naam stuurprogramma ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze instelling kan alleen worden gewijzigd van ` `config.json ` `-bestand, maar kan niet worden gewijzigd in de gebruikersinterface van de systeemconsole.

** ` ` mysql ` ` * *: Maakt driver aan MySQL database.

** ` ` postgres ` ` ` * *: Kan driver naar PostgreSQL database. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "DriverName": "mysql" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Gegevensbron ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Dit is de verbindingsreeks naar de masterdatabase. Wanneer ** DriverName** is ingesteld op ` ` postgres ` `, gebruik dan een verbindingsreeks in de vorm ` ` postgres: //mmuser:password@localhost: 5432/mattermost_test?sslmode=disable &connect_timeout=10 ` `. Deze instelling kan alleen worden gewijzigd van ` `config.json ` ` bestand. .. Opmerking:
  Als u SSL wilt inschakelen, voegt u ` ` &tls = true ` ` toe aan de verbindingsreeks van de database als uw SQL-stuurprogramma dit ondersteunt. Voeg ` ` &tls = skip-verify ' toe als u certificaten met eigen handtekening gebruikt. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze functie is' ` ' "DataSource": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Maximumaantal niet-actieve verbindingen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Maximumaantal niet-actieve verbindingen dat open is gehouden voor de database. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` ` MaxIdleConns': 10 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Maximumaantal Open Connections ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Maximumaantal geopende verbindingen dat open is gehouden voor de database. + -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
| De '`config.json ` ` instelling van deze feature is ` ` MaxOpenConns': 300 ` ` met numerieke invoer. |
+ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Querytimeout ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het aantal seconden dat moet worden gewacht op een respons van de database na het openen van een verbinding en het verzenden van de query. Fouten die u in de gebruikersinterface of in de logboeken ziet als gevolg van een query-timeout kunnen variëren afhankelijk van het type query. + ------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is' ` QueryTimeout ': 30 ` ` met numerieke invoer. |
+ ------------------------------------------------------------------------------------------------------------------------- +

Uitschakelen van database zoeken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Hiermee schakelt u het gebruik van de database uit om zoekopdrachten uit te voeren. Moet alleen worden gebruikt wanneer andere ` search engines <https://mattermost.com/pl/default-search-engine> ` _ zijn geconfigureerd. Als deze instelling is ingesteld op ` ` true ` ` en een andere zoekmachine niet is geconfigureerd, resulteert dit in lege zoekresultaten.

** False**: zoeken in database is niet uitgeschakeld. + ------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` DisableDatabaseSearch ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ------------------------------------------------------------------------------------------------------------------------- +

Maximale verbindingstijd ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Maximale levensduur voor een verbinding met de database, in milliseconden. Gebruik deze instelling om de maximale tijd te configureren voor het opnieuw gebruiken van een verbinding met de database. De standaardwaarde is een uur (3.600.000 milliseconden). + -------------------------------------------------------------------------------------------------------------------------
| Deze functie '` `config.json ` ` instelling is ` `' "ConnMaxLifetimeMilliseconds": 3600000 ` ` met numerieke invoer. |
+ ------------------------------------------------------------------------------------------------------------------------- +

Minimale hashtag-lengte ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Minimumaantal tekens in een hashtag. Dit moet groter zijn dan of gelijk zijn aan 2. MySQL-databases moeten worden geconfigureerd voor het ondersteunen van zoekreeksen die korter zijn dan drie tekens. Zie de ` documentatie <https://dev.mysql.com/doc/refman/8.0/en/fulltext-fine-tuning.html> ` _. + ------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is' ` '' 'MinimumHashtagLength': 3 ` ` met numerieke invoer. |
+ ------------------------------------------------------------------------------------------------------------------------- +

Bij De Rest Versleutelen Sleutel ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Een sleutel van 32 tekens voor het versleutelen en decoderen van gevoelige velden in de database. U kunt uw eigen cryptografisch willekeurige alfanumerieke reeks genereren, of u kunt naar ** System Console > Environment > Database * * gaan en op ** Regenerate** klikken, waarin de waarde wordt weergegeven totdat u op ** Save** klikt.

Bij gebruik van High Availability moet het zout identiek zijn in elke instance van Mattermost.

Er zijn geen velden versleuteld met ` ` AtRestEncryptKey ` `. Het is een verouderde instelling voor het versleutelen van opgeslagen gegevens in de database. + ------------------------------------------------------------------------------------------ +
| De instelling '`config.json' van deze feature is '`' "AtRestEncryptKey": "" ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------------ +

SQL Statement Logging (Trace) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: SQL-instructies worden weggeschreven naar het logboek voor ontwikkeling.

** False**: SQL-instructies worden niet naar het logboek geschreven. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ' "Trace": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Databaseverbindingen (^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

Met deze knop wordt opnieuw verbinding gemaakt met de database die wordt afgebeeld in de configuratie-instellingen. Alle oude verbindingen zijn gesloten na de twintiger jaren.

De werkstroom voor failover zonder downing van de server is het wijzigen van de databaseregel in het bestand ` `config.json ` `, klik op ** Reload Configuration from Disk * * in de sectie ** Environment > Database * * en klik op ** Recycle Database Connections * *.

Elasticsearch
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

*Beschikbaar in Enterprise Edition E20 *

Voor wijzigingen in de eigenschappen in deze sectie moet eerst een herstart van de server worden uitgevoerd.

Indexering van elasticzoekindexen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Het indexeren van nieuwe berichten vindt automatisch plaats. Zoekquery's maken gebruik van de databasezoekopdracht tot ** Enable Elasticsearch for search queries * * is ingeschakeld. ` Meer informatie over Elasticsearch in onze documentatie <https://about.mattermost.com/default-elasticsearch-documentation/> ` __.

** False**: Elasticsearch-indexering is uitgeschakeld en nieuwe posts worden niet geïndexeerd. Als de indexering is uitgeschakeld en opnieuw is ingeschakeld nadat een index is gemaakt, is het raadzaam om de index te verwijderen en opnieuw op te bouwen om te zorgen voor volledige zoekresultaten. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "EnableIndexing": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Serververbindingsadres: ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het adres van de Elasticsearch-server. ` Meer informatie over Elasticsearch in onze documentatie <https://about.mattermost.com/default-elasticsearch-documentation/> ` __. + ------------------------------------------------------------------------------------------------------------------------ +
| De instelling '` `config.json `' van deze feature is '`' "ConnectionUrl": "" ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------------------------------------------ +

TLS-verificatie overslaan ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Hiermee wordt de verificatiestap voor het certificaat overgeslagen voor TLS-verbindingen. Niet aanbevolen voor productieomgevingen waarbij TLS vereist is. Alleen voor tests.

** False**: Matterbest slaat certificaatverificatie niet over. + ------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` ` SkipTLSVerification': false ` ` met booleaanse invoer. |
+ ------------------------------------------------------------------------------------------------------- +

Servergebruikersnaam ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) De gebruikersnaam voor verificatie bij de Elasticsearch-server. + -------------------------------------------------------------------------------------------------------------------
| De ' ` `config.json ` ` instelling van deze feature is ` ` "Gebruikersnaam": "" ` ` met reeksinvoer. |
+ -------------------------------------------------------------------------------------------------------------------

Serverwachtwoord ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Het wachtwoord voor verificatie bij de Elasticsearch-server. + -------------------------------------------------------------------------------------------------------------------
| De instelling '`config.json `' van deze feature is '`' "Wachtwoord": "" ` ` met reeksinvoer. |
+ -------------------------------------------------------------------------------------------------------------------

Enable Cluster Sniffen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Sniffing vindt en maakt automatisch verbinding met alle gegevensknooppunten in uw cluster.

** False**: Sniffing is uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "Sniff": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Bulkindexering ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Met deze knop start u een bulkindex van alle bestaande berichten in de database. Als het indexeringsproces wordt geannuleerd, zijn de index en de zoekresultaten onvolledig.

Indexen opschonen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Met deze knop wordt de gehele Elasticsearch-index verwijderd. Wordt gewoonlijk alleen gebruikt als de i
ndex is beschadigd en zoek is niet gedragen zoals verwacht. Na het opschonen van de index kan een nieuwe index worden gemaakt met de knop ** Bulkindex * *.

De elasticsearch voor zoekquery's inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Elasticsearch wordt gebruikt voor alle zoekopdrachten met behulp van de nieuwste index. Zoekresultaten kunnen onvolledig zijn totdat een bulkindex van de bestaande post-database is voltooid.

** False**: Databasezoekopdracht wordt gebruikt voor zoekopdrachten. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "EnableZoeken": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Elasticsearch inschakelen voor Autocomplete query's ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Elasticsearch wordt gebruikt voor alle automatisch aanvullen query's op gebruikers en kanalen met behulp van de nieuwste index. Resultaten van automatisch aanvullen kunnen onvolledig zijn totdat een bulkindex van de bestaande gebruikers-en kanalen-database is voltooid.

** False**: Database autocompleet is gebruikt. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableAutocomplete ": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Bestandsopslag
~ ~ ~ ~ nopen ~ ~

Mattermeest ondersteunt momenteel het opslaan van bestanden op het lokale bestandssysteem en Amazon S3 of S3 compatibele containers. .. Opmerking:
  We hebben Matterbest getest met ` MinIO <https://www.minio.io/> ` __ en ` Digital Ocean Spaces <https://www.digitalocean.com/docs/spaces/> ` _ producten, maar niet alle S3 compatibele containers op de markt. Als u op zoek bent naar andere S3 compatibele containers te gebruiken adviseren wij u uw eigen testen te voltooien.

Bestandsopslagsysteem ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
| ``config.json ` ` instelling | ` ` DriverName ` ` | + ------------------------- + ----------------------- +
| Toegestane waarden | ` ` ` local ' ` ` (standaard) |
| | ` ` ` amasun3 " ` ` |
+ ------------------------- + ----------------------- +

Dit selecteert welk bestandssysteem wordt gebruikt: Lokaal bestandssysteem of Amazon S3.

** Lokaal bestandssysteem * *: Bestanden en afbeeldingen worden opgeslagen in de opgegeven lokale bestandsdirectory.

** Amazon S3 * *: Bestanden en afbeeldingen worden opgeslagen op Amazon S3 op basis van de verstrekte toegangssleutel, emmer en regio velden. Het ` ` ' amasun3 " ` ` driver is compatibel met MinIO (Beta) en Digital Ocean Spaces gebaseerd op de verstrekte toegangssleutel, emmer en regio velden.

Lokale Opslagdirectory ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De lokale directory waarnaar bestanden worden geschreven wanneer het bestandsopslagsysteem is ingesteld op ` ` 'lokaal' ` `. Dit is relatief ten opzichte van de directory die Matterbest is geïnstalleerd en de standaardwaarde is ` ` "./data" ` ` Wanneer File Storage System is ingesteld op S3 heeft deze instelling geen effect. + ------------------------- + ------------------------------------------------------------------------------------------ +
| ``config.json ` ` instelling | ` ` Directory ` ` ` | + ------------------------- + ------------------------------------------------------------------------------------------ +
| Toegestane waarden | Elke directory die door de gebruiker Matterbest kan worden geschreven, is actief. De standaardwaarde is '`' ./data/ ' ` `. |
+ ------------------------- + ------------------------------------------------------------------------------------------ +

Maximale bestandsgrootte ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Maximale bestandsgrootte voor berichtbijlagen die in megabytes zijn opgegeven in de gebruikersinterface van de systeemconsole. Geconverteerd naar bytes in ` `config.json ` ` op 1048576 bytes per megabyte. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` ` MaxFileSize': 52428800 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- + .. waarschuwing:: Controleer of het servergeheugen uw instelling kan ondersteunen. Grote bestandsgroottes verhogen het risico van crashes op de server en mislukte uploads als gevolg van netwerkstoringen. .. Opmerking:
  Als u gebruik maakt van een proxy of load balancer voor Matterbest zijn instellingen moeten dienovereenkomstig worden aangepast. Gebruik voor NGINX ` ` client_max_body_size ` `. Voor Apache gebruik ` ` LimitRequestBody ` `.

Amazon S3 Bucket ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De naam van de bucket voor uw S3-compatibele objectopslag-instance. + ------------------------- + ---------------------------------------------- +
| ``config.json ` ` instelling | ` ` AmazonS3Bucket ` ` ` | + ------------------------- + ---------------------------------------------- +
| Toegestane waarden | Een tekenreeks met de S3-compatibele bucketnaam. |
+ ------------------------- + ---------------------------------------------- +

Amazon S3 Regio ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De AWS regio die u hebt geselecteerd bij het maken van uw S3-emmer. Als er geen regio is ingesteld, probeert Matterbest de juiste regio te verkrijgen van AWS en wordt deze ingesteld op ` ` 'us-east-1' ` als er geen wordt gevonden. Voor MinIO of Digital Ocean Spaces laat u deze instelling leeg. + ------------------------- + -----------------------------------------------------
| ``config.json ` ` instelling | ` ` AmazonS3Region ` ` ` | + ------------------------- + ----------------------------------------------------- +
| Toegestane waarden | Een tekenreeks met de AWS-regio die de emmer bevat. |
+ ------------------------- + -----------------------------------------------------

Amazon S3 Access Key-ID ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Dit is vereist voor toegang, tenzij u een ` Amazon S3 IAM Role <https://about.mattermost.com/default-iam-role-settings-documentation> ` __ met Amazon S3 gebruikt. De EC2-beheerder kan u het toegangssleutel-ID leveren. + ------------------------- + ---------------------------------------------------------------------- +
| ``config.json ` ` instelling | ` ` AmazonS3AccessKeyId ` ` | + ------------------------- + ---------------------------------------------------------------------- +
| Toegestane waarden | Een tekenreeks met de toegangssleutel voor de S3-compatibele opslaginstantie. |
+ ------------------------- + ---------------------------------------------------------------------- +

Amazon S3-eindpunt ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Hostnaam van uw S3-compatibele instantie. De standaardwaarde is '`"s3.amazonaws.com' ` `. .. Opmerking:
  Voor digitale oceaanruimten moet de hostnaam worden ingesteld op ` ` "<region>.digitaloceanspaces.com" ` `, waarbij ` ``` ` de afkorting is voor de regio die u hebt gekozen bij het instellen van de ruimte. Het kan ` ` nyc3 ` `, ` ` ams3 ` `, of ` ` sgp1 ` ` `. + ------------------------- + ------------------------------------------------------------------- +
| ``config.json ` ` instelling | ` ` AmazonS3Endpoint ` ` | + ------------------------- + ------------------------------------------------------------------- +
| Toegestane waarden | Een tekenreeks met de hostnaam van de S3-compatibele opslaginstantie. |
+ ------------------------- + ------------------------------------------------------------------- +

Amazon S3 Secret Access Key ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De geheime toegangssleutel die is gekoppeld aan uw Amazon S3 Access Key-ID. + ------------------------- + ----------------------------------------------------------------------------- +
| ``config.json ` ` instelling | ` ` AmazonS3SecretAccessKey ` ` ` | + ------------------------- + ----------------------------------------------------------------------------- +
| Toegestane waarden | Een tekenreeks met de geheime toegangssleutel voor de S3-compatibele opslaginstantie. |
+ ------------------------- + ----------------------------------------------------------------------------- +

Secure Amazon S3 Connections ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Hiermee kunnen alleen beveiligde Amazon S3-verbindingen worden beveiligd.

** False**: Hiermee kunnen onzekere verbindingen met Amazon S3. + ------------------------- + ---------------------------------------------- +
| ``config.json ` ` instelling | ` ` AmazonS3SSL ` ` ` | + ------------------------- + ---------------------------------------------- +
| Toegestane waarden | ` ` true ` ` of ` ` false ` ` `. Standaard ingesteld op ` ` true ` `. |
+ ------------------------- + ---------------------------------------------- +

Server-Side Encryption for Amazon S3 ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

** True**: Versleutelde bestanden in Amazon S3 met server-side encryptie met ` Amazon S3-managed keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html> ` __.

** False**: Niet versleutelen bestanden in Amazon S3. .. opmerking: De versleuteling van de server werkt alleen met Amazon S3. + ------------------------- + ----------------------------------------------- +
| ``config.json ` ` instelling | ` ` AmazonS3SSE ` ` | + ------------------------- + ----------------------------------------------- +
| Toegestane waarden | ` ` true ` ` of ` ` false ` ` `. Standaard ingesteld op ` ` false ` `. |
+ ------------------------- + ----------------------------------------------- +

Amazon S3-foutopsporing inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Wanneer ` ` true ` ` `, log extra debugging informatie naar de systeemlogs. Standaard ingesteld op ` ` false ` ` in productie.

** False**: Er is geen Amazon S3-foutopsporingsinformatie opgenomen in de systeemlogboeken. + ------------------------- + ----------------------------------------------- +
| ``config.json ` ` instelling | ` ` AmazonS3Trace ` ` ` | + ------------------------- + ----------------------------------------------- +
| Toegestane waarden | ` ` true ` ` of ` ` false ` ` `. Standaard ingesteld op ` ` false ` `. |
+ ------------------------- + ----------------------------------------------- +

Verbinding testen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Zorgt ervoor dat de gebruiker toegang heeft tot de server en dat de instellingen geldig zijn.

Afbeeldingsproxy
~ ~ ~ ~ nopen ~ ~

Afbeeldingsproxy ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als ` ` true ` ` is, schakelt u een afbeeldingsproxy in voor het laden van externe afbeeldingen. De image-proxy wordt gebruikt door de Mattermeeste apps om te voorkomen dat ze rechtstreeks verbinding maken met servers op afstand. Deze anonimiseert hun verbindingen en voorkomt dat ze toegang krijgen tot onveilige inhoud.

Zie de :doc: ` documentatie <image-proxy>` voor meer informatie. + ---------------------------------------------------------------------------------------------------------------------
| De instelling ``config.json van deze feature is ` ` ' "Inschakelen": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------

Afbeeldingsproxytype ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het type afbeeldingsproxy dat Matterbest gebruikt. Er zijn twee opties:

** local**: De Mattermeeste server zelf fungeert als de afbeeldingsproxy. Dit is de standaardoptie.

** atmos/camo**: Een externe ' atmos/camo <https://github.com/atmos/camo> ` _ image proxy wordt gebruikt.

Zie de ` documentatie <https: //docs.mattermost.com/administration/image-proxy.html#atmos-camo-image-proxy> ` _ voor meer informatie. + -------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` ` ImageProxyType ":" local "` `, met opties ` ` ` lokale' ` ` en ` ` ` atmos/camo" ` ` voor de bovenstaande instellingen. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------------- +

URL van afbeeldingsproxy op afstand ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De URL van de ` ` atmos/camo ` ` proxy. Deze instelling is niet nodig bij gebruik van de lokale afbeeldingsproxy. + ---------------------------------------------------------------------------------------------------------------------
| De instelling ``config.json van deze feature is ` ` ' "RemoteImageProxyURL": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------

Opties voor afbeeldingsproxy op afstand ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De URL-ondertekeningssleutel is doorgegeven aan een ` ` atmos/camo ` ` image-proxy. Deze instelling is niet nodig bij gebruik van de lokale imageproxy.

Zie de ` documentatie <https: //docs.mattermost.com/administration/image-proxy.html#atmos-camo-image-proxy> ` _ voor meer informatie. + ---------------------------------------------------------------------------------------------------------------------
| De instelling '` `config.json `' van deze feature is ` ` "" RemoteImageProxyOptions ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------

SMTP
~ ~ ~ geven

SMTP-server ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Locatie van SMTP-e-mailserver. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "SMTPServer": "" ` ` met string invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

SMTP-serverpoort ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Poort van SMTP-e-mailserver. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is' ` ' "SMTPPort": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

SMTP-servertimeout ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De maximale tijd (in seconden) die is toegestaan voor het tot stand brengen van een TCP-verbinding tussen Matterbest en de SMTP-server, inactief te zijn voordat deze wordt beëindigd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` ` SMTPServerTimeout': 10 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

SMTP-authenticatie inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: SMTP-gebruikersnaam en -wachtwoord worden gebruikt voor verificatie bij de SMTP-server.

** False**: Matterbest probeert niet te verifiëren bij de SMTP-server. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` `' EnableSMTPAuth ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

SMTP-servergebruikersnaam ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De gebruikersnaam voor verificatie bij de SMTP-server. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` SMTPUsername ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

SMTP-serverwachtwoord ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het wachtwoord dat hoort bij de SMTP-gebruikersnaam. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` 'SMTPPassword ': "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- + .. _email-tls:

Verbindingsbeveiliging ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** Geen **: E-mail versturen over een onbeveiligde verbinding.

**TLS* *: De communicatie tussen Matterbest en uw e-mailserver is versleuteld.

**STARTTLS* *: Pogingen om een bestaande onbeveiligde verbinding met een beveiligde verbinding te upgraden met TLS. + --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ConnectionSecurity ': "" ` met opties ` ` ` ` ` ` ` ` ` TLS "` ` en ` ` ` STARTTLS" ` `. |
+ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Controle van servercertificaat overslaan ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Matterbest controleert het certificaat van de e-mailserver niet.

** False**: Matterbest controleert het certificaat van de e-mailserver. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` ` SkipServerCertificateVerification': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Inschakelen van beveiligingswaarschuwingen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Schakel de systeembeheerders in om per e-mail te worden gewaarschuwd als er een relevante waarschuwing voor de beveiliging is aangekondigd. Vereist e-mail om te kunnen worden ingeschakeld. Voor meer informatie over deze functie raadpleegt u :doc: ` telemetrie `.

** False**: Beveiligingswaarschuwingen zijn uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "EnableSecurityFixAlert": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Push-berichtenserver
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Push-berichten inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Uw Mattermeeste server verzendt mobiele push-meldingen naar de server die is opgegeven in ** PushNotificationServer**.

** False**: Mobiele push-meldingen zijn uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` 'SendPushNotifications ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Push-berichten-server ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Locatie van de Mattermeest Push Notification Service (MPNS), die push-meldingen van Mattermeest naar services stuurt, zoals Apple Push Notification Service (APNS) en Google Cloud Messaging (GCM).

Om te bevestigen dat de push-berichten werken, maakt u verbinding met de ` Matterbest iOS-app op iTunes <https://about.mattermost.com/mattermost-ios-app> '__ of de ` Mattermeeste Android-app op Google Play <https://about.mattermost.com/mattermost-android-app>' __:

-Voor Enterprise Edition, typt u ' https: //push.mattermost.com ` ` voor de push-berichtenserver die in de Verenigde Staten wordt gehost. Als u liever een push-meldingsserver wilt gebruiken in Duitsland, typt u ' https: //hpns-de.mattermost.com/ ` `.
-Voor Team Edition, typt u ' `https: //push-test.mattermost.com ` `.

Bekijk de volledige documentatie over ` push notificaties en mobiele toepassingen <https://docs.mattermost.com/deployment/push.html> ` __ inclusief begeleiding bij het compileren van uw eigen mobiele apps en MPNS voordat u de productie in gebruik neemt. .. Opmerking:
  De ' `https: //push-test.mattermost.com ` ` ` server is beschikbaar voor het testen van push-berichten voorafgaand aan het compileren van uw eigen service. Zorg ervoor dat ` lees over de beperkingen <https: //docs.mattermost.com/deployment/push.html#push-notifications-for-team-edition-users> ` _. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` PushNotificationServer ":" https: //push-test.mattermost.com " ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Max berichten per kanaal ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Maximumaantal gebruikers in een kanaal vóór @all, @here, en @channel geen meldingen meer verzenden om de prestaties te maximaliseren.

Als u deze waarde wilt verhogen, is de aanbeveling om het een beetje te verhogen en de systeemgezondheid te bewaken met ` performance monitoring metrics <https://docs.mattermost.com/deployment/metrics.html> ` __. We raden ook aan alleen deze waarde te verhogen als grote kanalen de permissies hebben beperkt voor wie kan posten naar het kanaal (bijvoorbeeld een alleen-lezen kanaal). + -------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` MaxNotificationsPerChannel ": 1000 ` ` met numerieke invoer. |
+ -------------------------------------------------------------------------------------------------------- +

** Problemen met push-berichten oplossen * *

Om de push-berichten te bevestigen werkt u:

1. Ga naar ** System Console > Notifications > Environment > Push Notification Server > Enable Push Notifications * * and select ** Use TPNS connection to send notifications to iOS and Android apps * *.
2. Set ** Push Notification Server * * to ` `https: //push.mattermost.com ` ` if using Enterprise Edition. Als u Team Edition gebruikt, stelt u de waarde in op ' `https: //push-test.mattermost.com ` `.
3. Om push-berichten te bevestigen werkt u met de ` Matterbest iOS App op iTunes <https://about.mattermost.com/mattermost-ios-app> ` __ of de ` Mattermeeste Android App op Google Play <https://about.mattermost.com/mattermost-android-app> ' __ en meld u aan bij uw teamsite.
4. Sluit de app op uw apparaat en sluit alle andere verbindingen met uw teamsite.
5. Wacht 5 minuten en een ander teamlid sturen u een direct bericht, die moet leiden tot een push-bericht naar de Mattermeeste app op uw mobiele apparaat.
6. U moet een push-bericht ontvangen op uw apparaat dat u waarschuwt voor het directe bericht.

Als u geen waarschuwing hebt ontvangen:

1. Set ** System Console > Environment > Logging > File Log Level * * to *DEBUG* (zorg ervoor dat u dit instelt op *INFO* na het oplossen van problemen met het opslaan van schijfruimte).
2. Herhaal de bovenstaande stappen.
3. Ga naar ** System Console > Reporting > Server Logs * * en kopieer de log-uitvoer naar een bestand.
4. Voor klanten van Enterprise Edition: ` dien een ondersteuningsaanvraag in bij het bestand <https://mattermost.zendesk.com/hc/en-us/requests/new> ` __. Voor gebruikers van Team Edition start u een thread in het ` troubleshooting forum <https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150> ` __ voor peer-to-peer ondersteuning. .. _hoge beschikbaarheid:

Hoge beschikbaarheid
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

*Beschikbaar in Enterprise Edition E20 *

Voor wijzigingen in de eigenschappen in deze sectie moet eerst een herstart van de server worden uitgevoerd.

Als de modus voor hoge beschikbaarheid is ingeschakeld, is de systeemconsole ingesteld op alleen-lezen en kunnen de instellingen alleen worden gewijzigd door rechtstreeks het configuratiebestand te bewerken. Voor het testen en valideren van een installatie voor hoge beschikbaarheid kunt u ` ` ReadOnlyConfig ` ` instellen op ` ` false ` `, waarmee wijzigingen in de System Console kunnen worden opgeslagen in het configuratiebestand.

Meer informatie over het configureren van hoge beschikbaarheid vindt u in 'High Availability Cluster <https://docs.mattermost.com/deployment/cluster.html>' _.

Modus voor hoge beschikbaarheid inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: De Matterendste server probeert communicatie tussen knooppunten te maken met de andere servers in de cluster die dezelfde clusternaam hebben. Hiermee wordt de werkstand van de systeemconsole ingesteld op de werkstand Alleen lezen, zodat de bestanden van de server ' `config.json ` ` ` server synchroon blijven.

** False**: Matterbest High Availability is uitgeschakeld. + ----------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` inschakelen ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ----------------------------------------------------------------------------------------------------- +

Clusternaam ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De cluster om mee te doen met de naam. Alleen knooppunten met dezelfde clusternaam worden samengevoegd. Dit is om Blue-Green-implementaties of staging naar dezelfde database te ondersteunen. + ------------------------------------------------------------------------------------ +
| De '`config.json ` `-instelling van deze feature is' ` 'ClusterName': ' " ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------ +

Hostnaam overschrijven ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als dit veld leeg is, probeert Matterbest de hostnaam van het besturingssysteem te krijgen of het IP-adres te gebruiken. U kunt de hostnaam van deze server vervangen door deze eigenschap. Het is niet aan te raden om de hostnaam te vervangen, tenzij dit nodig is. Deze eigenschap kan indien nodig ook worden ingesteld op een specifiek IP-adres. Zie ook ` cluster discovery <https: //docs.mattermost.com/deployment/cluster.html#cluster-discovery> ` _ voor meer informatie. + ----------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` "OverrideHostname": "" ` ` met reeksinvoer. |
+ ----------------------------------------------------------------------------------------- +

IP-adres gebruiken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: De cluster probeert te communiceren met behulp van het IP-adres.

** False**: De cluster probeert te communiceren met de hostnaam. + ---------------------------------------------------------------------------------------------------------
| De '``config.json ` ` instelling van deze feature is ` `' "UseIpAddress": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ --------------------------------------------------------------------------------------------------------- +

Experimentele Roddels Gebruiken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: De server probeert te communiceren via het roddelprotocol over de roddelpoort.

** False**: De server probeert te communiceren via de streamingpoort.

Merk op dat het gossip port en gossip protocol worden gebruikt om de clustergezondheid te bepalen, zelfs als deze instelling ` ` false ` ` is. + ------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ' "UseExperimentalGossip": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ -------------------------------------------------------------------------------------------------------------------

Experimentele Roddelversleuteling ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Alle communicatie via de cluster met behulp van het roddel protocol zal worden versleuteld.

** False**: Alle communicatie met roddelprotocol blijft niet versleuteld.

De versleuteling gebruikt standaard AES-256 en is niet configureerbaar door het ontwerp. U kunt de rijwaarde ' ` ClusterEncryptionKey ` ` echter handmatig instellen in de tabel Systemen. Een sleutel is een bytereeks geconverteerd naar base64. Het moet 16, 24 of 32 bytes zijn om AES-128, AES-192 of AES-256 te selecteren. + -------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "EnableExperimentalGossipEncryption": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ -------------------------------------------------------------------------------------------------------------------------------- + Gossip Port ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De haven voor het roddelprotocol. Zowel UDP als TCP moeten op deze poort worden toegestaan. + ------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is ` ` GossipPort': 8074 ` ` met numerieke invoer. |
+ ------------------------------------------------------------------------------------------- +

Streamingpoort ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De poort die wordt gebruikt voor het streamen van gegevens tussen servers. + ---------------------------------------------------------------------------------------------- +
| De '`config.json `'-instelling van deze feature is ` ` StreamingPort ': 8075 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------- +

Inter-Node Luisteren Adres ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Deprecated. Niet gebruikt in versie 4.0 en hoger *

Het adres waar de Mattermeeste Server naar luistert voor communicatie tussen knooppunten. Bij het instellen van uw netwerk moet u het luisteradres beveiligen zodat alleen machines in de cluster toegang hebben tot die poort. Dit kan op verschillende manieren worden gedaan, bijvoorbeeld door gebruik te maken van IPsec, beveiligingsgroepen of routetabellen. + ----------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` ` instelling van deze feature is ` ` "" InterNodeListenAddress ":": 8075 " ` ` met string invoer. |
+ ----------------------------------------------------------------------------------------------------- +

URL's tussen knooppunten ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Deprecated. Niet gebruikt in versie 4.0 en hoger *

Een lijst van alle machines in de cluster, zoals ` `["http://10.10.10.2 "," http://10.10.10.4 "] ` `. Het wordt aanbevolen om de interne IP-adressen te gebruiken zodat alle verkeer beveiligd kan worden. + -------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json `'-instelling van deze feature is ` ` "" "InterNodeUrls": [] ` ` met tekenreeksinvoer bestaande uit de machines in de cluster. |
+ -------------------------------------------------------------------------------------------------------------------------------------- +

Snelheidsbeperking
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Voor wijzigingen in de eigenschappen in deze sectie moet eerst een herstart van de server worden uitgevoerd.

Snelheid van tarief beperken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: API's zijn throttled voor de snelheid die is opgegeven door ** PerSec**.

** False**: API's zijn niet throttled. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` inschakelen ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Maximumaantal query's per seconde ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Throttle API op dit aantal verzoeken per seconde als snelheidsbeperking is ingeschakeld.

De locatie van de logboekbestanden. Als dit veld leeg is, worden deze opgeslagen in de directory ` ./logs ` `. Het pad dat u instelt moet bestaan en Mattermost moet schrijfrechten hebben. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` PerSec ": 10 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Maximale burst-grootte ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Standaard ingesteld op ` ` true ` ` in productie. Wh
en ` ` true ` `, zijn vastgelegde gebeurtenissen geschreven in een machineleesbare JSON-indeling. Anders worden ze afgedrukt als platte tekst.

Maximumaantal aanvragen dat is toegestaan boven de limiet voor de tweede query. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is' ` MaxBurst ': 100 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Grootte geheugenruimte ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Maximumaantal gebruikerssessies dat is verbonden met het systeem, zoals bepaald door ` ` VaryByRemoteAddr ` ` en ` ` VaryByHeader ` ` variabelen.

Standaard ingesteld op het aantal gebruikers in het systeem. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` MemoryStoreSize ": 10000 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

De snelheidslimiet per adres op afstand ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Tarieflimiet API-toegang per IP-adres. Aanbevolen om in te stellen op ` ` true ` ` als je een proxy gebruikt.

** False**: Tariefbeperking varieert niet per IP-adres. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "" VaryByRemoteAddr ": true ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Limietsnelheid per gebruiker (^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: API-toegang voor snelheidslimiet per gebruiker-verificatietoken. Aanbevolen om in te stellen op ` ` true ` ` als je een proxy gebruikt.

** False**: De snelheidsbeperking is niet afhankelijk van het token voor gebruikersverificatie. + --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "VaryByUser": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Limietsnelheid per HTTP-header ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De snelheidsbeperking voor het HTTP-headerveld dat is opgegeven (bijvoorbeeld bij het configureren van Ngnix ingesteld op ` ` X-Real-IP ` `, bij het configureren van het Amazonegebied ingesteld op ` ` X-Doorgezonden-Voor ` `). Aanbevolen te worden ingesteld als u een proxy gebruikt. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "VaryByHeader": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Geavanceerde logboekregistratie ~ ~ ~ ~ ~ ~ ~ melden

*Beschikbaar in Enterprise Edition E20 *

Uitvoerlogboeken naar meerdere doelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Elke combinatie van lokale bestands-, syslog-en TCP-socketdoelen toestaan en logboekrecords verzenden naar meerdere doelen:

-Meerdere lokale bestandsdoelen: Ondersteunt rotatie en compressie veroorzaakt door grootte en/of duur.
-Meerdere syslogs: ondersteunt lokale en remote syslog servers, met of zonder TLS transport.
-Meerdere TCP-sockets: TCP-socketdoel kan worden geconfigureerd met een IP-adres of domeinnaam, poort en optioneel TLS-certificaat.

Deze drie doelen zijn gekozen om de overgrote meerderheid van log aggregators en andere log-analyse tools te ondersteunen zonder dat u extra software hoeft te installeren. 

Naast de standaard logniveaus (trace, debug, info, panic) kunnen ook discrete logniveaus worden opgegeven. .. Opmerking:
   Beschikbare discrete logniveaus worden weergegeven in ` `mattermost-server:mlog/levels.go ` `. Logboeken worden asynchroon opgenomen om de wachttijd voor de beller te verminderen. Geavanceerde logboekregistratie ondersteunt hot-reloading van logboekconfiguratie.

De instelling '`config.json' van deze feature is ' `LogSettings.AdvancedLoggingConfig ` ` die een filespec kan bevatten naar een ander configuratiebestand, een database-DSN of een JSON. De opties worden beschreven in dit txt-bestand: ` Log Settings Options <https://github.com/mattermost/docs/files/5066579/Log.Settings.Options.txt> ` _. Sample config: ` Advanced Logging Options Sample.json.zip <https://github.com/mattermost/docs/files/5066597/Advanced.Logging.Options.Sample.json.zip> ` _.

Standaard ~ ~ ~ ngen ~ ~ ~ ~ ~ ~ ~ ~ ngen

*Beschikbaar in alle edities *

Uitvoerlogboeken op console ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ Opmerking:
   Logboeken worden geroteerd zodra het logboekbestand een grootte van 100 MB of meer bereikt.

** True**: Berichten voor uitvoer naar de console op basis van de optie ` ` ConsoleLevel ` `. De server schrijft berichten naar de standaarduitvoerstroom (stdout).

** False**: De berichten van het uitvoerlogboek worden niet naar de console geschreven.

Wijzigingen in deze instelling vereisen een herstart van de server voordat deze wordt uitgevoerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` ` EnableConsole ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Consoleslogniveau ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Detailniveau waarop logboekevents worden weggeschreven naar de console wanneer ` ` EnableConsole ` ` = ` ` true ` ` is.

**DEBUG* *: Hiermee worden de foutopsporingsproblemen voor ontwikkelaars uitgebreid afgedrukt.

**FOUT* *: Alleen foutberichten.

**INFO* *: Foutberichten en informatie over opstarten en initialisatie. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "ConsoleLevel": "DEBUG" ` ` met opties ` ` "DEBUG" ` `, ` ` "ERROR" ` ` en ` ` "INFO" ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Uitvoerconsolelogboeken als JSON ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Standaard ingesteld op ` ` true ` ` in productie. Wanneer ` ` true ` ` zijn, worden vastgelegde gebeurtenissen geschreven in een machineleesbare JSON-indeling. Anders worden ze afgedrukt als platte tekst.

** True**: Logged events zijn geschreven in een machineleesbare JSON-indeling.

** False**: Logged events zijn geschreven in platte tekst.

Wijzigingen in deze instelling vereisen dat de server opnieuw wordt gestart voordat het effect wordt uitgevoerd. + ---------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "ConsoleJson": true ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------- +

Uitvoerlogboeken naar bestand ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Standaard ingesteld op ` ` true ` ` in productie. Wanneer ` ` true ` ` zijn, worden vastgelegde gebeurtenissen geschreven naar het ` `mattermost.log ` ` bestand in de directory die is opgegeven door de instelling ** FileLocation**. De logboeken worden gearchiveerd in een bestand in dezelfde directory, en krijgen een naam met een datestamp en serienummer. Bijvoorbeeld: ```mattermost.2017-03-31.001 ` `.

** True**: Logboekbestanden worden weggeschreven naar bestanden die zijn opgegeven in ` ` FileLocation ` `.

** False**: Logbestanden zijn niet geschreven.

Wijzigingen in deze instelling vereisen dat de server opnieuw wordt gestart voordat het effect wordt uitgevoerd. + ---------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` ` EnableFile': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------- +

Bestandslogniveau ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Detailniveau waarop logboekevents worden weggeschreven naar logboekbestanden wanneer ` ` EnableFile ` ` = ` ` true ` ` is.

**FOUT* *: Alleen foutberichten.

**INFO* *: Foutberichten en informatie over opstarten en initialisatie.

**DEBUG* *: Hoge details afdrukken voor foutopsporingsproblemen voor ontwikkelaars. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` FileLevel ': "INFO" ` met opties ` ` ` DEBUG "` `, ` `" ERROR "` ` en ` `" INFO " ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Uitvoerbestandlogboeken als JSON ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Standaard ingesteld op ` ` true ` ` in productie. Wanneer ` ` true ` ` zijn, worden vastgelegde gebeurtenissen geschreven in een machineleesbare JSON-indeling. Anders worden ze afgedrukt als platte tekst.

** True**: Logged events zijn geschreven in een machineleesbare JSON-indeling.

** False**: Logged events zijn geschreven in platte tekst.

Wijzigingen in deze instelling vereisen dat de server opnieuw wordt gestart voordat het effect wordt uitgevoerd. + ---------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` ` instelling van deze feature is ` ` FileJson': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------- +

Bestandslogdirectory ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De locatie van de logboekbestanden. Als dit veld leeg is, worden deze opgeslagen in de directory ` ./logs ` `. Het pad dat u instelt moet bestaan en Mattermost moet schrijfrechten hebben.

Wijzigingen in deze instelling vereisen een herstart van de server voordat deze wordt uitgevoerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is' ` '-bestandslocatie': "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Webhook-foutopsporing inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: De inhoud van binnenkomende webhaken wordt afgedrukt op logboekbestanden voor foutopsporing.

** False**: De inhoud van binnenkomende webhaken wordt niet afgedrukt in logbestanden. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` EnableWebhookDebugging ": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Diagnose en foutenrapportage inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Om de kwaliteit en de prestaties van toekomstige Mattermeeste updates te verbeteren, stuurt deze optie foutmeldingen en diagnosegegevens naar Matterbest, Inc. Alle diagnose-en foutmeldingen worden versleuteld in doorvoer en bevatten geen persoonlijk identificeerbare informatie of berichtinhoud. Voor meer informatie over deze functie raadpleegt u :doc: ` telemetrie `.

** False**: Diagnose en foutenrapportage zijn uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is ` ` ` EnableDiagnostics': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Sessielengtes
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Gebruikerssessies worden gewist als een gebruiker zich probeert aan te melden. Daarnaast wordt elke 24 uur een taak uitgevoerd om sessies te wissen uit de databasetabel van de sessies.

Lengte van sessie verlengen met activiteit ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Verbetert gebruikerservaring door sessies uit te breiden en gebruikers aangemeld te houden als ze actief zijn in hun Mattermeeste apps. 

** True**: Sessies worden automatisch uitgebreid wanneer de gebruiker actief is in hun Matterendste client. Gebruikerssessies verlopen alleen als ze niet actief zijn in de meest overeenkomende client voor de gehele duur van de sessielengtes die in de onderstaande velden zijn gedefinieerd.

** False**: Sessies worden niet uitgebreid met activiteit in Matterbest. Gebruikerssessies vervallen onmiddellijk aan het einde van de sessielengte of inactieve timeouts die hieronder zijn gedefinieerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` ` ` ` Extend360 SessionLengthWithActivity ": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Sessielengte voor e-mail en AD/LDAP-verificatie (dagen) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Stel het aantal dagen in vanaf de laatste keer dat een gebruiker zijn legitimatiegegevens heeft ingevoerd bij het vervallen van de sessie van de gebruiker op e-mail en AD/LDAP-verificatie.

Nadat u deze instelling hebt gewijzigd, wordt de nieuwe sessielengte van kracht na de volgende keer dat de gebruiker zijn legitimatiegegevens invoert. + -------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "SessionLengthWebInDays": 30 ` ` met numerieke invoer. |
+ -------------------------------------------------------------------------------------------------------------- +

Sessielengte voor mobiele apps (dagen) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Stel het aantal dagen in vanaf de laatste keer dat een gebruiker zijn legitimatiegegevens heeft ingevoerd bij het vervallen van de sessie van de gebruiker op mobiele apps.

Nadat u deze instelling hebt gewijzigd, wordt de nieuwe sessielengte van kracht na de volgende keer dat de gebruiker zijn legitimatiegegevens invoert. + ------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` SessionLengthMobileInDays ": 180 ` ` met numerieke invoer. |
+ -----------------------------------------------------------------------------------------------------------------------

Sessielengte voor SSO-verificatie (dagen) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze instelling definieert de sessielengte voor SSO-verificatie, zoals SAML, GitLab en OAuth 2.0.

Stel het aantal dagen in vanaf de laatste keer dat een gebruiker zijn legitimatiegegevens heeft ingevoerd bij het vervallen van de sessie van de gebruiker. Als de verificatiemethode SAML, GitLab of OAuth 2.0 is, kan de gebruiker automatisch worden aangemeld bij Matterbest als ze al zijn aangemeld bij SAML, GitLab, of met OAuth 2.0.

Nadat u deze instelling hebt gewijzigd, wordt de instelling van kracht na de volgende keer dat de gebruiker zijn legitimatiegegevens invoert. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` SessionLengthSSOInDays ": 30 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Sessiecache (minuten) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Stel het aantal minuten in dat een sessie in het cachegeheugen moet worden opgeslagen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' 'van deze functie is' ` ' "SessionCacheInMinutes": 10 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Timeout voor stationair sessie (minuten) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het aantal minuten van de laatste keer dat een gebruiker actief was op het systeem tot het einde van de sessie van de gebruiker. Na het vervallen van de procedure moet de gebruiker zich aanmelden om door te gaan. Minimaal 5 minuten en 0 is onbeperkt.

Is van toepassing op de desktop-app en browsers. Voor mobiele apps gebruikt u een EMM-provider om de app te vergrendelen wanneer deze niet wordt gebruikt. In de modus voor hoge beschikbaarheid schakelt u de IP-hashbelastingsverdeling in voor een betrouwbare timeoutmeting.

Deze instelling wordt niet van kracht als ` ` Extend360 SessionLengthWithActivity ` ` is ingesteld op ` ` true ` ` `. + ----------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' van deze feature is '` 'SessionIdleTimeoutInMinutes': 43200 ` ` met numerieke invoer. |
+ ----------------------------------------------------------------------------------------------------------------- +

Prestatiebewaking
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

*Beschikbaar in Enterprise Edition E20 *

Voor wijzigingen in de eigenschappen in deze sectie moet eerst een herstart van de server worden uitgevoerd.

Prestatiebewaking inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Matterbest zorgt voor het verzamelen en profileren van prestatiebewaking. Zie de 'documentatie <https://docs.mattermost.com/deployment/metrics.html>' om meer te weten te komen over het configureren van prestatiebewaking voor Matterbest.

** False**: Mattermeeste prestatiebewaking is uitgeschakeld. + -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` inschakelen ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Luisteradres ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het adres waar de Mattermeeste server naar luistert om prestatiecijfers aan de kaak te stellen. + ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is' ` ' "InterNodeListenAddress": ": 8067" ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Ontwikkelaar
~ ~ ~ ~ nopen ~ ~

Testen van testen inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: ` ` /test ` ` slash opdracht is ingeschakeld om testaccounts en testgegevens te laden.

** False**: ` ` /test ` ` slash opdracht is uitgeschakeld.

Wijzigingen in deze instelling vereisen een herstart van de server voordat deze wordt uitgevoerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "EnableTesting": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Enable Developer Mode ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Javascript-fouten worden weergegeven in een paarse balk aan de bovenkant van de gebruikersinterface. Niet aanbevolen voor gebruik in de productie.

** False**: Gebruikers worden niet gewaarschuwd voor Javascript-fouten.

-----------------------------------------------------------------------------------------------
----------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` 'EnableDeveloper': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Niet-vertrouwde interne verbindingen toestaan ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze instelling beperkt de mogelijkheid voor de Matterigste server om onbetrouwbare aanvragen binnen het lokale netwerk te maken. Een verzoek wordt als "onbetrouwbaar" beschouwd wanneer het namens een client wordt gemaakt. De volgende functies maken onbetrouwbare aanvragen en worden beïnvloed door deze instelling:

-Integraties met behulp van webhooks, slash-opdrachten, of bericht acties. Dit voorkomt dat ze eindpunten vragen binnen het lokale netwerk.
-Link previews. Wanneer een link naar een lokaal netwerkadres in een chatbericht wordt geplaatst, voorkomt dit dat er een preview van een link wordt afgebeeld.
-De ` lokale image-proxy <https: //docs.mattermost.com/administration/image-proxy.html#local-image-proxy> ` _. Als de lokale afbeeldingsproxy is ingeschakeld, kunnen afbeeldingen die zich op het lokale netwerk bevinden niet worden gebruikt door integraties of in chatberichten.

Aanvragen die alleen kunnen worden geconfigureerd door beheerders worden als betrouwbaar beschouwd en worden niet beïnvloed door deze instelling. Betrouwbare URL's bevatten de URL's die worden gebruikt voor OAuth-aanmelding of voor het verzenden van push-berichten. .. waarschuwing:
   Deze instelling is bedoeld om te voorkomen dat gebruikers buiten uw lokale netwerk de Mattermeeste server gebruiken om vertrouwelijke gegevens van binnen uw netwerk aan te vragen. Bij het configureren van deze instelling dient u voorzichtig te zijn om onbedoelde toegang tot uw lokale netwerk te voorkomen.

Enkele voorbeelden van wanneer u deze instelling kunt wijzigen zijn:

-Bij het installeren van een plugin die zijn eigen afbeeldingen bevat, zoals ` Matterpoll <https://github.com/matterpoll/matterpoll> ` __, moet u de domeinnaam van de Matterste server toevoegen aan deze lijst.
-Bij het uitvoeren van een bot-of webhook-gebaseerde integratie op uw lokale netwerk, moet u de hostnaam van de bot/integratie toevoegen aan deze lijst.
-Als uw netwerk zodanig is geconfigureerd dat toegankelijke webpagina's of afbeeldingen door de Mattermeeste server worden benaderd met behulp van hun interne IP-adres, moeten de hostnamen voor die servers aan deze lijst worden toegevoegd.

Deze instelling is een goedgekeurde lijst van lokale netwerkadressen die kunnen worden aangevraagd door de Matterendste server. Het is geconfigureerd als een witruimte gescheiden lijst van hostnamen, IP adressen en CIDR bereiken die toegankelijk zijn, zoals ` ` webhooks.internal.example.com 127.0.0.1 10.0.16.0/28 ` `. Sinds v5.9 het publieke IP van de Mattermeeste toepassingenserver zelf wordt ook beschouwd als een gereserveerde IP. .. Opmerking:
   Gebruik witespaces in plaats van komma's om de hostnamen, IP-adressen of CIDR-bereiken af te beelden. Bijvoorbeeld: ` ` webhooks.internal.example.com 127.0.0.1 10.0.16.0/28 ` `.

IP-adres en domeinnaamregels worden toegepast voordat de hostomzetting wordt uitgevoerd. De CIDR-regels worden toegepast na de resolutie van de host. Als het domein "webhooks.internal.example.com" bijvoorbeeld wordt omgezet in het IP-adres ` ` 10.0.16.20 ` `, kan een webhook met de URL "https: //webhooks.internal.example.com/webhook" worden witgeisted met behulp van ` `webhooks.internal.example.com ` ` of ` ` 10.0.16.16/28 ` ` `, maar niet ` ` 10.0.16.20 ` `. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json' van deze feature is '`' "AllowedUntrustedInternalConnections": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Vestigingsconfiguratie
-------------------

Instellingen voor het aanpassen van uw Mattermeest implementatie.

Aanpassing
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Sitenaam ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Naam van de service die wordt afgebeeld in de aanmeldschermen en de gebruikersinterface. Maximaal 30 tekens. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` ` SiteName': "Matterbest" ` ` met string input. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Sitebeschrijving ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Beschrijving van de service die wordt afgebeeld in aanmeldschermen en UI. Als dit niet is opgegeven, wordt "Alle teamcommunicatie op één plaats, doorzoekbaar en overal toegankelijk" afgebeeld. + ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is' ` ' "CustomDescriptionText": "" ` ` met reeksinvoer. |
+ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Aangepaste branding inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

* Deze functie is verplaatst naar Team Edition in Matterendste v5.0, uitgebracht op 16 juni 2018. In vorige versies is deze functie beschikbaar in Enterprise Edition E10 en higher.*

** True**: Met aangepaste branding kunt u op de aanmeldingspagina van de server een JPG-afbeelding in een aangepaste tekst weergeven.

** False**: Aangepaste branding is uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` ` EnableCustomBrand ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Aangepaste merkafbeelding ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Aangepaste JPG-afbeelding wordt aan de linkerkant van de aanmeldingspagina van de server afgebeeld. Aanbevolen maximale afbeeldingsgrootte is kleiner dan 2 MB, omdat de afbeelding wordt geladen voor elke gebruiker die zich aanmeldt. + -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Deze functies hebben geen ` `config.json ` ` instelling en moeten worden ingesteld in de gebruikersinterface van de systeemconsole. |
+ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Aangepaste merktekst ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Aangepaste tekst wordt afgebeeld onder de aangepaste merkafbeelding aan de linkerkant van de aanmeldingspagina van de server. Maximaal 500 tekens toegestaan. U kunt deze tekst opmaken met dezelfde ` Markdown opmaak codes <https://docs.mattermost.com/help/messaging/formatting-text.html> ' __ als in de meeste berichten. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' van deze feature is '`' "CustomBrandText": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Inschakelen Vraag Community Link ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: ** Vraag de community * * link is zichtbaar in de Mattermeeste kanaalkop, in het menu ** Help**. Wanneer geklikt wordt, worden gebruikers doorgestuurd naar https://mattermost.com/pl/default-ask-mattermost-community/, waar ze kunnen deelnemen aan de Mattermeest Gemeenschap om vragen te stellen en anderen te helpen bij het oplossen van problemen. Deze optie is niet beschikbaar op de mobiele apps.

** False**: De link is niet zichtbaar voor gebruikers. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` ` instelling van deze feature is ` ` enable_ask_community_link': "" ` ` met opties ` ` true ` ` en ` ` false ` `. Standaard ingesteld op true. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Help-koppeling ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Configureerbare link naar een Help-pagina die uw organisatie kan leveren aan eindgebruikers. Standaard worden links naar de Mattermeest Help-documentatie gehost op 'docs.mattermost.com <https://docs.mattermost.com/>' __. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| De instelling '`config.json' van deze feature is '`'-HelpLink ':' https: //about.mattermost.com/default-help/' ` ` met tekenreeksinvoer. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +

E-mail ondersteunen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Stel een e-mailadres in voor feedback-of ondersteuningsaanvragen.

Zodat u geen berichten mist, zorg er dan voor dat u deze waarde wijzigt in een e-mailadres dat uw systeembeheerder ontvangt, bijvoorbeeld '`"support@yourcompany.com' ` ` `. Dit adres wordt afgebeeld op e-mailmeldingen en tijdens het zelfstudieprogramma voor eindgebruikers om vragen te stellen over ondersteuning. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ``config.json ` ` instelling van deze feature is ` ` "SupportEmail": "feedback@mattermost.com" ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Voorwaarden van de dienstbetrekking ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Configureerbare link naar Servicevoorwaarden uw organisatie kan leveren aan eindgebruikers op de voettekst van de aanmeldingspagina's. Standaard worden links naar de pagina Servicevoorwaarden gehost op about.mattermost.com. Als u de link naar een andere Servicevoorwaarden wijzigt, moet u ervoor zorgen dat de "Mattermost Conditions of Use"-kennisgeving wordt opgenomen voor eindgebruikers die ook moeten worden afgebeeld voor gebruikers van de link "Terms of Service".

In versie 5.17 en hoger wijzigt deze instelling de voorwaarden van de servicelink niet in ** Hoofdmenu > Over Matterbest * *, dat verwijst naar de Mattermeeste Servicevoorwaarden. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` TermsOfServiceLink ":" https: //about.mattermost.com/default-terms/" ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Privacybeleid link ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Configureerbare link naar Privacybeleid uw organisatie kan leveren aan eindgebruikers op de voettekst van de sign-up en login pagina's. Standaard worden links naar een pagina met het privacybeleid op about.mattermost.com gehost.

In versie 5.17 en hoger verandert deze instelling niet in de link voor privacy policy in ** Hoofdmenu > Over Matterbest * *, die verwijst naar het Matterbest Privacy Policy. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is' ` ' "PrivacyPolicyLink": "https: //about.mattermost.com/default-privacy-policy/" ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Over de link ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Configureerbare link naar een Info-pagina die uw organisatie beschrijft, kan aan eindgebruikers worden voorzien. Standaard worden links naar een pagina Info gehost op about.mattermost.com. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| De '` `config.json ` ` instelling van deze feature is' ` ' "AboutLink": "https: //about.mattermost.com/default-about/" ` ` with string input. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +

Een probleemkoppeling melden ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De link voor de ondersteuningswebsite instellen. + -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "ReportAProblemLink": "https: //about.mattermost.com/default-report-a-problem/" ` ` met tekenreeksinvoer. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

De meest belangrijke downloadpagina voor apps ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Configureerbare link naar een downloadpagina voor Mattermeeste Apps. Als er een link aanwezig is, wordt er een optie * * Download Apps * * toegevoegd in het hoofdmenu zodat gebruikers de downloadpagina kunnen vinden. Laat dit veld leeg om de optie te verbergen in het hoofdmenu. Standaard is er een pagina op about.mattermost.com waar gebruikers de iOS-, Android-en Desktop-clients kunnen downloaden. Als u werkt met een ` Enterprise App Store <https: //docs.mattermost.com/deployment/push.html?highlight=enterprise%20app#push-meldingen-en-mobile-devices> ` __ voor uw mobiele apps, wijzigt u deze link zodat u naar een aangepaste downloadpagina gaat waar gebruikers de juiste apps kunnen vinden. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| De '` `config.json ` ` instelling van deze feature is ` ` AppDownloadLink': "https: //about.mattermost.com/downloads/" ` ` met tekenreeksinvoer. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +

Downloadlink Android App ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Configureerbare link voor het downloaden van de Android-app. Wanneer er een link aanwezig is, zullen gebruikers die toegang hebben tot de site op een mobiele web browser worden gevraagd met een pagina die hen de mogelijkheid geeft om de app te downloaden. Laat dit veld leeg om te voorkomen dat de pagina verschijnt. Als u een 'Enterprise App Store <https: //docs.mattermost.com/deployment/push.html#enterprise-app-store-eas>' __ gebruikt voor uw mobiele apps, wijzigt u deze link zodat deze naar de juiste app gaat. + -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` AndroidAppDownloadLink ":" https: //about.mattermost.com/mattermost-android-app/" ` ` met tekenreeksinvoer. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

iOS App downloaden Link ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Configureerbare link voor het downloaden van de iOS-app. Wanneer er een link aanwezig is, zullen gebruikers die toegang hebben tot de site op een mobiele web browser worden gevraagd met een pagina die hen de mogelijkheid geeft om de app te downloaden. Laat dit veld leeg om te voorkomen dat de pagina verschijnt. Als u een 'Enterprise App Store <https: //docs.mattermost.com/deployment/push.html#enterprise-app-store-eas>' __ gebruikt voor uw mobiele apps, wijzigt u deze link zodat deze naar de juiste app gaat. + -------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` ' "IosAppDownloadLink": "https: //about.mattermost.com/mattermost-ios-app/" ` ` met tekenreeksinvoer. |
+ -------------------------------------------------------------------------------------------------------------------------------------- +

Lokalisatie
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Standaard-servertaal ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Standaardtaal voor systeemberichten en logboeken.

Wijzigingen in deze instelling vereisen een herstart van de server voordat deze wordt uitgevoerd. + -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| De instelling '`config.json' 'van deze feature is' ` '"DefaultServerLocale": "en" ` ` met opties ` ` ` de' `, ` ` 'en' ` `, ` ` 'es' ` `, ` ` ` ` ` ` ` `, ` ` ` ` ` ` ` `, ` ` ` ` ` ` ` `, ` ` ` ` ` ` ` `, ` ` ` ` ` ` ` ` `, ` ` ' pl "` `, ` ` ` pt-br" ` `, ` ` "ro" ` `, ` ` ` ru "` `, ` ` ` tr" ` `, ` ` ` ttr "` `, ` ` ` zh_CN" ` `, en ` ` ` 'zh_TW " ` `. |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Standaard Clienttaal ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Standaardtaal voor nieuwe gebruikers en pagina's waar de gebruiker niet is aangemeld. + -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| De instelling ``config.json van deze feature is ` ` '"DefaultClientLocale": "en" ` ` met opties ` ` ` de' ` `, ` ` en "` `, ` `" es "` `, ` ` ` ` ` ` ` `, ` ` ` ` ` ` ` ` `, ` ` ` ja" ` `, ` ` ` ko "` `, ` ` ` ` pt-br" ` `, ` ` ` pt-br "` `, ` `" ro "` `, ` ` ` ru" ` `, ` ` ` tr "` `, ` ` ` zh_CN" ` `, en ` ` ` 'zh_CN "` `, en ` ` ` 'zh_TW" ` `. |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Beschikbare talen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Sets welke talen beschikbaar zijn voor gebruikers in ** Accountinstellingen > Weergeven > Talen * *. Laat het veld leeg om automatisch nieuwe talen toe te voegen, of voeg nieuwe talen handmatig toe met behulp van het vervolgkeuzemenu. Als u handmatig nieuwe talen toevoegt, moet u * * Default Client Language * * toevoegen voordat u de instelling opslaat. .. Opmerking:
  Servers die zijn geüpgraded naar v3.1 moeten dit veld handmatig instellen om nieuwe talen standaard toe te voegen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| De instelling ``config.json van deze feature is ` ` AvailableLocales ":" "` ` met opties ` ` ` ` ` `, ` ` ` de" ` `, ` ` "en" ` `, ` ` "es" ` `, ` ` ` ` ` ` ` `, ` ` ` ` ` ` `, ` ` ` ` ` ` `, ` ` ` ` ` ` `, ` ` ` ` ` ` ` `, ` ` "` ` ` ` ` `, ` ` ` ` p-br" ` `, ` ` "` ro" ` `, ` ` ` ru "` `, ` `" ` tr "` `, ` ` ` ` ` ` ` ` ` `, ` ` ` zh_CN" ` `, en ` ` ` ''zh_TW " ` `. |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Gebruikers en teams
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Max gebruikers per team ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Maximumaantal gebruikers per team, met uitzondering van inactieve gebruikers.

Het ** Max Gebruikers Per Team * * verwijst naar de grootte van de "teamsite" die een "team van mensen"-ingewoontes is. Een team van mensen wordt beschouwd als een kleine organisatie waar mensen nauw samenwerken in de richting van een specifiek gemeenschappelijk doel en dezelfde etiquette delen. In de fysieke wereld, een team van mensen kan meestal zitten rond een tafel om een maaltijd te hebben en hun project te bespreken.

De standaard maximum van 50 mensen, is aan het uiterste einde van een enkel team van mensen. Op dit punt zijn organisaties vaker "meerdere teams van mensen" en investeringen in expliciet definiërende etiquette, zoals ` channel organization <https://docs.mattermost.com/help/getting-started/organizing.html> ` __ of draaien op ` policy features <https: //docs.mattermost.com/administration/config-settings.html#policy> ` __ in Enterprise Edition, worden vaak gebruikt om de hoge niveaus van de productiviteit te schalen in een team van mensen die Matterbest gebruiken voor meerdere teams van mensen.

In termen van technische prestaties, ` met de juiste hardware, kan Matterbest gemakkelijk tot honderden en zelfs duizenden gebruikers <https://docs.mattermost.com/install/requirements.html> ` __ schalen, en mits de beheerder van mening is dat de juiste etiquette aanwezig is, moeten ze zich vrij voelen om de standaardwaarde te verhogen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` MaxUsersPerTeam ': 50 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Max Kanalen Per Team ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Maximumaantal kanalen per team, inclusief zowel actieve als gewiste kanalen. + --------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` MaxChannelsPerTeam ': 2000 ` ` met numerieke invoer. |
+ --------------------------------------------------------------------------------------------------- +

Gebruikers de mogelijkheid bieden om rechtstreekse berichtenkanalen te openen met ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** Elke gebruiker op de Mattermeeste server * *: Het menu Directe berichten ** More** heeft de optie om een Direct Message kanaal te openen met elke gebruiker op de server.

** Elk lid van het team * *: Het menu Directe berichten ** More** heeft alleen de mogelijkheid om een Direct Message kanaal te openen met gebruikers in het huidige team, en CTRL/CMD + K channel switcher geeft alleen een overzicht van de gebruikers van het huidige team. Als een gebruiker deel uitmaakt van meerdere teams, worden directe berichten nog steeds ontvangen, ongeacht welk team ze momenteel hebben.

Deze instelling is alleen van invloed op de UI, niet op machtigingen op de server. Een Direct Message-kanaal kan bijvoorbeeld met iedereen op de server worden gemaakt, ongeacht deze instelling. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` ` instelling is ` ` ` RestrictDirectMessage ":" any "` ` met opties ` ` ` ` ` ` en ` ` ` team" ` ` voor de bovenstaande instellingen. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Toestaan dat teambeheerders andere posten bewerken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Deze machtiging wordt opgeslagen in th
e database en kan worden gewijzigd met behulp van de System Console-gebruikersinterface.*

** True**: Teambeheerders en systeembeheerders kunnen posts van andere gebruikers bewerken.

** False**: Alleen systeembeheerders kunnen posts van andere gebruikers bewerken. Opmerking:
   Deze instelling is alleen beschikbaar voor servers van Team Edition. Enterprise Edition-servers kunnen de machtiging 'Geavanceerde machtigingen <https://docs.mattermost.com/deployment/advanced-permissions.html>' __ gebruiken om deze machtiging te configureren.

Enable Team Directory ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in mei 16, 2016 release *

** True**: Teams die zijn geconfigureerd om te verschijnen in de teamdirectory worden weergegeven op de hoofdpagina van het systeem. Teams kunnen deze instelling configureren vanuit ** Teaminstellingen > Dit team opnemen in de teamdirectory * *.

** False**: Teamdirectory op de hoofdpagina van het systeem is uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableTeamListing ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Teamgenoot-naam wordt afgebeeld ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geeft aan hoe namen standaard worden afgebeeld in de gebruikersinterface. Let op: gebruikers kunnen deze instelling overschrijven in ** Accountinstellingen > Weergeven > Teammat-naamweergave * *.

** Toon gebruikersnaam * *: Geeft de gebruikersnaam van de gebruiker weer.

** Toon roepnaam als er een bestaat * *: Geeft de bijnaam van de gebruiker weer. Als de gebruiker geen roepnaam heeft, wordt de volledige naam afgebeeld. Als de gebruiker geen volledige naam heeft, wordt de gebruikersnaam afgebeeld.

** Eerste en achternaam afbeelden * *: De volledige naam van de gebruiker. Als de gebruiker geen volledige naam heeft, wordt de gebruikersnaam afgebeeld. Aanbevolen bij gebruik van SAML of LDAP als de kenmerken voor de voornaam en achternaam zijn geconfigureerd. + -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` TeammateNameDisplay': "gebruikersnaam" ` ` met opties ` ` "gebruikersnaam" ` `, ` ` 'nickname_full_name "` `, en ` `" full_name " ` ` voor de bovenstaande instellingen. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Gebruikers toestaan om gearchiveerde kanalen (Beta) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Hiermee kunnen gebruikers content bekijken, delen en zoeken naar content van kanalen die zijn gearchiveerd. Gebruikers kunnen alleen de content bekijken in kanalen waarvan ze lid waren voordat het kanaal werd gearchiveerd.

** False**: Gebruikers kunnen geen content bekijken, delen of zoeken naar content van kanalen die zijn gearchiveerd. + -------------------------------------------------------------------------------------------------------------------------------------------------------
| Deze functie ' ` `config.json ` ` instelling is ` ` "ExperimentalViewArchivedChannels": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------- +

E-mailadressen afbeelden ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Toon e-mailadres van alle gebruikers.

** False**: Verberg het e-mailadres van gebruikers van andere gebruikers in de gebruikersinterface, inclusief Team Admins. Dit is ontworpen voor het beheren van teams waar gebruikers hun contactgegevens privé houden. Systeembeheerders kunnen nog steeds e-mailadressen in de gebruikersinterface zien. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "ShowEmailAddress": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Volledige naam tonen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Toon volledige naam van alle gebruikers.

** False**: Verberg de volledige naam van gebruikers van andere gebruikers, waaronder Team Admins. Dit is ontworpen voor het beheren van teams waar gebruikers hun contactgegevens privé houden. Systeembeheerders kunnen nog steeds volledige namen in de gebruikersinterface zien. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "ShowFullName": true ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Kennisgevingen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

De bevestigings-dialoog @channel en @all ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Gebruikers worden gevraagd om te bevestigen wanneer @channel en @all worden gepost in kanalen met meer dan vijf leden.

** False**: Geen bevestiging vereist. + -------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` ` EnableConfirmNotificationsToChannel': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ -------------------------------------------------------------------------------------------------------------------------------- +

E-mailberichten inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Hiermee kunt u e-mailmeldingen verzenden.

** False**: schakelt e-mailmeldingen voor berichten uit. Dit is handig voor ontwikkelaars die kunnen willen overslaan e-mail setup voor snellere ontwikkeling. Als u de previewmodus ** wilt verwijderen: E-mailmeldingen zijn niet geconfigureerd * * banner, moet u ook de optie ** Enable Preview Mode Banner * * instellen op ` ` false ` `.

Als deze instelling is ingesteld op ` ` false ` ` en de SMTP-server is ingesteld, worden accountgerelateerde e-mails (zoals wachtwoord, e-mail, gebruikersnaam, gebruikerstoken, MFA en andere verificatiegerelateerde wijzigingen) verzonden, ongeacht deze instelling. 

E-mailuitnodigingen en e-mails voor het deactiveren van accounts worden niet beïnvloed door deze instelling. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "SendEmailNotifications": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- + .. _email-preview-mode-banner-config:

Voorbeeldmodus Banner Inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Previewmodus-banner wordt voor alle gebruikers afgebeeld wanneer ` ` "SendEmailNotifications": false ` `, zodat gebruikers zich ervan bewust zijn dat e-mailmeldingen zijn uitgeschakeld.

** False**: De banner van de previewmodus wordt niet afgebeeld voor gebruikers. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` ` EnablePreviewModeBanner ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

E-mail Batching (^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Gebruikers kunnen selecteren hoe vaak e-mailmeldingen moeten worden ontvangen, en meerdere meldingen binnen die periode worden gecombineerd in één e-mail. Batching zal plaatsvinden bij een standaard interval van 15 minuten, configureerbaar in ** Accountinstellingen > Meldingen * *. .. Opmerking:
  E-mailbatching kan alleen worden ingeschakeld als de ` SiteURL <https: //docs.mattermost.com/administration/config-settings.html#site-url> ` __ is geconfigureerd. E-mailbatching in ` High Availability mode <https: //docs.mattermost.com/administration/config-settings.html#enable-high-availability-mode> ` __ is gepland maar nog niet ondersteund.

** False**: Als e-mailmeldingen zijn ingeschakeld in Accountinstellingen, worden e-mails afzonderlijk verzonden voor elke ontvangen vermelding of rechtstreeks ontvangen bericht. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` ` instelling van deze feature is ` ` "EnableEmailBatching": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Inhoud van e-mailmeldingen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

** Stuur volledige berichtinhoud * *: Naam en kanaal van de afzender zijn opgenomen in e-mailmeldingen.

** generieke beschrijving verzenden met alleen de naam van de afzender * *: De naam van het team en de naam van de persoon die het bericht heeft verzonden, zonder informatie over de naam van het kanaal of de inhoud van het bericht, is opgenomen in e-mailmeldingen. Meestal gebruikt om nalevingsredenen als Mattermeesten vertrouwelijke informatie en beleid bevat, kan het niet in e-mail worden opgeslagen. + -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Deze functie ' ` `config.json ` ` ` instelling is ` ` ` EmailNotificationContentsType ":" full "` ` met opties ` `" full "` ` en ` `" generieke " ` ` voor de bovenstaande instellingen. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Weergavenaam melding ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Naam die wordt weergegeven op een e-mailaccount dat wordt gebruikt bij het verzenden van e-mailberichten van Mattermeeste-systeem. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is' ` ' "FeedbackName": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Kennisgeving Van Adres ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Adres dat wordt weergegeven op een e-mailaccount dat wordt gebruikt bij het verzenden van e-mailberichten van binnen Matterbest.

Zodat u geen berichten mist, zorg er dan voor dat u deze waarde wijzigt in een e-mail die de systeembeheerder ontvangt, zoals '`"admin@yourcompany.com' ` ` `. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` ` instelling van deze feature is ` `' FeedbackEmail ':' ' ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Meldingenantwoord-Op adres ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

E-mailadres dat wordt gebruikt in de header Reply-To bij het verzenden van e-mailberichten van Matterbest. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is ` `' "ReplyToAddress": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Postadres van de aanmeldingvoettekst ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De naam van de organisatie en het postadres worden weergegeven in de voettekst van e-mailmeldingen van Matterbest, zoals "© ABC Corporation, 565 Knight Way, Palo Alto, California, 94305, USA". Als het veld leeg wordt gelaten, worden de organisatienaam en het postadres niet afgebeeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is '`' "FeedbackOrganization": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Inhoud van push-berichten ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** Algemene beschrijving met alleen de naam van de afzender * *: Voor push-berichten wordt alleen de naam vermeld van de persoon die het bericht heeft verzonden, maar geen informatie over kanaalnaam of berichttekst.

** Algemene beschrijving met afzender en kanaalnamen * *: Push-meldingen bevatten namen van gebruikers en kanalen, maar geen specifieke gegevens uit de berichttekst.

** Volledige berichtinhoud verzonden in de melding payload * *: Selecteren ** Stuur volledige berichtsnippet * * verzendt fragmenten uit berichten die aanleiding geven tot meldingen met details en kunnen vertrouwelijke informatie bevatten die in berichten is verzonden. Als uw Push Notification Service zich buiten uw firewall bevindt, is het HIGHLY RECOMMENDED deze optie alleen te gebruiken met een "https" protocol om de verbinding te versleutelen.

** ID-Alleen push-berichten-Volledige berichtinhoud opgehaald vanaf de server bij ontvangst * * (*Beschikbaar in Enterprise Edition E20 *): De payload van de melding doorgegeven via de ` Apple Push Notification service <https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1> ` _ of ` Firebase Cloud Messaging <https://firebase.google.com/docs/cloud-messaging> ` _ service bevat geen berichtinhoud. In plaats daarvan bevat het een uniek bericht-ID dat wordt gebruikt om berichtcontent op te halen van de server wanneer een push-bericht wordt ontvangen door een apparaat via een ` notification service app extention <https://developer.apple.com/documentation/usernotifications/modifying_content_in_newly_delivered_notifications> ` _ on iOS of ` een uitbreidbaar meldingspatroon <https://developer.android.com/training/notify-user/expanded> ` _ op Android. Als de server niet kan worden bereikt, wordt er een generiek push-bericht afgebeeld zonder de berichtinhoud of de naam van de afzender. 

Voor klanten die ervoor kiezen om de Mattermeeste mobiele toepassing in een beveiligde container te laten teruglopen, zoals BlackBerry Dymanics, MobileIron, AirWatch of andere oplossingen, moet de container de inhoud van het bericht ophalen uit het unieke bericht-ID wanneer u push-berichten ontvangt. Als de container niet in staat is de fetch uit te voeren, kan de inhoud van de push-berichten niet worden ontvangen door de mobiele toepassing van de klant zonder de inhoud van het bericht door te geven via de service ` Apple Push Notification service <https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1> ` _ of ` Firebase Cloud Messaging <https://firebase.google.com/docs/cloud-messaging> ` _ service. 

+ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "PushNotificationContents": "full" ` ` met opties ` ` "generic_no_channel" ` `, ` ` "generiek" ` `, ` ` full "` `, en ` ` ` id_loaded" ` ` voor de bovenstaande instellingen. |
+ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Banner voor mededeling
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Aankondiging Banner Inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Schakel een banner voor alle teams in. De banner wordt boven aan het scherm weergegeven en is de gehele breedte van het scherm. Standaard kunnen gebruikers de banner verwijderen totdat u de tekst van de banner wijzigt of totdat u de banner opnieuw inschakelt nadat deze is uitgeschakeld. U kunt voorkomen dat gebruikers de banner niet verwijderen en u kunt de kleur van de tekst en de achtergrondkleur bepalen.

** True**: De banner voor de aankondiging inschakelen. De banner wordt alleen afgebeeld als ` ` BannerText ` ` een waarde heeft.

** False**: De annondebanner uitschakelen. + ----------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "EnableBanner": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ -----------------------------------------------------------------------------------------------------------------------

Bannertekst ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De tekst van de annoncering. + ------------------------------------------------------------------------------------ +
| Deze functie ' ` `config.json ` ` instelling is ` ` "" BannerText ":" " ` ` met string invoer. |
+ ------------------------------------------------------------------------------------ +

Bannerkleur ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De achtergrondkleur van de annoncering van de annoncering. + --------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "BannerColor": "#f2a93b" ` ` met tekenreeksinvoer. |
+ --------------------------------------------------------------------------------------------- +

Bannertekst Kleur ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De kleur van de tekst in de annoncering van de aankondiging. + ------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ' BannerTextColor ":"#333333" ` ` met tekenreeksinvoer. |
+ ------------------------------------------------------------------------------------------------- +

Bannerontslag Toestaan ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ _

** False**: De banner is permanent zichtbaar totdat het is uitgeschakeld door de systeembeheerder. + -------------------------------------------------------------------------------------------------------------------
| De instelling ``config.json van deze feature is ` ` AllowBannerDismissal ": true ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ -------------------------------------------------------------------------------------------------------------------

Emoji
~ ~ ~ geven

Enable Emoji Picker ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Maakt een emoji-kiezer mogelijk die gebruikers in staat stelt om emojis te selecteren als reactie of gebruik in berichten. Het inschakelen van de emoji picker met een groot aantal Custom Emojis kan de prestaties vertragen.

** False**: Emoji picker is uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` ` ` EnableEmojiPicker': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Aangepaste Emoji (^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ _

** False**: Aangepaste Emojis zijn uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` ` EnableCustomEmoji ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Aangepaste Emoji-creatie beperken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

* Deze machtiging is gemigreerd naar de database en het wijzigen van de ` `config.json ` ` ` waarde wordt niet meer van kracht na het upgraden naar v4.9, vrijgegeven op 16 april 2018. Deze machtiging kan worden gewijzigd met behulp van de gebruikersinterface van de systeemconsole. *

*Beschikbaar in Enterprise Edition E10 en hoger *

** Laat iedereen op maat maken emoji * *: Hiermee kan iedereen aangepaste Emoji maken van het ** Hoofdmenu > Custom Emoji * *.

** Allow System and Team Admins to create custom emoji * *: The Custom Emoji option is hidden from the Main Menu for users who are not System or Team Admins.

** Alleen systeembeheerders toestaan aangepaste emoji * * maken: De optie Aangepaste Emoji is verborgen in het hoofdmenu voor gebruikers die geen systeembeheerders zijn. + -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` ` RestrictCustomEmojiCreation': "all" ` ` met opties ` ` ` all "` ` `, ` ` ` admin" ` `, en ` ` ` system_admin " ` ` voor de bovenstaande instellingen. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Posten
~ ~ ~ geven

Koppelingspreviews inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Link previews zijn previews van gekoppelde website-content, afbeeldingslinks en YouTube-video's die worden weergegeven onder posts wanneer beschikbaar.

Koppelingspreviews worden aangevraagd door de server, wat betekent dat de Mattermost server verbonden moet zijn met het internet voor het weergeven van previews. Deze verbinding kan tot stand worden gebracht via een ` firewall of uitgaande proxy <https://docs.mattermost.com/install/outbound-proxy.html> ' __ in omgevingen waar directe internetconnectiviteit niet wordt gegeven of beveiligingsbeleid dit noodzakelijk maakt.

** True**: Website link previews, afbeelding link previews en YouTube-previews zijn ingeschakeld op de server. Gebruikers kunnen de website previews voor zichzelf in-of uitschakelen via ** Account Settings > Display > Website Link Previews * *.

** False**: Website link previews, afbeelding link previews en YouTube-previews zijn uitgeschakeld. De server vraagt geen metagegevens voor links naar berichten. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` ` ` EnableLinkPreviews': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Inschakelen van SVG ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Hiermee kunnen gebruikers previews van SVG-bestandsbijlagen en SVG-afbeeldingslinks bekijken.

** False**: Previews van SVG-bestandsbijlagen en SVG-afbeeldingslinks worden niet afgebeeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` "EnableSVGs": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Inschakelen LaTeX ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: maakt het mogelijk om LaTeX-code te genereren.

** False**: Hiermee wordt de weergave van LaTeX-code uitgeschakeld om te voorkomen dat de app crasht bij het delen van code die kan worden uitbesteed aan het toegewezen geheugen. Als deze optie is uitgeschakeld, wordt de LaTeX-code geaccentueerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` ` EnableLatex ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Schakel Lokale modus ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Zorgt voor lokale modus voor mmctl.

** False**: De lokale werkstand voor mmctl. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableLocalMode ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Lokale Modus Socketlocatie Inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het pad voor de socket die door de server wordt gemaakt voor mmctl om verbinding te maken en via de lokale werkstand te communiceren. Als de standaardwaarde voor deze sleutel wordt gewijzigd, moet u mmctl in de lokale modus verwijzen naar het nieuwe socketpad, met de vlag ` `--local-socket-path /new/path/to/socket ` ' in aanvulling op de ` ` -- local ` ` vlag.

Als er niets is opgegeven, is het standaardpad voor de server en het mmctl-pad ' `/var/tmp/mattermost_local.socket ` `. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is' ` ' LocalModeSocketLocation ":" /var/tmp/mattermost_local.socket " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Aangepaste URL-schema's ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Een lijst van URL-schema's die worden gebruikt voor het automatisch koppelen van berichttekst. ` ` http ` `, ` ` https ` `, ` ` ftp ` `, ` ` tel ` ` en ` ` mailto ` ` altijd links maken. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json'-instelling van deze feature is ` ` CustomUrlSchemes ': [] ` ` met tekenreeksinvoer bestaande uit URL-schema &apos; s, zoals ` ` [ "git", "smtp"] ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------
---------------------------------- +

Google API-toets ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Mattermost biedt de mogelijkheid om YouTube-video's uit te sluiten van URL's die door eindgebruikers worden gedeeld. 

Stel deze sleutel in en voeg YouTube Data API v3 toe als een service aan uw sleutel om de weergave van titels voor ingebedde YouTube-videovoorbeelden mogelijk te maken. Zonder de sleutel zullen YouTube-previews nog steeds worden gemaakt op basis van hyperlinks die in berichten of reacties verschijnen, maar ze zullen de video-titel niet tonen. Als Google detecteert dat het aantal weergaven uiterst hoog is, kunnen ze de toegang tot inbedden insluiten. 

Mocht dit gebeuren, dan kunt u de gasklep verwijderen door zich te registreren voor een Google Developer Key en deze in te voeren op dit veld volgens deze instructies: https://www.youtube.com/watch?v=Im69kzhpR3I. Uw Google Developer Key wordt gebruikt in JavaScript op de client.

Met behulp van een Google API-sleutel kan Matterbest detecteren wanneer een video niet meer beschikbaar is en de post met het label *Video niet gevonden. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` ' "GoogleDeveloperKey": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Bestanden delen en downloaden
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Bestandsdeling toestaan ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als ` ` false ` ` is, schakelt u het delen van bestanden op de server uit. Alle uploads van bestanden en afbeeldingen op berichten zijn niet toegestaan voor alle clients en apparaten, inclusief mobiel. + ---------------------------------------------------------------------------------------------------------------------
| De instelling ``config.json van deze feature is ` ` ` EnableFileAttachments ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------

Bestandsuploads op mobiel toestaan ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

Als ` ` false ` ` is, wordt het uploaden van bestanden op mobiele apps uitgeschakeld. Alle uploads van bestanden en afbeeldingen op berichten zijn niet toegestaan voor alle clients en apparaten, inclusief mobiel. + ---------------------------------------------------------------------------------------------------------------------
| De instelling ``config.json van deze feature is ` ` ` EnableMobileUpload ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------

Bestandsdownloads toestaan op mobiel ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

Als ` ` false ` ` is, worden bestandsdownloads op mobiele apps uitgeschakeld. Gebruikers kunnen nog steeds bestanden downloaden van een mobiele webbrowser. + ---------------------------------------------------------------------------------------------------------------------
| De '`config.json ` ` instelling van deze feature is' ` ` EnableMobileDownload ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------

Openbare koppelingen
~ ~ ~ ~ nopen ~ ~

Enable Public File Links ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Gebruikers toestaan om openbare links te genereren naar bestanden en afbeeldingen voor het delen buiten het Mattereste systeem met een openbare URL.

** False**: De optie ** Get Public Link * * is verborgen in de gebruikersinterface van de afbeeldingspreview.

** Opmerking: ** Wanneer u bent overgeschakeld op ` ` False ` `, ontvangt iedereen die een eerder gegenereerde openbare link probeert te bezoeken een foutbericht waarin staat dat de openbare links zijn uitgeschakeld. Wanneer teruggeschakeld wordt naar ` ` True ` `, zullen oude openbare links opnieuw werken tenzij de ** Public Link Salt * * is geregenereerde. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnablePublicLink ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Openbare koppeling Zout ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

32-bits zout toegevoegd aan de URL van openbare koppelingen wanneer openbare koppelingen zijn ingeschakeld. Klik op ** Regenerate** in de systeemconsole om een nieuw zout te maken dat alle bestaande openbare links ongeldig maakt. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "PublicLinkSalt": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Kennisgevingen
~ ~ ~ ~ nten

Activeer beheerberichten ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Systeembeheerders ontvangen berichten over beschikbare serverupgrades en relevante systeembeheerfuncties. ` Meer informatie <https://about.mattermost.com/default-notices> ` _

** False**: Systeembeheerders ontvangen geen berichten met uitzondering van berichten die van toepassing zijn op alle eindgebruikers (zie ` ` UserNoticesEnabled ` ` `). + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` AdminNoticesEnabled ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

De berichten voor eindgebruikers inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Alle gebruikers ontvangen berichten over de beschikbare client-upgrades en relevante eindgebruikersfuncties om de gebruikerservaring te verbeteren. ` Meer informatie <https://about.mattermost.com/default-notices> ` _

** False**: Gebruikers ontvangen geen berichten over beschikbare clientupgrades en relevante eindgebruikersfuncties. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` UserNoticesEnabled ': true ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Verificatie
---------------

Authenticatie-instellingen om account aanmaken en aanmelden met e-mail, GitLab, Google of Office 365 OAuth, AD/LDAP of SAML mogelijk te maken.

Aanmelding
~ ~ ~ geven

Maken van account aanmaken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Mogelijkheid om nieuwe accounts te maken is ingeschakeld via het uitnodigen van nieuwe leden of het delen van de teamuitnodiginglink.

** False**: De mogelijkheid om accounts te maken is uitgeschakeld. Met de knop ** Account maken * * wordt een fout weergegeven bij het aanmelden via een e-mailuitnodiging of een teamuitnodiging. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` `' EnableUserCreation ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Het aanmaken van het account beperken tot bepaalde e-maildomeinen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Teams en gebruikersaccounts kunnen alleen worden gemaakt door een geverifieerde e-mail uit deze lijst met door komma's gescheiden domeinen (bijv. "corp.mattermost.com, mattermost.org").

Deze instelling is alleen van invloed op aanmelding bij e-mail. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` ` instelling is ` ` ` RestrictCreationToDomains ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Open server inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Gebruikers kunnen zich zonder uitnodiging aanmelden bij de server vanaf de hoofdpagina.

** False**: Gebruikers kunnen alleen aanmelden bij de server als ze een uitnodiging ontvangen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` "EnableOpenServer": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

E-mailuitnodigingen Inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Gebruikers kunnen anderen uitnodigen voor het Mattermeeste systeem per e-mail.

** False**: E-mailuitnodigingen zijn uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` ` ` EnableEmailInvitations': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Ongeldigheid in afwachting van e-mail wordt gevraagd ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze knop maakt actieve e-mailuitnodigingen ongeldig die niet door de gebruiker zijn geaccepteerd. Standaard e-mailuitnodigingen verlopen na 48 uur.

Schakel het team in ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

* Deze machtiging is gemigreerd naar de database en het wijzigen van de ` `config.json ` ` ` waarde wordt niet meer van kracht na het upgraden naar v4.9, vrijgegeven op 16 april 2018. Deze machtiging kan worden gewijzigd met behulp van de gebruikersinterface van de systeemconsole. *

** True**: Mogelijkheid om een nieuw team te maken is ingeschakeld voor alle gebruikers.

** False**: Alleen systeembeheerders kunnen teams maken op basis van de teamselectiepagina. De knop ** Een nieuw team maken * * is verborgen in de gebruikersinterface van het hoofdmenu. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` ` instelling van deze feature is ` ` EnableTeamCreation': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

E-mail
~ ~ ~ geven

Maken van account aanmaken met e-mail ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Toestaan teamcreatie en account aanmelden met behulp van e-mail en wachtwoord.

** False**: E-mail aanmelden is uitgeschakeld. Deze limiet is aangegeven voor enkelvoudige aanmelding als OAuth of AD/LDAP. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableSignUpWithEmail ": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

E-mailverificatie vereisen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: e-mailverificatie vereist na maken van account voorafgaand aan het toestaan van aanmelden.

** False**: Gebruikers hoeven hun e-mailadres niet te verifiëren voordat ze zich aanmelden. Ontwikkelaars kunnen dit veld instellen op ` ` false ` ` voor het overslaan van het verzenden van verificatie-e-mails voor een snellere ontwikkeling. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` `' RequireEmailVerification ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Aanmelden met e-mail inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Matterbest staat het maken van accounts toe met behulp van e-mail en wachtwoord.

** False**: Aanmelden met e-mail is uitgeschakeld en verschijnt niet op het aanmeldscherm. Gebruik deze waarde als u de aanmelding wilt beperken tot één aanmelding zoals AD/LDAP, SAML of GitLab. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableSignInWithEmail ": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Aanmelden inschakelen met gebruikersnaam ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Matterbest stelt gebruikers met e-mailaanmelding in staat om hun gebruikersnaam en wachtwoord te gebruiken. Deze instelling heeft geen invloed op AD/LDAP-aanmelding.

** False**: Aanmelden met gebruikersnaam is uitgeschakeld en verschijnt niet op het aanmeldingsscherm. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` EnableSignInWithUsername ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Wachtwoord
~ ~ ~ nopen ~ ~

Minimumlengte wachtwoord ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

* Deze functie is verplaatst naar Team Edition in Matterendste v5.0, uitgebracht op 16 juni 2018. In vorige versies is deze functie beschikbaar in Enterprise Edition E10 en higher.*

Minimumaantal tekens vereist voor een geldig wachtwoord. Moet een geheel getal zijn dat groter is dan of gelijk is aan 5 en kleiner dan of gelijk aan 64. + ---------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' 'MinimumLength ': 10 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------- +

Wachtwoordvereisten ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

* Deze functie is verplaatst naar Team Edition in Matterendste v5.0, uitgebracht op 16 juni 2018. In vorige versies is deze functie beschikbaar in Enterprise Edition E10 en higher.*

Stel de vereiste tekentypen in die moeten worden opgenomen in een geldig wachtwoord. Standaard worden alle tekens toegestaan, tenzij anders aangegeven door de selectievakjes. Als een gebruiker een ongeldig wachtwoord invoert, verschijnt de preview van de fout in de systeemconsole op de pagina voor het maken van accounts.

-** Ten minste één kleine letter * *: Selecteer dit vakje als een geldig wachtwoord minimaal één kleine letter moet bevatten.
-** Minstens één hoofdletter * *: Selecteer dit vakje als een geldig wachtwoord ten minste één hoofdletter moet bevatten.
-** Ten minste één cijfer * *: Selecteer dit vakje als een geldig wachtwoord ten minste één nummer moet bevatten.
-** Minstens één symbool * *: Selecteer dit vakje als een geldig wachtwoord ten minste één symbool moet bevatten. Geldige symbolen zijn: ` `! "# $%& ' () * +,-./:; <=>? @[] ^ _ ` | ~ ` `.

De ' `config.json ` ` instellingen van deze feature zijn respectievelijk: .. lijst-tabel ::
    :breedten: 80

    *-` ` 'Lowercase': true ` ` met opties ` ` true ` ` en ` ` false ` `.
    *-` ` "Aantal": true ` ` met opties ` ` true ` ` en ` ` false ` `.
    *-` ` 'Uppercase': true ` ` met opties ` ` true ` ` en ` ` false ` `.
    *-` ` "Symbool": true ` ` met opties ` ` true ` ` en ` ` false ` `.

Maximumaantal aanmeldingspogingen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Mislukte aanmeldingspogingen voordat een gebruiker is vergrendeld en vereist om hun wachtwoord opnieuw in te stellen via e-mail. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is' ` '' MaximumLoginAttempts ': 10 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

MFA
~ ~ ~ geven

Beveiligingsinstellingen configureren voor verificatie met meerdere factoren.

De standaardaanbeveling voor beveiligde implementatie is om Matterbest te hosten binnen uw eigen besloten netwerk, met VPN-clients op mobiel, dus alles werkt onder uw bestaande beveiligingsbeleid en authenticatie protocollen, die al multi-factor authenticatie kunnen omvatten.

Als u ervoor kiest om Matterbest buiten uw besloten netwerk uit te voeren, zonder uw bestaande beveiligingsprotocollen te omzeilen, is het raadzaam om een verificatieservice met meerdere factoren in te stellen, specifiek voor toegang tot Matterbest.


Multi-Factor Authenticatie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Als het waar is, krijgen gebruikers met LDAP en e-mailverificatie de optie om een toegangscode op basis van een telefoon te vereisen, naast hun verificatie op basis van wachtwoorden, om zich aan te melden bij de Matterefste server. Ze zullen specifiek gevraagd worden om de app ` Google Authenticator <https://en.wikipedia.org/wiki/Google_Authenticator> ` __ te downloaden naar hun iOS of Android mobiele apparaat, de app te verbinden met hun account, en vervolgens een toegangscode in te voeren die door de app op hun telefoon wordt gegenereerd wanneer ze zich aanmelden bij de Mattertiste server.

** False**: verificatie met meerdere factoren is uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` `' EnableMultifactorAuthentication ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Toezien op de toepassing van de multifactorificatie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E10 en hoger *

** True**: Wanneer waar, ` multi-factor authenticatie (MFA) <https://docs.mattermost.com/deployment/auth.html> ` __ is vereist voor login. Er zijn nieuwe gebruikers nodig om de MFA te configureren. Aangemelde gebruikers zonder MFA-configuratie worden doorgestuurd naar de configuratiepagina van MFA totdat de configuratie is voltooid. Als uw systeem gebruikers heeft met andere aanmeldingsopties dan AD/LDAP en e-mail, moet MFA worden afgedwongen met de verificatieprovider buiten Mattermost.

** False**: verificatie met meerdere factoren is optioneel. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` EnforceMultifactorAuthentication ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

AD/LDAP
~ ~ ~ ~ nten

*Beschikbaar in Enterprise Edition E10 en hoger *

Aanmelden met AD/LDAP inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Matterbest staat login toe met behulp van AD/LDAP of Active Directory.

** False**: Aanmelden met AD/LDAP is uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` inschakelen ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Synchronisatie met AD/LDAP inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Matterbest synchroniseert periodiek gebruikers uit AD/LDAP.

** False**: AD/LDAP-synchronisatie is uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` `' EnableSync ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

AD/LDAP-server ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het domein of het IP-adres van de AD/LDAP-server. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` ` LdapServer ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

AD/LDAP-poort ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De poort die Matterbest gebruikt om verbinding te maken met de AD/LDAP-server. De standaardwaarde is ` ` 389 ` `. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` LdapPort ": 389 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Verbindingsveiligheid ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het type verbindingsbeveiliging Mattermeeste gebruikt om verbinding te maken met AD/LDAP.

** None**: Geen versleuteling, Matterbest zal niet proberen een versleutelde verbinding tot stand te brengen met de AD/LDAP-server.

**TLS* *: Versleutelde de communicatie tussen Matterbest en uw server met behulp van TLS.

**STARTTLS* *: Neemt een bestaande onveilige verbinding op en probeert deze te upgraden naar een beveiligde verbinding met TLS.

Als de optie "Geen versleuteling" is geselecteerd, is het raadzaam om de AD/LDAP-verbinding buiten Matterbest te sluiten, bijvoorbeeld door een stunnel-proxy toe te voegen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ConnectionSecurity ': "" ` met opties ` ` ` ` ` ` ` ` ` TLS "` ` en ` ` ` STARTTLS" ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Persoonlijke sleutel ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Het persoonlijke sleutelbestand van uw LDAP Authentication Provider en geüpload als TLS-clientcertificaten worden gebruikt als primair verificatiemechanisme. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` PrivateKeyFile ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Overheidscertificaat ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Het openbare TLS-certificaatbestand dat door uw LDAP Authentication Provider wordt geleverd en geüpload als TLS-clientcertificaten worden gebruikt als primair verificatiemechanisme. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` ' "PublicCertificateFile": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +


Certificaatcontrole overslaan ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Hiermee wordt de verificatiestap voor het certificaat overgeslagen voor verbindingen met TLS of STARTTLS. Niet aanbevolen voor productieomgevingen waarbij TLS vereist is. Alleen voor tests.

** False**: Matterbest slaat certificaatverificatie niet over. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` SkipCertificateVerification ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Basis-DN ^ ^ ^ ^ ^ ^ ^ ^

De ** Basis unieke naam * * van de locatie waar Matterbest moet beginnen met het zoeken naar gebruikers in de AD/LDAP-structuur. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` "" BaseDN ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Bindgebruikersnaam ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De gebruikersnaam die wordt gebruikt om de AD/LDAP-zoekopdracht uit te voeren. Dit moet een account zijn dat speciaal gemaakt is voor gebruik met Matterbest. De machtigingen moeten beperkt zijn tot alleen-leestoegang tot het gedeelte van de AD/LDAP-structuur dat is opgegeven in het veld ** Basis DN* *. Bij het gebruik van Active Directory, moet ** Bind Username * * domein opgeven in ` ` "DOMAIN/username" ` ` format. Dit veld is vereist en de anonieme bind wordt momenteel niet ondersteund. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is' ` ' "BindUsername": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Bindwachtwoord ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Wachtwoord van de gebruiker opgegeven in ** Bind-gebruikersnaam * *. Anonieme bind wordt momenteel niet ondersteund. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json `' van deze feature is '`' "BindPassword": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Gebruikersfilter ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Geef een AD/LDAP-filter op dat moet worden gebruikt bij het zoeken naar gebruikersobjecten (accepteert 'algemene syntaxis <https://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm>' __). Alleen de gebruikers die door de query zijn geselecteerd, hebben toegang tot Matterbest.

Voorbeeldfilters voor Active Directory:

-Voor het uitfilteren van uitgeschakelde gebruikers: ``( &(objectCategory=Person) (! (UserAccountControl: 1.2.840.113556.1.4.803: = 2))) ` `.
-Als u wilt filteren op groepslidmaatschap, bepaalt u de distinguishedName van uw groep en gebruikt u de algemene syntaxis voor het groepslidmaatschap als uw filter.

  * Als de beveiligingsgroep distinguishedName bijvoorbeeld ` ` CN=group1, OU=groups, DC=example, DC=com ` ` is, dan is het te gebruiken gebruikersfilter: ` ` (memberOf=CN=group1, OU=groups, DC=example, DC=com) ` `. Opmerking: de gebruiker moet expliciet tot deze groep behoren om het filter toe te passen.

Dit filter gebruikt de toegangsrechten van de account ** Bind Username * * om de zoekopdracht uit te voeren. Beheerders moeten ervoor zorgen dat er een speciaal gemaakte account wordt gebruikt voor de Bind-gebruikersnaam met alleen-leestoegang tot het gedeelte van de AD/LDAP-structuur dat is opgegeven in het veld ** Base DN* *. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json `'-instelling van deze feature is ` ` UserFilter ': "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Gastenfilter ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

(Optioneel) Voer een AD/LDAP-filter in om te gebruiken bij het zoeken naar externe gebruikers die gasttoegang hebben tot Matterbest. Alleen de gebruikers die door de query zijn geselecteerd, kunnen zich aanmelden en Matterbest gebruiken als Gasten. Deze filterstandaardwaarde is leeg.

Zie de ` Guest Accou
nts documentatie <https://docs.mattermost.com/deployment/guest-accounts.html> ` __ voor meer informatie. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is ` `' GuestFilter ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Beheerfilter ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

(Optioneel) Geef een filter op voor het aanwijzen van de rol Systeembeheer voor gebruikers. Als deze optie is ingeschakeld, wordt de gebruiker gepromoveerd naar deze rol bij de volgende aanmelding of bij de volgende geplande AD/LDAP-synchronisatie. Als het beheerfilter wordt verwijderd, behouden de gebruikers die momenteel zijn aangemeld hun beheerdersrol. Wanneer ze zich afmelden is dit ingetrokken en hebben ze bij hun volgende aanmelding geen beheerdersrechten meer.

Deze filterstandaard is ` ` false ` ` en moet worden ingesteld op ` ` true ` ` om het Beheerfilter te gebruiken. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableAdminFilter ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Groepsfilter ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

(Optioneel) Voer een AD/LDAP-filter in om te gebruiken bij het zoeken naar groepsobjecten (accepteert 'algemene syntaxis <https://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm>' __). Alleen de groepen die door de query zijn geselecteerd, hebben toegang tot Matterbest.

Dit filter is standaard ingesteld op ` ` (| (objectClass=group) (objectClass=groupOfNames) (objectClass=groupOfUniqueNames)) ` ` wanneer blanco. .. Opmerking:
  Dit filter wordt alleen gebruikt als AD/LDAP Group Sync is ingeschakeld. Zie ' AD/LDAP Group Sync documentation <https://docs.mattermost.com/deployment/ldap-group-sync.html> ` _ voor meer informatie over het inschakelen en configureren van AD/LDAP Group Sync. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` ` instelling is ` ` "GroupFilter": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Kenmerk weergavenaam groep ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

(Vereist) Voer een AD/LDAP Group-kenmerk weergavenaam in dat wordt gebruikt om Matterbest Group-namen te vullen. .. Opmerking:
  Dit kenmerk wordt alleen gebruikt als AD/LDAP Group Sync is ingeschakeld. Zie ' AD/LDAP Group Sync documentation <https://docs.mattermost.com/deployment/ldap-group-sync.html> ` _ voor meer informatie over het inschakelen en configureren van AD/LDAP Group Sync. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "GroupDisplayNameAttribute": "" ` ` met string input. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Kenmerk van groep-ID ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

(Vereist) Geef een AD/LDAP Group ID-kenmerk op om te gebruiken als uniek ID voor groepen. Dit moet een AD/LDAP-waarde zijn die niet verandert. Dit is meestal ` ` entryUUID ` ` voor LDAP en ` ` objectGUID ` ` ` voor AD. .. Opmerking:
  Dit kenmerk wordt alleen gebruikt als AD/LDAP Group Sync is ingeschakeld. Zie ' AD/LDAP Group Sync documentation <https://docs.mattermost.com/deployment/ldap-group-sync.html> ` _ voor meer informatie over het inschakelen en configureren van AD/LDAP Group Sync. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' 'van deze feature is' ` ' "GroupIdAttribute": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Voornaam Kenmerk ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Het kenmerk in de AD/LDAP-server dat wordt gebruikt om de voornaam van gebruikers in Matterbest te vullen. Als deze optie is ingesteld, kunnen gebruikers hun voornaam niet bewerken, omdat deze wordt gesynchroniseerd met de LDAP-server. Wanneer dit veld leeg is, kunnen gebruikers hun voornaam in Accountinstellingen instellen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` "FirstNameAttribute": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Laatste naamkenmerk ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Het kenmerk in de AD/LDAP-server dat wordt gebruikt om de achternaam van gebruikers in Matterbest te vullen. Als deze optie is ingesteld, kunnen gebruikers hun achternaam niet bewerken, omdat deze is gesynchroniseerd met de LDAP-server. Als u dit veld leeg laat, kunnen gebruikers hun achternaam in Accountinstellingen instellen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` ' "LastNameAttribute": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Roepnaam attribuut ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Het kenmerk in de AD/LDAP-server dat wordt gebruikt om de schermnaam van gebruikers in Matterbest te vullen. Als deze optie is ingesteld, kunnen gebruikers hun roepnaam niet bewerken, omdat deze wordt gesynchroniseerd met de LDAP-server. Wanneer dit veld leeg is, kunnen gebruikers hun roepnaam instellen in Accountinstellingen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` ' "NicknameAttribute": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Positiekenmerk ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Het kenmerk in de AD/LDAP-server dat wordt gebruikt om het positieveld in Matterbest te vullen. Als deze optie is ingesteld, kunnen gebruikers hun positie niet bewerken, omdat deze is gesynchroniseerd met de LDAP-server. Wanneer dit veld leeg is, kunnen gebruikers hun positie instellen in Accountinstellingen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` "PositionAttribute": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

E-mailkenmerk ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het kenmerk in de AD/LDAP-server dat wordt gebruikt om het veld e-mailadres in Matterbest te vullen.

E-mailberichten worden naar dit e-mailadres verzonden en dit e-mailadres kan door andere gebruikers worden bekeken, afhankelijk van de privacyinstellingen die door de systeembeheerder zijn gekozen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "EmailAttribute": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Profielfoto-attribuut ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het kenmerk in de AD/LDAP-server dat wordt gebruikt voor het synchroniseren (en vergrendelen) van de profielafbeelding die in Matterbest wordt gebruikt.

De Mattermeeste server zal de profielafbeelding van de gebruiker vervangen bij aanmelding (niet op het synchronisatieinterval als met andere kenmerken). De synchronisatie vindt niet plaats als de huidige Mattermeest profielafbeelding overeenkomt met de afbeelding die is gekoppeld aan die gebruiker in AD/LDAP. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json' van deze feature is '`' "" PictureAttribute ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Gebruikersnaamkenmerk ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het kenmerk in de AD/LDAP-server dat wordt gebruikt om het veld gebruikersnaam in Matterbest te vullen. Dit kan hetzelfde zijn als het kenmerk voor het aanmeldings-ID.

Dit kenmerk wordt gebruikt in de interface van Matterendste om gebruikers te identificeren en te vermelden. Als een Username-kenmerk bijvoorbeeld is ingesteld op ** john.smith * *, wordt in de opties voor het automatisch voltooien van een gebruiker ` `@john.smith ` '` `see.smith `' afgebeeld en wordt een bericht gepost met ` `@john.smith ` ` een bericht naar die gebruiker dat ze zijn genoemd.

Het kenmerk ** Gebruikersnaamkenmerk * * kan worden ingesteld op dezelfde waarde die wordt gebruikt voor aanmelding bij het systeem, met de naam ** Login ID Attribute * *, of kan worden toegewezen aan een andere waarde. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` 'UsernameAttribute': ' " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

ID-kenmerk ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het kenmerk in de AD/LDAP-server wordt gebruikt als uniek ID in Matterbest. Het moet een AD/LDAP-kenmerk zijn met een waarde die niet wordt gewijzigd.

Als de ID-kenmerken van een gebruiker worden gewijzigd, wordt er een nieuwe Mattermeeste account (niet gekoppeld aan de vorige) gemaakt. Om dit te voorkomen, wordt aanbevolen dat een uniek kenmerk, zoals ` ` objectGUID ` ` in Active Directory en ` ` entryUUID ` ` in LDAP wordt gebruikt.

Voordat u wijzigingen kunt aanbrengen met uw LDAP-provider, kunt u aangeven of deze kenmerken in uw omgeving beschikbaar zijn.

Als u dit veld wilt wijzigen nadat gebruikers al zijn aangemeld, gebruikt u de functie 'matterbest ldap idmigrate <https://about.mattermost.com/default-platform-ldap-idmigrate>' __ CLI. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json' van deze feature is ` ` ' IdAttribute ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Kenmerk voor aanmeldings-ID ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het kenmerk in de AD/LDAP-server dat wordt gebruikt voor aanmelding bij Matterbest. Normaal gesproken is dit kenmerk gelijk aan het veld ** Username Attribute * *.

Als uw team doorgaans gebruik maakt van domain\gebruikersnaam voor aanmelding bij andere services met AD/LDAP, kunt u in dit veld domain\username opgeven om de consistentie tussen sites te behouden. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json' van deze feature is '`' LoginIdAttribute ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Naam aanmeldingsveld
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

De plaatshoudertekst die wordt afgebeeld in het aanmeldingsveld op de aanmeldingspagina. Meestal is dit de naam die wordt gebruikt om te verwijzen naar de AD/LDAP-legitimatiegegevens in uw bedrijf, zodat het herkenbaar is voor uw gebruikers. De standaardwaarde is ** AD/LDAP gebruikersnaam * *. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` LoginFieldName ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

SynchronisInterval (minuten) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Instellen hoe vaak de meeste accounts kenmerken synchroniseren met AD/LDAP, in minuten. 

Bij het synchroniseren van de kenmerken (voornaam, achternaam, achternaam en roepnaam) wordt Mattermeeste query's AD/LDAP voor relevante accountgegevens en updates van Mattermeeste bijgewerkt. 

Wanneer accounts uitgeschakeld zijn in AD/LDAP-gebruikers, worden deze in Matterbest inactief gemaakt en worden hun actieve sessies ingetrokken zodra Mattermore de kenmerken synchroniseert. Gebruik de knop ** AD/LDAP Synchronize Now * * om onmiddellijk te synchroniseren na het uitschakelen van een account. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' 'van deze feature is' ` 'SyncIntervalMinutes': 60 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- + .. opmerking::
  LDAP-synchronisaties leiden tot een groot aantal database-leesquery's. Zorg ervoor dat u de databasebelasting tijdens een synchronisatie bewaakt om te bepalen hoe vaak deze synchronisaties in uw omgeving moeten gebeuren om de prestatievermindering te minimaliseren.

Maximale paginagrootte ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het maximumaantal gebruikers dat de Mattermeeste-server tegelijk van de AD/LDAP-server zal aanvragen. Gebruik deze instelling als uw AD/LDAP-server het aantal gebruikers beperkt dat tegelijk kan worden aangevraagd.

-De waarde 0 is onbeperkt en de resultaten worden niet gepagineert.
-Een waarde van 1500 wordt aanbevolen om af te stemmen met de standaard AD/LDAP ` ` MaxPageSize ` ` instelling. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is ` ` MaxPageSize': 0 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Query-timeout (seconden) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De timeoutwaarde voor query's op de AD/LDAP-server. Verhoog deze waarde als u timeoutfouten krijgt die worden veroorzaakt door een langzame AD/LDAP-server. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "QueryTimeout": 60 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

AD/LDAP-test ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Met deze knop kunt u de verbinding met de AD/LDAP-server testen. Als de test slaagt, wordt er een bevestigingsbericht afgebeeld en als er een probleem is met de configuratie-instellingen, wordt er een foutbericht afgebeeld.

AD/LDAP Synchroniseren Nu ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze knop zorgt ervoor dat de AD/LDAP-synchronisatie plaatsvindt zodra het wordt ingedrukt. Gebruik het wanneer u een wijziging hebt aangebracht in de AD/LDAP-server die u onmiddellijk van kracht wilt laten worden. Nadat u de knop hebt gebruikt, treedt de volgende AD/LDAP-synchronisatie op na de tijd die is opgegeven in het synchronisatieinterval.

U kunt de status van de synchronisatietaak bewaken in de tabel onder deze knop. .. Opmerking:
  Als de synchronisatie ** Status** wordt afgebeeld als ` ` Wacht op ` ` en niet voltooid, zorg er dan voor dat de instelling ** Enable Synchronization with AD/LDAP* * is ingesteld op ` ` true ` `. .. figuur:: ../images/ldap-sync-table.png .. _saml-onderneming:

SAML
~ ~ ~ geven

*Beschikbaar in Enterprise Edition E20 * .. Opmerking:
   In lijn met Microsoft ADFS begeleiding raden wij ` het configureren van intranet formulieren-gebaseerde authenticatie voor apparaten die niet ondersteunen WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia> ` _.

Gebruik nieuwe SAML-bibliotheek ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Een bijgewerkte SAML-bibliotheek inschakelen, waarvoor de te installeren XML-beveiligingsbibliotheek (xmlsec1) niet vereist is.

** False**: Doorgaan met het gebruik van de bestaande implementatie die gebruikmaakt van de XML-beveiligingsbibliotheek (xmlsec1). + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ' "UseNewSAMLLibrary": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Aanmelden inschakelen met SAML ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Matterbest staat login toe met behulp van SAML. Zie de 'documentatie <https://docs.mattermost.com/deployment/sso-saml.html>' om meer te weten te komen over het configureren van SAML voor Matterbest.

** False**: Aanmelden met SAML is uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` inschakelen ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Synchroniseren van SAML-accounts inschakelen met AD/LDAP ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Matterbest synchroniseert periodiek SAML-gebruikerskenmerken, inclusief deactivering en verwijdering van gebruikers, met AD/LDAP. Synchronisatie-instellingen inschakelen en configureren op ** Verificatie > AD/LDAP* *. Raadpleeg 'documentatie <https://about.mattermost.com/default-saml-ldap-sync>' __ om meer te weten te komen.

** False**: Synchronisatie van SAML-accounts met AD/LDAP is uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "EnableSyncWithLdap": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Overschrijven van SAML Bind-gegevens met AD/LDAP-gegevens ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Matterbest overschrijft het kenmerk SAML ID met het kenmerk AD/LDAP als dit is geconfigureerd of overschrijft het kenmerk SAML Email met het kenmerk AD/LDAP Email als SAML ID-kenmerk niet aanwezig is. Raadpleeg 'documentatie <https://about.mattermost.com/default-saml-ldap-sync>' __ om meer te weten te komen.

** False**: Matterbest gebruikt het e-mailkenmerk om gebruikers te binden aan SAML. .. Opmerking:
  Bij het verplaatsen van ` true ` naar ` ` false ` ` wordt voorkomen dat de vervanging plaatsvindt. Om het uitschakelen van gebruikersaccounts te voorkomen, moeten SAML-ID's overeenkomen met de LDAP-ID's wanneer deze functie is ingeschakeld. Deze instelling moet worden ingesteld op ` ` false ` ` tenzij LDAP-synchronisatie is ingeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "EnableSyncWithLdapIncludeAuth": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

SAML SSO-URL ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De URL waar Matterbest een SAML-opdracht verzendt om de aanmeldingsprocedure te starten. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json' van deze feature is ` ` 'IdpURL ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Identiteit provider verstrekkende instantie URL ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De verstrekker-URL voor de ID-provider die u gebruikt voor SAML-aanvragen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' ' van deze feature is ` ` "IdpDescriptorUrl": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Metagegevens-URL van identiteitsprovider ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De URL waar Matterbest een opdracht verzendt voor het verkrijgen van de configuratiegegevens van de provider. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json' van deze feature is ` ` ` IdpMetadataUrl ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Identiteitsprovider Openbaar Certificaat ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het openbare verificatiecertificaat dat is afgegeven door uw ID-provider. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' van deze feature is '`' "IdpCertificateFile": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Verifieer Handtekening ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Matterbest controleert of de handtekening die is verzonden vanuit de SAML-respons overeenkomt met de aanmeldings-URL van de serviceprovider.

** False**: Niet aanbevolen voor productieomgevingen. Alleen voor testen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` Controleren ": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Serviceverlener-ID ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het unieke ID voor de serviceprovider, gewoonlijk hetzelfde als de aanmeldings-URL van de serviceprovider. In ADFS moet dit overeenkomen met het ID van de Relying Party. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is' ` '-ServiceProviderIdentifier: "" ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Aanmeldings-URL van serviceprovider ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Typ ' ` https: //<your-mattermost-url>/login/sso/saml ` ` (bijvoorbeeld: ``https: //example.com/login/sso/saml ` `). Controleer of u HTTP of HTTPS gebruikt in uw URL, afhankelijk van de serverconfiguratie. Dit veld wordt ook wel de URL van de consumentenservice voor bevestiging genoemd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json' van deze feature is '`' "AssertionConsumerServiceURL": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

SignatureAlgorithm ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het handtekeningalgoritme dat wordt gebruikt om het verzoek te ondertekenen. De ondersteunde opties zijn ` RSAwithSHA1 <https: //www.w3.org/2000/09/xmldsig#rsa-sha1> ` _, ` RSAwithSHA256 <https: //www.w3.org/2000/09/xmldsig#rsa-sha1> ` _ en ` RSAwithSHA512 <https: //www.w3.org/2001/04/xmldsig-meer#rsa-sha512 > ` _. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` ` instelling van deze feature is' ` SignatureAlgorithm ': "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

CanonicalAlgorithm ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het canonicalisatie-algoritme. De ondersteunde opties zijn ' Exclusive XML Canonicalization 1.0 <https://www.w3.org/2001/10/xml-exc-c14n#> ` _ en ` Canonical XML 1.1 <https://www.w3.org/2006/12/xml-c14n11> ` _. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '``config.json' van deze feature is '`' "CanonicalAlgorithm": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Versleuteling inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Matterbest zal SAML Assertions decoderen die zijn versleuteld met uw Serviceverlener Public Certificate.

** False**: Niet aanbevolen voor productieomgevingen. Alleen voor testen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` ` instelling van deze feature is' ` 'Encrypt ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Persoonlijke sleutel serviceprovider ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De persoonlijke sleutel voor het decoderen van SAML-Assertions van de Identity Provider. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` PrivateKeyFile ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Openbaar certificaat van serviceprovider ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het certificaatbestand dat wordt gebruikt voor het genereren van de handtekening op een SAML-aanvraag naar de Identity Provider voor een serviceprovider die SAML-aanmelding heeft gestart, wanneer Matterbest de Service Provider is. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` ` instelling is ` ` "PublicCertificateFile": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Aanmeldingsaanvraag ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
Wanneer ` ` true ` ` ` `, Mattermeeste ondertekent de SAML-aanvraag met behulp van uw Serviceverlener Private Key. Wanneer ` ` false ` ` `, teken Matterbest de SAML-aanvraag niet. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' van deze feature is '`' SignRequest ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

E-mailkenmerk ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het kenmerk in de SAML Assertion dat wordt gebruikt om de e-mailadressen van gebruikers in Matterbest te vullen.

E-mailberichten worden naar dit e-mailadres verzonden, en dit e-mailadres kan door andere gebruikers worden bekeken, afhankelijk van de privacyinstellingen die worden gekozen door de systeembeheerder. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "EmailAttribute": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Gebruikersnaamkenmerk ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het kenmerk in de SAML Assertion dat wordt gebruikt voor het invullen van het gebruikersnaamveld in de interface van Mattermeeste. Dit kenmerk wordt gebruikt in de interface van Matterendste om gebruikers te identificeren en te vermelden. Als een Username-kenmerk bijvoorbeeld is ingesteld op ** john.smith * * wordt in de auto-complete opties een gebruiker met ` `@john.smith ` ` zien en een bericht gepost met ` `@john.smith ` ` een bericht naar die gebruiker sturen dat ze zijn genoemd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` 'UsernameAttribute': ' " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Id-attribuut ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Het kenmerk in de SAML Assertion dat wordt gebruikt om gebruikers van SAML te binden aan gebruikers in Matterbest.

+ ---------------------------------------------------------------------------------------------------------------------------------
------------------------------------- +
| De instelling '` `config.json' van deze feature is ` ` ' IdAttribute ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Gastenkenmerk ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

(Optioneel) Het kenmerk in de SAML Assertion dat wordt gebruikt om een gastrol toe te passen op gebruikers in Matterbest.

Zie de ` Guest Accounts documentation <https://docs.mattermost.com/deployment/guest-accounts.html> ` __ voor meer informatie. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "GuestAttribute": "" ` ` met string invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Beheerderskenmerk ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

(Optioneel) Het kenmerk in de SAML-verklaring voor het aanduiden van systeembeheerders. De gebruiker wordt automatisch gepromoveerd naar deze rol bij de volgende aanmelding. Als het Beheerkenmerk wordt verwijderd, behouden de gebruikers die momenteel zijn aangemeld hun beheerdersrol. Wanneer ze zich afmelden is dit ingetrokken en hebben ze bij hun volgende aanmelding geen beheerdersrechten meer.

De standaardwaarde van dit kenmerk is ` ` false ` ` en moet worden ingesteld op ` ` true ` ` om het Beheerkenmerk te gebruiken. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableAdminAttribute ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Voornaam Kenmerk ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Het kenmerk in de SAML Assertion dat wordt gebruikt om de voornaam van gebruikers in Matterbest te vullen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` "FirstNameAttribute": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Laatste naamkenmerk ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Het kenmerk in de SAML Assertion dat wordt gebruikt om de achternaam van gebruikers in Matterbest te vullen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` ' "LastNameAttribute": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Roepnaam attribuut ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Het kenmerk in de SAML Assertion dat wordt gebruikt om de schermnaam van gebruikers in Matterbest te vullen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` ' "NicknameAttribute": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Positiekenmerk ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Het kenmerk in de SAML Assertion dat wordt gebruikt om het positieveld voor gebruikers in Matterbest te vullen (meestal gebruikt om de functie of rol van een persoon in het bedrijf te beschrijven). + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` "PositionAttribute": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Voorkeur voor taalkenmerk ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Het kenmerk in de SAML Assertion dat wordt gebruikt om de taal van gebruikers in Matterbest te vullen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' van deze feature is ' ` "LocaleAttribute": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Aanmeldknop Tekst ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) De tekst die verschijnt in de aanmeldknop op de aanmeldingspagina. De standaardwaarde is **SAML* *. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is '`' LoginButtonText ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

IDP-provider-ID afbakenen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Hiermee kan een geverifieerde gebruiker de eerste aanmeldingspagina van hun federatieve Azure AD-server overslaan en alleen een wachtwoord vereisen om zich aan te melden. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is '`' "ScopingIDPProviderId": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

ID's afbakenen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Hiermee voegt u de naam toe die is gekoppeld aan het ID van een Scoping-ID van een gebruiker. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is '`' "ScopingIDPName": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

OAuth 2.0
~ ~ ~ ~ nopen ~ ~

Instellingen voor het configureren van OAuth-aanmelding voor het maken en aanmelden van accounts.

OAuth 2.0-serviceprovider selecteren
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Kies of OAuth kan worden gebruikt voor het maken van accounts en het aanmelden. Opties zijn onder andere:

    -* * Niet toestaan aanmelding via een OAuth 2.0-provider * *
    -** GitLab** (zie ` GitLab Settings <https: //docs.mattermost.com/administration/config-settings.html#gitlab> ` __ voor meer informatie)
    -** Google Apps * * (beschikbaar in Enterprise Edition E20, zie ` Google Settings <https: //docs.mattermost.com/administration/config-settings.html#google> ` __ voor meer informatie)
    -** Office 365 * * (beschikbaar in Enterprise Edition E20, zie ` Office 365 Settings <https: //docs.mattermost.com/administration/config-settings.html#office-365 > ` __ voor meer informatie)

De instelling van deze functie wordt niet afgebeeld in ` `config.json ` `.

GitLab
~ ~ ~ ~ nten

Authenticatie met GitLab inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ Als u wilt configureren, geeft u de legitimatiegegevens ** Secret** en ** Id** op.

** False**: GitLab OAuth kan niet worden gebruikt voor het creëren van teams of het aanmelden van accounts.

** Note**: Voor Enterprise kunt u GitLab-instellingen vinden onder ** OAuth 2.0 * * + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` inschakelen ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Toepassings-ID ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Verkrijg deze waarde door u aan te melden bij uw GitLab-account. Ga naar ** Profielinstellingen > Toepassingen > Nieuwe toepassing * *, voer een naam in en voer vervolgens Redirect-URL's in ' ` https: //<your-mattermost-url>/login/gitlab/complete ` ` (voorbeeld: ` ` https: //example.com: 8065/login/gitlab/complete ` ` en ` ` https: //<your-mattermost-url>/signup/gitlab/complete ` `. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ' "Id": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Toepassingsgeheime sleutel ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Verkrijg deze waarde door u aan te melden bij uw GitLab-account. Ga naar ** Profielinstellingen > Toepassingen > Nieuwe toepassing * *, voer een naam in en voer vervolgens Redirect-URL's in ' ` https: //<your-mattermost-url>/login/gitlab/complete ` ` (voorbeeld: ` ` https: //example.com: 8065/login/gitlab/complete ` ` en ` ` https: //<your-mattermost-url>/signup/gitlab/complete ` `. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is' ` ' "geheim": "" ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Gebruiker API-eindpunt ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Typ ' ` https: //<your-gitlab-url>/api/v3/user ` ` (bijvoorbeeld: ``https: //example.com: 3000/api/v3/user ` `). Gebruik HTTP of HTTPS afhankelijk van hoe uw server is geconfigureerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json' ' van deze feature is ` ` ` UserApiEndpoint ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

* ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ Gebruik HTTP of HTTPS afhankelijk van hoe uw server is geconfigureerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is '`' AuthEndpoint ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Tokeneindpunt ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Typ ` ` https: //<your-gitlab-url>/oauth/token ` ` ` (voorbeeld: ``https: //example.com: 3000/oauth/token ` `). Gebruik HTTP of HTTPS afhankelijk van hoe uw server is geconfigureerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is '` TokenEndpoint': "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Google
~ ~ ~ ~ nten

*Beschikbaar in Enterprise Edition E20 *

Schakel de verificatie met Google in door ` ` Google Apps ` ` te selecteren uit ** OAuth 2.0 > Selecteer OAuth 2.0-serviceprovider * *.

** True**: Toestaan teamcreatie en account aanmelden met behulp van Google OAuth. Als u wilt configureren, geeft u de legitimatiegegevens voor ** Client ID* * en ** Client Secret * * op. Raadpleeg de documentatie <https://docs.mattermost.com/deployment/sso-google.html> voor meer informatie.

** False**: Google OAuth kan niet worden gebruikt voor het maken of account van een team. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` inschakelen ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Client-ID ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Verkrijg deze waarde door Matterbest te registreren als een toepassing in uw Google-account. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ' "Id": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Klantgeheim ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Verkrijg deze waarde door Matterbest te registreren als een toepassing in uw Google-account. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is' ` ' "geheim": "" ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Gebruiker API-eindpunt ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het wordt aanbevolen om ' https: //people.googleapis.com/v1/people/me?personFields=names, emailAddresses, nicknames, metadata ` te gebruiken als het User API Endpoint. Anders voert u een aangepast eindpunt in in ` `config.json ` ` met HTTP of HTTPS, afhankelijk van hoe uw server is geconfigureerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json `' instelling van deze feature is '`' "UserApiEndpoint": "https: //people.googleapis.com/v1/people/me?personFields=names, emailAddresses, nicknames, metadata" ` ` |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het is raadzaam om ` ` "https: //accounts.google.com/o/oauth2/v2/auth" ` ` te gebruiken als het Auth Endpoint. Anders voert u een aangepast eindpunt in in ` `config.json ` ` met HTTP of HTTPS, afhankelijk van hoe uw server is geconfigureerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "AuthEndpoint": "https: //accounts.google.com/o/oauth2/v2/auth" ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Tokeneindpunt ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het is raadzaam om ` ` "https: //www.googleapis.com/oauth2/v4/token" ` ` te gebruiken als het Token-eindpunt. Anders voert u een aangepast eindpunt in in ` `config.json ` ` met HTTP of HTTPS, afhankelijk van hoe uw server is geconfigureerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is '` TokenEndpoint': 'https: //www.googleapis.com/oauth2/v4/token' ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Kantoor 365
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

*Beschikbaar in Enterprise Edition E20 * .. Opmerking:
   In lijn met Microsoft ADFS begeleiding raden wij ` het configureren van intranet formulieren-gebaseerde authenticatie voor apparaten die niet ondersteunen WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia> ` _.

Schakel verificatie met Office 365 in door ** Office 365 * * from ** System Console > Authentication > OAuth 2.0 > OAuth 2.0 service provider * * te selecteren.

** True**: Toestaan teamcreatie en account aanmelden met Office 365 OAuth. Als u wilt configureren, geeft u de legitimatiegegevens voor ** Application ID* * en ** Application Secret Password * * op. Raadpleeg de documentatie <https://docs.mattermost.com/deployment/sso-office.html> voor meer informatie.

** False**: Office 365 OAuth kan niet worden gebruikt voor het maken of account van het team. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` inschakelen ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Toepassings-ID ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

U kunt deze waarde verkrijgen door Matterbest te registreren als een toepassing in uw Microsoft-of Office-account. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ' "Id": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Wachtwoord van toepassingsgeheim ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

U kunt deze waarde verkrijgen door Matterbest te registreren als een toepassing in uw Microsoft-of Office-account. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is' ` ' "geheim": "" ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Map (tenant) ID ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze waarde is het ID van de AAD-directory van de toepassing. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is '` ` DirectoryId': "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Gebruiker API-eindpunt ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het is raadzaam om ` ` "https: //graph.microsoft.com/v1.0/me" ` ` te gebruiken als het User API Endpoint. Anders voert u een aangepast eindpunt in in ` `config.json ` ` met HTTP of HTTPS, afhankelijk van hoe uw server is geconfigureerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is '`' "UserApiEndpoint": "https: //graph.microsoft.com/v1.0/me" ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het is raadzaam om ` ` "https: //accounts.google.com/o/oauth2/v2/auth" ` ` te gebruiken als het Auth Endpoint. Anders voert u een aangepast eindpunt in in ` `config.json ` ` met HTTP of HTTPS, afhankelijk van hoe uw server is geconfigureerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "AuthEndpoint": "https: //login.microsoftonline.com/common/oauth2/v2.0/authorize" ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Tokeneindpunt ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het is raadzaam om ` ` "https: //login.microsoftonline.com/common/oauth2/v2.0/token" ` ` te gebruiken als het Token-eindpunt. Anders voert u een aangepast eindpunt in in ` `config.json ` ` met HTTP of HTTPS, afhankelijk van hoe uw server is geconfigureerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is '` TokenEndpoint': 'https: //login.microsoftonline.com/common/oauth2/v2.0/token' ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Gasttoegang (Beta)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Gasttoegang inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Toestaan gastuitnodigingen aan kanalen binnen teams. Zie de ` Guest Accounts documentation <https://docs.mattermost.com/deployment/guest-accounts.html> ' _ voor meer informatie.

** False**: E-mail aanmelden is uitgeschakeld. Deze limiet is aangegeven voor SSO-services zoals OAuth of AD/LDAP. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` inschakelen ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Goedgekeurde gastdomeinen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Indien gevuld, kunnen gastaccounts alleen worden gemaakt door een geverifieerde e-mail uit deze lijst met door komma's gescheiden domeinen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` ` instelling is ` ` ` RestrictCreationToDomains ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Toezien op de toepassing van de multifactorificatie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze instelling is standaard ingesteld op 'false' en is alleen-lezen als verificatie met meerdere factoren niet wordt afgedwongen voor gewone gebruikers.

** True**: Wanneer waar, is multi-factor authenticatie (MFA) vereist voor login. Er zijn nieuwe gastgebruikers vereist voor het configureren van MFA bij het aanmelden. Gelogd in gastgebruikers zonder MFA geconfigureerd worden doorgestuurd naar de MFA setup pagina totdat de configuratie is voltooid.

** False**: Multi-factor authenticatie voor gasten is optioneel. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` EnforceMultifactorAuthentication ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Plugins (Beta)
--------------

Instellingen voor het configureren van plugins.

Pluginbeheer
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Plugins inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Stelt plugins in staat op uw Mattertiste server. Gebruik plugins om te integreren met systemen van derden, uitbreiding van de functionaliteit, of het aanpassen van de gebruikersinterface van uw Matterendste server. Raadpleeg 'documentatie <https://about.mattermost.com/default-plugins>' __ om meer te weten te komen.

** False**: Hiermee schakelt u plugins uit op uw Matterste-server. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ' "Inschakelen": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Automatisch voorverpakte plugins ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Alle vooraf ingepakte plugins die in de configuratie zijn ingeschakeld, worden automatisch geïnstalleerd of geüpgraded. Als er al een nieuwere versie is geïnstalleerd, worden er geen wijzigingen aangebracht.

** False**: Voorverpakte plugins worden niet automatisch geïnstalleerd of geüpgraded, maar kunnen handmatig worden geïnstalleerd vanuit de Plugin Marketplace, zelfs wanneer offline. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` AutomaticPrepackagedPlugins ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Markt inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Hiermee schakelt u de plugin-markt in op uw Matterste-server voor alle systeembeheerders.

** False**: Schakelt Plugin Marketplace op uw Mattermeeste server uit voor alle systeembeheerders. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` ` EnableMarketplace': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Schakel Op Afstand Markt ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: De server zal proberen om verbinding te maken met de geconfigureerde Plugin Marketplace om de nieuwste plugins te tonen. Als de verbinding mislukt, toont de Plugin Marketplace alleen voorverpakte en reeds geïnstalleerde plugins naast een verbindingsfout.

** False**: De server zal niet proberen om verbinding te maken met een externe markt, in plaats daarvan alleen te tonen voorverpakt en al geïnstalleerde plugins. Gebruik deze instelling als uw server geen verbinding kan maken met internet. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` ` instelling van deze feature is ` `' EnableRemoteMarketplace ': true ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Markt-URL ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als de Marketplace is ingeschakeld, geeft deze instelling aan welke URL moet worden gebruikt voor het zoeken naar nieuwe marktplugins. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "MarketplaceUrl": "https: //api.integrations.mattermost.com" ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Plugin-instellingen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Instellingen die specifiek zijn voor elke plugin. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json `' van deze feature is ` ` 'Plugins': { } ` ` met objectinvoertoewijzingsplugin-ID's als sleutels voor objecten die pluginspecifieke gegevens bevatten. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Geïnstalleerde Plugin Staat ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geeft een lijst van geïnstalleerde plugins op uw Mattermeeste-server en of deze zijn ingeschakeld. Voorverpakte plugins zijn standaard geïnstalleerd en kunnen worden gedeactiveerd, maar niet verwijderd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json `' van deze feature is ` ` PluginStates ': { } ` ` met objectinvoertoewijzingsplugin-ID's als sleutels voor objecten, die elk een sleutel' ` 'inschakelen' bevatten: 'false' ` met opties ` ` true ` ` of ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Plugin-handtekening vereist ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Vereist geldige plugin-handtekeningen voordat u beheerde of niet-beheerde plugins start. Voorverpakte plugins zijn niet onderworpen aan verificatie van de plugin. Plugins geïnstalleerd via de Plugin Marketplace zijn altijd onderworpen aan plugin handtekening controle op het moment van downloaden.

** False**: vereisen geen geldige plugin-handtekeningen voordat u beheerde of niet-beheerde plugins start. Voorverpakte plugins zijn niet onderworpen aan verificatie van de plugin. Plugins die zijn geïnstalleerd via de Plugin Marketplace zijn altijd onderhevig aan controle van de plugin handtekening op het moment van downloaden. + ---------------------------------------------------------------------------------------------------------------------
| De '`config.json ` ` instelling van deze feature is ` `' RequirePluginSignature ': true ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------

Ondertekening Openbare sleutelbestanden ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Naast de plugin voor de Matterbest-plugin die in de server is ingebouwd, is elke openbare sleutel die hier is opgegeven, betrouwbaar voor het valideren van de plugin-handtekeningen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' van deze feature is '` SignaturePublicKeyFiles': { } ` ` met met tekenreeksinvoer bestaande uit inhoud die relatieve of absolute paden zijn naar handtekeningbestanden. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Autolink
~ ~ ~ ~ nten

Configureer deze plugin rechtstreeks in het ` `config.json ` ` bestand. Lees meer " in onze documentatie <https://github.com/mattermost/mattermost-plugin-autolink/blob/master/README.md> ` _.

Aangepaste gebruikerskenmerken
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Configureer deze plugin rechtstreeks in het ` `config.json ` ` bestand. Lees meer " in onze documentatie <https://github.com/mattermost/mattermost-plugin-custom-attributes/blob/master/README.md> ` _.

GitHub
~ ~ ~ ~ nten

Configureer deze plugin rechtstreeks in het ` `config.json ` ` bestand. Lees meer " in onze documentatie <https://github.com/mattermost/mattermost-plugin-github/blob/master/README.md> ` _.

Jira
~ ~ ~ geven

Configureer deze plugin rechtstreeks in het ` `config.json ` ` bestand. Lees meer " in onze documentatie <https://github.com/mattermost/mattermost-plugin-jira/blob/master/README.md> ` _.

Nettopromotor
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Configureer deze plugin rechtstreeks in het ` `config.json ` ` bestand. Lees meer " in onze documentatie <https://mattermost.com/pl/default-nps> ` _.

Welkom Bot
~ ~ ~ ~ nopen ~ ~

Configureer deze plugin rechtstreeks in het ` `config.json ` ` bestand. Lees meer " in onze documentatie <https://github.com/mattermost/mattermost-plugin-welcomebot/blob/master/README.md> ` _.

Zoomen
~ ~ ~ geven

Configureer deze plugin rechtstreeks in het ` `config.json ` ` bestand. Lees meer " in onze documentatie <https://github.com/mattermost/mattermost-plugin-zoom/blob/master/README.md> ` _.

Integraties
-------------

Instellingen voor het configureren van webhooks, slash-opdrachten en externe integratieservices.

Integratiebeheer
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Inkomende Webhooks ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ Zie onze ` documentatiepagina <https://docs.mattermost.com/developer/webhooks-incoming.html> ` __ om te leren over het maken van webhaken, bekijk voorbeelden, en om de gemeenschap te laten weten over integraties die u hebt gebouwd.

** True**: Inkomende webhaken zijn toegestaan. Voor het beheren van binnenkomende webhooks gaat u naar ** Accountinstellingen > Integraties * *. De webhook-URL's die zijn gemaakt in Accountinstellingen kunnen worden gebruikt door externe toepassingen voor het maken van berichten in een openbare of besloten kanalen waartoe u toegang hebt.

** False**: De sectie ** Integraties > Inkomende Webhooks * * De sectie Accountinstellingen is verborgen en alle inkomende webhooks zijn uitgeschakeld.

Beveiligingsopmerking: Door deze functie in te schakelen kunnen gebruikers 'phishing aanvallen <https://en.wikipedia.org/wiki/Phishing>' __ uitvoeren door te proberen andere gebruikers te imiteren. Om deze aanvallen te bestrijden, een BOT-tag verschijnt naast alle berichten van een webhook. Activeer op eigen risico. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' `config.json ` ` instelling van deze feature is ` ` ` Ena
bleIncomingWebhooks ": true ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Uitgaande Webhaken Inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Ontwikkelaars bouwen van integraties kan maken webhook tokens voor Openbare kanalen. Triggerwoorden worden gebruikt om nieuwe berichten te starten voor externe integraties. Om veiligheidsredenen zijn uitgaande webhaken alleen beschikbaar in de openbare kanalen. Zie onze ` documentatiepagina <https://docs.mattermost.com/developer/webhooks-outgoing.html> ` __ om te leren over het maken van webhaken en bekijk voorbeelden.

** True**: Uitgaande webhaken zijn toegestaan. Om uitgaande webhooks te beheren, gaat u naar ** Accountinstellingen > Integraties * *.

** False**: De sectie ** Integraties > Outgoing Webhooks * * van Accountinstellingen is verborgen en alle uitgaande webhooks zijn uitgeschakeld.

Beveiligingsopmerking: Door deze functie in te schakelen kunnen gebruikers 'phishing aanvallen <https://en.wikipedia.org/wiki/Phishing>' __ uitvoeren door te proberen andere gebruikers te imiteren. Om deze aanvallen te bestrijden, een BOT-tag verschijnt naast alle berichten van een webhook. Activeer op eigen risico. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` ` EnableOutgoingWebhooks': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Aangepaste slash-opdrachten ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Schuine streep naar rechts sturen gebeurtenissen naar externe integraties die een reactie terugsturen naar Matterbest.

** True**: Gebruikers toestaan om aangepaste slash-opdrachten te maken van ** Hoofdmenu > Integraties > Opdrachten * *.

** False**: Slash-opdrachten worden verborgen in de gebruikersinterface ** Integrations**. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableOpdrachten ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

OAuth 2.0-serviceprovider inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Mattermeeste werkt als een OAuth 2.0 service provider die Matterbest toestaat om API-aanvragen van externe toepassingen te machtigen.

** False**: Matterbest werkt niet als een OAuth 2.0-serviceprovider. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "EnableOAuthServiceProvider": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Het beheer van integraties beperken tot de beheerders ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

* Deze machtiging is gemigreerd naar de database en het wijzigen van de ` `config.json ` ` ` waarde wordt niet meer van kracht na het upgraden naar v4.9, vrijgegeven op 16 april 2018. Deze machtiging kan worden gewijzigd met behulp van de gebruikersinterface van de systeemconsole. *

** True**: Wanneer ` ` true ` ` ` ` kunnen webhooks en slash opdrachten alleen worden gemaakt, bewerkt, en bekeken door Team en System Admins, en OAuth 2.0 toepassingen door System Admins. Integraties zijn beschikbaar voor alle gebruikers nadat ze zijn gemaakt door de Admin.

** False**: Alle teamleden kunnen webhooks, slash-opdrachten en OAuth 2.0-toepassingen maken vanuit ** Hoofdmenu > Integraties * *. Opmerking:
  OAuth 2.0-toepassingen kunnen door alle gebruikers worden geautoriseerd als ze de Client ID* * en ** Client Secret * * hebben voor een app-installatie op de server. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` `' EnableOnlyAdminIntegrations ': true ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Schakel integratie in om gebruikersnamen te overschrijven ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Webhooks, slash-commando's, OAuth 2.0 apps en andere integraties zoals ` Zapier <https://docs.mattermost.com/integrations/zapier.html> ` __, zullen de gebruikersnaam die ze posten kunnen wijzigen. Als er geen gebruikersnaam aanwezig is, is de gebruikersnaam voor de post hetzelfde als voor de instelling van ` ` False ` `.

** False**: Aangepaste slash-opdrachten kunnen alleen posten als de gebruikersnaam van de gebruiker die de slash-opdracht heeft gebruikt. OAuth 2.0 apps kunnen alleen posten als de gebruikersnaam van de gebruiker die de integratie heeft ingesteld. Voor binnenkomende webhaken en uitgaande webhooks is de gebruikersnaam "webhook". Zie https://mattermost.org/webhooks voor meer informatie. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnablePostUsernameOverride ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Inschakelen van integraties om profielfoto pictogrammen te overschrijven ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Webhooks, slash-opdrachten en andere integraties, zoals ` Zapier <https://docs.mattermost.com/integrations/zapier.html> ` __, kunnen de profielfoto waarmee ze worden gepost wijzigen.

** False**: Webhooks, slash-opdrachten en OAuth 2.0 apps kunnen alleen posten met het profielbeeld van het account waarmee ze zijn ingesteld. Zie https://mattermost.org/webhooks voor meer informatie. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnablePostIconOverride ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Persoonlijke Toegangstokens Inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Wanneer ` ` true ` ` ` `, kunnen gebruikers ` personal access tokens <https://about.mattermost.com/default-user-access-tokens> ` __ voor integraties in ** Account Instellingen > Beveiliging * *. Ze kunnen worden gebruikt voor de verificatie van de API en voor volledige toegang tot het account.

Ga naar de pagina ** System Console > Users * * om te beheren wie persoonlijke toegangstokens kan maken of gebruikers kunnen zoeken op token-ID.

** False**: Persoonlijke toegangstokens zijn uitgeschakeld op de server. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` 'EnableUserAccessTokens': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Bot-accounts
~ ~ ~ ~ nopen ~ ~

Bot Account Aanmaken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Wanneer ` ` true ` ` ` `, kunnen gebruikers bot accounts aanmaken voor integraties in ** Integraties > Bot Accounts * *. Bot accounts zijn vergelijkbaar met gebruikersaccounts, behalve dat ze niet kunnen worden gebruikt om in te loggen. Zie de ` documentatie <https://docs.mattermost.com/developer/bot-accounts.html> ` _ voor meer informatie.

** False**: Bot-accounts kunnen niet worden gemaakt via de gebruikersinterface of de RESTful API. Plugins kunnen bot nog steeds maken en beheren. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableBotAccountCreation ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Bot-accounts uitschakelen wanneer de eigenaar wordt gedeactiveerd ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Als een gebruiker gedeactiveerd is, schakelt u alle bot-accounts uit die door de gebruiker worden beheerd. Voor het opnieuw inschakelen van bot accounts, ga naar ** Integraties > Bot Accounts * *.

** False**: Als een gebruiker wordt gedeactiveerd, blijven alle bot-accounts die door de gebruiker worden beheerd actief. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json' van deze feature is '` DisableBotswana WhenOwnerIsDeactivated': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

GIF (Beta)
~ ~ ~ ~ nopen ~ ~

GIF-kiezer (^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Gebruikers toestaan GIFs te selecteren uit de emoji picker via een Gfycat-integratie.

** False**: GIFs kunnen niet worden geselecteerd in de emoji-kiezer. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` ` ` EnableGifPicker': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- + .. opmerking:: ` Link previews <https: //docs.mattermost.com/administration/config-settings.html#enable-link-previews> ` _ moet worden ingeschakeld om previews van GIF-links af te beelden. De meeste implementaties die beperkt zijn tot toegang achter een firewall moeten poort 443 openen naar zowel https://api.gfycat.com/v1 als https://gfycat.com/<id> (voor alle opdrachttypen) om deze functie te laten werken.

Gfycat API-toets ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als dit veld leeg is, gebruikt Gfycat de standaard API-sleutel. U kunt ook een unieke API-sleutel aanvragen op https://developers.gfycat.com/signup/#/. Geef het client-ID op dat u ontvangt via e-mail naar dit veld. + ----------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` ' "GfycatApiKey": "2_KtH_W5" ` ` met reeksinvoer. |
----------------------------------------------------------------------------------------------- +

Gfycat API-geheim ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het API-geheim dat is gegenereerd door Gfycat voor uw API-sleutel. Als dit veld leeg is, gebruikt Gfycat het standaard-API-geheim. + --------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "GfycatApiSecret": "3wLVZPiswc3DnaiaFoLkDvB4X0IV6CpMkj4tf2inJRsBY6-FnkT08zGmppWFgeof" ` ` met reeksinvoer. |
+ --------------------------------------------------------------------------------------------------------------------------------------------------------- +

CORS
~ ~ ~ geven

Aanvragen van meerdere oorsprong inschakelen van ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

HTTP-kruis-oorsprongaanvragen inschakelen op basis van specifieke domeinen, gescheiden door spaties. Typ ` ` * ` ` om CORS toe te staan van elk domein of laat het leeg om het uit te schakelen. .. Opmerking:
 Zorg ervoor dat u uw site-URL hebt ingevoerd voordat u deze instelling inschakelt om te voorkomen dat u na het opslaan toegang krijgt tot de systeemconsole. Als u na het wijzigen van deze instelling de toegang tot de systeemconsole hebt verloren, kunt u uw ` Site-URL <https: //docs.mattermost.com/administration/config-settings.html#site-url> ' __ instellen via het bestand ` `config.json ` `. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' van deze feature is '`' "AllowCorsFrom": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

CORS-blootgestelde kopteksten ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Goedgekeurde lijst van headers die toegankelijk zijn voor de aanvrager. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json' van deze feature is '`' "CorsExposedHeaders": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

CORS Legitimatiegegevens ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Aanvragen die pass-pass valideren bevatten de header ` ` Access-Control-Allow-Credentials ` `.

** False**: Aanvragen bevatten geen koptekst ` ` Access-Control-Allow-Credentials ''. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` 'CorsAllowCredentials': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

CORS foutopsporing ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Berichten in de logboeken afdrukken om te helpen bij het ontwikkelen van een integratie die CORS gebruikt. Deze berichten bevatten de waarde van het gestructureerde sleutelwaardepaar ` ` "bron": "cors" ` `.

** False**: Foutopsporingsberichten die niet worden afgedrukt in de logboeken. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` 'CorsDebug': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Naleving
------------

Gegevensbewaarbeleid
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Ng~

*Beschikbaar in Enterprise Edition E20 *

Voor wijzigingen in de eigenschappen in deze sectie is het nodig dat de server opnieuw wordt gestart voordat de wijzigingen worden doorgevoerd. waarschuwing: als een bericht of bestand eenmaal is gewist, is de actie onomkeerbaar. Wees voorzichtig bij het instellen van een aangepast gegevensretentiebeleid.

Retentie Van Berichten ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Instellen hoe lang Matterbest berichten in kanalen en directe berichten bewaart.

Als ** Berichten bewaren voor een ingestelde hoeveelheid tijd * * wordt gekozen, stelt u in hoeveel dagen de berichten in Matterbest worden bewaard. Berichten, inclusief bestandsbijlagen die ouder zijn dan de duur die u hebt ingesteld, worden ' s nachts gewist. De minimumtijd is één dag. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' van deze feature is '` ` EnableMessageDeletion': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. | + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- + en + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` MessageRetentionDays ": 365 ` ` met numerieke invoer. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Bestandsretentie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Stel in hoe lang Matterbest bestanden en directe berichten uploadt.

Als ** Bestanden bewaren voor een ingestelde hoeveelheid tijd * * is gekozen, stelt u in hoeveel dagen de uploads van bestanden in Matterbest worden bewaard. Bestanden die ouder zijn dan de tijdsduur die u instelt, worden ' s nachts gewist. De minimumtijd is één dag. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableFileDeletion ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. | + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- + en + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ``config.json ` ` instelling van deze feature is ` ` "FileRetentionDays": 365 ` ` met numerieke invoer. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Gegevenswistime ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Stel de begintijd in van de dagelijkse geplande bewaartermijn voor gegevens. Kies een tijd waarin minder mensen uw systeem gebruiken. Moet een tijdsaanduiding van 24 uur zijn in de vorm ` ` UU:MM ` ` `.

Deze instelling is gebaseerd op de lokale tijd van de server. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "DeletionJobStartTime": "02:00" ` ` met 24-uurs tijdsaanduiding invoer in het formulier ` ` "UU:MM" ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Wissen-taak uitvoeren nu ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Met deze knop start u onmiddellijk een taak voor het wissen van gegevens.

U kunt de status van de taak bewaken in de tabel met gegevenswisacties onder deze knop.

Nalevingsexport (Beta)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Ng~

*Beschikbaar als addon voor Enterprise Edition E20 *

Naleving Van Compliance Mogelijk Maken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Wanneer ` ` true ` ` ` ` is, zal Matterbest een exportbestand genereren dat alle berichten bevat die in de afgelopen 24 uur zijn gepost. De exporttaak wordt eenmaal per dag uitgevoerd. Zie de ` documentatie voor meer informatie over <https://about.mattermost.com/default-compliance-export-documentation> ` __.

** False**: Wanneer ` ` false ` ` ` `, genereert Matterbest geen nalevingsexportbestand. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "EnableExport": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Uitvoeringstijd (^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Stel de begintijd in van de taak voor het exporteren van de geplande dagelijkse naleving. Kies een tijd waarin minder mensen uw systeem gebruiken. Moet een tijdsaanduiding van 24 uur zijn in de vorm ` ` UU:MM ` ` `.

Deze instelling is gebaseerd op de lokale tijd van de server. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` DailyRunTime ': 01:00 ` ` met 24-uurs tijdaanduidinginvoer in het formulier ` ` "UU:MM" ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Exportbestandsformaat ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Bestandsindeling van de nalevingsexport. Correspondeert met het systeem waarmee u de gegevens wilt importeren.

Momenteel ondersteunde formaten zijn CSV, Actiance XML en Global Relay EML.

Als Global Relay wordt gekozen, worden de volgende opties gepresenteerd:

Globaal Relais-klantenaccount ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Type Global Relay-klantenaccount dat uw organisatie heeft, ` ` A9/Type 9 ` ` ` of ` ` A10/Type 10 ` `. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is' ` KlantType ': "A9/Type 9" ` ` met opties ` ` "A9/Type 9" ` ` en ` ` "A10/Type 10" ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Algemene SMTP-gebruikersnaam (global relay) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De gebruikersnaam voor verificatie bij de Global Relay SMTP-server. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` SmtpUsername ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Global Relay SMTP-wachtwoord ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het wachtwoord dat hoort bij de SMTP-gebruikersnaam van Global Relay. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` SmtpPassword ': "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Globaal-Relais-e-mailadres ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het e-mailadres van uw Global Relay-servermonitors voor inkomende nalevingsexporten. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` "EmailAddress": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Global Relay SMTP-servertimeout ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het aantal seconden dat kan verstrijken voordat de verbinding met de SMTP-server wordt opgegeven. De standaardwaarde is 1800 seconden. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` `' instelling is ` ` ` SMTPServerTimeout ': "1800" ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Voer De Nalevingsexporttaak Nu Uit ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Met deze knop start u onmiddellijk een nalevingsexporttaak. U kunt de status van de taak bewaken in de taaktabel voor nalevingsexport onder deze knop.

Nalevingsmonitoring
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

*Beschikbaar in Enterprise Edition E20 *

Instellingen voor het inschakelen en configureren van Matterbest-nalevingsrapporten.

Compliancerapportage (^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Nalevingsrapportage is ingeschakeld in Matterbest.

** False**: Nalevingsrapportage is uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` inschakelen ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Adresboeklijst ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De directory waarin nalevingsrapporten worden geschreven. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` "Directory": "./data/" ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Dagelijks rapport inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Matterbest genereert een dagelijks nalevingsrapport.

** False**: Dagelijkse rapporten worden niet gegenereerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` 'EnableDaily': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Aangepaste servicevoorwaarden (Beta)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Vragen

Aangepaste servicevoorwaarden
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

*Beschikbaar in Enterprise Edition E20 *

Aangepaste servicevoorwaarden inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ Opmerking:

  Deze pagina kan alleen worden gewijzigd met behulp van de gebruikersinterface van de systeemconsole.

** True**: Wanneer ` ` true ` ` ` ` zijn, moeten nieuwe gebruikers de Servicevoorwaarden accepteren voordat ze toegang krijgen tot alle Mattermost teams op desktop, web of mobiel. Bestaande gebruikers moeten deze accepteren na aanmelding of een pagina vernieuwen. Als u de link voor de servicevoorwaarden wilt bijwerken die wordt weergegeven in het maken van accounts en aanmeldingspagina's, gaat u naar ** System Console > Legal and Support > Terms of Service Link * *.

** False**: Tijdens het maken of aanmelden van accounts kunnen gebruikers de servicevoorwaarden bekijken door de link te openen die is geconfigureerd via ** System Console > Legal and Support > Terms of Service link * *.

Aangepaste Servicevoorwaarden ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Tekst die wordt afgebeeld in uw aangepaste servicevoorwaarden. Ondersteunt Markdown-ingedeelde tekst.

Re-Acceptatieperiode ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het aantal dagen voordat de servicevoorwaarden worden geaccepteerd, en de voorwaarden moeten opnieuw worden geaccepteerd.

De standaardwaarde is 365 dagen. 0 geeft aan dat de termen niet vervallen.

Experimenteel
-------------

Er zijn een aantal instellingen die worden beschouwd als "experimenteel" dat kan worden geconfigureerd vanuit de systeemconsole. Deze kunnen in een toekomstige release worden vervangen of verwijderd.

Functies
~ ~ ~ nopen ~ ~

AD/LDAP-instellingen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

AD/LDAP Login-knop Kleur ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geef de kleur van de AD/LDAP-aanmeldingsknop op voor witte labeling. Gebruik een hex code met een #-teken voor de code. Deze instelling is alleen van toepassing op de mobiele apps. + -------------------------------------------------------------------------------------------------------------------------------
| De instelling '` `config.json `' van deze feature is ` ` LoginButtonColor ":" " ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------------------------------------------------- +

AD/LDAP-Aanmeldingsknop-kaderkleur ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geef de kleur op van de rand van de AD/LDAP-aanmeldknop voor witlabeldoeleinden. Gebruik een hex code met een #-teken voor de code. Deze instelling is alleen van toepassing op de mobiele apps. + -------------------------------------------------------------------------------------------------------------------------------
| De instelling '` `config.json `' van deze feature is ` ` LoginButtonBorderColor ":" " ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------------------------------------------------- +

AD/LDAP Login-teksttekstkleur ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geef de kleur van de aanmeldingsknop voor AD/LDAP op voor witte labeldoeleinden. Gebruik een hex code met een #-teken voor de code. Deze instelling is alleen van toepassing op de mobiele apps. + -------------------------------------------------------------------------------------------------------------------------------
| De instelling '` `config.json `' van deze feature is ` ` LoginButtonTextColor ":" " ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------------------------------------------------- +

(Experimental) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E10 en hoger *

** True**: Gebruikers kunnen hun aanmeldingsmethode wijzigen in een methode die is ingeschakeld op de server, hetzij via Accountinstellingen, hetzij via de API's.

** False**: Gebruikers kunnen hun aanmeldingsmethode niet wijzigen, ongeacht welke verificatieopties zijn ingeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ExperimentalEnableAuthenticationTransfer ": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Autoclose Direct Messages in Sidebar (Experimental) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Standaard worden berichten voor directe berichten zonder activiteit gedurende 7 dagen verborgen in de flankbalk. Gebruikers kunnen dit uitschakelen in ** Accountinstellingen > Flankbalk * *.

** False**: Conversaties blijven in de flankbalk totdat ze handmatig worden gesloten. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ' CloseUnusedDirectMessages ": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Metagegevens-timeout: ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Hiermee voegt u een configureerbare timeout toe voor opdrachten voor het retourneren van de metagegevens van de koppeling. Als de metagegevens niet worden geretourneerd voordat deze timeout is verstreken, wordt het bericht verzonden zonder dat er metagegevens nodig zijn. Deze timeout heeft betrekking op de storingsgevallen van gebroken URL's en foutecontenttypen op trage netwerkverbindingen. + --------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` LinkMetadataTimeoutMilliseconds ": 5000 ` ` met numerieke invoer. |
+ --------------------------------------------------------------------------------------------------------------------------------- +

E-mailinstellingen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Buffergrootte E-mailbeslag ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geef het maximumaantal meldingen op dat in één e-mail is uitgevoerd. + -------------------------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` EmailBatchingBufferSize ": 256 ` ` met numerieke invoer. |
+ -------------------------------------------------------------------------------------------------------------------------- +

Interval Voor E-mailen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geef de maximumfrequentie op, in seconden, die door de batching-taak wordt gecontroleerd voor nieuwe meldingen. Langere slagintervallen verhogen de prestaties. + ----------------------------------------------------------------------------------------------------------------------- +
| De '`config.json `' instelling van deze feature is ` ` EmailBatchingInterval ": 30 ` ` met numerieke invoer. |
+ ----------------------------------------------------------------------------------------------------------------------- +

Knop Voor Aanmelding Bij E-mail ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geef de kleur op van de aanmeldingsknop voor het e-mailprogramma voor witlabeldoeleinden. Gebruik een hex code met een #-teken voor de code. Deze instelling is alleen van toepassing op de mobiele apps. + -------------------------------------------------------------------------------------------------------------------------------
| De instelling '` `config.json `' van deze feature is ` ` LoginButtonColor ":" " ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------------------------------------------------- +

Kaderkleur voor aanmeldingsknop voor e-mail ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geef de kleur van de rand van de e-mailaanmeldknop op voor witte labeling. Gebruik een hex code met een #-teken voor de code. Deze instelling is alleen van toepassing op de mobiele apps. + -------------------------------------------------------------------------------------------------------------------------------
| De instelling '` `config.json `' van deze feature is ` ` LoginButtonBorderColor ":" " ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------------------------------------------------- +

Tekstkleur voor aanmeldingspoging e-mail ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geef de kleur van de tekst voor de e-mailaanmeldknop op voor witte labeldoeleinden. Gebruik een hex code met een #-teken voor de code. Deze instelling is alleen van toepassing op de mobiele apps. + -------------------------------------------------------------------------------------------------------------------------------
| De instelling '` `config.json `' van deze feature is ` ` LoginButtonTextColor ":" " ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------------------------------------------------- +

Deactivering van account inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: De mogelijkheid voor gebruikers om hun eigen account uit te schakelen van ** Accountinstellingen > Geavanceerd * *. Als een gebruiker zijn eigen account deactiveert, krijgen ze een e-mailbericht waarin wordt bevestigd dat ze zijn gedeactiveerd.

** False**: De mogelijkheid voor gebruikers om hun eigen account te deactiveren is uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is ` `' EnableUserDeactivation ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Automatische antwoorden (experimenteel) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Gebruikers kunnen automatische antwoorden inschakelen in ** Accountinstellingen > Meldingen * *. Gebruikers stellen een aangepast bericht in dat automatisch wordt verzonden als reactie op directe berichten.

** False**: Hiermee schakelt u de functie Automatische directe berichten onderdrukken uit en verbergt u deze uit accountinstellingen. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| Deze functie ' ` `config.json ` ` instelling is ` ` "ExperimentalEnableAutomaticReplies": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +

Enable Channel-berichten Van Het Kanaal ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze instelling bepaalt of ` ` channel_bekeken WebSocket ` ` ` events worden verzonden, die ongelezen meldingen synchroniseren tussen clients en apparaten. Het uitschakelen van de instelling in grotere implementaties kan de serverprestaties verbeteren. + ------------------------------------------------------------------------------------------------------------------------ +
| De '`config.json ` ` instelling van deze feature is ` `' EnableChannelViewedMessages: true ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ------------------------------------------------------------------------------------------------------------------------ +

Activeer client-side-certificering ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

** True**: Hiermee kunt u de clientcertificering voor uw Mattermeeste server inschakelen. Zie ` de documentatie <https://docs.mattermost.com/deployment/certificate-based-authentication.html> ` __ om meer te weten te komen.

** False**: certificering van clientzijde is uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ClientSideCertEnable ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------
--------------------- +

Aanmeldingspoging op client-side: ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

Wordt gebruikt in combinatie met de instelling ` ` ClientSideCertEnable ` `.

** Primary**: Nadat het clientcertificaat is geverifieerd, wordt de e-mail van de gebruiker opgehaald uit het certificaat en wordt gebruikt om zonder wachtwoord aan te melden.

** Secondary**: Nadat het client-side certificaat is geverifieerd, wordt de e-mail van de gebruiker opgehaald uit het certificaat en vergeleken met de door de gebruiker geleverd. Als deze overeenkomen, meldt de gebruiker zich aan met gewone legitimatiegegevens voor e-mail en wachtwoord. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` ` ClientSideCertCheck': 'secundair' ` ` met opties ` ` ` primaire '` ` en ` `' secundair ' ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Standaard kanaal verlaten/deelnemen systeemberichten ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze instelling bepaalt of teamverlaten/join-systeemberichten worden gepost in het standaard ` ` town-square ` ` kanaal.

** True**: Hiermee kunt u systeemberichten verlaten/samenvoegen in het standaard ` ` town-square ` ` kanaal.

** False**: Hiermee worden de berichten van het verlof/join van het standaardkanaal ` ` town-square ` ' uitgeschakeld. Deze systeemberichten worden ook niet aan de database toegevoegd. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ExperimentalEnableDefaultChannelLeaveJoinMessages ": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Verhard-modus (experimenteel) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Zorgt voor een gehard modus voor Matterbest waardoor de gebruiker in het belang van de beveiliging afwegingen maakt.

** False**: Verharde modus wordt uitgeschakeld.

Wijzigingen die worden aangebracht wanneer de verharde modus is ingeschakeld:

    -Mislukte aanmelding retourneert een generiek foutbericht in plaats van een specifiek bericht voor gebruikersnaam en wachtwoord.
    -Als ` multi-factor authenticatie (MFA) <https://docs.mattermost.com/deployment/auth.html> ` __ is ingeschakeld, de route om te controleren of een gebruiker heeft MFA ingeschakeld altijd terug waar. Hierdoor verschijnt het invoerscherm van MFA, zelfs als de gebruiker geen MFA-functie heeft ingeschakeld. De gebruiker kan elke waarde invoeren om het scherm door te geven. Houd er rekening mee dat de gehard modus geen invloed heeft op de gebruikerservaring wanneer de MFA wordt afgedwongen.
    -Password reset geeft de gebruiker niet op de hoogte dat ze hun SSO-account niet kunnen resetten via Matterbest en in plaats daarvan beweert dat ze het wachtwoord reset e-mail hebben verzonden.
    -Matterbest sanitizes alle 500 fouten voordat ze terug naar de client. Gebruik de bijgeleverde ` ` request_id ` ` om de gebruiker te vergelijken met fouten in de serverlogboeken. + --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` ` instelling van deze feature is' ` ExperimentalEnableHardenedMode ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Synchronisatie van AD/LDAP-groepen inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

** True**: Hiermee schakelt u AD/LDAP Group Sync configureerbaar onder ** Toegangsbeheer > Groepen * *.

** False**: schakelt AD/LDAP Group Sync uit en verwijdert ** Access Controls > Groepen * * van de systeemconsole.

Zie voor meer informatie over AD/LDAP Group Sync de 'AD/LDAP Group Sync-documentatie <https://docs.mattermost.com/deployment/ldap-group-sync.html>' _. + --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' van deze feature is '` ExperimentalLdapGroupSync': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Previewfuncties inschakelen (Experimental) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Previewfuncties kunnen worden ingeschakeld vanuit ** Accountinstellingen > Geavanceerd > Previewfuncties bekijken * *.

** False**: Voorzien en verbergen van previewfuncties van ** Account Settings > Advanced > Preview pre-release features * *. + --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` `' EnablePreviewFeatures ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Themaselectie inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E10 en hoger *

** True**: Met de tab * * Display > Thema * * in Accountinstellingen kunnen gebruikers hun thema selecteren.

** False**: Gebruikers kunnen geen ander thema selecteren. Het tabblad * * Weergeven > Thema * * is verborgen in Accountinstellingen. + ----------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` `' EnableThemeSelection ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ----------------------------------------------------------------------------------------------------------------- +

Aangepaste thema's toestaan ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E10 en hoger *

** True**: Hiermee schakelt u het gedeelte * * Weergeven > Thema > Aangepast thema * * in in Accountinstellingen.

** False**: Gebruikers kunnen geen aangepast thema gebruiken. De sectie * * Weergave > Thema > Aangepast thema * * is verborgen in Accountinstellingen. + -------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json `' van deze feature is ` ` AllowCustomThemes ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ -------------------------------------------------------------------------------------------------------------- +

Standaardthema ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E10 en hoger *

Stel een standaardthema in dat van toepassing is op alle nieuwe gebruikers op het systeem. + -------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ' "DefaultTheme": "default" ` met opties ` ` ` standaard "` `, ` `" organisatie "` `, ` ` ` mattermostDark" ` ` en ` ` "windows10" ` `. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Zelfstudieprogramma (experimenteel) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Gebruikers worden met een zelfstudieprogramma gevraagd wanneer ze Matterbest voor het eerst openen na het aanmaken van het account.

** False**: Het zelfstudieprogramma is uitgeschakeld. Gebruikers worden geplaatst op het stadsplein wanneer ze Matterbest voor de eerste keer openen na het maken van accounts. + -------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` ` EnableTutorial': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ -------------------------------------------------------------------------------------------------------------------------------------------- +

Gebruiker Typen Berichten Inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze instelling bepaalt of "gebruiker typt ..." berichten worden weergegeven onder het berichtvenster. Het uitschakelen van de instelling in grotere implementaties kan de serverprestaties verbeteren. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is ` `' EnableUserTypingMessages: true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

De Tijd Tussen De Updates Van De Gebruiker (User Typing Timeout) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze instelling bepaalt hoe vaak "gebruiker typt ..." berichten worden bijgewerkt, gemeten in milliseconden. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` TimeBetweenUserTypingUpdatesMilliseconds ": 5000 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

X de kanalen verlaten van de linkerflankbalk (Experimental) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Gebruikers kunnen Public and Private Channels verlaten door te klikken op de "x" naast de kanaalnaam.

** False**: Gebruikers moeten de optie ** Leave Channel * * gebruiken in het kanaalmenu om kanalen te verlaten. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableXToLeaveChannelsFromLHS ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Het primaire team (Experimental) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het primaire team waarvan gebruikers op de server lid zijn. Als een primair team is ingesteld, zijn de opties voor het samenvoegen van andere teams of het verlaten van het primaire team uitgeschakeld.

Als de teamURL van het primaire team https://example.mattermost.com/myteam/, is, stelt u de waarde in op ` ` myteam ` ` in ` `config.json ` ` `. + ----------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "ExperimentalPrimaryTeam": "" ` ` met reeksinvoer. |
+ ----------------------------------------------------------------------------------------------------------------- +

SAML-instellingen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

SAML Login-knop Kleur ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geef de kleur op van de SAML-aanmeldknop voor witlabeldoeleinden. Gebruik een hex code met een #-teken voor de code. Deze instelling is alleen van toepassing op de mobiele apps. + -------------------------------------------------------------------------------------------------------------------------------
| De instelling '` `config.json `' van deze feature is ` ` LoginButtonColor ":" " ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------------------------------------------------- +

SAML-Aanmeldingsknopkaderkleur ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geef de kleur op van de rand van de SAML-aanmeldknop voor witlabeldoeleinden. Gebruik een hex code met een #-teken voor de code. Deze instelling is alleen van toepassing op de mobiele apps. + -------------------------------------------------------------------------------------------------------------------------------
| De instelling '` `config.json `' van deze feature is ` ` LoginButtonBorderColor ":" " ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------------------------------------------------- +

SAML Login-teksttekstkleur ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geef de kleur van de SAML-aanmeldknoptekst op voor white labeling-doeleinden. Gebruik een hex code met een #-teken voor de code. Deze instelling is alleen van toepassing op de mobiele apps. + -------------------------------------------------------------------------------------------------------------------------------
| De instelling '` `config.json `' van deze feature is ` ` LoginButtonTextColor ":" " ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------------------------------------------------- +

Experimentele zijbalk (experimenteel) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** Disabled**: Gebruikers hebben geen toegang tot de functie voor de experimentele kanaalflankbalk.

** Ingeschakeld (Standaard op) * *: Hiermee kunnen de experimentele flankbalkfeatures voor alle gebruikers op deze server worden ingeschakeld. Gebruikers kunnen de functies uitschakelen in ** Account Instellingen > Sidebar > Experimental Sidebar Features * *. Kenmerken omvatten aangepaste samenvouwbare kanaalcategorieën, slepen en neerzetten om kanalen te reorganiseren, en ongelezen filtering. ` Leer meer of geef ons feedback <https://about.mattermost.com/default-sidebar/> ` _.

** Ingeschakeld (Standaard uitgeschakeld) * *: Gebruikers moeten de experimentele flankbalkfuncties inschakelen in Accountinstellingen. ` Meer informatie of geef ons feedback <https://about.mattermost.com/default-sidebar/> ` _. + ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is' ` ExperimentalChannelSidebarOrganization ': off ` ` met opties ` ` uit ` `, ` ` default_on ` ` en ` ` default_off ` `. |
+ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Zijbalk Organisatie (Experimental) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Schakelopties voor kanalen in de zijbalk van het kanaal in ** Accountinstellingen > Flankbalk > Groeperen en sorteren van kanalen * * inclusief opties voor het groeperen van ongelezen kanalen, het sorteren van kanalen door de meest recente posting en het combineren van alle kanaaltypen in een enkele lijst.

** False**: De instellingen van de kanaalflankbalk worden afgebeeld in ** Accountinstellingen > Flankbalk > Kanaalgroep en sorteren * *. + --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ExperimentalChannelOrganization ": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Tijdzone ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Selecteer de tijdzone die wordt gebruikt voor tijdsaanduidingen in de gebruikersinterface en e-mailmeldingen.

** True**: De instelling ** Timezone** is zichtbaar in de accountinstellingen en een tijdzone wordt automatisch toegewezen in de volgende actieve sessie.

** False**: De instelling ** Timezone** is verborgen in de accountinstellingen. + ------------------------------------------------------------------------------------------------------------------ +
| Deze functie '` `config.json ` ` instelling is ` ` ExperimentalTimezone': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ------------------------------------------------------------------------------------------------------------------ +

Town Square is verborgen in de linkerzijbalk (Experimental) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E10 en hoger *

** True**: Hides Town Square in de linker zijbalk als er geen ongelezen berichten in het kanaal.

** False**: Stadsplein is altijd zichtbaar in de flankbalk aan de linkerkant, zelfs als alle berichten zijn gelezen. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| Deze functie ' ` `config.json ` ` instelling is ` ` "ExperimentalHideTownSquareinLHS": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +

Town Square is Read-Only (Experimental) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E10 en hoger *

** True**: Alleen systeembeheerders kunnen plaatsen op het stadsplein. Andere leden zijn niet in staat om te posten, antwoorden, uploaden van bestanden, emoji reageren, of speld berichten naar het stadsplein, noch zijn zij in staat om de kanaalnaam, header, of doel te wijzigen.

** False**: Iedereen kan posten op het stadsplein. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| De instelling ``config.json van deze feature is ` ` ExperimentalTownSquareIsReadOnly ": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +

Kanaalnaam in e-mailmeldingen (Experimental) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: De naam van het kanaal en het team wordt weergegeven in de onderwerpelijnen voor e-mailberichten. Nuttig voor servers die slechts één team gebruiken.

** False**: Alleen teamnaam wordt weergegeven in de onderwerpregel van de e-mailmelding. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is ` `' "UseChannelInEmailNotifications": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Gebruiker Status afwezig Timeout ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze instelling bepaalt het aantal seconden waarna de statusindicator van de gebruiker verandert in "Away", wanneer ze niet meer Matterbest zijn. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` ` UserStatusAwayTimeout': 300 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Instellingen kunnen alleen worden geconfigureerd in ` `config.json ` ` `
------------------------------------------------------

Er zijn een aantal instellingen die aanpasbaar zijn in ` `config.json ` ` die niet beschikbaar zijn in de systeemconsole en die moeten worden bijgewerkt vanuit het bestand zelf.

Service-instellingen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Automatisch De Threads Volgen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze instelling is toegevoegd als vereiste voor het ondersteunen van ` Gestorte Reply Threads <https: //docs.google.com/presentation/d/1QSrPws3N8AMSjVyOKp15FKT7O0fGMSx8YidjSDS4Wng/edit#slide= id.g2f0aecc189_0_245 > ` _ (vrijgeven in bèta in Q1 2021) en kan van invloed zijn op de serverprestaties. Aanbevolen wordt om onze ` documentatie over hardwarevereisten <https: //docs.mattermost.com/install/requirements.html#hardware-requirements> ` _ te bekijken om ervoor te zorgen dat uw servers op de juiste manier worden geschaald voor de grootte van uw gebruikersbasis.

** True**: Threads een gebruiker start, neemt deel aan of wordt vermeld in zijn automatisch gevolgd. Er wordt een nieuwe ` ` Threads ` ` tabel toegevoegd in de database die threads en threaddeelnemers bijhoudt, en een ` ` ThreadMembership ` ` tabelsporen volgden threads voor elke gebruiker en de lees-of ongelezen status van elke gevolgde thread.   

** False**: Threads worden niet automatisch gevolgd en Ingevouwen antwoordthreads kunnen niet worden ingeschakeld (vrijgeven in bèta in Q1 2021). + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` ` instelling van deze feature is ` ` ThreadAutoFollow': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +


Gegevenprefetch ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Berichten in alle ongelezen kanalen worden van de server vooraf geladen wanneer de client opnieuw verbinding maakt met het netwerk om de laadtijd te elimineren wanneer gebruikers overschakelen op ongelezen kanalen.

** False**: Berichten worden op verzoek opgehaald van de server wanneer gebruikers wisselen van kanaal. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ExperimentalDataPrefetch ": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

WebSocket URL ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Met deze instelling kan de server clients instrueren waar ze WebSockets moeten proberen aan te sluiten. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` "WebsocketURL": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Licentiebestandslocatie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Pad en bestandsnaam van het licentiebestand op schijf. Bij het opstarten, als Matterbest geen geldige licentie kan vinden in de database van een vorige upload, ziet het er hier uit. Het kan een absoluut pad zijn of een pad ten opzichte van de ` ` mattermeest ` ` directory. + --------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` ` LicenseFileLocation ":" " ` ` met reeksinvoer. |
+ --------------------------------------------------------------------------------------------- +

TLS-minimumversie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De minimale TLS-versie die wordt gebruikt door de Mattertiste server. TLS v1.2 is standaard gegeven ineffecten voor TLS 1.0 en 1.1.

Deze instelling wordt alleen van kracht als u de ingebouwde server-binary rechtstreeks gebruikt en geen omgekeerde proxy-laag gebruikt, zoals NGINX. + -------------------------------------------------------------------------------------
| De instelling '` `config.json `' van deze feature is '`' "TLSMinVer": "1.2" ` ` met reeksinvoer. |
+ -------------------------------------------------------------------------------------

Betrouwbare proxy-IP-header ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Opgegeven kopteksten die één voor één worden gecontroleerd voor IP-adressen (volgorde is belangrijk). Alle andere headers worden genegeerd.

Vanaf v5.12 hebben nieuwe configs deze set standaard ingesteld op ` ` [] ` `, wat betekent dat er geen header wordt vertrouwd. De configuratie die is gemaakt vóór v5.12 zonder dat dit configuratiegegeven is ingesteld, wordt ingesteld op ` ` [ "X-Doorgezonden-For", "X-Real-Ip"] ` ` on upgrade om de compatibiliteit met achterwaartse kracht te behouden.

We raden aan om de standaardinstelling te houden wanneer Matterit draait zonder een proxy, om te voorkomen dat de client de headers verzendt en het tarief beperken en/of het auditlogboek. Voor omgevingen die gebruikmaken van een omgekeerde proxy bestaat dit probleem niet, mits de headers worden ingesteld door de omgekeerde proxy. In die omgevingen wordt alleen expliciet de koptekst die is ingesteld door de omgekeerde proxy en geen aanvullende waarden. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' van deze feature is '` TrustedProxyIPHeader': [] ` ` met tekenreeksinvoer bestaande uit headernamen, zoals ` ` [ "X-Doorgezonden-For", "X-Real-Ip"] ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

-Strikte vervoerszekerheid (HST) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Voegt de Strict Transport Security-header (HSTS) toe aan alle antwoorden, waardoor de browser wordt gedwongen om alle resources te vragen via HTTPS. Lees meer " hier <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security> ` __.

** False**: Geen beperkingen op TLS transport. De HSTS-header (strict Transport Security) wordt niet toegevoegd aan de antwoorden. + -------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` TLSStrictTransport ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------- +

Veilige TLS Transport Expiry ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De tijd in seconden dat de browser onthoudt dat een site alleen toegankelijk is via HTTPS. Na deze periode kan een site worden geopend met behulp van HTTP, tenzij ` ` TLSStrictTransport ` ` is ingesteld op ` ` true ` `. Standaard is dit twee jaar. Lees meer "hier <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security>" __. + ------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is' ` 'TLSStrictTransportMaxAge': 63072000 ` ` met numerieke invoer. |
+ -----------------------------------------------------------------------------------------------------------------------

TLS-codering overschrijven ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Stel TLS-ciphers overschrijd om te voldoen aan de eisen van legacy clients die geen ondersteuning bieden aan moderne ciphers, of om de soorten geaccepteerde ciphers te beperken.

Als er geen is opgegeven, neemt de Mattermeeste server een set van momenteel beschouwd beveiligde coderingen aan en maakt het mogelijk dat er overschrijfbewerkingen worden uitgevoerd in de randcase. Zie de variabele ` ` ServerTLSSupportedCiphers ` ` in `/model/config.go <https://github.com/mattermost/mattermost-server/blob/master/model/config.go> ` __ voor de lijst van beveiligde coderingen.

Deze instelling wordt alleen van kracht als u de ingebouwde server-binary rechtstreeks gebruikt en geen omgekeerde proxy-laag gebruikt, zoals NGINX. + ------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is' ` 'TLSStrictTransportMaxAge': 63072000 ` ` met numerieke invoer. |
+ -----------------------------------------------------------------------------------------------------------------------

Go Routine Gezondheid Drempel ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Stel een drempelwaarde in op het aantal goroutines wanneer het Mattermeeste systeem wordt beschouwd als een gezonde staat. Wanneer de goroutines deze limiet overschrijden, wordt er een waarschuwing geretourneerd in de serverlogboeken.

Als u de controle voor de drempel wilt uitschakelen, stelt u deze waarde in op ` ` -1 ` `. + ---------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is' ` ' "GoroutineHealthThreshold": -1 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------- +

Cookies toestaan voor subdomeinen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Hiermee kunnen cookies voor subdomeinen worden gebruikt door het instellen van de domeinparameter op Mattermeeste cookies.

** False**: Cookies niet toegestaan voor subdomeinen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` 'AllowCookiesForSubdomains': true ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Clusterlogboektimeout ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze instelling definieert de frequentie van de logboekregistratie van de clusteropdrachttijd voor :doc: ` ../deployment/metrics `, gemeten in milliseconden. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is' ` ' ClusterLogTimeoutMilliseconds ": 2000 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Alleen-lezen Config ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Wijzigingen in instellingen in de systeemconsole worden genegeerd.

** False**: Wijzigingen in instellingen in de systeemconsole worden weggeschreven naar ` `config.json ` ` `. + ----------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` ReadOnlyConfig ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ -----------------------------------------------------------------------------------------------------------------------

Het zoeken naar Posten ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als deze instelling is ingeschakeld, kunnen gebruikers berichten doorzoeken. Het uitschakelen van de zoekfunctie kan leiden tot een prestatieverhoging, maar gebruikers krijgen een foutbericht wanneer ze proberen het zoekvak te gebruiken. + ------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` ` instelling van deze feature is ` ` EnablePostSearch': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ -----------------------------------------------------------------------------------------------------------------------

De statusupdates voor de gebruiker inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ Wanneer statusupdates uitgeschakeld zijn, verschijnen gebruikers online alleen voor korte perioden bij het plaatsen van een bericht, en alleen voor leden van het kanaal waarin het bericht is geplaatst. + --------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` 'EnableUserStatuses': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ --------------------------------------------------------------------------------------------------------------- +

Segmentschrijftoets ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in maart 16, 2017 release *

Voor implementaties die aanvullende tracering van systeemgedrag zoeken met behulp van Segment.com, kunt u een Segment ` ` WRITE_KEY ` ` invoeren met behulp van dit veld. Deze waarde werkt als een trackingcode en wordt gebruikt in client-side JavaScript en stuurt events naar Segment.com toe aan het account dat u hebt gebruikt voor het genereren van de ` ` WRITE_KEY ` `. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` ' "SegmentDeveloperKey": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

WebSocket Secure Port ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Met deze instelling wordt de poort gedefinieerd waarop de beveiligde WebSocket luistert met het ` ` wss ` ` protocol. De standaardwaarde is ` ` 443 ` `. Wanneer de client probeert een WebSocket-verbinding te maken, controleert het eerst of de pagina met HTTPS wordt geladen. Als dit het geval is, wordt de beveiligde WebSocket-verbinding gebruikt. Als dit niet het geval is, wordt de niet-beveiligde WebSocket-verbinding gebruikt. HET IS STERK AANBEVOLEN PRODUCTIE-IMPLEMENTATIES ALLEEN WERKEN ONDER HTTPS EN WSS.

Wijzigingen in deze instelling vereisen een herstart van de server voordat deze wordt uitgevoerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is' ` 'WebsocketSecurePort': 443 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

WebSocket-poort ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

(Optioneel) Met deze instelling wordt de poort gedefinieerd waarop de ongedekte WebSocket luistert met het ` ` ws ` ` protocol. De standaardwaarde is ` ` 80 ` `. Wanneer de client probeert een WebSocket-verbinding te maken, controleert het eerst of de pagina met HTTPS wordt geladen. Als dit het geval is, wordt de beveiligde WebSocket-verbinding gebruikt. Als dit niet het geval is, wordt de niet-beveiligde WebSocket-verbinding gebruikt. HET IS STERK AANBEVOLEN PRODUCTIE-IMPLEMENTATIES ALLEEN WERKEN ONDER HTTPS EN WSS.

Wijzigingen in deze instelling vereisen een herstart van de server voordat deze wordt uitgevoerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` ` WebsocketPort': 80 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

API-teamverwijdering inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Het ` ` api/v4/teams/ { teamid } ?permanent=true ` ` API-eindpunt kan door team-en systeembeheerders worden aangeroepen om een team permanent te verwijderen.

** False**: Het API-eindpunt kan niet worden aangeroepen. Merk op dat ` ` api/v4/teams/ { teamid } ` ` nog steeds kan worden gebruikt om een team zacht te verwijderen.

mmctl lokale modus negeert deze instelling en gedraagt zich alsof ` ` EnableAPITeamDeletion ` ` is ingesteld op ` ` true ` ` `. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableAPITeamDeletion ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

API-gebruiker Wissen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Het ` ` api/v4/users/ { userid } ?permanent=true ` ` API-eindpunt kan door System Admins of gebruikers met de juiste machtigingen worden aangeroepen om een gebruiker permanent te wissen.

** False**: Het API-eindpunt kan niet worden aangeroepen. Merk op dat ` ` api/v4/users/ { userid } ` ` nog steeds kan worden gebruikt om een gebruiker te verwijderen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` 'EnableAPIUserDeletion': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

mmctl lokale modus negeert deze instelling en gedraagt zich alsof ` ` EnableAPIUserDeletion ` ` is ingesteld op ` ` true ` `.

API-kanaalverwijdering inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Het ` ` api/v4/channels/ { channelid } ?permanent=true ` ` API-eindpunt kan door System Admins of gebruikers met de juiste machtigingen worden aangeroepen om een kanaal permanent te verwijderen.

** False**: Het API-eindpunt kan niet worden aangeroepen. Opmerking: ` ` api/v4/channels/ { channelid } ` ` kan nog steeds worden gebruikt om een kanaal te verwijderen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableAPIChannelDeletion ': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

mmctl lokale modus negeert deze instelling en gedraagt zich alsof ` ` EnableAPIChannelDeletion ` ` is ingesteld op ` ` true ` `.

OpenTracing (^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Een Jaeger-client wordt geïnstantieerd en wordt gebruikt om elke HTTP-aanvraag te traceren als deze door App en Store-lagen gaat. Context wordt toegevoegd aan App en Store en wordt doorgegeven aan de laagketen om OpenTracing 'spans' te maken.

Om lekken van gevoelige informatie te voorkomen, worden standaard geen methodeparameters gerapporteerd voor OpenTracing. Alleen de naam van de methode wordt gerapporteerd.

** False**: OpenTracering is niet ingeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` `-instelling van deze feature is ` `' EnableOpenTracing ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

SQL-instellingen
~ ~ ~ ~ nopen ~ ~

Lezen van replica's ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E10 en hoger *

De verbindingsreeksen voor de gelezen replica-databases. Elke tekenreeks moet in dezelfde vorm zijn als die voor de instelling 'Gegevensbron' _.

Wijzigingen in deze instelling vereisen een herstart van de server voordat ze worden uitgevoerd. + --------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` ' DataSourceReplicas ": [] ` ` met tekenreeksinvoer bestaande uit reeksen databaseverbindingen. |
+ --------------------------------------------------------------------------------------------------------------------------------------------- +

Zoeken naar replica's ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E10 en hoger *

De verbindingsreeksen voor de zoekreplica-databases. Een zoekreplica is vergelijkbaar met een leesreplica, maar wordt alleen gebruikt voor het afhandelen van zoekopdrachten. Elke tekenreeks moet in dezelfde vorm zijn als die voor de instelling 'Gegevensbron' _.

Wijzigingen in deze instelling vereisen een herstart van de server voordat deze wordt uitgevoerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------
| De instelling '` `config.json `' van deze feature is ` ` ' DataSourceSearchReplicas ": [] ` ` met tekenreeksinvoer bestaande uit reeksen databaseverbindingen. |
+ --------------------------------------------------------------------------------------------------------------------------------------------------- +

Bestandsinstellingen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Oorspronkelijk lettertype ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Lettertype gebruikt in automatisch gegenereerde profielfoto's met gekleurde achtergronden. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json' ' van deze feature is ` ` InitialFont ":" luximbi.ttf " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Amazon S3 Bucket eindpunt ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Stel een eindpunt-URL in voor Amazon S3 buckets.

*Verwijderd in 16 november 2016 release * + ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is' ` ' "" AmazonS3BucketEndpoint ":" " ` ` met reeksinvoer. |
+ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Amazon S3 Locatie voorwaarde ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: S3 regio is locatie beperkt.

** False**: S3 regio is geen locatie beperkt.

*Verwijderd in 16 november 2016 release * + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` AmazonS3LocationConstraint ": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Amazon S3 Lowercase Bucket ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: S3 emmernamen zijn volledig kleine letters.

** False**: S3-emmernamen kunnen hoofdletters en kleine letters bevatten.

*Verwijderd in november 16, 2016 release *

+ --------------------------------------------------------------------------------------------------------------------------------------------------------
-------------- +
| De instelling '`config.json `' van deze feature is '` AmazonS3LowercaseBucket': false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Amazon S3 Handtekening V2 ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Standaard gebruikt Matterbest Signature V4 om API-aanroepen te ondertekenen naar AWS, maar onder bepaalde omstandigheden is V2 vereist. Zie https://docs.aws.amazon.com/general/latest/gr/signature-version-2.html voor meer informatie over het gebruik van V2.

** True**: Handtekeningproces Versie 2 Gebruiken.

** False**: Handtekeningproces voor handtekeningversie 4. + ------------------------------------------------------------------------------------------------------------ +
| De instelling ``config.json van deze feature is ` ` AmazonS3SignV2 ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ------------------------------------------------------------------------------------------------------------ +

Amazon S3 Pad ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Hiermee kunt u dezelfde S3-bucket gebruiken voor meerdere implementaties. + ------------------------------------------------------------------------------------------------------------ +
| De instelling '`config.json' 'van deze feature is' ` ' "AmazonS3PathPrefix:" " ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------------------------------ +


GitLab-instellingen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Bereik ^ ^ ^ ^ ^ ^

Standaardinstelling voor OAuth om het bereik te bepalen van de informatie die wordt gedeeld met de OAuth-client. Momenteel niet ondersteund door GitLab OAuth. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is ` `' Scope ':' " ` ` met tekenreeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Google-instellingen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Bereik ^ ^ ^ ^ ^ ^

Standaardinstelling voor OAuth om het bereik te bepalen van de informatie die wordt gedeeld met de OAuth-client. Aanbevolen instelling is ` ` profile email ` `. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` ` instelling is ` ` "Scope": "profile email" ` ` met string input. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Office 365-instellingen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Bereik ^ ^ ^ ^ ^ ^

Standaardinstelling voor OAuth om het bereik te bepalen van de informatie die wordt gedeeld met de OAuth-client. Aanbevolen instelling is ` `User.Read ` `. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is ` `' Scope ': "User.Read" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Clusterinstellingen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Maximumaantal niet-actieve verbindingen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het maximumaantal niet-actieve verbindingen dat open is gehouden van de ene server naar alle andere servers in de cluster. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` ` MaxIdleConns ': 100 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Maximumaantal niet-actieve verbindingen per host ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het maximumaantal niet-actieve verbindingen dat open is gehouden van de ene server naar een andere server in de cluster. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` MaxIdleConnsPerHost ': 128 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Timeout voor niet-actieve verbinding (in milliseconden) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het aantal milliseconden voor het verlaten van een niet-actieve verbinding tussen servers in de cluster. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` IdleConnTimeoutMilliseconds ": 90000 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Netwerkinterface ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Een IP-adres dat wordt gebruikt om het apparaat te identificeren dat automatische IP-detectie doet in High Availability-clusters. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json `'-instelling van deze feature is '`' NetworkInterface ":" " ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Bindadres ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Een IP-adres dat wordt gebruikt om het clusterverkeer te binden aan een specifiek netwerkapparaat. Deze instelling wordt voornamelijk gebruikt voor servers met meerdere netwerkapparaten of een ander Bind-adres en een Advertentie-adres zoals in implementaties met NAT (Network Address Translation). + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is' ` ' "BindAddress": "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Reclameadres ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het IP-adres dat wordt gebruikt om toegang te krijgen tot de server van andere knooppunten. Deze instellingen worden primair gebruikt als clusterknooppunten zich niet in hetzelfde netwerk bevinden en NAT (Network Address Translation) hebben. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is ` ` AdvertiseAddress': "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Instellingen gebruikscijfers
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Blokprofielsnelheid ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Waarde voor het controleren van de ' fractie van de blokkeringsgebeurtenissen van goroutine die zijn gemeld in het blokkeringsprofiel <https: //golang.org/pkg/runtime/#SetBlockProfileRate> ` __.

De profileringsregel heeft als doel om een gemiddelde van één blokkerende gebeurtenis per snelheid van nanoseconden te bemoneren.

Als u elke blokkeringsevent in het profiel wilt opnemen, stelt u de snelheid in op ` ` 1 ` `. Als u de profilering volledig wilt uitschakelen, stelt u de waarde in op ` ` 0 ` `.

Wijzigingen in deze instelling vereisen een herstart van de server voordat deze wordt uitgevoerd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "BlockProfileRate": 0 ` ` met opties ` ` 0 ` ` en ` ` 1 ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Experimentele instellingen alleen in ` `config.json ` ` `
-------------------------------------------------------

Auditinstellingen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Met de audit-instellingen worden auditrecords uitgevoerd naar syslog (lokale server of server op afstand via TLS) en/of naar een lokaal bestand. Beide zijn standaard uitgeschakeld. Ze kunnen tegelijkertijd worden ingeschakeld.

Syslog-configuratieopties ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Schakel deze instelling in om auditrecords te schrijven naar een lokale of niet-lokale syslog, waarbij u de IP-, poort-, door de gebruiker gegenereerde velden en certificaatinstellingen opgeeft.

** True**: Wanneer ` ` true ` ` ` syslog uitvoer is ingeschakeld.

** False**: Syslog-uitvoer is uitgeschakeld. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "SysLogEnabled": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Syslog IP ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het IP-adres of het domein van de syslog-server. Gebruik ` ` localhost ` ` voor lokale syslog. + -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` `' instelling is ` ` ` SysLogIP ":" localhost " ` ` met reeksinvoer bestaande uit een IP-adres of domeinnaam. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Syslog-poort ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De poort waarop de syslog-server luistert. De standaardpoort is 6514. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json `'-instelling van deze feature is ` ` SysLogPort ': 6514 ` ` met numerieke invoer die bestaat uit een poortnummer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Syslog-tag ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het veld voor de syslog-metagegevenstag. + -------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' van deze feature is '`' SysLogTag ":" " ` ` met reeksinvoer bestaande uit een door de gebruiker gedefinieerd tag-veld. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Syslog: ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Dit is het pad naar het syslog-servercertificaat voor TLS-verbindingen (` ` .crt ` ` ` of ` ` .pem ` ` `). + --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json' van deze functie is '`' "SysLogCert": "" ` ` met reeksinvoer bestaande uit het pad naar het certificaat. |
+ --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Syslog zit los (^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Met deze instelling bepaalt u of een client de certificaatketen en de hostnaam van de server controleert. Als ` ` true ` ` ` `, TLS accepteert elk certificaat gepresenteerd door de server en elke hostnaam in dat certificaat. In deze modus is TLS gevoelig voor man-in-the-middle-aanvallen.

** Note:** Dit moet alleen worden gebruikt voor testen en niet in een productieomgeving. + --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` SysLogInsecure ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Syslog max wachtrij grootte ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze instelling bepaalt hoeveel auditrecords er op elk moment in de wachtrij/buffer kunnen worden geplaatst wanneer ze naar syslog gaan. De standaardwaarde is 1000 records.

Deze instelling kan standaard worden ingesteld als u geen fouten in het serverlogboek ziet en het aantal dienovereenkomstig moet aanpassen. + --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json' van deze feature is ` ` SysLogMaxQueueSize ': 1000 ` ` met numerieke invoer. |
+ --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Opties voor bestandsconfiguratie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Schakel deze instelling in om auditbestanden lokaal te schrijven, met vermelding van grootte, backupinterval, compressie en maximumleeftijd voor het beheren van bestandsrotatie.

** True**: Wanneer ` ` true ` ` ` bestand uitvoer is ingeschakeld.

** False**: Uitvoer van bestanden is uitgeschakeld. + ------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` FileEnabled ": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Bestandsnaam ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Dit is het pad naar de locatie van het uitvoerbestand. + -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| De instelling ``config.json van deze feature is ` ` "bestandsnaam": "" ` ` met reeksinvoer bestaande uit een door de gebruiker gedefinieerd pad (bijvoorbeeld ` `/var/log/mattermost_audit.log ` `). |
+ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Bestand max grootte MB ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Dit is de maximumgrootte (in megabytes) die het bestand kan laten groeien voordat de rotatie wordt geactiveerd. De standaardinstelling is 100. + --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` FileMaxSizeMB ": 100 ` ` met numerieke invoer. |
+ --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Max. aantal dagen per bestand ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Dit is de maximumleeftijd in dagen waarop een bestand kan worden bereikt voordat de rotatie wordt geactiveerd. De standaardwaarde is 0, die geen limiet aangeeft op de leeftijd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' `config.json ` ` instelling van deze feature is ` ` "FileMaxAgeDays": 0 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Bestand max backups ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Dit is het maximum aantal opgeslagen bestanden; de oudste wordt eerst verwijderd. De standaardwaarde is 0, waarbij geen limiet wordt aangegeven voor het aantal backups. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` ` FileMaxBackups': 0 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Bestandscompressie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Wanneer ` ` true ` ` ` gedraaid bestanden worden gecomprimeerd met ` ` gzip ` ` `. + -------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` ` instelling van deze feature is ` ` FileCompress': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Maximale bestandsgrootte bestand ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze instelling bepaalt hoeveel auditrecords er op elk moment in de wachtrij/buffer kunnen worden geplaatst wanneer ze naar een bestand worden geschreven. De standaardwaarde is 1000 records.

Deze instelling kan standaard worden ingesteld als u geen fouten in het serverlogboek ziet en het aantal dienovereenkomstig moet aanpassen. + -------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` FileMaxQueueSize ": 1000 ` ` met numerieke invoer. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Configuratie geavanceerde logboekregistratie
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

*Beschikbaar in Enterprise Edition E20 *

Uitvoerlogboeken naar meerdere doelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Logboekrecords verzenden naar meerdere doelen:

-Meerdere lokale bestandsdoelen
-Meerdere syslogs
-Meerdere TCP-sockets

Elke combinatie van lokale bestands-, syslog-en TCP-socketdoelen toestaan. 

Bestandsdoel ondersteunt rotatie en compressie op basis van grootte en/of duur. Syslog doel ondersteunt lokale en remote syslog servers, met of zonder TLS transport. TCP-socketdoel kan worden geconfigureerd met een IP-adres of domeinnaam, poort en optioneel TLS-certificaat.

De '``config.json ` ` instelling van deze feature is' `ExperimentalAuditSettings.AdvancedLoggingConfig ` ` die een filespec kan bevatten naar een ander configuratiebestand, een database-DSN of een JSON. De opties worden beschreven in dit txt-bestand: ` Log Settings Options <https://github.com/mattermost/docs/files/5066579/Log.Settings.Options.txt> ` _. Sample config: ` Advanced Logging Options Sample.json.zip <https://github.com/mattermost/docs/files/5066597/Advanced.Logging.Options.Sample.json.zip> ` _.

Service-instellingen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Groep Ongelezen Kanalen (Experimenteel) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in december 16, 2018 release en vervangen door een nieuwe ` ` ExperimentalChannelOrganization ` ` instelling *

** Disabled**: Ongelezen kanalen sectie is uitgeschakeld voor alle gebruikers.

* * Standaard op * *: Hiermee schakelt u standaard de flankbalk voor ongelezen kanalen in. Gebruikers kunnen het uitschakelen in ** Accountinstellingen > Flankbalk * *.

* * Standaard uit * *: Hiermee schakelt u standaard de flankbalk voor ongelezen kanalen uit. Gebruikers kunnen deze inschakelen in ** Accountinstellingen > Flankbalk * *. + -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is' ` ExperimentalGroupUnreadChannels ':' disabled '` ` with options ` ` ` disabled' ` `, ` ` "default_on" ` ` en ` ` 'default_off " ` `. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Strict CSRF Token Enforcement (Experimental) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Hiermee kunnen CSRF-beveiligingstokens voor extra verharding worden vergeleken met de momenteel gebruikte aangepaste header. Wanneer de gebruiker zich aanmeldt, wordt er een extra cookie gemaakt met het CSRF-token.

** False**: Hiermee worden CSRF-beveiligingstokens uitgeschakeld. + --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ' ExperimentalStrictCSRFEnforcement ": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ --------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Toegang tot configuratie-instellingen beperken voorafgaand aan aanmelding ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in december 16, 2018 release *

Schakel deze instelling in om het aantal configuratieinstellingen dat voor aanmelding naar gebruikers is verzonden, te beperken.

Ondersteund voor Matterendste server v5.1.0 en hoger, en Matterbest Mobile-apps v1.10.0 en hoger. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ExperimentalLimitClientConfig ":" false " ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Legacy MFA API-eindpunt uitschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Hiermee schakelt u het eindpunt van het oude checkMfa-eindpunt uit, dat alleen vereist is voor Matterbest Mobile Apps op versie 1.16 of eerder bij gebruik van multifactorverificatie (MFA). Aanbevolen om in te stellen op ` ` true ` ` voor extra beveiligingsverharding.

** False**: Keeps de erfenis ` ` checkMfa ` ` eindpunt ingeschakeld om mobiele versies 1.16 en eerder te ondersteunen. Als het eindpunt is ingeschakeld, wordt er informatie openbaar gemaakt over de vraag of een gebruiker MFA heeft ingesteld. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` DisableLegacyMFA ": true, ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Systeembeheer beperken (Experimental) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Hiermee kunt u een subset van de instellingen voor de serverconfiguratie van de systeemconsole beperken en wijzigen. Niet aanbevolen voor gebruik in on-prem-installaties. Dit is bedoeld om Matterbest Private Cloud te ondersteunen bij het geven van de rol van System Admin aan gebruikers, maar het beperken van bepaalde acties alleen voor Cloud Admins.

** False**: Er worden geen beperkingen toegepast op de rol Systeembeheer. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` RestrictSystemAdmin ': "false" ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Teaminstellingen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Teamgenoot-naam wordt afgebeeld ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

Stuurteamgenoot-naam wordt afgebeeld op systeemniveau.

** True**: Hiermee kunnen systeembeheerders de Teammate-naamweergave op systeemniveau besturen.

** False**: Systeembeheerders kunnen Teammate-naamscherm niet beheren op systeemniveau. + ------------------------------------------------------------------------------------------------------------------ +
| De '`config.json ` `-instelling van deze feature is' ` "LockTeammateNameDisplay": [] ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ------------------------------------------------------------------------------------------------------------------ +

Standaardkanalen (experimenteel) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Standaardkanalen elke gebruiker wordt automatisch toegevoegd na het deelnemen aan een nieuw team. Geldt alleen voor openbare kanalen, maar is van invloed op alle teams op de server.

Als dit niet is ingesteld, wordt elke gebruiker standaard toegevoegd aan de ` ` off-topic ` ` ` en ` ` town-square ` ` kanalen.

Zelfs als ` ` town-square ` ` niet in de lijst staat, wordt elke gebruiker toegevoegd aan dat kanaal nadat hij een nieuw team heeft toegevoegd. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "ExperimentalDefaultChannels": [] ` ` met string array input bestaande uit kanaalnamen, zoals ` ` [ "aankondiging", "developers"] ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

E-mailinstellingen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Instellingen voor clientvereisten (Experimental)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Laatste Android-versie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De meest recente versie van de app Android React Native die wordt aanbevolen voor gebruik. + ---------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ``config.json ` `-instelling van deze feature is ` ` AndroidLatestVersion ":" "` ` met tekenreeksinvoer die overeenkomt met een versiereeks, zoals ` `" 1.2.0 " ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------- +

Minimum Android-versie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De minimale versie van de Android React Native app die moet worden gebruikt. + ------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` `-instelling van deze feature is ` ` AndroidMinVersion': "" ` ` met tekenreeksinvoer die overeenkomt met een versiereeks, zoals ` ` "1.2.0" ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------- +

Laatste Desktop Versie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De meest recente versie van de desktop-app die wordt aanbevolen voor gebruik. + ---------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` DesktopLatestVersion ":" "` ` met reeksinvoer die overeenkomt met een versiereeks, zoals ` `" 1.2.0 " ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------- +

Minimale Destonversie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De minimale versie van de te gebruiken desktopapp. + ------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "" "DesktopMinVersion": "" ` ` met reeksinvoer die overeenkomt met een versiereeks, zoals ` ` "1.2.0" ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------- +

Laatste iOS-versie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De meest recente versie van de iOS-app die wordt aanbevolen voor gebruik. + ------------------------------------------------------------------------------------------------------------------------------------------------ +
| De instelling ``config.json van deze feature is ` ` "IosLatestVersion": "" ` ` met tekenreeksinvoer die overeenkomt met een versiereeks, zoals ` ` "1.2.0" ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------ +

Minimum iOS-versie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De minimale versie van de iOS React Native app die moet worden gebruikt. + --------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '`config.json `' van deze feature is '`' "IosMinVersion": "" ` ` met tekenreeksinvoer die overeenkomt met een versiereeks, zoals ` ` "1.2.0" ` `. |
+ --------------------------------------------------------------------------------------------------------------------------------------------- +

Buffer voor push-berichten ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Wordt gebruikt voor het besturen van de buffer van uitstaande push-berichten die moeten worden verzonden. Als het aantal berichten dat aantal overschrijdt, wordt de opdracht tot het maken van de push-berichten geblokkeerd totdat er ruimte is. + --------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' `config.json ` `-instelling van deze feature is ` ` PushNotificationBuffer ": 1000" ` ` met numerieke invoer. |
+ --------------------------------------------------------------------------------------------------------------------------------------------- +

Thema-instellingen (Experimental)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Ng~

Toegestane thema's ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E10 en hoger *

Selecteer de thema's die kunnen worden gekozen door gebruikers wanneer ` ` EnableThemeSelection ` ` is ingesteld op ` ` true ` ` `. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| Deze functie '` `config.json ` ` instelling is ` `' AllowedThemes ': [] ` ` met string array-invoer bestaande uit de opties ` `' standaard '` `, ` `' organisatie ' ` `, ` ` ` mattermostDark "` `, en ` `" windows10 "` `, zoals ` ` [" mattermostDark "," windows10 "] ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +

Weergave-instellingen (Experimental)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Vragen

Ondersteunde Timezones Pad ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in april 16, 2019 release *

Stel het pad in van het JSON-bestand dat de ondersteunde tijdzones weergeeft wanneer ` ` ExperimentalTimezone ` ` is ingesteld op ` ` true ` `.

Het bestand moet in dezelfde directory staan als het bestand ` `config.json ` ` als u een relatief pad instelt. De standaardwaarde is ' `timezones.json ` `. + ----------------------------------------------------------------------------------------------------------------- +
| De ' ``config.json ` ` instelling van deze feature is ` ` 'SupportedTimezonesPath ":" timezones.json " ` ` met reeksinvoer. |
+ ----------------------------------------------------------------------------------------------------------------- +

Experimentele instellingen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

*Beschikbaar in Enterprise Edition E20 *

^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Het uitschakelen van postmetagegevens wordt alleen aanbevolen als u een significante daling van de prestaties rond kanaal en post-laadtijden ondervindt.

** False**: Laadkanalen met nauwkeuriger schuifpositionering door post-metagegevens te laden. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` DisablePostMetadata ': false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Analyseinstellingen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

*Beschikbaar in Enterprise Edition E10 en hoger *

Maximum aantal gebruikers voor de statistiek ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Stelt het maximumaantal gebruikers op de server in voor de statistieken voor het totaal aantal berichten, de totale hashtag-berichten, de totale bestandsberichten, de posts per dag en de actieve gebruikers met de posts per dag zijn uitgeschakeld.

Deze instelling wordt gebruikt voor het maximaliseren van de prestaties voor grote Enterprise-implementaties. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` `' instelling is ` ` ` MaxUsersForStatistics ": 2500 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Instellingen voor elasticsearch
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Na indexreplicatie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het aantal replica's dat voor elke post-index moet worden gebruikt. Als deze instelling wordt gewijzigd, is deze alleen van toepassing op nieuw gemaakte indexen. Om de wijziging toe te passen op bestaande indexen, moet u de index opschonen en opnieuw opbouwen nadat u deze instelling hebt gewijzigd. + --------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` ` PostIndexReplicas': 2 ` ` met numerieke invoer. |
+ --------------------------------------------------------------------------------------------------- +

Na indexshares ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het aantal shards dat voor elke post-index moet worden gebruikt. Als deze instelling wordt gewijzigd, is deze alleen van toepassing op nieuw gemaakte indexen. Om de wijziging toe te passen op bestaande indexen, moet u de index opschonen en opnieuw opbouwen nadat u deze instelling hebt gewijzigd. + ------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` ` PostIndexShards': 1 ` ` met numerieke invoer. |
+ ------------------------------------------------------------------------------------------------- +

Geaggregeerde zoekindexen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De elasticzoekindexen over de leeftijd die door deze instelling worden opgegeven, worden geaggregeerd tijdens de dagelijkse geplande taak. .. Opmerking:
  Als u ` data retention <https://docs.mattermost.com/administration/data-retention.html> ` _ en ` ElasticSearch <https://docs.mattermost.com/deployment/elasticsearch.html> ` _ gebruikt, controleer dan de ' ElasticSearch aggregate zoekindexen <https: //docs.mattermost.com/administration/config-settings.html#aggregate-search-indexes> ` _ instelling is ingesteld op een waarde die groter is dan uw gegevensbewaarbeleid in dagen. + ----------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` `' "AggregatePostsAfterDays": 365 ` ` met numerieke invoer. |
+ -----------------------------------------------------------------------------------------------------------------------

Begintijd post-aggregatie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De begintijd van de dagelijkse geplande aggregatortaak. Moet een tijdsaanduiding van 24 uur zijn in de vorm ` ` UU:MM ` ` `.

Deze instelling is gebaseerd op de lokale tijd van de server. + -------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ' PostsAggregatorJobStartTime ":" 03:00 "` ` met 24-uurs tijdaanduidinginvoer in het formulier ` `" UU:MM " ` `. |
+ -------------------------------------------------------------------------------------------------------------------------------------------- +

Indexprefix ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Prefix op de naam van de Elasticsearch-index. Hiermee schakelt u het gebruik van Matterbest Elasticsearch in op een gemeenschappelijke Elasticsearch-cluster. + ---------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is '` IndexPrefix': "" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------- + .. opmerking::
  Wanneer deze instelling wordt gebruikt, krijgen alle Elasticsearch-indexen die door Matterbest zijn gemaakt deze prefix. U kunt verschillende prefixen instellen zodat meerdere Mattermeeste-implementaties een Elasticsearch-cluster kunnen delen zonder dat de indexnamen botsen.
  
Batchgrootte Live indexeren ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Bepaalt hoeveel nieuwe berichten worden samengevoegd voordat ze worden toegevoegd aan de Elasticsearch-index. Het kan nodig zijn om deze waarde te verhogen om te voorkomen dat de snelheidslimiet van uw Elasticsearch-cluster wordt bereikt op de installatie van meerdere berichten per seconde. + -------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` `' LiveIndexingBatchSize ': 1 ` ` met numerieke invoer. |
+ -------------------------------------------------------------------------------------------------------- +

Timeout voor aanvragen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Timeout in seconden voor aanroepen van Elasticsearch. + ------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` "RequestTimeoutSeconds": 30 ` ` met numerieke invoer. |
+ ------------------------------------------------------------------------------------------------------- +

Tijdvenster voor bulkindexering ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Bepaalt het maximale tijdvenster voor een batch van posts die worden geïndexeerd door de Bulk Indexer. Deze instelling servers als een performance optimalisatie voor installaties met meer dan ~ 10 miljoen berichten in de database. Benader deze waarde op basis van het gemiddelde aantal seconden voor 2000 posten die op een normale dag in de productie moeten worden toegevoegd aan de database. Als u deze waarde te laag instelt, worden de taken voor bulkindexeringstaken traag uitgevoerd. + ----------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "" BulkIndexingTimeWindowSeconds ": 3600 ` ` met numerieke invoer. |
+ ----------------------------------------------------------------------------------------------------------------- +

Tracering ^ ^ ^ ^ ^ ^ ^

Opties voor het afdrukken van Elasticsearch-traceerfouten.  Accepteert ` ` fout ` `, ` ` ` ` ` `, of leeg.  ` ` error ` ` zal de fouttracering maken bij het initialiseren van de Elasticsearch-client en het afdrukken van elke sjabloon of zoekquery die een fout als onderdeel van het foutbericht oplevert. ` ` all ` ` zal de drie traceringen (fout, spoor en info) voor het stuurprogramma maken en de query's niet afdrukken omdat ze deel zullen zijn van het traceerlogniveau van de driver. + ------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` ' "Trace": "" ` ` met reeksinvoer. |
+ ------------------------------------------------------------------------------------------------------- +

Bleve-instellingen (Experimental)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Ng~

Indexdir ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Directorypad voor het opslaan van bleve-indexen. + ----------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "IndexDir": "" ` ` met string invoer. |
+ -----------------------------------------------------------------------------------------------------------------------

Indexering ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Het indexeren van nieuwe berichten vindt automatisch plaats. Zoekquery's gebruiken geen bleef zoeken totdat ** Bleve inschakelen voor zoekquery's * * is ingeschakeld.

** False**: Het indexeren van nieuwe posts vindt niet automatisch plaats. + ------------------------------------------------------------------------------------------------------------ +
| De instelling ``config.json van deze feature is ` ` "EnableIndexing": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ------------------------------------------------------------------------------------------------------------ +

Zoeken inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Zoekquery's maken gebruik van bleeve zoekopdracht.

** False**: Zoekquery's gebruiken geen zoekresultaten. + -------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` "EnableZoeken": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ -------------------------------------------------------------------------------------------------------------- +

Automatisch voltooien inschakelen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Autocomplete query's gebruiken bleeve zoekopdracht.

** False**: Autocomplete query's gebruiken geen zoekresultaten. + ----------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableAutocomplete ": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ----------------------------------------------------------------------------------------------------------------- +

(') ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Bepaalt het maximale tijdvenster voor een batch van posts die worden geïndexeerd door de Bulk Indexer. Deze instelling dient als prestatieoptimalisatie voor installaties met meer dan ~ 10 miljoen postings in de database. Benader deze waarde op basis van het gemiddelde aantal seconden voor 2000 posten die op een normale dag in de productie moeten worden toegevoegd aan de database. Als u deze waarde te laag instelt, worden de taken voor bulkindexeringstaken langzaam uitgevoerd. + -----------------------------------------------------------------------------------------------------------------------
| Deze functie ' ` `config.json ` ` instelling is ` ` "" BulkIndexingTimeWindowSeconds ": 3600 ` ` met numerieke invoer. |
+ -----------------------------------------------------------------------------------------------------------------------

Instellingen voor berichtuitvoer
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Export Vanaf Tijdsaanduiding ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Stel de Unix-tijdsaanduiding (seconden sinds epoch, UTC) in om gegevens uit te exporteren. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is' ` ExportFromTimestamp ': 0 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Bestandslocatie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Stel de bestandslocatie in van de nalevingsexporten.

Standaard worden ze geschreven naar de subdirectory ` ` exports ` van de geconfigureerde ` Local Storage-directory <https: //docs.mattermost.com/administration/config-settings.html#storage> ` _. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` "FileLocation": "export" ` ` met reeksinvoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Batchgrootte ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Bepaalt hoeveel nieuwe berichten worden samengevoegd in een exportbestand voor naleving. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is ` ` BatchSize': 10000 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Plugin-instellingen (Beta)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Enable Plugin Uploads ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Hiermee schakelt u de uploads van plugins in met behulp van System Admins at ** Plugins > Management * *. Als u niet p
lan om een plugin te uploaden, ingesteld op ` ` false ` ` om te bepalen welke plugins zijn geïnstalleerd op uw server. Raadpleeg 'documentatie <https://about.mattermost.com/default-plugin-uploads>' __ om meer te weten te komen.

** False**: Hiermee worden de uploads van plugins op de Mattermeeste server uitgeschakeld. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling ``config.json van deze feature is ` ` ` EnableUploads ": false ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Sta onveilige download URL ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Hiermee kunt u een plugin downloaden en installeren vanaf een URL op afstand.

** False**: Hiermee wordt het downloaden en installeren van een plugin uit een URL op afstand uitgeschakeld. + -----------------------------------------------------------------------------------------------------------------------------------------
| De instelling ``config.json van deze feature is ` ` AllowInsecureDownloadUrl ": false ` ` met opties ` ` true ` ` en ` ` false ` `. |
+ ----------------------------------------------------------------------------------------------------------------------------------------- +

Inschakelen Plugin Health Check ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

** True**: Zorgt voor plugin Health check om ervoor te zorgen dat alle plugins worden periodiek gecontroleerd, en opnieuw gestart of gedeactiveerd op basis van hun gezondheidstoestand.

De health check draait om de 30 seconden. Als de plugin wordt gedetecteerd om drie keer binnen een uur te mislukken, probeert de Mattermeeste server het opnieuw te starten. Als de herstart 3 opeenvolgende keren mislukt, wordt het automatisch uitgeschakeld.

** False**: Hiermee schakelt u de Health-controle van de plugin uit op uw Mattermeeste-server. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is ` ` 'EnableHealthCheck': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Map ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De locatie van de pluginbestanden. Als dit veld leeg is, worden ze opgeslagen in de directory ` ` ./plugins ` `. Het pad dat u instelt moet bestaan en Mattermost moet schrijfrechten hebben. + ----------------------------------------------------------------------------------------------------------------- +
| De '`config.json `'-instelling van deze feature is ` ` "Directory": "./plugins" ` ` met tekenreeksinvoer. |
+ ----------------------------------------------------------------------------------------------------------------- +

Clientdirectory ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De locatie van clientpluginbestanden. Als dit veld leeg is, worden ze opgeslagen in de directory ` ` ./client/plugins ` `. Het pad dat u instelt moet bestaan en Mattermost moet schrijfrechten hebben. + ----------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json' ` ` instelling is ` ` "Directory": "./client/plugins" ` ` met tekenreeksinvoer. |
+ ----------------------------------------------------------------------------------------------------------------- +

Taken
~ ~ ~ geven

Instellingen om te configureren hoe Mattermeeste planningen en voltooit periodieke taken, zoals het verwijderen van oude berichten met Data Retention ingeschakeld of indexeren van berichten met Elasticsearch. Deze instellingen bepalen welke Mattermeeste servers worden aangeduid als Planner, een server die de taken op de juiste tijden in de wachtrij plaatst, en als een Worker, een server die de opgegeven taken voltooit.

Bij het uitvoeren van Matterbest op een enkele machine moeten ` ` RunJobs ` ` en ` ` RunScheduler ` ` ingeschakeld zijn. Zonder deze beide functies zal Matterbest niet goed functioneren.

Wanneer Matterbest wordt uitgevoerd in de modus voor hoge beschikbaarheid, moet ` ` RunJobs ` ` worden ingeschakeld op een of meer servers terwijl ` ` RunScheduler ` ` op alle servers onder normale omstandigheden moet worden ingeschakeld. Een cluster voor hoge beschikbaarheid heeft één planner en een of meer medewerkers. Zie de onderstaande gedeelten voor meer informatie.

Taken uitvoeren ^ ^ ^ ^ ^ ^ ^ ^ ^

Instellen of deze Matterfde server taken afhandelen die door de Planner zijn gemaakt.

Bij het uitvoeren van Matterbest op een enkele machine moet deze instelling altijd ingeschakeld zijn.

Bij het uitvoeren van Matterbest in High Availablity-modus moeten een of meer servers deze instelling ingeschakeld hebben. Het wordt aanbevolen dat een High Availability-cluster een of meer toegewijde medewerkers met deze instelling heeft ingeschakeld terwijl de resterende Matterbest-appservers het hebben uitgeschakeld. + ------------------------------------------------------------------------------------------------------------------------------------ +
| Deze functie ' ` `config.json ` ` instelling is ` ` "RunJobs": true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ------------------------------------------------------------------------------------------------------------------------------------ +

Planner ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geef aan of deze Mattermeeste server taken zal plannen die door een Worker worden uitgevoerd.

Bij het uitvoeren van Matterbest op een enkele machine moet deze instelling altijd ingeschakeld zijn.

Bij het uitvoeren van Matterbest in High Availablity-modus moet deze instelling altijd worden ingeschakeld. In een High Availability-cluster wordt precies een van de servers op een gegeven moment aangewezen als Planner om ervoor te zorgen dat er geen dubbele taken worden gemaakt. Zie ` High Availability documentation <https: //docs.mattermost.com/deployment/cluster.html#job-server> ` __ voor meer informatie. .. waarschuwing:

   Het wordt ten zeerste aanbevolen om deze instelling niet te wijzigen van de standaardinstelling van ` ` true ` ` omdat dit voorkomt dat de ` ` ClusterLeader ` ` in staat is om de planner uit te voeren. Als gevolg daarvan worden terugkerende taken zoals LDAP-synchronisatie, Compliance-export en gegevensopslag niet meer gepland.

In de vorige versies van de Mattermeeste Server en deze documentatie zijn de instructies voor het uitvoeren van de taakserver met ` ` RunScheduler: false ' `. Het clusterontwerp is geëvolueerd en dit is niet langer het geval. + ----------------------------------------------------------------------------------------------------------------------------------------- +
| De instelling '` `config.json `' van deze feature is ` ` RunScheduler ': true ` ` met opties ` ` true ` ` en ` ` false ` ` `. |
+ ----------------------------------------------------------------------------------------------------------------------------------------- +

Gedeprecieerde configuratie-instellingen
-----------------------------------

Beleid
~ ~ ~ geven

*Verwijderd in juni 16, 2018 release * .. opmerking:: Permission policy settings zijn beschikbaar in Enterprise Edition E10 en E20. Vanaf v5.0 worden deze instellingen gevonden in de pagina ' Geavanceerde machtigingen <https://docs.mattermost.com/deployment/advanced-permissions.html> ` __ in plaats van configuratie-instellingen.

Het verzenden van een team nodigt uit (^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juni 16, 2018 release * .. Opmerking: 

   Vanaf v5.0 is dit vervangen door geavanceerde machtigingen die beheerders een manier bieden om acties in Matterbest alleen te beperken tot geautoriseerde gebruikers. Zie de ` Geavanceerde machtigingen voor machtigingen <https://docs.mattermost.com/deployment/advanced-permissions.html> ' _ voor meer informatie.

Beleid instellen voor wie anderen kan uitnodigen voor een team met behulp van de optie ** E-mail verzenden * *, ** Get Team Invite Link * *, en ** Leden toevoegen aan team * * opties in het hoofdmenu. Als ** Get Team Invite Link * * wordt gebruikt voor het delen van een link, kunt u de uitnodigingcode van ** Teaminstellingen > Uitnodigingscode * * laten vervallen nadat de gewenste gebruikers zich bij het team hebben aangesloten. Opties zijn onder andere:

** Alle teamleden * *: Staat een teamlid toe om anderen uit te nodigen met behulp van een e-mailuitnodiging, een teamuitnodiging of door leden rechtstreeks aan het team toe te voegen.

** Team-en systeembeheerders * *: De e-mailuitnodiging, de link voor het team uitnodigen en de knoppen voor het toevoegen van leden aan de teamknoppen in het hoofdmenu van gebruikers die geen teambeheerders of systeembeheerders zijn.

** Systeembeheerders * *: Hides de e-mailuitnodiging, team uitnodigen link, en voeg leden toe aan teamknoppen in het hoofdmenu van gebruikers die geen systeembeheerders zijn. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` ` RestrictTeamInvite': "all" ` ` met opties ` ` ` all "` ` `, ` ` ` team_admin" ` `, en ` ` "system_admin" ` ` voor de bovenstaande instellingen. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Inschakelen van het openbaar kanaal voor ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juni 16, 2018 release * .. Opmerking: 

   Vanaf v5.0 is dit vervangen door geavanceerde machtigingen die beheerders een manier bieden om acties in Matterbest alleen te beperken tot geautoriseerde gebruikers. Zie de ` Geavanceerde machtigingen voor machtigingen <https://docs.mattermost.com/deployment/advanced-permissions.html> ' _ voor meer informatie.

Beperk het machtigingsniveau dat vereist is voor het maken van openbare kanalen.

** Alle teamleden * *: Alle teamleden toestaan om openbare kanalen te maken.

** Team Admins en systeembeheerders * *: Beperken tot het maken van openbare kanalen voor teambeheerders en systeembeheerders.

** Systeembeheerders * *: Beperken tot het maken van openbare kanalen voor systeembeheerders. + --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` RestrictPublicChannelCreation ":" all "` ` met opties ` ` ` all" ` ` `, ` ` ` team_admin "` `, en ` ` 'system_admin" ` ` voor de bovenstaande instellingen. |
+ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Inschakelen van het openbare kanaal hernoemen naar ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juni 16, 2018 release * .. Opmerking: 

   Vanaf v5.0 is dit vervangen door geavanceerde machtigingen die beheerders een manier bieden om acties in Matterbest alleen te beperken tot geautoriseerde gebruikers. Zie de ` Geavanceerde machtigingen voor machtigingen <https://docs.mattermost.com/deployment/advanced-permissions.html> ' _ voor meer informatie.

Beperk het machtigingsniveau dat vereist is voor het wijzigen van de naam en het instellen van de koptekst of het doel voor openbare kanalen.

** Alle kanaalleden * *: Alle kanaalleden toestaan om de openbare kanalen te hernoemen.

** Channel Admins, Team Admins, and System Admins * *: Beperken de naam van de openbare kanalen aan de Channel Admins, Team Admins en System Admins die lid zijn van het kanaal.

** Teambeheerders en systeembeheerders * *: Beperken van de naam van openbare kanalen tot Teambeheerders en systeembeheerders die lid zijn van het kanaal.

** System Admins * *: beperken van het hernoemen van openbare kanalen naar systeembeheerders die lid zijn van het kanaal. + -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` RestrictPublicChannelManagement ":" all "` ` met opties ` ` ` all" ` `, ` ` ` channel_admin "` `, ` ` ` team_admin" ` `, en ` ` ` system_admin " ` ` voor de bovenstaande instellingen. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------- +

Het wissen van het openbaar kanaal inschakelen voor ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juni 16, 2018 release * .. Opmerking: 

   Vanaf v5.0 is dit vervangen door geavanceerde machtigingen die beheerders een manier bieden om acties in Matterbest alleen te beperken tot geautoriseerde gebruikers. Zie de ` Geavanceerde machtigingen voor machtigingen <https://docs.mattermost.com/deployment/advanced-permissions.html> ' _ voor meer informatie.

Beperk het machtigingsniveau dat vereist is om openbare kanalen te wissen. Verwijderde kanalen kunnen worden hersteld van de database met behulp van een ` command line tool <https://docs.mattermost.com/administration/command-line-tools.html> ` __.

** Alle kanaalleden * *: Alle kanaalleden toestaan om openbare kanalen te verwijderen.

** Channel Admins, Team Admins, and System Admins * *: Beperken tot het verwijderen van openbare kanalen naar Channel Admins, Team Admins en System Admins die lid zijn van het kanaal.

** Teambeheerders en systeembeheerders * *: Beperken tot het wissen van openbare kanalen voor Teambeheerders en systeembeheerders die lid zijn van het kanaal.

** Systeembeheerders * *: Beperken tot het wissen van openbare kanalen naar systeembeheerders die lid zijn van het kanaal. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| Deze functie '` `config.json ` ` instelling is ` ` ` RestrictPublicChannelDeletion': "all" ` ` met opties ` ` ` all "` `, ` ` ` channel_admin" ` `, ` ` ` team_admin "` `, en ` ` ` system_admin" ` ` voor de bovenstaande instellingen. |
+ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +

Schakel het maken van private kanalen in voor ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juni 16, 2018 release * .. Opmerking: 

   Vanaf v5.0 is dit vervangen door geavanceerde machtigingen die beheerders een manier bieden om acties in Matterbest alleen te beperken tot geautoriseerde gebruikers. Zie de ` Geavanceerde machtigingen voor machtigingen <https://docs.mattermost.com/deployment/advanced-permissions.html> ' _ voor meer informatie.

Beperk het machtigingsniveau dat vereist is voor het maken van persoonlijke kanalen.

** Alle teamleden * *: Alle teamleden toestaan om besloten kanalen te maken.

** Teambeheerders en systeembeheerders * *: Beperken tot het maken van persoonlijke kanalen voor teambeheerders en systeembeheerders.

** System Admins * *: Beperken tot het maken van persoonlijke kanalen voor systeembeheerders. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie '` `config.json ` ` instelling is ` ` ` RestrictPrivateChannelCreation': "all" ` ` met opties ` ` ` all "` ` `, ` ` ` team_admin" ` `, en ` ` 'system_admin " ` ` voor de bovenstaande instellingen. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Inschakelen van privé-kanaal hernoemen voor ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juni 16, 2018 release * .. Opmerking: 

   Vanaf v5.0 is dit vervangen door geavanceerde machtigingen die beheerders een manier bieden om acties in Matterbest alleen te beperken tot geautoriseerde gebruikers. Zie de ` Geavanceerde machtigingen voor machtigingen <https://docs.mattermost.com/deployment/advanced-permissions.html> ' _ voor meer informatie.

Beperk het machtigingsniveau dat vereist is voor het wijzigen van de naam en het instellen van de koptekst of het doel voor besloten kanalen.

** Alle kanaalleden * *: Alle kanaalleden toestaan om persoonlijke kanalen te hernoemen.

** Channel Admins, Team Admins en System Admins * *: Beperken tot het hernoemen van persoonlijke kanalen naar Channel Admins, teambeheerders en systeembeheerders die lid zijn van het besloten kanaal.

** Teambeheerders en systeembeheerders * *: Beperken tot het hernoemen van persoonlijke kanalen naar Teambeheerders en systeembeheerders die lid zijn van het besloten kanaal.

** Systeembeheerders * *: Beperken tot het hernoemen van besloten kanalen naar de systeembeheerders die lid zijn van het besloten kanaal. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Deze functie ' ` `config.json ` ` instelling is ` ` ` RestrictPrivateChannelManagement ":" all "` ` met opties ` ` ` all" ` ` `, ` ` ` channel_admin "` `, ` ` ` team_admin" ` `, en ` ` 'system_admin " ` ` voor de bovenstaande instellingen. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Het beheer van particuliere kanaalleden mogelijk maken voor ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juni 16, 2018 release * .. Opmerking: 

   Vanaf v5.0 is dit vervangen door geavanceerde machtigingen die beheerders een manier bieden om acties in Matterbest alleen te beperken tot geautoriseerde gebruikers. Zie de ` Geavanceerde machtigingen voor machtigingen <https://docs.mattermost.com/deployment/advanced-permissions.html> ' _ voor meer informatie.

Beleid instellen voor het toevoegen en verwijderen van leden uit besloten kanalen.

** Alle teamleden * *: Alle teamleden toestaan om leden toe te voegen en te verwijderen.

** Team Admins, Channel Admins en System Admins * *: Alleen teambeheerders, kanaalbeheerders en systeembeheerders toestaan om leden toe te voegen en te verwijderen.

** Teambeheerders en systeembeheerders * *: Alleen teambeheerders en systeembeheerders toestaan om leden toe te voegen en te verwijderen.

** System Admins * *: Alleen systeembeheerders toestaan om leden toe te voegen en te verwijderen. + ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| Deze functie '` `config.json ` ` instelling is ` ` ` RestrictPrivateChannelManageMembers': "all" ` ` met opties ` ` ` all "` `, ` ` ` channel_admin" ` `, ` ` ` team_admin "` `, en ` ` ` system_admin" ` ` voor de bovenstaande instellingen. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------- +

Schakel het persoonlijk kanaal in voor ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juni 16, 2018 release * .. Opmerking: 

   Vanaf v5.0 is dit vervangen door geavanceerde machtigingen die beheerders een manier bieden om acties in Matterbest alleen te beperken tot geautoriseerde gebruikers. Zie de ` Geavanceerde machtigingen voor machtigingen <https://docs.mattermost.com/deployment/advanced-permissions.html> ' _ voor meer informatie.

Beperk het machtigingsniveau dat vereist is om besloten kanalen te wissen. Verwijderde kanalen kunnen worden hersteld van de database met behulp van een ` command line tool <https://docs.mattermost.com/administration/command-line-tools.html> ` __.

** Alle kanaalleden * *: Alle kanaalleden toestaan om besloten kanalen te verwijderen.

** Channel Admins, Team Admins, and System Admins * *: Beperken tot het verwijderen van persoonlijke kanalen naar Channel Admins, Team Admins en System Admins die lid zijn van het besloten kanaal.

** Teambeheerders en systeembeheerders * *: Beperken tot het wissen van persoonlijke kanalen voor Team Admins en System Admins die lid zijn van het besloten kanaal.

** Systeembeheerders * *: Beperken tot het verwijderen van besloten kanalen naar Systeembeheerders die lid zijn van het besloten kanaal. + -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Deze functie '` `config.json ` ` instelling is ` ` ` RestrictPrivateChannelDeletion': "all" ` ` met opties ` ` ` all "` ` `, ` ` ` channel_admin" ` `, ` ` ` team_admin "` `, en ` ` 'system_admin" ` ` voor de bovenstaande instellingen. |
+ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Toestaan dat gebruikers berichten kunnen verwijderen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juni 16, 2018 release * .. Opmerking: 

   Vanaf v5.0 is dit vervangen door geavanceerde machtigingen die beheerders een manier bieden om acties in Matterbest alleen te beperken tot geautoriseerde gebruikers. Zie de ` Geavanceerde machtigingen voor machtigingen <https://docs.mattermost.com/deployment/advanced-permissions.html> ' _ voor meer informatie.

Beperk het machtigingsniveau dat nodig is voor het wissen van berichten. Teambeheerders, kanaalbeheerders en systeembeheerders kunnen berichten alleen verwijderen in kanalen waar ze lid zijn. Berichten kunnen elk moment worden gewist.

** Berichtauteurs kunnen hun eigen berichten wissen, en beheerders kunnen elk bericht wissen * *: Auteurs toestaan hun eigen berichten te wissen en teambeheerders, Channel Admins en System Admins toe te staan om een bericht te wissen.

** Teambeheerders en systeembeheerders * *: Alleen teambeheerders en systeembeheerders kunnen berichten wissen.

** System Admins * *: Alleen systeembeheerders kunnen berichten wissen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` ` RestrictPostDelete ":" all "` ` met opties ` ` ` all" ` ` `, ` ` ` team_admin "` `, en ` ` 'system_admin" ` ` voor de bovenstaande instellingen. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Gebruikers toestaan hun berichten te bewerken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juni 16, 2018 release * .. Opmerking: 

   Vanaf v5.0 is dit vervangen door geavanceerde machtigingen die beheerders een manier bieden om acties in Matterbest alleen te beperken tot geautoriseerde gebruikers. Zie de ` Geavanceerde machtigingen voor machtigingen <https://docs.mattermost.com/deployment/advanced-permissions.html> ' _ voor meer informatie.

Stel de tijdslimiet in dat gebruikers hun berichten moeten bewerken na het posten.

** Elke keer * *: Gebruikers toestaan om hun berichten te bewerken op elk gewenst moment na het posten.

** Never**: Gebruikers kunnen niet hun berichten bewerken.

** { n } seconden na het posten * *: Gebruikers kunnen hun berichten bewerken binnen de opgegeven tijdslimiet na het posten. De tijdslimiet wordt toegepast met de instelling ` ` config.json ` ` ` instelling ` ` PostEditTimeLimit ` ` hieronder beschreven. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "AllowEditPost": "altijd" ` ` met opties ` ` ` ` altijd "` `, ` `" nooit "` `, en ` `" time_limit " ` ` voor de bovenstaande instellingen. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Tijdslimiet na bewerken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Wanneer post bewerken is toegestaan, kan het instellen van deze optie op ` ` -1 ` ` het bewerken van een willekeurig tijdstip mogelijk maken en dit instellen op een positief geheel beperkt het bewerken van de tijd in seconden. Als post bewerken uitgeschakeld is, is deze instelling niet van toepassing. + -------------------------------------------------------------------------------------------------- +
| De '` `config.json ` ` instelling van deze feature is' ` ` PostEditTimeLimit ': -1 ` ` met numerieke invoer. |
+ -------------------------------------------------------------------------------------------------- +

Afbeeldingen
~ ~ ~ geven

Breedte van bijlage-miniatuur ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juli 16, 2017 release *

Breedte van miniaturen gegenereerd uit geüploade afbeeldingen. Bij het bijwerken van deze waarde wordt de weergave van miniatuurafbeeldingen in de toekomst gewijzigd, maar worden geen wijzigingen aangebracht die in het verleden zijn gemaakt. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De ' ` `config.json ` ` instelling van deze feature is ` ` "" ThumbnailWidth ": 120 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Miniatuurhoogte van bijlagen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juli 16, 2017 release *

Hoogte van miniaturen gegenereerd uit geüploade afbeeldingen. Bij het bijwerken van deze waarde wordt de weergave van miniatuurafbeeldingen in de toekomst gewijzigd, maar worden geen wijzigingen aangebracht die in het verleden zijn gemaakt. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is ` `' "ThumbnailHeight": 100 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Afbeeldingsvoorbeeldbreedte ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juli 16, 2017 release *

Maximumbreedte van previewafbeelding. Bij het bijwerken van deze waarde wordt de weergave van afbeeldingen in de toekomst gewijzigd, maar worden geen wijzigingen aangebracht die in het verleden zijn gemaakt. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| Deze functie ' ` `config.json ` ` instelling is ` ` "PreviewWidth": 1024 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Afbeelding Voorbeeld Hoogte ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juli 16, 2017 release *

Maximale hoogte van previewafbeelding. Als u deze waarde instelt op ` ` 0 ` ` instrueert Matterbest de hoogte van de previewafbeelding op basis van de afbeeldingsbreedte van het bronimage en de breedte van de previewafbeelding. Bij het bijwerken van deze waarde wordt de weergave van afbeeldingen in de toekomst gewijzigd, maar worden geen wijzigingen aangebracht die in het verleden zijn gemaakt. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` `-instelling van deze feature is ` ` PreviewHeight': 0 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Profielfoto Breedte ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juli 16, 2017 release *

De breedte waarnaar profielfoto's worden aangepast na het uploaden via Accountinstellingen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '`config.json ` ` instelling van deze feature is ` ` ProfileWidth': 128 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +

Profielfoto Hoogte ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Verwijderd in juli 16, 2017 release *

De hoogte waarop profielafbeeldingen worden aangepast na het uploaden via Accountinstellingen. + ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
| De '``config.json ` ` instelling van deze feature is ` ` ProfileHeight': 128 ` ` met numerieke invoer. |
+ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- +
