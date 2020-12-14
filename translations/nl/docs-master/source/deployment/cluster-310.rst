Hoge-beschikbaarheidscluster (v3.10 en eerder)
== == == == == == == == == == == == == == == == == == == == == == =

*Beschikbaar in Enterprise Edition E20 .* .. Opmerking:

  Dit document is van toepassing op Mattermeest Server versie 3.10 en eerder. Voor de meest recente versie, zie :doc: ` cluster `.

Een cluster met hoge beschikbaarheid maakt het mogelijk dat een Matterbest-systeem service onderhoudt tijdens storingen en hardwarestoringen door het gebruik van redundante infrastructuur.

Hoge beschikbaarheid in Mattermeeste bestaat uit het uitvoeren van redundante Mattermeeste toepassingenservers, redundante databaseservers en redundante belastingsverdelers. Het uitvallen van een van deze componenten onderbrekt de werking van het systeem niet. .. Inhoud:
  :backlinks: boven: lokaal:

Eisen voor continubedrijf
-------------------------------------

Om te allen tijde ononderbroken gebruik mogelijk te maken, ook tijdens serverupdates en serverupgrades, moet u ervoor zorgen dat de redundante componenten correct zijn gelijmd en dat u de juiste volgorde volgt voor het bijwerken van elk van de componenten van het systeem.

Redundantie op verwachte schaal Bij een storing van één component moeten de overige toepassingenservers, databaseservers en werklastverdelers worden gesorteerd en geconfigureerd voor het uitvoeren van de volledige belasting van het systeem. Als niet aan deze eis wordt voldaan, kan een storing van één component leiden tot een overbelasting van de resterende componenten, waardoor een volledige systeemstoring wordt veroorzaakt.

Updatesequentie voor continue bewerking U kunt de meeste configuratiewijzigingen toepassen en beveiligings-updates voor de release van de punt vrijgeven zonder de service te onderbreken, op voorwaarde dat u de systeemcomponenten in de juiste volgorde bijwerkt. Raadpleeg de 'Upgradehandleiding' ' voor instructies over hoe u dit doet.

  ** Exception:** Wijzigingen in de configuratie-instellingen waarvoor een herstart van de server vereist is, en upgrades van de serverversie die een wijziging van het databaseschema vereisen, vereisen een korte periode van downtime. De uitvaltijd voor een herstart van de server is ongeveer 5 seconden en voor een update van een databaseschema kan de uitvaltijd maximaal 30 seconden bedragen.

Implementatiehandleiding
----------------

Implementatiegids voor het instellen en onderhouden van hoge beschikbaarheid op uw Mattermeeste servers.

Initiële installatiehandleiding voor hoge beschikbaarheid
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Om te zorgen dat uw instance en configuratie compatibel zijn met hoge beschikbaarheid, controleer dan de sectie ` Configuratie en compatibiliteit '. .. Opmerking:
  Maak voor het configureren van hoge beschikbaarheid een backup van uw Mattermeeste database-en bestandsopslaglocaties. Voor meer informatie over het maken van backups raadpleegt u :doc: ` ../administration/backup `.

1. Volg onze :doc: ` ../administration/upgrade ` om uw Matterendste server te upgraden naar v3.3 of later.
2. Stel een nieuwe Matterigste server in met v3.3 of een latere versie van onze ** Install Guides * *. Deze server moet een identieke kopie van het configuratiebestand gebruiken, ``config.json ` `. Controleer of de servers functioneren door elke onafhankelijke server te raken via zijn besloten IP-adres.
3. Wijzig de ` `config.json ` ` ` bestanden op beide servers om de ` ` ClusterSettings ` ` toe te voegen zoals beschreven in :ref: ` high availability `.
4. Ve
De configuratiebestanden zijn identiek aan beide servers en start elke machine opnieuw in de cluster.
5. Wijzig uw NGINX-configuratie zodat deze proxy's voor beide servers. Meer informatie hierover vindt u in 'Proxyserverconfiguratie' _.
6. Open ** System Console > Advanced > High Availability * * in eerdere versies of ** System Console * * > ** Environment** > ** High Availability * * in versies na 5.12 om te controleren of alle machines in de cluster communiceren zoals verwacht met groene statusindicators. Als dit niet het geval is, moet u de logboekbestanden voor eventuele aanvullende informatie onderzoeken.

