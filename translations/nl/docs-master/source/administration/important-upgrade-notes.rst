Belangrijke upgrade Notes
== == == == == == == == == == == = .. Belangrijk:
   PostgreSQL eindigde lange termijn ondersteuning voor ` versie 9.4 in februari 2020 <https://www.postgresql.org/support/versioning> ` _. Matterbest is officieel de ondersteuning van PostgreSQL versie 10 met v5.26 release als PostgreSQL 9.4 wordt niet langer ondersteund. Nieuwe installaties vereisen PostgreSQL 10 +. Previous Mattermeeste versies, inclusief ons huidige ESR, zullen compatibel blijven met PostgreSQL 9.4. We zijn van plan om PostgreSQL 9.4 en alle 9.x versies volledig te depreciëren in onze v5.30 release (16 december). Volg de instructies onder de sectie Upgraden binnen ` de PostgreSQL-documentatie <https://www.postgresql.org/support/versioning/> ` _. .. Belangrijk:
   Ondersteuning voor Mattermeest Server v5.19 ` Extended Support Release <https://docs.mattermost.com/administration/extended-support-release.html> ` _ is tot het einde van de levenscyclus gekomen. Upgraden naar v5.25 of hoger is vereist. .. Belangrijk:
   TLS-versies 1.0 en 1.1 zijn gedeprecieerd door browserleveranciers. Vanaf v5.31 (16 januari 2021) zal mmctl een fout terugzenden wanneer er verbinding wordt gemaakt met Mattermeeste servers die in gebruik zijn genomen met die TLS-versies. Systeembeheerders moeten expliciet een vlag in hun opdrachten toevoegen om ze te blijven gebruiken. Aanbevolen wordt een upgrade naar TLS-versie 1.2 of hoger te maken. + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| Als u een upgrade uitvoert vanaf een eerdere versie dan ... | Dan ... | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