Een server toevoegen aan het cluster ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ out

1. Backup maken van uw Mattermeeste database en de bestandsopslaglocatie. Voor meer informatie over het maken van backups raadpleegt u :doc: ` ../administration/backup `.
2. Stel een nieuwe Matterigste server in. Deze server moet een identieke kopie van het configuratiebestand gebruiken, ``config.json ` `. Controleer of de server functioneert door het persoonlijk IP-adres op te slaan.
3. Wijzig de ` `config.json ` ` bestanden op alle servers met de ` ` ClusterSettings ` ` zoals beschreven in :ref: ` high availability `. Zorg ervoor dat de nieuwe server URL wordt toegevoegd aan ` ` InterNodeUrls ` `.
4. Controleer of de configuratiebestanden identiek zijn op alle servers en start vervolgens elke machine in de cluster opnieuw in met 10 of meer seconden tussen elke herstart.
5. Wijzig de NGINX-instelling om de nieuwe server toe te voegen. Voor meer informatie hierover raadpleegt u 'Proxyserverconfiguratie' _.
6. Open de ** System Console > Advanced > High Availability * * in eerdere versies of ** System Console * * > ** Environment** > ** High Availability * * in versies na 5.12 om te controleren of alle machines in de cluster communiceren zoals verwacht met groene statusindicators. Als dit niet het geval is, moet u de logboekbestanden voor eventuele aanvullende informatie onderzoeken.

Bezig met het verwijderen van een server uit de cluster ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ out

1. Backup maken van uw Mattermeeste database en de bestandsopslaglocatie. Voor meer informatie over het maken van backups raadpleegt u :doc: ` ../administration/backup `.
2. Wijzig de NGINX-instelling om de server te verwijderen. Voor meer informatie hierover raadpleegt u 'Proxyserverconfiguratie' _.
3. Op alle servers die actief blijven in de cluster, wijzigt u de ` ` ClusterSettings ` ` in ` `config.json ` ` om de server te verwijderen uit ` ` InterNodeUrls ` `
4. Controleer of de configuratiebestanden identiek zijn op alle servers en start vervolgens elke machine in de cluster opnieuw in met 10 of meer seconden tussen elke herstart.
5. Open de ** System Console > Advanced > High Availability * * in eerdere versies of ** System Console * * > ** Environment** > ** High Availability * * in versies na 5.12 om te controleren of alle machines in de cluster communiceren zoals verwacht met groene statusindicators. Als dit niet het geval is, moet u de logboekbestanden voor eventuele aanvullende informatie onderzoeken.

Configuratie en compatibiliteit
------------------------------- Details over het configureren van uw systeem voor hoge beschikbaarheid.

Mattermeeste serverconfiguratie
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Vragen

Configuratie-instellingen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Hoge beschikbaarheid wordt geconfigureerd in het gedeelte ` ` ClusterSettings ` ` van ` `config.json ` ` en de instellingen zijn zichtbaar in de systeemconsole. Als de hoge beschikbaarheid is ingeschakeld, is de systeemconsole ingesteld op de modus Alleen lezen om ervoor te zorgen dat alle ` `config.json ` ` ` bestanden op de Mattermeeste servers identiek zijn. .. code-blok :: geen

  "Clusterinstellingen": {
        "Enable": false, "InterNodeListenAddress": ": 8075", "InterNodeUrls": []
  }

Voor meer informatie over deze instellingen, zie :ref: ` high availability `.

Stand ^ ^ ^ ^ ^ ^

De Mattermeeste Server is ontworpen om zeer weinig staat te hebben voor horizontale schaling. De items in de staat die worden beschouwd voor het schalen van Matterbest zijn hieronder opgesomd:

-In de cache van de geheugensessie voor snelle validatie en kanaaltoegang,
-In het geheugen online/offline cache voor snelle reactie,
-Systeemconfiguratiebestand dat in het geheugen wordt geladen en opgeslagen,
-WebSocket verbindingen van clients gebruikt om berichten te verzenden.

Wanneer de Mattermeeste Server is geconfigureerd voor hoge beschikbaarheid, gebruiken de servers een communicatieprotocol tussen knooppunten op een ander luisteradres om de status te synchroniseren. Wanneer een status wordt gewijzigd, wordt deze teruggeschreven naar de database en wordt er een bericht van een knooppunt verzonden om de andere servers van de statuswijziging op de hoogte te stellen. De werkelijke status van de items kan altijd worden gelezen uit de database. Matterit gebruikt ook inter-node communicatie om WebSocket berichten naar de andere servers in de cluster te sturen voor real-time berichten zoals "[ Gebruiker X] is typen."


Proxyserverconfiguratie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De proxyserver stelt de cluster van Mattermeeste servers bloot aan de buitenwereld. De Mattermeeste servers zijn ontworpen voor gebruik met een proxy server zoals NGINX, een hardware load balancer, of een cloud-service zoals Amazon Elastic Load Balancer.

Als u de server wilt bewaken met een health check, kunt u ` ` http://10.10.10.2/api/v3/general/ping ` ` gebruiken en de respons voor ` ` Status 200 ` ` controleren, wat aangeeft dat het succes is. Gebruik deze route voor het controleren van de status van de server * in-service * of * out-of-service *.

Hieronder vindt u een voorbeeldconfiguratie voor NGINX. Er wordt van uitgegaan dat u twee Mattermeeste servers hebt die worden uitgevoerd op persoonlijke IP-adressen van ` ` 10.10.10.2 ` ` en ` ` 10.10.10.4 ` `.


... code-blok :: geen

    upstream-backend {
            server 10.10.10.2:8065; server 10.10.10.4:8065;
      }

      server {
          server_name mattermost.example.com;

          locatie ~ /api/v [ 0-9] +/(users/) ?websocket$ {
                proxy_set_header Upgrade $http_upgrade; proxy_set_header Connection "upgrade"; client_max_body_size 50M; proxy_set_header Host $http_host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Doorgezonden-Voor $proxy_add_x_forwarded_for; proxy_set_header X-Doorgezonden-Proto $scheme;
                proxy_set_header X-Frame-Options SAMEORIGIN;
                proxy_buffers 256 16k; proxy_buffer_grootte 16k; proxy_read_timeout 600s; proxy_pass http://backend; }
locatie/{
                client_max_body_size 50M; proxy_set_header Upgrade $http_upgrade; proxy_set_header Connection "upgrade"; proxy_set_header Host $http_host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Doorgezonden-Voor $proxy_add_x_forwarded_for; proxy_set_header X-Doorgezonden-Proto $scheme;
                proxy_set_header X-Frame-Options SAMEORIGIN;
                proxy_pass http://backend;
          }
    }


U kunt meerdere proxyservers gebruiken om één enkel punt van storing te beperken, maar dat valt buiten het bereik van deze documentatie.

Bestandsopslagconfiguratie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ Opmerking:
  1. De opslag van bestanden wordt verondersteld te worden gedeeld tussen alle machines die gebruik maken van services zoals NAS of Amazon S3.
  2. Als ` ` "DriverName": "local" ` ` wordt gebruikt dan de directory op ` ` "FileSettings": ` ` ` ` ` "Directory": "./data/" ` ` wordt verwacht dat een NAS-locatie wordt toegewezen als een lokale directory, anders zal hoge beschikbaarheid niet correct functioneren en kan de bestandsopslag beschadigd raken.
  3. Als u gebruik maakt van Amazon S3 of Minio voor de opslag van bestanden dan is er geen andere configuratie vereist.

Als u de functie Compliance Reports gebruikt in Enterprise Edition E20, moet u de ` ` ComplianceSettings ' (ComplianceSettings) configureren: ` ` ` ` "Directory": "./data/", ` ` om te delen tussen alle machines of de rapporten zullen alleen beschikbaar zijn via de System Console op de lokale Matterendste server.