| v5.29.0 | Er is een nieuwe configuratie-instelling ` ` ThreadAutoFollow ` ` toegevoegd ter ondersteuning van ` Gestorte Reply Threads |
| | <https: //docs.google.com/presentation/d/1QSrPws3N8AMSjVyOKp15FKT7O0fGMSx8YidjSDS4Wng/edit#slide= id.g2f0aecc189_0_245 > ` _ vrijgeven in bèta in Q1 2021. Dit |
| | instelling is standaard ingeschakeld en kan invloed hebben op de prestaties van de server. Aanbevolen wordt om onze ` documentatie over hardwarevereisten te bekijken |
| | <https: //docs.mattermost.com/install/requirements.html#hardware-requirements> ` _ om ervoor te zorgen dat uw servers op de juiste manier worden geschaald voor de grootte van uw gebruikersbasis.  |   
| + -------------------------------------------------------------------------------------------------------------------------------
----------------------------------- +
| | Uitgeschakeld de xmlsec1-based SAML-bibliotheek in het voordeel van de opnieuw ingeschakelde en verbeterde SAML bibliotheek.                                                                    | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.28.0 | Nu wanneer de dienst crasht, zal het genereren van een coredump in plaats van gewoon dumpen van de stacktracering naar de console. Dit stelt ons in staat om de volledige te behouden |
| | informatie van de crash om te helpen met het opsporen van fouten.                                                                                                              |
| | |
| | Voor meer informatie over coredumps, zie: https://man7.org/linux/man-pages/man5/core.5.html.                                                             |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | In-product kennisgevingen zijn geïntroduceerd om System Admins en eindgebruikers op de hoogte te houden van de nieuwste productverbeteringen die beschikbaar zijn in nieuwe server en desktop | 
| | versies. ` Meer informatie over in-product kennisgevingen <https://docs.mattermost.com/administration/notices.html> ` _ en hoe ze uit te schakelen in onze documentatie.         |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Uitgeschakeld de xmlsec1-based SAML-bibliotheek in het voordeel van de opnieuw ingeschakelde en verbeterde SAML bibliotheek.                                                                    | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.27.0 | De in xmlsec1 gebaseerde SAML-bibliotheek is uitgeschakeld ten gunste van de opnieuw ingeschakelde en verbeterde SAML-bibliotheek.                                                                    | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.26.0 | In v5.26 moeten Elasticsearch-indexen opnieuw worden gemaakt. Admins moeten Elasticsearch opnieuw indexeren met behulp van de ** Purge index * * en dan ** Index nu * * knop zodat alle |
| | de wijzigingen worden opgenomen in de index. Systemen kunnen worden achtergelaten met een beperkte zoekopdracht tijdens de indexering, dus het moet worden gedaan in een tijd wanneer er is |
| | weinig tot geen activiteit omdat het enkele uren kan duren.                                                                                                         |
| + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------- +
| | Een ` ` EnableExperimentalGossipEncryption ` ` optie is toegevoegd onder ` ` ClusterSettings ` ` `. Als dit is ingesteld op ` ` true ` `, en ` ` UseExperimentalGossip ` ` is ook ` ` true ` `, | 
| | alle communicatie via de cluster met behulp van het roddel protocol zal worden versleuteld. De versleuteling gebruikt standaard ` ` AES-256 ` ` en het wordt niet configureerbaar bewaard |
| | door ontwerp. Als u wilt, kunt u de waarde in de tabel Systemen echter handmatig instellen voor de rij ' ` ClusterEncryptionKey ` `. Een sleutel is een bytereeks geconverteerd naar |
| | base64. Het moet 16, 24 of 32 bytes zijn om AES-128, AES-192 of AES-256 te selecteren.                                                                          |
| | |
| | Om de sleutel bij te werken, kan men uitvoeren: |
| | ` ` UPDATE Systems SET Value = '<value>' WHERE Name= 'ClusterEncryptionKey'; ` ` in MySQL en |
| | ` ` ` UPDATE systems SET waarde = '<value>' WHERE name= 'ClusterEncryptionKey' ` ` voor PostgreSQL.                                                                         |
| | |
| | Voor elke verandering in deze configuratie instelling te nemen effect, de hele clus
Moet eerst worden uitgeschakeld. Vervolgens wordt de configuratie gewijzigd en vervolgens opnieuw gestart. In een cluster, |
| | alle servers maken ofwel volledig gebruik van versleuteling. Er kan geen sprake zijn van gedeeltelijk gebruik.                                                                     |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | SAML Setting "Use Verbeterde SAML Library (Beta)" was krachtig uitgeschakeld. Volg de instructies op |
| | https://docs.mattermost.com/deployment/sso-saml-before-you-begin.html voor het inschakelen van SAML met behulp van het functie-equivalent ` ` xmlsec1 ` ` programma.                        | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.25.0 | Enkele onjuiste instructies met betrekking tot SAML-instellingen met Active Directory ADFS voor het instellen van het "Relying Party Trust Identifier" zijn gecorrigeerd. Hoewel de |
| | instellingen blijven werken, het wordt aangemoedigd dat u |
| | ` modify the settings <https: //docs.mattermost.com/deployment/sso-saml-adfs-msws2016.html#add-a-trust-party-trust> ` _. | 
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Uitgeschakeld de xmlsec1-based SAML-bibliotheek in het voordeel van de opnieuw ingeschakelde en verbeterde SAML bibliotheek.                                                                    | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.24.0 | Een nieuwe configuratie-instelling, ` ` Extend360 SessionLengthWithActivity ` ` breidt sessies automatisch uit om gebruikers ingelogd te houden als ze actief zijn in hun Mattermeeste |
| | apps. Het wordt aanbevolen deze instelling in te schakelen om de gebruikerservaring te verbeteren als dit voldoet aan het beleid van uw organisatie.                                        |
| | ` Lees meer hier <https://mattermost.com/blog/session-expiry-experience> ` _. |
| + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------- +
| | De ` ` mattermost_http_request_duration_seconds ` ` histogrammetriek (in Enterprise Edition) is verwijderd. Deze informatie is al vastgelegd door |
| | ` ` mattermost_api_time ` `, die ook de naam van de API-handler, de HTTP-methode en de responscode bevat.                                                           |
| | |
| | Als voorbeeld, als u gebruikt |
| | ` ` rate (mattermost_http_request_duration_seconds_sum { server= ~ "$var" } [ 5m])/rate (mattermost_http_request_duration_seconds_count { server= ~ "$var" } [ 5m]) ` ` |
| | om gemiddelde call-duur te meten, moet het vervangen worden met |
| | ` ` sum (rate (mattermost_api_time_sum { server= ~ "$var" } [ 5m])) door (instance)/sum (rate (mattermost_api_time_count { server= ~ "$var" } [ 5m])) door (instance) ` `. |
| + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------- +
| | Vanwege de vaststelling van prestaties met betrekking tot emoji reacties, de prestaties van de upgrade is beïnvloed in dat de schema upgrade nu meer tijd in |
| | omgevingen met veel reacties in hun database. Deze omgevingen worden aanbevolen om de schema-migratie uit te voeren tijdens lage gebruikstijden en mogelijk |
| | van tevoren van de upgrade. Aangezien deze migratie plaatsvindt voordat de Matterendste server volledig wordt gestart, is de installatie van niet-hoge beschikbaarheid onbereikbaar |
| | gedurende deze tijd.                                                                                                                                                |          
| | |
| | De migratie is een enkele lijn van SQL en kan rechtstreeks worden toegepast op de database via de MySQL/PSQL command line clients als u dit liever wilt ontkoppelen |
| | van het opnieuw starten van de Mattertiste server. Het is volledig backwards compatibel, zodat de schema verandering kan worden toegepast op een eerdere versie van Matterbest zonder probleem. |
| | Gedurende de tijd dat de schemawijziging draait (~ 30 per miljoen rijen in de tabel Reactions), als eindgebruikers proberen te reageren op berichten, zullen de emoji-reacties | 
| | niet laden voor eindgebruikers.                                                                                                                                          |
| | |
| | MySQL: ` ` ALTER TABLE Reacties DROP PRIMARY KEY, ADD PRIMARY KEY (PostId, UserId, EmojiName); ` ` |
| | |
| | PostgreSQL: ` ` ALTER TABLE reacties DROP CONSTRAINT reactions_pkey, ADD PRIMARY KEY (PostId, UserId, EmojiName); ` ` |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +                                                  
| | Op mobiele apps kunnen gebruikers de LDAP-groep (E20-functie) niet zien in de autocomplete dropdown. Gebruikers ontvangen nog steeds meldingen als ze zijn |
| | onderdeel van een LDAP-groep. Het sleutelwoord voor de groep wordt echter niet geaccentueerd.                                                                               |  
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | SAML Setting "Use Verbeterde SAML Library (Beta)" was krachtig uitgeschakeld. Volg de instructies op
|
| | https://docs.mattermost.com/deployment/sso-saml-before-you-begin.html voor het inschakelen van SAML met behulp van het functie-equivalent ` ` xmlsec1 ` ` programma.                        | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.22.0 | Als gevolg van de vaststelling van prestaties met betrekking tot emoji reacties, de prestaties van de upgrade is beïnvloed in dat de schema upgrade nu meer tijd in |
| | omgevingen met veel reacties in hun database. Deze omgevingen worden aanbevolen om de schema-migratie uit te voeren tijdens lage gebruikstijden en mogelijk |
| | van tevoren van de upgrade. Aangezien deze migratie plaatsvindt voordat de Matterendste server volledig wordt gestart, is de installatie van niet-hoge beschikbaarheid onbereikbaar |
| | gedurende deze tijd.                                                                                                                                                |          
| | |
| | De migratie is een enkele lijn van SQL en kan rechtstreeks worden toegepast op de database via de MySQL/PSQL command line clients als u dit liever wilt ontkoppelen |
| | van het opnieuw starten van de Mattertiste server. Het is volledig backwards compatibel, zodat de schema verandering kan worden toegepast op een eerdere versie van Matterbest zonder probleem. |
| | Gedurende de tijd dat de schemawijziging draait (~ 30 per miljoen rijen in de tabel Reactions), als eindgebruikers proberen te reageren op berichten, zullen de emoji-reacties | 
| | niet laden voor eindgebruikers.                                                                                                                                          |
| | |
| | MySQL: ` ` ALTER TABLE Reacties DROP PRIMARY KEY, ADD PRIMARY KEY (PostId, UserId, EmojiName); ` ` |
| | |
| | Postgres: ` ` ALTER TABLE reacties DROP CONSTRAINT reactions_pkey, ADD PRIMARY KEY (PostId, UserId, EmojiName); ` ` |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | De Channel Moderation Settings-functie wordt ondersteund op mobiele appversies v1.30 en hoger. In eerdere versies van de mobiele app, gebruikers die proberen om te posten of |
| | reageren op berichten zonder de juiste permissies zal een fout te zien.                                                                                                     |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Directe toegang tot het ` ` Props ` ` veld in de ` `model.Post ` ` ` structuur is gedeprecieerd. De beschikbare ` ` GetProps () ` ` en ` ` SetProps () ` ` ` methoden zouden nu moeten zijn |
| | gebruikt. Ook moet direct exemplaar van de ` `model.Post ` ` structuur worden vermeden ten gunste van de geleverde ` ` Clone () ` ` methode.                                             |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | SAML Setting "Use Verbeterde SAML Library (Beta)" was krachtig uitgeschakeld. Volg de instructies op |
| | https://docs.mattermost.com/deployment/sso-saml-before-you-begin.html voor het inschakelen van SAML met behulp van het functie-equivalent ` ` xmlsec1 ` ` programma.                        | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.21.0 | Honour belangrijkste waarde vervalt in KVCompareAndSet, KVCompareAndDelete en KVList. We verbeteren ook de verwerking van de plugin belangrijkste waarde race voorwaarden en verwijderde sleutels in |
| | Postgres.                                                                                                                                                        |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | SAML Setting "Use Verbeterde SAML Library (Beta)" was krachtig uitgeschakeld. Volg de instructies op |
| | https://docs.mattermost.com/deployment/sso-saml-before-you-begin.html voor het inschakelen van SAML met behulp van het functie-equivalent ` ` xmlsec1 ` ` programma.                        | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.20.0 | Elke ` voorverpakte plugin <https: //docs.mattermost.com/administration/plugins.html#pre-packaged-plugins> ` _ die niet is ingeschakeld in ` `config.json ` ` ` zal nee |
| | langere installatie automatisch, maar kan verder worden geïnstalleerd via de |
| | ` Plugin Marketplace <https: //docs.mattermost.com/administration/plugins.html#plugin-markplace> ` _. | 
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Booleaanse elementen uit interactieve dialoogvensters worden niet meer geserialiseerd als tekenreeksen. Terwijl we proberen te voorkomen dat het breken van wijzigingen, deze verandering noodzakelijk was om |
| | zowel de web-en mobiele apps om te werken met de booleaanse elementen geïntroduceerd met v5.16.                                                                            | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.19.0 | ` ` LockTeammateNameDisplay ` ` instelling werd verplaatst naar Enterprise Edition E20 omdat het ten onrechte beschikbaar was in Team Edition en Enterprise Edition E10.              | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.18.0 | Marking een post ongelezen van de mobiele app vereist v1.26 of later. Als u v5.18 gebruikt, maar mobiel is op v1.25 of eerder, markeert u een post ongelezen van webapp/desktop |
| | zal alleen worden weergegeven op mobiele de volgende keer dat de app lanceert of wordt gebracht op de voorgrond.                                                                 |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Het pad van de Go-module van ` ` mattermost-server ` ` is gewijzigd om te voldoen aan de versie van de Go-module versie. Ontwikkelaars met behulp van Go-modules met |
| | ` ` ` mattermost-server ` ` als een afhankelijkheid moet de module en importpaden veranderen naar ` ` github.com/mattermost/mattermost-server/v5 ` ` bij het upgraden van deze afhankelijkheid |
| | naar ` v5.18 `. Zie ` <https://blog.golang.org/v2-go-modules> ` __ voor meer informatie.                                                                             |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Verwijderde ` `Team.InviteId ` ` ` van de gerelateerde Websocket event en sanitized het op alle team API endpoints voor gebruikers zonder de toestemming.                      |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Verwijderde de mogelijkheid om het type van een kanaal te wijzigen met het API-eindpunt ` ` PUT /channels/ { channel_id } ` `. De nieuwe ` ` PUT /channels/ { channel_id } /privacy ' ` |
| | eindpunt moet worden gebruikt voor dat doel.                                                                                                                        | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.16.0 | Ondersteuning voor Internet Explorer (IE11) wordt verwijderd. Zie |
| | ` dit forum post <https://forum.mattermost.org/t/mattermost-is-dropping-support-for-internet-explorer-ie11-in-v5-16/7575> ` __ om meer te leren.                      |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | De ` Matte
rmeeste Desktop v4.3.0 <https://github.com/mattermost/desktop/blob/master/CHANGELOG.md> ` _ release bevat een wijziging van hoe desktop meldingen worden verzonden |
| | van niet-beveiligde URL's (http://). Organisaties die gebruikmaken van niet-beveiligde Matterendste Servers (http://) moeten bijwerken naar Mattermeeste Server-versies 5.16.0 +, 5.15.1, |
| | 5.14.4 of 5.9.5 (ESR) om door te gaan met het ontvangen van desktopmeldingen wanneer Mattermeeste Desktop v4.3.0 of hoger wordt gebruikt.                                                 | 
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Bij het inschakelen van ` Guest Accounts <https://docs.mattermost.com/deployment/guest-accounts.html> ` _, zijn alle gebruikers die de mogelijkheid hebben om gebruikers uit te nodigen in staat om |
| | nodigen gasten standaard uit. Systeembeheerders moeten deze machtiging voor elke rol verwijderen via ** Systeemconsole > Machtigingen * *.  In Mattermeeste Server |
| | versie 5.17, de System Admin zal de enige rol zijn om automatisch de uitnodiging gast toestemming te krijgen, maar de fix zal niet van toepassing zijn in 5.16 vanwege |
| | databasemigratieprocessen.                                                                                                                                    | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.14.0 | Webhooks worden nu alleen weergegeven als de gebruiker de maker van de webhook of systeembeheerder is.                                                             |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Met de update van Google + naar Google People moeten systeembeheerders ervoor zorgen dat de instelling ` `GoogleSettings.Scope ` ` config.json is ingesteld op ` ` profile email ` ` en |
| | ` ` UserAPIEndpoint ` ` instelling moet worden ingesteld op ` ` ` https: //people.googleapis.com/v1/people/me?personFields=names, emailAddresses, nicknames, metadata ` ` per |
| | ` bijgewerkte documentatie <https://docs.mattermost.com/deployment/sso-google.html> ` _. | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.12.0 | Als uw plugin de plugin API ` ` DeleteEphemeralMessage ` gebruikt, moet u deze bijwerken om een ' ` postId string ` ` parameter te accepteren.                                                |
| | Zie ` documentatie <https: //developers.mattermost.com/extend/plugins/server/reference/#API.DeleteEphemeralPost> ` _ voor meer informatie.                                 |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +                               
| | Image link en YouTube-previews worden niet afgebeeld tenzij ** System Console > Enable Link Previews * * is ingeschakeld. Controleer of uw Matterste-server is |
| | verbonden met het internet en heeft netwerktoegang tot de websites van waaruit de previews naar verwachting zullen verschijnen.                                                     |
| | ` Lees meer hier <https://forum.mattermost.org/t/link-previews-managed-server-side-in-v5-12-and-later/7712> ` _. | 
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | ` ` ExperimentalEnablePostMetadata ` ` instelling is verwijderd. Post-metagegevens, inclusief de post-dimensies, worden nu in de database opgeslagen om de schuifpositie te corrigeren en |
| | Schuif-sprongen uitschakelen als inhoud in een kanaal.                                                                                                            |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Toegevoegd de mogelijkheid om het beheer van teams/kanalen te handhaven met Group Sync. Als groepssynchronisatie is ingeschakeld, worden alle namen van Team-en Kanaal-beheerder gebruikt |
| | verloren bij upgrade. Het is raadzaam om voorafgaand aan de upgrade de beheerders van Team en Kanaal toe te voegen aan beheerspecifieke LDAP-groepen die overeenkomen met hun |
| | teams en kanalen. Na het upgraden moeten deze groepen worden gesynchroniseerd met de rol Team of Channel Admin.                                                 | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.11.0 | Als uw integratie ` ` Update.Props == nil ` ` gebruikt om ` ` Props ` ` te verwijderen, zal dit niet meer werken in 5.11 +. Gebruik in plaats daarvan ` ` Update.Props == { } ` ` om de eigenschappen te wissen. |
| | |
| | Deze wijziging is gemaakt omdat ` ` Update.Props == nil ` ` onbedoeld alle ` ` Props ` ` ` ` ` ` ` ` ` ` ` ` ` ` `, zoals het profiel afbeelding, in plaats van het behoud van hen.             | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.10.0 | ` ` SupportedTimezonesPath ` ` instelling in config.json en wijzigingen in tijdzones in de gebruikersinterface op basis van het ` timezones.json ` ` bestand is verwijderd. Dit is gemaakt om te ondersteunen |
| | ` opslaan van configuraties in de database <https: //docs.mattermost.com/administration/config-in-database.html#configuration-in-the-mattermeest-database> ` _. | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.9.0 | Als ` ` DisableLegacyMfa ` ` instelling in ` `config.json ` ` is ingesteld op ` ` true ` ` en ` multi-factor authenticatie <https://docs.mattermost.com/deployment/auth.html> ` _ is |
| | ingeschakeld, zorg ervoor dat uw gebruikers hebben een upgrade naar mobiele app versie 1.17 of later. Als dit niet het geval is, kunnen gebruikers met een MFA-functie niet worden aangemeld.      |
| | |
| | Als de instelling niet is gedefinieerd in het bestand ` `config.json ` `, wordt de instelling ` ` DisableLegacyMfa ` ` ingesteld op ` ` false ` ` standaard om ervoor te zorgen dat er geen wijzigingen worden aangebracht.        |
| | |
| | Wij adviseren ' ` DisableLegacyMfa ` ` to ` ` true ` ` aan te stellen voor extra beveiligingsverharding.                                                                         |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Het publieke IP van de Mattermeeste toepassingenserver wordt beschouwd als een gereserveerd IP voor extra beveiligingsverharding in de context van niet-vertrouwde externe verzoeken |
| | zoals Open Graph-metagegevens, webhooks of slash-opdrachten.                                                                                                        |
| | ` Zie de documentatie <https: //docs.mattermost.com/administration/config-settings.html-untrusted-internal-connections-to> ` _ voor aanvullende informatie.       | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.8.0 | De lokale afbeeldingsproxy is toegevoegd en afbeeldingen die worden afgebeeld binnen de client worden nu beïnvloed door de instelling ` ` AllowUntrustedInternalConnections ` `.              |
| | ` Zie documentatie <https: //docs.mattermost.com/administration/image-proxy.html#local-image-proxy> ` _ voor meer informatie als u problemen hebt met het laden van afbeeldingen.        | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.6.0 | Built-in WebRTC is verwijderd. Zie ` hier voor meer informatie <https: //forum.mattermost.org/t/built-in-webrtc-video-and-audio-aanroepen-removed-in-v5-6-| 
| | in-favor-of-open-source-plugins/5998 > ` __. |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Als ` ` EnablePublicChannelsMaterialization ` ` instelling in ` `config.json ` ` is ingesteld op ` ` false ` `, kan een offline migratie voorafgaand aan de upgrade vereist zijn om te synchroniseren |
| | de gematerialiseerde tabel voor openbare kanalen om de prestaties van het kanaal te vergroten in de kanaalswitcher (CTRL/CMD + K), kanaal autocomplete (~), en elders |
| | in de gebruikersinterface. Gebruik de volgende stappen: |
| | |
| | 1. Sluit de toepassingenservers af.                                                                                                                           |
| | 2. Verbinden met uw Mattermeeste database.                                                                                                                          |
| | 3. Voer de volgende query's uit: |
| | |
| | .. code-block :: SQL |
| | |
| | DELETE FROM PublicChannels; |
| | INSERT INTO PublicChannels |
| | (Id, DeleteAt, TeamId, DisplayName, Name, Header, Purpose) |
| | SELECT |
| | c.Id, c.DeleteAt, c.TeamId, c.DisplayName, c.Name, c.Header, c. Purpose |
| | FROM |
| | Kanalen c
|
| | WHERE |
| | c. Type = 'O '; |
| | |
| | De bovenstaande query's herbouwen de opgebouwde ` ` PublicChannels ` ` ` tabel zonder de gezaghebbende ` ` Channels ` ` tabel te wijzigen.                                      |
| | |
| | Merk op dat deze migratie niet vereist is als de experimentele ' ` PublicChannels ` ` functie nooit is uitgeschakeld. Deze functie is gestart in Matterbest v5.4 met een |
| | tijdelijke vlag om uit te schakelen als er een probleem ontstaat, maar er is niets gevraagd. Als u deze instelling niet hebt gewijzigd, hoeft u deze migratie niet uit te voeren.  | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.4.0 | Mattermeest mobiele app versie 1.13+ is vereist. Uploads van bestanden mislukken op eerdere versies van mobiele apps.                                                          |                                        
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | In bepaalde upgradescenario's de nieuwe ** Laat teambeheerders andere berichten bewerken * * instelling onder ** General** dan ** Gebruikers en teams * * kunnen zijn |
| | ingesteld op ** True** terwijl de Mattermeest standaard in 5.1 en eerder en met nieuwe 5.4+ installaties is ** False**. | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.3.0 | Deze servers met Elasticsearch ingeschakeld zullen merken dat het zoeken naar hashtags hoofdlettergevoelig is.                                                                      | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.2.0 | Deze servers upgraden van v4.1-v4.4 rechtstreeks naar v5.2 of hoger en hebben Jira ingeschakeld om de Jira-plugin opnieuw in te schakelen na een upgrade.                | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.1.0 | ` ` ` matterbest export ` ` CLI opdracht wordt hernoemd naar ` ` matterbest export schedule ` `. Zorg ervoor dat u uw scripts bijwerkt als u deze opdracht gebruikt.                        | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v5.0.0 | Alle API v3-eindpunten worden verwijderd. ` Zie de documentatie <https: //api.mattermost.com/#tag/APIv3-Deprecation> ` __ voor informatie over het migreren van uw integraties naar API v4. |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | ` ` platform ` ` binary wordt hernoemd naar ` ` matterbest ` ` voor een duidelijker installatie-en upgrade-ervaring. Je moet je ` ` systemd ` ` servicebestand wijzen op de nieuwe |
| | ` ` ` matterbest ` ` binair. Alle opdrachtregeltools, met inbegrip van de tools voor het laden van bulk en ontwikkelaars, worden ook hernoemd van ` ` platform ` ` naar ` ` matterbest ` `. |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Een Mattermeest gebruikersinstelling voor het configureren van de duur van de bureaubladmelding in ** Accountinstellingen > Meldingen > Bureaublad berichten * * wordt verwijderd.                 |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Slash-opdrachten die zijn geconfigureerd voor het ontvangen van een GET-opdracht, hebben de payload die wordt gecodeerd in de queryreeks, in plaats van deze in de lopende tekst van de opdracht te ontvangen, |
| | consistent met standaard HTTP-verzoeken. Hoewel het onwaarschijnlijk is, kan dit aangepaste slash-opdrachten breken die GET-opdrachten onjuist gebruiken.                             |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Een nieuwe ` `config.json ` ` instelling aan whitelist soorten protocollen voor auto-linking zal worden toegevoegd.                                                                    |
| | Als u afhankelijk bent van aangepaste protocollen auto-linking in Matterbest, whitelist ze in ` `config.json ` ` vóór de upgrade.                                                  |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Een nieuwe ` `config.json ` ` instelling om de ' permanente APIv4 delete teamparameter | uit te schakelen |
| | <https: //api.mattermost.com/#tag/teams%2Fpaths%2F ~ 1teams ~ 1%7Bteam_id%7D%2Fput> ` __ wordt toegevoegd. De instelling is standaard uitgeschakeld voor alle nieuwe en bestaande |
| | installeert, behalve die op GitLab Omnibus. Als u antwoordt met de parameter APIv4, schakelt u de instelling in ' `config.json ` ` in voordat u een upgrade uitvoert.                  |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Een ongebruikt ` ` ExtraUpdateAt ` ` veld wordt verwijderd uit het kanaal modaal.                                                                                        |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Deze release bevat ondersteuning voor berichten die langer zijn dan de standaardwaarde van 4000 tekens, maar vereist mogelijk een handmatige databasemigratie. Deze migratie is |
| | volledig optioneel, en hoeft alleen te worden gedaan als u wilt plaatsen berichten tot 16383 tekens. Voor veel installaties is geen migratie vereist, of |
| | de oude limiet blijft voldoende.                                                                                                                                |
| | |
| | Om uw huidige postlimiet na het upgraden naar 5.0.0 te controleren, zoekt u een logboekbericht bij het opstarten: |
| | |
| | [ 2018/03/27 09:08:00 EDT] [ INFO] Post.Message ondersteunt maximaal 16383 tekens (65535 bytes) |
| | |
| | Vanaf 5.0.0 is de maximale postberichtgrootte 16383 (multi-byte) tekens. Als uw logboeken een aantal minder dan deze limiet weergeven en u wilt langer inschakelen |
| | post berichten, u moet handmatig migreren van uw database zoals hieronder beschreven. Deze migratie kan traag zijn voor grotere ` ` Posts ` ` tabellen, dus het is het beste om |
| | schema deze upgrade tijdens daluren.                                                                                                                     |
| | |
| | Om een MySQL-database te migreren, maakt u verbinding met uw database en voert u het volgende uit: |
| | |
| | ALTER TABLE Posts MODIFY COLUMN Message TEXT; |
| | |
| | Om een PostgreSQL-database te migreren, maakt u verbinding met uw database en voert u de volgende opdracht uit: |
| | |
| | ALTER TABLE Posts ALTER COLUMN Message TYPE VARCHAR (65535); |
| | |
| | Start de meeste instances opnieuw op.                                                                                                                               |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Deployments op Enterprise E20 moeten ' ` RunJobs ` ` in de ` `config.json ` ` inschakelen en toestaan dat de toestemmingen migratie voltooid zijn voordat ` Team |
| | Schema's negeren <https://docs.mattermost.com/deployment/advanced-permissions.html> ` __. | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v4.10.0 | Oude e-mailuitnodiginglinks werken niet meer als gevolg van een bug-fix waarbij teams opnieuw kunnen worden samengevoegd via de link.                                                     |
| | Team uitnodigde links kopiëren vanuit het dialoogvenster Team Uitnodigen Link, wachtwoord reset links en e-mail verificatie links worden niet beïnvloed en zijn nog steeds geldig.               |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Server logs geschreven naar ** System Console > Logboeken * * en naar het ` `mattermost.log ` ` bestand dat is opgegeven in ** System Console > Logging > File Log Directory * * |
| | Gebruik nu JSON-indeling. Als u een tool hebt gebouwd waarmee de serverlogboeken worden ontleed en naar een extern systeem wordt verzonden, moet u ervoor zorgen dat deze de JSON-indeling ondersteunt.       |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Teampictogrammen met transparantie worden gevuld met een witte achtergrond in de teamflankbalk.                                                                         |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Deze servers met SAML-verificatie moeten tijdens niet-piekuren worden geüpgraded. SAML-e-mailadressen worden gemigreerd naar kleine letters om aanmeldingsproblemen te voorkomen, |
| | die kan leiden tot meer dan de gebruikelijke upgrade tijd.                                                                                                            |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Als u PostgreSQL-database gebruikt en het wachtwoord speciale tekens bevat (bijvoorbeeld ` ` [] ` `), ontsnap u deze in uw wachtwoord, bijvoorbeeld xxx [] xxx is xxx%5B%5Dxxx.    | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v4.9.0 | Om het productiegebruik van Matterbest te verbeteren met Docker, wordt de Docker-afbeelding nu uitgevoerd als niet-root gebruiker en luistert naar poort 8000. Lees de |
| | ` upgrade instructies <https: //github.com/mattermost/mattermost-docker#upgrading-mattermost-49 > ` __ voor belangrijke wijzigingen in bestaande installaties.           |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Er zijn verschillende configuratie-instellingen gemigreerd naar rollen in de database en het wijzigen van de waarden voor ` `config.json ` ` ` duurt niet meer. Deze machtigingen |
| | kan nog steeds worden gewijzigd door de respectievelijke instellingen van de systeemconsole zoals voorheen. De instellingen ` `config.json ` ` instellingen zijn: |
| |
|
| | ` ` RestrictPublicChannelManagement ` `, |
| | ` ` RestrictPrivateChannelManagement ` ` `, |
| | ` ` RestrictPublicChannelCreation ` `, |
| | ` ` RestrictPrivateChannelCreation ` `, |
| | ` ` RestrictPublicChannelDeletion ` `, |
| | ` ` RestrictPrivateChannelDeletion ` `, |
| | ` ` RestrictPrivateChannelManageMembers ` `, |
| | ` ` EnableTeamCreation ` `, |
| | ` ` EnableOnlyAdminIntegrations ` `, |
| | ` ` RestrictPostDelete ` `, |
| | ` ` AllowEditPost ` `, |
| | ` ` RestrictTeamInvite ` `, |
| | ` ` RestrictCustomEmojiCreation ` `. |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Het gedrag van de instelling ` `config.json ` ` ` PostEditTimeLimit ` ` is bijgewerkt om de migratie naar een op rollen gebaseerd machtigingssysteem te kunnen ontvangen.               |
| | Wanneer post bewerken is toegestaan, stelt u ` ` "PostEditTimeLimit": -1 ` ` toe om het bewerken op elk gewenst moment, of stel ` ` "PostEditTimeLimit" ` ` toe aan een positief geheel getal om te beperken | 
| | tijd in seconden bewerken. Als post bewerken uitgeschakeld is, is deze instelling niet van toepassing.                                                                               |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Als u gebruik laten maken van Let's Encrypt zonder een proxyserver, zal de server niet beginnen met een foutbericht tenzij de ` Forward80To443 |
| | <https: //docs.mattermost.com/administration/config-settings.html#forward-port-80-naar-443 > ` __ ` config.json ` ` instelling is ingesteld op ` ` true ` `. |
| | |
| | Als de poort 80 wordt doorgestuurd naar 443, wordt de server niet gestart met een foutbericht, tenzij het ' ListenAddress |
| | <https: //docs.mattermost.com/administration/config-settings.html#listen-address> ` __ ``config.json ` ` instelling is ingesteld om te luisteren op poort 443.                        | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v4.6.2 | Als u gebruikmaakt van Let's Encrypt zonder een proxyserver, stuur poort 80 door via een firewall, met de ` Forward80To443 |
| | <https: //docs.mattermost.com/administration/config-settings.html#forward-port-80-to-443 > ` __ ` config.json ` ` instelling ingesteld op ` ` true ` ` om de Let's te voltooien |
| | Versleutelde certificering.                                                                                                                                           | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v4.4.0 | Samengestelde database-indexen zijn toegevoegd aan de tabel ` ` Posts ` `. Dit kan leiden tot langere tijden voor servers met meer dan 1 miljoen berichten.               |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | LDAP-synchronisatie is nu afhankelijk van e-mail. Zorg ervoor dat alle gebruikers op uw AD/LDAP-server een e-mailadres hebben of dat hun account in Matterbest wordt gedeactiveerd.             | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v4.2.0 | Matterbest behandelt nu meerdere inhoudtypen voor integraties, inclusief het contenttype van platte tekst. Als uw integratie plotseling de gegevens van de JSON-payload drukt |
| | in plaats van het gegenereerde bericht te genereren, moet u ervoor zorgen dat uw integratie het contenttype ` ` application/json ` retourneert om eerder gedrag te behouden.           |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Standaard worden door de gebruiker geleverde URL's, zoals die welke worden gebruikt voor metagegevens van Open Graph, webhooks of slash, niet meer toegestaan om verbinding te maken met gereserveerde IP |
| | adressen met inbegrip van loopback of link-lokale adressen die worden gebruikt voor interne netwerken.                                                                                 |
| | |
| | Deze wijziging kan leiden tot persoonlijke integraties om te breken in testomgevingen, die kunnen verwijzen naar een URL zoals http://127.0.0.1:1021/my-command.                  |
| | |
| | Als u persoonlijke integraties naar dergelijke URL's wijst, mag u dergelijke domeinen, IP-adressen of CIDR-notaties via de |
| | ` AllowedUntrustedInternalConnections config setting <https: //docs.mattermost.com/administration/config-settings.html#allow-untrusted-internal-connections-to> ` __ |
| | in uw lokale omgeving. Hoewel het niet wordt aanbevolen, kunt u ook de adressen in uw productieomgeving op de witte lijst zetten. Zie |
| | ` documentatie voor meer informatie over <https: //docs.mattermost.com/administration/config-settings.html#allow-niet-vertrouwde-interne-verbindingen-to> ` __. |
| | |
| | Push notification, OAuth 2.0 en WebRTC server URL's worden vertrouwd en niet beïnvloed door deze instelling.                                                                |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Uploaded bestandsbijlagen zijn nu gegroepeerd op dag en opgeslagen in ` ` /data/<date-of-upload-as-YYYYMMDD>/teams/... ` ` van uw bestandssysteem.                     |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | Matterbest `/platform ` ` repo is afgescheiden van ` ` /mattermost-webapp ` ` en ` ` /mattermost-server ` ` `. Dit kan van invloed zijn op u als u een eigen vork van de |
| | ` ` /platform ` ` repo. ` Meer details hier <https://forum.mattermost.org/t/mattermost-separating-platform-into-two-repositories-on-september-6th/3708> ` __. | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v4.0.0 | (Alleen hoge beschikbaarheid) |
| | |
| | U moet handmatig nieuwe items toevoegen aan het gedeelte ` ` ClusterSettings ` ` van uw bestaande ` `config.json ` ` `. |
| | Zie de sectie *Upgraden naar versie 4.0 en hoger * van :doc: ` ../deployment/cluster ` voor meer informatie.                                                                | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v3.9.0 | Oude e-mailuitnokoppelingen, wachtwoordresetlinks en e-mailverificatielinks werken niet meer vanwege een beveiligingswijziging.                                     |
| | Team uitnodigen links kopiëren van het dialoogvenster Team Invite Link worden niet beïnvloed en zijn nog steeds geldig.                                                                  | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v3.8.0 | Een wijziging is vereist in de proxyconfiguratie.                                                                                                                 |
| | Als u NGINX gebruikt: |
| | 1. Open het NGINX-configuratiebestand als root. Het bestand is meestal ` ` /etc/nginx/sites-available/matterbest ` ` maar kan anders zijn op je systeem.             |
| | 2. Zoek de regel: ` ` locatie /api/v3/users/websocket { ` ` |
| | 3. Vervang de regel door ` ` location ~ /api/v [ 0-9] +/(users/) ?websocket$ { ` ` |
| | Als u een andere proxy gebruikt dan NGINX, moet u de overeenkomstige wijziging aanbrengen in de configuratie van die proxy.                                                             |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | U moet de instellingen in de systeemconsole controleren vanwege een wijziging in de beveiliging.                                                                              |
| | |
| | 1. Ga naar het algemene gedeelte van de systeemconsole |
| | 2. Klik op ** Logging** |
| | 3. Zorg ervoor dat het veld ** File Log Directory * * leeg is of alleen een directorypad heeft. Het mag geen bestandsnaam hebben als onderdeel van het pad.              |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | De compatibiliteit met de oude CLI-tool is verwijderd. Als u scripts hebt die afhankelijk zijn van de oude CLI, moeten ze worden gereviseerd voor gebruik van de |
| | ` new CLI <../administration/command-line-tools.html> ` __. | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v3.6.0 | Het maximumaantal bestanden bijwerken dat kan worden geopend.                                                                                                             |
| | |
| | Op RHEL6 en Ubuntu 14.04: |
| |-Controleer of de regel ` ` limit nofile 50000 50000 ` ` is opgenomen in het ` `/etc/init/mattermost.conf ` ` bestand.                                                     |
| | Op RHEL7 en Ubuntu 16.04: |
| |-Controleer of de regel ` ` LimitNOFILE = 49152 ` ` is opgenomen in het ` /etc/systemd/system/mattermost.service ` ` bestand.                                               |
| + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| | (Alleen Enterprise) |
| | |
| | Vorige ` `config.json ` ` ` waarden voor het beperken van Public en Private channel management zullen gebruikt worden als de standaardwaarden voor nieuwe instellingen voor het beperken |
| | Openbare en private kanalen maken en verwijderen.                                                                                                                | + ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
| v3.4.0 | Als openbare koppelingen zijn ingeschakeld, zijn bestaande openbare links niet meer geldig. Dit komt doordat bestaande openbare links in eerdere versies niet ongeldig zijn gemaakt |
| | toen de Public Link Salt opnieuw werd gegenereerd. U moet elke plaats waar u deze links hebt gepubliceerd bijwerken. |
+ ---------------------------------------------------- + ------------------------------------------------------------------------------------------------------------------------------------------------------------------ +