Migreren naar NAS of S3 vanuit lokale opslag valt buiten het bereik van dit document.

Databaseconfiguratie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Gebruik de functie voor het lezen van replica's om de database te schalen. De Mattermeeste server kan worden ingesteld voor gebruik van een "master" database en meerdere lees replica databases. Mattermeeste distribueert opdrachten voor alle databases en verzendt schrijfopdrachten naar de masterdatabase en deze wijzigingen worden vervolgens verzonden om de lees-replica's bij te werken.

Bij grote implementaties kunt u overwegen de zoekreplica te gebruiken om zoekquery's op een of meer databaseservers te isoleren. Een zoekreplica is vergelijkbaar met een leesreplica, maar wordt alleen gebruikt voor het afhandelen van zoekopdrachten.

Formaatdatabases ` ` ` ` ` ` ` ` ` ` ` ` ` ` `

Voor informatie over het bepalen van de grootte van databaseservers raadpleegt u :ref: ` hardware-sizing-for-enterprise `.

In een master/slave-omgeving, zorg ervoor dat de grootte van de slaaf machine om 100% van de lading in het geval dat de master machine gaat naar beneden en je moet falen over.

Implementatie Van Een Multi-databaseconfiguratie ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` `

Ga als volgt te werk om een Matterigste server met meerdere databases te configureren:

1. Werk de instelling ` ` DataSource ` ` in ` `config.json ` ` bij met een verbindingsreeks naar de hoofddatabaseserver. De verbindingsreeks is gebaseerd op het databasetype dat is ingesteld in ` ` DriverName ` `, ` ` postgres ` ` ` of ` ` mysql ` `.
2. Werk de instelling ` ` DataSourceReplicas ` ` in ` `config.json ` ` bij met een reeks verbindingsreeksen naar uw database lees replicaservers in de indeling ` ` [ "readreplica1", "readreplica2"] ` `. Elke verbinding moet ook compatibel zijn met de ` ` DriverName ` ` instelling.

De nieuwe instellingen kunnen worden toegepast door de server te stoppen en te starten, of door de configuratie-instellingen te laden zoals beschreven in de volgende sectie.

Na het laden worden databaseschrijfopdrachten naar de masterdatabase gezonden en worden de leesopdrachten verdeeld over de andere databases in de lijst.

Een configuratie met meerdere databases laden op een Active Server ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` `

Nadat een configuratie met meerdere databases is gedefinieerd in ` `config.json ` `, kan de volgende procedure worden gebruikt om de instellingen toe te passen zonder de Matterigste server af te sluiten:

1. Ga naar ** System Console > Configuratie * * en klik op * Configuratie herladen van schijf * * om de configuratie-instellingen voor de Mattermeeste server opnieuw te laden vanuit ` `config.json ` `.
2. Ga naar ** System Console > Database * * en klik op ** Recycle Database Connections * * om bestaande databaseverbindingen te maken en nieuwe verbindingen in te stellen in de multi-database configuratie.

Terwijl de verbindingsinstellingen aan het veranderen zijn, kan er een kort moment zijn wanneer de schrijfbewerkingen naar de masterdatabase mislukken. Het proces wacht totdat alle bestaande verbindingen zijn voltooid en start nieuwe opdrachten met de nieuwe verbindingen. Eindgebruikers die berichten proberen te verzenden terwijl de switch gebeurt, hebben dezelfde ervaring als de verbinding met de Mattertiste server wordt verbroken.

Handmatige failover voor masterdatabase ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` `

Als het nodig is om over te schakelen van de huidige hoofddatabase -- bijvoorbeeld, als het uit de schijfruimte raakt, of als er onderhoud updates nodig zijn, of om andere redenen -- dan kan de Mattermeeste server een van de gelezen replica's gebruiken als een masterdatabase door ` ` DataSource ` ` te updaten in ` `config.json ` `.

De instellingen toepassen zonder de Matterendste server af te sluiten:

1. Ga naar ** System Console > Configuratie * * in eerdere versies of ** Systeemconsole * * > ** Environment** > ** Web Server * * in versies na 5.12 en klik op ** Reload Configuration from Disk * * om de configuratie-instellingen voor de Mattermeeste server opnieuw te laden vanuit ` `config.json ` `.
2. Ga naar ** System Console > Database * * in eerdere versies of ** Systeemconsole * * > ** Environment** > ** Database** in versies na 5.12 en klik ** Recycle Database Connections * * om bestaande databaseverbindingen af te sluiten en nieuwe verbindingen in te stellen in de configuratie met meerdere databases.

Terwijl de verbindingsinstellingen aan het veranderen zijn, kan er een kort moment zijn wanneer de schrijfbewerkingen naar de masterdatabase mislukken. Het proces wacht totdat alle bestaande verbindingen zijn voltooid en start nieuwe opdrachten met de nieuwe verbindingen. Eindgebruikers die berichten proberen te verzenden terwijl de switch plaatsvindt, kunnen dezelfde ervaring hebben als de verbinding met de Mattertiste server wordt verbroken.

Transparante Failover ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` `

De database kan worden geconfigureerd voor hoge beschikbaarheid en transparante failover maken gebruik van de bestaande databasetechnologieën. Wij adviseren MySQL Clustering, Postgres Clustering, of Amazon Aurora. Transparante failover voor databases valt buiten het bereik van deze documentatie.

Upgradehandleiding
-------------

Een update is een incrementele wijziging in de Mattermeeste server die bugs of prestatieproblemen vaststelt. Een upgrade voegt nieuwe of verbeterde functionaliteit toe aan de server.

Wijzigingen In De Configuratie Tijdens Het Continu Werken Bijwerken
~ ~ ~ ~ > ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~

Een onderbreking van de service is niet vereist voor de meeste configuratie-updates. Zie ` Server Upgrades That Require Service Onderbreking ` _ voor een lijst van configuratie-updates die een onderbreking van de dienst vereisen.

U kunt updates aanbrengen gedurende een periode van lage belasting, maar als uw HA-cluster correct is ingesteld, kunt u dat op elk gewenst moment doen. Het systeem uitvaltijd is kort en hangt af van het aantal Mattermeeste servers in uw cluster. Merk op dat u de machines niet opnieuw start, alleen de Mattermeeste servertoepassingen. Een Mattermeeste server start over het algemeen ongeveer 5 seconden.

1. Maak een backup van het bestaande ` `config.json ` ` bestand.
2. Om een van de meest overeenkomende servers te maken, wordt de configuratie gewijzigd in ` `config.json ` ` en slaat u het bestand op. Het bestand nog niet opnieuw laden.
3. Kopieer het ` `config.json ` ` ` bestand naar de andere servers.
4. Sluit Matterbest af op alle maar één server.
5. Herlaad het configuratiebestand op de server die nog actief is. Ga naar ** System Console > Configuratie * * in eerdere versies of ** Systeemconsole * * > ** Omgeving ** > ** Webserver * * in versies na 5.12 en klik op ** Reload Configuration from Disk * *
6. Start de andere servers.

Serverversie Bijwerken Terwijl Het Continu Wordt Uitgevoerd
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Er is geen service-onderbreking vereist voor de beveiligingspatches van de Mattermeeste-server.

U kunt updates aanbrengen gedurende een periode waarin de verwachte belasting klein genoeg is dat een server tijdens de update de volledige belasting van het systeem kan uitvoeren.

Merk op dat u de machines niet opnieuw start, alleen de Mattermeeste servertoepassingen. Een Mattermeeste server start over het algemeen ongeveer 5 seconden.

1. Controleer de upgradeprocedure in de sectie *Upgrade Enterprise Edition * van :doc: ` ../administration/upgrade `.
2. Maak een backup van het bestaande ` `config.json ` ` bestand.
3. Stel uw proxy in om alle nieuwe aanvragen naar een enkele server te verplaatsen. Als u NGINX gebruikt en het is geconfigureerd met een upstream-backend sectie in ` ` /etc/nginx/sites-available/matterbest ` `, dan commentaar uit op de ene server die u eerst wilt bijwerken, en NGINX herladen.
4. Sluit Matterbest af op elke server, behalve degene die u eerst bijwerkt.
5. Het bijwerken van elke Matterste instantie die wordt afgesloten.
6. Vervang op elke server het nieuwe ` `config.json ` ` ` bestand door de kopie van de backup.
7. Start de Mattermeeste servers.
8. Herhaal de updateprocedure voor de actieve server.

Serverupgrades waarvoor onderbreking van de service vereist is
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Een serviceonderbreking is vereist wanneer de upgrade een wijziging in het databaseschema bevat of wanneer een wijziging in ` `config.json ` ` a s vereist
erver opnieuw starten, zoals bij het maken van de volgende wijzigingen:

  * Standaard Server-taal
  * Snelheidsbeperking
  * Webserver-modus
  * Database
  * Hoge beschikbaarheid

Als de upgrade een wijziging in het databaseschema bevat, wordt de database bijgewerkt door de eerste server die wordt gestart.

Upgrades aanbrengen gedurende een periode van lage belasting. Het systeem uitvaltijd is kort en hangt af van het aantal Mattermeeste servers in uw cluster. Merk op dat u de machines niet opnieuw start, alleen de Mattermeeste servertoepassingen.

1. Controleer de upgradeprocedure in de sectie *Upgrade Enterprise Edition * van :doc: ` ../administration/upgrade `.
2. Maak een backup van het bestaande ` `config.json ` ` bestand.
3. Stop NGINX.
4. Upgrade elke Mattermeeste instantie.
5. Vervang op elke server het nieuwe ` `config.json ` ` ` bestand door de kopie van de backup.
6. Start een van de Mattermeeste servers.
7. Als de server actief is, start u de andere servers.
8. Start NGINX opnieuw op.

Problemen oplossen
---------------

Status rode server
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Als de hoge beschikbaarheid is ingeschakeld, geeft de systeemconsole de status van de server weer als rood of groen, hetgeen aangeeft of de servers correct communiceren met de cluster. De servers gebruiken communicatie tussen knooppunten om de andere machines in de cluster te pingen, en zodra een ping is ingesteld, wisselen de gegevens van de servers uit, zoals serverversie en configuratiebestanden.

Een serverstatus van rood kan de volgende oorzaken hebben:

-** Niet-overeenkomende configuratiebestand * *: Matterbest probeert nog steeds de communicatie tussen knooppunten te proberen, maar de systeemconsole geeft een rode status aan voor de server, omdat de functie voor hoge beschikbaarheid hetzelfde configuratiebestand gebruikt om goed te functioneren.
-** Server-versie komt niet overeen * *: Matterbest probeert nog steeds de communicatie tussen knooppunten te proberen, maar de systeemconsole zal een rode status voor de server laten zien, omdat de functie voor hoge beschikbaarheid er van uitgaat dat dezelfde versie van Matterbest is geïnstalleerd op elke server in de cluster. Het wordt aanbevolen om op alle servers de 'nieuwste versie van Mattermore <https://mattermost.org/download/>' __ te gebruiken. Volg de upgradeprocedure in :doc: ` ../administration/upgrade ` voor elke server die moet worden geüpgraded.
-* * Server is down * *: Als een communicatie tussen knooppunten een bericht niet verzendt, maakt het een andere poging binnen 15 seconden. Als de tweede poging mislukt, wordt aangenomen dat de server down is. Er wordt een foutbericht naar de logboeken geschreven en de systeemconsole bevat een status van rood voor die server. De communicatie tussen knooppunten blijft in 15 seconden doorgaan met het pingen van de downserver. Als de server weer omhoog komt, worden er nieuwe berichten verzonden.

WebSocket-verbinding verbreken
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Wanneer een client WebSocket een verbinding ontvangt, zal het automatisch proberen om elke drie seconden een verbinding te herstellen met een backoff. Nadat de verbinding tot stand is gebracht, probeert de client alle berichten te ontvangen die zijn verzonden tijdens het verbreken van de verbinding.
