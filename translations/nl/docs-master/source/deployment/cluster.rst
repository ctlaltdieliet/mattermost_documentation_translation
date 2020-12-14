Cluster voor hoge beschikbaarheid (E20)
== == == == == == == == == == == == == == == =

*Beschikbaar in Enterprise Edition E20 *

Met een High Availability-cluster kan een Matterbest-systeem service onderhouden tijdens storingen en hardwarestoringen door het gebruik van redundante infrastructuur.

High Availability in Matterbest bestaat uit het uitvoeren van redundante Mattermeeste toepassingenservers, redundante databaseservers en redundante load balancers. Het uitvallen van een van deze componenten onderbrekt de werking van het systeem niet. .. opmerking: Dit document is van toepassing op Mattermeeste Server versie 4.0 en hoger. Voor eerdere versies, zie :doc: ` cluster-310 `. .. Inhoud:
  :backlinks: boven: lokaal:

Eisen voor continubedrijf
-------------------------------------

Om te allen tijde ononderbroken gebruik mogelijk te maken, ook tijdens serverupdates en serverupgrades, moet u ervoor zorgen dat de redundante componenten correct zijn gelijmd en dat u de juiste volgorde volgt voor het bijwerken van elk van de componenten van het systeem.

Redundantie op verwachte schaal Bij een storing van één component moeten de overige toepassingenservers, databaseservers en werklastverdelers worden gesorteerd en geconfigureerd voor het uitvoeren van de volledige belasting van het systeem. Als niet aan deze eis wordt voldaan, kan een storing van één component leiden tot een overbelasting van de resterende componenten, waardoor een volledige systeemstoring wordt veroorzaakt.

Updatesequentie voor continue bewerking U kunt de meeste configuratiewijzigingen toepassen en beveiligings-updates voor de release van de punt vrijgeven zonder de service te onderbreken, op voorwaarde dat u de systeemcomponenten in de juiste volgorde bijwerkt. Raadpleeg de 'Upgradehandleiding' ' voor instructies over hoe u dit doet.

  ** Exception:** Wijzigingen in de configuratie-instellingen waarvoor een herstart van de server vereist is, en upgrades van de serverversie die een wijziging van het databaseschema vereisen, vereisen een korte periode van downtime. Downtime voor een herstart van de server is ongeveer 5 seconden. Voor een update van een databaseschema kan de uitvaltijd maximaal 30 seconden bedragen.

Implementatiehandleiding
----------------

Implementatiegids voor het instellen en onderhouden van hoge beschikbaarheid op uw Mattermeeste servers. Dit document heeft geen betrekking op de configuratie van databases in termen van herstel na calamiteiten, maar u kunt verwijzen naar de sectie 'Veelgestelde vragen (FAQ)' _ sectie voor onze aanbevelingen.

Initiële installatiehandleiding voor hoge beschikbaarheid
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Om ervoor te zorgen dat uw instance en configuratie compatibel zijn met hoge beschikbaarheid, controleer dan de sectie ` Configuratie en compatibiliteit '. .. opmerking:: Maak een backup van uw Mattermeeste database-en bestandsopslaglocaties voordat u hoge beschikbaarheid configureert. Voor meer informatie over het maken van backups raadpleegt u :doc: ` ../administration/backup `.

1. Upgrade Mattermeeste Server naar versie 4.0 of hoger. Zie :doc: ` ../administration/upgrade `.
2. Stel een nieuwe Matterigste server in met versie 4.0 of hoger door een van onze ** Install Guides * * te volgen. Deze server moet een identieke kopie van het configuratiebestand gebruiken, ``config.json ` `. Controleer of de servers functioneren door elke onafhankelijke serv te raken.
er via zijn privé IP adres.
3. Wijzig de ` `config.json `-bestanden op beide servers om ` ` ClusterSettings ` ` toe te voegen zoals beschreven in :ref: ` high availability `.
4. Controleer of de configuratiebestanden identiek zijn op beide servers en start elke machine opnieuw in de cluster.
5. Wijzig uw NGINX-configuratie zodat deze proxy's voor beide servers. Meer informatie hierover vindt u in 'Proxyserverconfiguratie' _.
6. Open ** System Console > Environment > High Availability * * (of ** System Console > Advanced > High Availability * * in versies ouder dan 5.12) om te controleren of elke machine in de cluster communiceert zoals verwacht met groene statuslampjes. Als dit niet het geval is, moet u de logboekbestanden voor eventuele aanvullende informatie onderzoeken.

Een server toevoegen aan het cluster ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ out

1. Maak een backup van uw Matterendste database en de opslaglocatie van het bestand. Voor meer informatie over het maken van backups raadpleegt u :doc: ` ../administration/backup `.
2. Stel een nieuwe Matterigste server in. Deze server moet een identieke kopie van het configuratiebestand gebruiken, ``config.json ` `. Controleer of de server functioneert door het persoonlijk IP-adres op te slaan.
3. Wijzig de NGINX-instelling om de nieuwe server toe te voegen. Voor meer informatie hierover raadpleegt u 'Proxyserverconfiguratie' _.
4. Open ** System Console > Environment > High Availability * * (of ** System Console > Advanced > High Availability * * in versies ouder dan 5.12) om te controleren of alle machines in de cluster communiceren zoals verwacht met groene statusindicators. Als dit niet het geval is, moet u de logboekbestanden voor eventuele aanvullende informatie onderzoeken.

Bezig met het verwijderen van een server uit de cluster ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ out

1. Maak een backup van uw Matterendste database en de opslaglocatie van het bestand. Voor meer informatie over het maken van backups raadpleegt u :doc: ` ../administration/backup `.
2. Wijzig de NGINX-instelling om de server te verwijderen. Voor meer informatie hierover raadpleegt u 'Proxyserverconfiguratie' _.
3. Open ** System Console > Environment > High Availability * * (of ** System Console > Advanced > High Availability * * in versies ouder dan 5.12) om te controleren of alle machines in de cluster communiceren zoals verwacht met groene statusindicators. Als dit niet het geval is, moet u de logboekbestanden voor eventuele aanvullende informatie onderzoeken.

Configuratie en compatibiliteit
-------------------------------

Details over het configureren van uw systeem voor hoge beschikbaarheid.

Mattermeeste serverconfiguratie
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Vragen

Configuratie-instellingen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

1. Hoge beschikbaarheid is geconfigureerd in de ` ` ClusterSettings ` ` sectie van ` `config.json ` ` ` en de instellingen zijn zichtbaar in de System Console. Als Hoge beschikbaarheid is ingeschakeld, is de systeemconsole ingesteld op de werkstand Alleen lezen, zodat alle ` `config.json `-bestanden op de Mattermeeste servers altijd identiek zijn. Voor het testen en valideren van een installatie voor hoge beschikbaarheid kunt u ` ` ReadOnlyConfig ` ` instellen op ` ` false ` `, waarmee wijzigingen in de System Console kunnen worden opgeslagen in het configuratiebestand.

  .. code-blok :: geen

    "Clusterinstellingen": {
            "Enable": false, "ClusterName": "production", "OverrideHostname": "," UseIpAddress ": true," UseExperimentalGossip ": false," ReadOnlyConfig ": true," GossipPort ": 8074," StreamingPort ": 8075
    }

  Voor meer informatie over deze instellingen, zie :ref: ` high availability `.

2. Wijzig de proceslimiet in 8192 en het maximumaantal geopende bestanden naar 65536.

  Wijzig ` `/etc/security/limits.conf ` ` op elke machine die een Mattermeeste server host door de volgende regels toe te voegen:

  .. code-blok :: geen

    * zachte nofile 65536
    * hard nobestand 65536
    * zachte nproc 8192
    * hard nproc 8192

3. Verhoog het aantal WebSocket-verbindingen:

  Wijzig ` `/etc/sysctl.conf ` ` op elke machine die een Mattermeeste server host door de volgende regels toe te voegen:

  .. code-blok :: geen

    net.ipv4.ip_local_port_range = 1025 65000 net.ipv4.tcp_fin_timeout = 30 net.ipv4.tcp_tw_reuse = 1 net.core.somaxconn = 4096 net.ipv4.tcp_max_syn_backlog = 8192

U kunt hetzelfde doen voor de proxyserver.

Clusterdetectie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als u niet-standaard (d.w.z. complexe) netwerkconfiguraties hebt, moet u mogelijk de instelling ' Hostnaam overschrijven <https: //docs.mattermost.com/administration/config-settings.html#override-hostname> ` _ gebruiken om de clusterknooppunten te helpen elkaar te ontdekken. De clusterinstellingen in de configuratie worden om deze reden uit het config bestand hash verwijderd, wat betekent dat u ` `config.json ` ` ` ` bestanden kunt hebben die iets anders zijn in de modus voor hoge beschikbaarheid. De ` Override Hostname <https: //docs.mattermost.com/administration/config-settings.html#override-hostname> ` _ is bedoeld om voor elk geclusterd knooppunt in ` `config.json ` ` te verschillen als je de ontdekking moet forceren.

Als ` ` UseIpAddress ` ` is ingesteld op ` ` true ` `, probeert het het IP-adres te verkrijgen door te zoeken naar het eerste niet-lokale IP-adres (niet-lus-back, niet-localunicast, niet-localmulticast-netwerkinterface). Het enumereert de netwerkinterfaces met de ingebouwde go-functie ` net.InterfaceAddrs () <https: //golang.org/pkg/net/#InterfaceAddrs> ` _. Anders wordt geprobeerd de hostnaam op te halen met de ` os.Hostname () <https: //golang.org/pkg/os/#Hostname> ` _ ingebouwde go-functie.

U kunt ook ` ` SELECT * FROM ClusterDiscovery ` ` uitvoeren op uw database om te zien hoe het is ingevuld in het veld ** Hostname**. Dit veld is de hostnaam of het IP-adres dat de server gebruikt om contact op te nemen met andere knooppunten in de cluster. We proberen een verbinding te maken met de ` ` url Hostname: Port ` ` ` en ` ` Hostname :PortGossipPort ` `. Je moet er ook voor zorgen dat alle juiste poorten open zijn zodat de cluster correct kan roddelen. Deze poorten bevinden zich onder ` ` ClusterSettings ` ` ` in uw configuratie.

Kortom, u dient gebruik te maken van:

 1. IP adres ontdekking als het eerste niet-lokale adres kan worden gezien van de andere machines.
 2. Vervangen van hostnaam op het besturingssysteem, zodat het een goede vindbare naam is voor de andere knooppunten in de cluster.
 3. Hostnaam vervangen in ` `config.json ` ` als de bovenstaande stappen niet werken. U kunt een IP-adres in dit
indien nodig. De ` `config.json ` ` zal voor elk clusterknooppunt verschillend zijn.

Tijdsynchronisatie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Elke server in de cluster moet beschikken over de daemon 'ntpd `' van de Network Time Protocol-daemon, zodat de berichten in de juiste volgorde worden geplaatst.

Stand ^ ^ ^ ^ ^ ^

De Mattermeeste Server is ontworpen om zeer weinig staat te hebben voor horizontale schaling. De items in de staat die worden beschouwd voor het schalen van Matterbest zijn hieronder opgesomd:

-In de cache van de geheugensessie voor snelle validatie en toegang tot het kanaal.
-In het geheugen online/offline cache voor snelle reactie.
-Systeemconfiguratiebestand dat wordt geladen en opgeslagen in het geheugen.
-WebSocket verbindingen van clients gebruikt om berichten te verzenden.

Wanneer de Mattermeeste server is geconfigureerd voor hoge beschikbaarheid, gebruiken de servers een communicatieprotocol tussen knooppunten op een ander luisteradres om de status te synchroniseren. Wanneer een status wordt gewijzigd, wordt deze teruggeschreven naar de database en wordt er een bericht van een knooppunt verzonden om de andere servers van de statuswijziging op de hoogte te stellen. De werkelijke status van de items kan altijd worden gelezen uit de database. Matterit gebruikt ook inter-node communicatie om WebSocket berichten naar de andere servers in de cluster te sturen voor real-time berichten zoals "[ Gebruiker X] is typen."

Proxyserverconfiguratie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De proxyserver stelt de cluster van Mattermeeste servers bloot aan de buitenwereld. De Mattermeeste servers zijn ontworpen voor gebruik met een proxy server zoals NGINX, een hardware load balancer, of een cloud-service zoals Amazon Elastic Load Balancer.

Als u de server wilt bewaken met een health check, kunt u ` ` http://10.10.10.2/api/v4/system/ping ` ` gebruiken en de respons voor ` ` Status 200 ` ` controleren, wat aangeeft dat het succes is. Gebruik deze route voor het controleren van de status van de server * in-service * of * out-of-service *.

Hieronder vindt u een voorbeeldconfiguratie voor NGINX. Er wordt van uitgegaan dat u twee Mattermeeste servers hebt die worden uitgevoerd op persoonlijke IP-adressen van ` ` 10.10.10.2 ` ` ` en ` ` 10.10.10.4 ` `. .. code-blok :: geen

    upstream-backend {
            server 10.10.10.2:8065; server 10.10.10.4:8065;
      }

      server {
          server_name mattermost.example.com;

          locatie ~ /api/v [ 0-9] +/(users/) ?websocket$ {
                proxy_set_header Upgrade $http_upgrade; proxy_set_header Connection "upgrade"; client_max_body_size 50M; proxy_set_header Host $http_host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Doorgezonden-Voor $proxy_add_x_forwarded_for; proxy_set_header X-Doorgezonden-Proto $scheme;
                proxy_set_header X-Frame-Options SAMEORIGIN;
                proxy_buffers 256 16k; proxy_buffer_grootte 16k; proxy_read_timeout 600s; proxy_pass http://backend;
          }

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
  3. Als u gebruik maakt van Amazon S3 of MinIO voor de opslag van bestanden dan is er geen andere configuratie vereist.

Als u de functie Compliance Reports gebruikt in Enterprise Edition E20, moet u de ` ` ComplianceSettings ' (ComplianceSettings) configureren: ` ` ` ` "Directory": "./data/", ` ` om te delen tussen alle machines of de rapporten zullen alleen beschikbaar zijn via de System Console op de lokale Matterendste server.

Migreren naar NAS of S3 vanuit lokale opslag valt buiten het bereik van dit document.

Databaseconfiguratie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Gebruik de functie voor het lezen van replica's om de database te schalen. De Matterendste server kan worden ingesteld voor het gebruik van één masterdatabase en meerdere leesreplica-databases. Mattermeeste distribueert opdrachten voor alle databases en verzendt schrijfopdrachten naar de masterdatabase en deze wijzigingen worden vervolgens verzonden om de lees-replica's bij te werken.

Bij grote implementaties kunt u overwegen de zoekreplica te gebruiken om zoekquery's op een of meer databaseservers te isoleren. Een zoekreplica is vergelijkbaar met een leesreplica, maar wordt alleen gebruikt voor het afhandelen van zoekopdrachten.

Als er geen zoekreplica's zijn, gebruikt de server de leesreplica's. Als er geen leesreplica's zijn, valt de server terug naar de master.

Formaatdatabases ` ` ` ` ` ` ` ` ` ` ` ` ` ` `

Voor informatie over het bepalen van de grootte van databaseservers raadpleegt u :ref: ` hardware-sizing-for-enterprise `.

In een master/slave-omgeving, zorg ervoor dat de grootte van de slaaf machine om 100% van de lading in het geval dat de master machine gaat naar beneden en je moet falen over.

Implementatie Van Een Multi-databaseconfiguratie ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` `

Ga als volgt te werk om een Matterigste server met meerdere databases te configureren:

1. Werk de instelling ` ` DataSource ` ` in ` `config.json ` ` bij met een verbindingsreeks naar de hoofddatabaseserver. De verbindingsreeks is gebaseerd op het databasetype dat is ingesteld in ` ` DriverName ` `, ` ` postgres ` ` ` of ` ` mysql ` `.
2. Werk de instelling ` ` DataSourceReplicas ` ` in ` `config.json ` ` bij met een reeks verbindingsreeksen naar uw database lees replicaservers in de indeling ` ` [ "readreplica1", "readreplica2"] ` `. Elke verbinding moet ook compatibel zijn met de ` ` DriverName ` ` instelling.

Hier is een voorbeeld ` ` SqlSettings ` ` blok voor een master en twee lees replica's:

  "SqlSettings": {
        "DriverName": "mysql", "DataSource": "master_user:master_password@tcp (master.server) /mattermost?charset=utf8mb4,utf8\u0026readTimeout=30s ", "DataSourceReplicas": [ "slave_user:slave_password@tcp (replica1.server) /mattermost?charset=utf8mb4,utf8\u0026readTimeout=30s\u0026writeTimeout=30s "," slave_user:slave_password@tcp (replica2.server) /mattermost?charset=utf8mb4,utf8\u0026writeTimeout=30s "], "DataSourceSearchReplicas": [], "MaxIdleConns": 20, "MaxOpenConns": 300, "Trace": false,
        "AtRestEncryptKey": "," QueryTimeout ": 30 }  

De nieuwe instellingen kunnen worden toegepast door de server te stoppen en te starten, of door de configuratie-instellingen te laden zoals beschreven in de volgende sectie.

Na het laden worden databaseschrijfopdrachten naar de masterdatabase gezonden en worden de leesopdrachten verdeeld over de andere databases in de lijst.

Een configuratie met meerdere databases laden op een Active Server ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` `

Nadat een configuratie met meerdere databases is gedefinieerd in ` `config.json ` `, kan de volgende procedure worden gebruikt om de instellingen toe te passen zonder de Matterigste server af te sluiten:

1. Ga naar ** System Console > Environment > Environment > Web Server * * (of ** System Console > Configuration * * in versies vóór 5.12) en klik op ** Reload Configuration from Disk * * om de configuratie-instellingen voor de Mattermeeste server opnieuw te laden vanuit ` `config.json ` `.
2. Ga naar ** System Console > Environment > Database * * (of ** System Console > Database * * in versies ouder dan 5.12) en klik op ** Recycle Database Connections * * om bestaande databaseverbindingen af te sluiten en nieuwe verbindingen in te stellen in de configuratie met meerdere databases.

Terwijl de verbindingsinstellingen aan het veranderen zijn, kan er een kort moment zijn wanneer de schrijfbewerkingen naar de masterdatabase mislukken. Het proces wacht totdat alle bestaande verbindingen zijn voltooid en start nieuwe opdrachten met de nieuwe verbindingen. Eindgebruikers die berichten proberen te verzenden terwijl de switch gebeurt, hebben dezelfde ervaring als de verbinding met de Mattertiste server wordt verbroken.

Handmatige failover voor masterdatabase ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` `

Als het nodig is om over te schakelen van de huidige master database-bijvoorbeeld, als het uit de schijfruimte raakt, of het vereist onderhoud updates, of om andere redenen-kunt u overschakelen op Matterbest server om een van de lees replica's als een master database door het bijwerken van ` ` DataSource ` ` in ` `config.json ` `.

De instellingen toepassen zonder de Matterendste server af te sluiten:

1. Ga naar ** System Console > Environment > Environment > Web Server * * (of ** System Console > Configuration * * in versies vóór 5.12) en klik op ** Reload Configuration from Disk * * om de configuratie-instellingen voor de Mattermeeste server opnieuw te laden vanuit ` `config.json ` `.
2. Ga naar ** System Console > Environment > Database * * (of ** System Consol)
e > Database * * in versies ouder dan 5.12) en klik op ** Recycle Database Connections * * om bestaande databaseverbindingen af te sluiten en nieuwe verbindingen in te stellen in de multi-database configuratie.

Terwijl de verbindingsinstellingen aan het veranderen zijn, kan er een kort moment zijn wanneer de schrijfbewerkingen naar de masterdatabase mislukken. Het proces wacht totdat alle bestaande verbindingen zijn voltooid en start nieuwe opdrachten met de nieuwe verbindingen. Eindgebruikers die berichten proberen te verzenden terwijl de switch plaatsvindt, kunnen dezelfde ervaring hebben als de verbinding met de Mattertiste server wordt verbroken.

Transparante Failover ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` `

De database kan worden geconfigureerd voor hoge beschikbaarheid en transparante failover maken gebruik van de bestaande databasetechnologieën. Wij adviseren MySQL Clustering, Postgres Clustering, of Amazon Aurora. Transparante failover voor databases valt buiten het bereik van deze documentatie.

Leader-verkiezing ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

In Mattermeest v4.2 en hoger wijst een proces voor clusterleidersverkiezingen alle geplande taken, zoals LDAP-synchronisatie, toe om op een enkel knooppunt in een clusteromgeving met meerdere knooppunten te worden uitgevoerd.

Het proces is gebaseerd op een veelgebruikte 'bully leader election-algoritme <https://en.wikipedia.org/wiki/Bully_algorithm>' __ waar het proces met het laagste knooppunt ID-nummer uit de niet-mislukte processen wordt geselecteerd als de leider.

Taakserver ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Mattermeeste runt periodieke taken via de ` job server <https: //docs.mattermost.com/administration/config-settings.html#jobs> ` __. Deze taken omvatten:

 -LDAP-synchronisatie
 -Gegevens retentie
 -naleving van de uitvoer
 -Elasticsearch-indexering

Zorg ervoor dat u ` `JobSettings.RunScheduler ` ` ` true ` ` ` true ` ` in ` `config.json ` ` hebt ingesteld voor alle app-en taakservers in de cluster. De clusterleider is dan verantwoordelijk voor het plannen van terugkerende taken. Opmerking:

  Het wordt ten zeerste aanbevolen om deze instelling niet te wijzigen van de standaardinstelling van ` ` true ` ` omdat dit voorkomt dat de ` ` ClusterLeader ` ` in staat is om de planner uit te voeren. Als gevolg daarvan worden terugkerende taken zoals LDAP-synchronisatie, Compliance-export en gegevensopslag niet meer gepland.

In de vorige versies van de Mattermeeste Server en deze documentatie zijn de instructies voor het uitvoeren van de taakserver met ` ` RunScheduler: false ' `. Het clusterontwerp is geëvolueerd en dit is niet langer het geval.

Plugins en Hoge Beschikbaarheid ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als van Mattermeeste 5.14, wanneer u installeert of een upgrade van een plugin, wordt gedistribueerd over de servers in de cluster automatisch. Het opslaan van bestanden wordt verondersteld te worden gedeeld tussen alle servers, met behulp van services zoals NAS of Amazon S3.

Als ` ` "DriverName": "local" ` ` wordt gebruikt dan is de directory op ` ` "FileSettings": ` ` ` ` ` "Directory": "./data/" ` ` wordt verwacht dat het een NAS-locatie is die is toegewezen als een lokale directory. Als dit niet het geval is Hoge beschikbaarheid zal niet correct functioneren en kan corrupte uw bestand opslag.

Opmerking: een kleine gedragswijziging in 5.15: Wanneer u een plugin opnieuw installeert in 5.14, wordt de vorige ** Enabled** of ** Disabled**-status behouden. Vanaf 5.15 is de oorspronkelijke staat van een geïnstalleerde plugin ** Disabled**.

Upgradehandleiding
-------------

Een update is een incrementele wijziging in de Mattermeeste server die bugs of prestatieproblemen vaststelt. Een upgrade voegt nieuwe of verbeterde functionaliteit toe aan de server.

Wijzigingen In De Configuratie Tijdens Het Continu Werken Bijwerken
~ ~ ~ ~ > ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~

Een onderbreking van de service is niet vereist voor de meeste configuratie-updates. Zie ` Server Upgrades That Require Service Onderbreking ` _ voor een lijst van configuratie-updates die een onderbreking van de dienst vereisen.

U kunt updates aanbrengen gedurende een periode van lage belasting, maar als uw High Availability-cluster correct is ingesteld, kunt u dat op elk gewenst moment doen. Het systeem uitvaltijd is kort en hangt af van het aantal Mattermeeste servers in uw cluster. Merk op dat u de machines niet opnieuw start, alleen de Mattermeeste servertoepassingen. Een Mattermeeste server start over het algemeen ongeveer 5 seconden. .. Opmerking:

  Wijzig de configuratie-instellingen niet via de systeemconsole. Anders hebt u twee servers met verschillende ` `config.json ` ` ` bestanden in een High Availability-cluster die elke keer dat een gebruiker verbinding maakt met een andere app-server wordt vernieuwd.

1. Maak een backup van het bestaande ` `config.json ` ` bestand.
2. Om een van de meest overeenkomende servers te maken, wordt de configuratie gewijzigd in ` `config.json ` ` en slaat u het bestand op. Het bestand nog niet opnieuw laden.
3. Kopieer het ` `config.json ` ` ` bestand naar de andere servers.
4. Sluit Matterbest af op alle maar één server.
5. Herlaad het configuratiebestand op de server die nog actief is. Ga naar in eerdere versies of ** System Console > Environment > Environment > Web Server * * (of ** System Console > Configuration * * in versies prior to 5.12) en klik op ** Reload Configuration from Disk * *.
6. Start de andere servers.

Serverversie Bijwerken Terwijl Het Continu Wordt Uitgevoerd
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Er is geen service-onderbreking vereist voor de beveiligingspatches van de Mattermeeste-server.

U kunt updates aanbrengen gedurende een periode waarin de verwachte belasting klein genoeg is dat een server tijdens de update de volledige belasting van het systeem kan dragen. .. Opmerking:

  We ondersteunen slechts een klein versieverschil tussen de serverversies bij het uitvoeren van een rolling upgrade (bijvoorbeeld v5.27.1 + v5.27.2 of v5.26.4 + v5.27.1 wordt ondersteund, terwijl v5.25.5 + v5.27.0 niet wordt ondersteund). Het uitvoeren van twee verschillende versies van Mattermeeste in uw cluster mag niet buiten een upgradescenario worden uitgevoerd.

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

Een serviceonderbreking is vereist wanneer de upgrade een wijziging in het databaseschema bevat of wanneer een wijziging in ` `config.json ` ` een herstart van de server vereist, zoals bij het maken van de volgende wijzigingen:

  -Standaardtaal server
  -Snelheidsbeperking
  -Webserver-modus
  -Database
  -Hoge beschikbaarheid

Als de upgrade een wijziging in het databaseschema bevat, wordt de database bijgewerkt door de eerste server die wordt gestart.

Upgrades aanbrengen gedurende een periode van lage belasting. Het systeem uitvaltijd is kort en hangt af van het aantal Mattermeeste servers in uw cluster. Merk op dat u de machines niet opnieuw start, alleen de Mattermeeste servertoepassingen.

1. Controleer de upgradeprocedure in de sectie *Upgrade Enterprise Edition * van :doc: ` ../administration/upgrade `.
2. Maak een backup van het bestaande ` `config.json ` ` bestand.
3. Stop NGINX.
4. Upgrade elke Mattermeeste instantie.
5. Vervang op elke server het nieuwe ` `config.json ` ` bestand door de kopie van de backup.
6. Start een van de Mattermeeste servers.
7. Als de server actief is, start u de andere servers.
8. Start NGINX opnieuw op.

Upgraden naar versie 4.0 en hoger
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Vanaf Matterste Server versie 4.0 kan een server automatisch andere servers in dezelfde cluster opsporen. U kunt servers toevoegen en verwijderen zonder dat u wijzigingen hoeft aan te brengen in het configuratiebestand, ``config.json ` `. Om deze mogelijkheid te ondersteunen, werden nieuwe items toegevoegd aan de ` ` ClusterSettings ` ` sectie van ` `config.json ` ` `. Bij het upgraden van 3.10 of eerder naar 4.0 of hoger, moet u handmatig de nieuwe items toevoegen aan uw bestaande ` `config.json ` ` `.

1. Controleer de upgradeprocedure in :doc: ` ../administration/upgrade `.
2. Maak een backup van het bestaande ` `config.json ` ` bestand.
3. Herzien van uw bestaande ` `config.json ` ` om de ` ` ClusterSettings ` ` sectie bij te werken. De volgende instellingen moeten in de meeste gevallen werken:

  .. code-blok :: geen

    "Clusterinstellingen": {
        "Enable": true, "ClusterName": "production", "OverrideHostname": "," UseIpAddress ": true," UseExperimentalGossip ": false," ReadOnlyConfig ": true," GossipPort ": 8074," StreamingPort ": 8075
    },

  Meer informatie over deze instellingen vindt u in :ref: ` high availability `.
4. Stop NGINX.
5. Upgrade elke Mattermeeste instantie.
6. Vervang op elke server het nieuwe ` `config.json ` ` bestand door de gewijzigde versie.
7. Start een van de meest overeenkomende servers.
8. Als de server actief is, start u de andere servers.
9. Start NGINX opnieuw op.

Veelgestelde vragen (FAQ)
---------------------------------

Ondersteunt Mattermeest multi-regio High Availability-implementatie?
~ ~ ~ ~ ~ > ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~

-Ja, Hoewel niet officieel getest, kunt u een cluster in AWS regio's, bijvoorbeeld, en het moet werken zonder problemen.

Wat is Mattermeest aan te bevelen voor diaster herstel van de databases?
~ ~ ~ ~ ~ > ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden

Bij het implementeren van Matterbest in een configuratie voor hoge beschikbaarheid, raden wij u aan een database load balancer tussen Mattermany en uw database te gebruiken. Afhankelijk van uw implementatie heeft dit meer of minder aandacht nodig.

Bijvoorbeeld, als u de implementatie van Matterbest op AWS met Amazon Aurora wij raden gebruik te maken van meerdere Beschikbaarheid Zones. Als u Mattermeeste op uw eigen cluster gebruikt, raadpleeg dan uw IT-team voor een oplossing die het meest geschikt is voor uw bestaande architectuur.

Problemen oplossen
---------------

Status rode server
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Als de hoge beschikbaarheid is ingeschakeld, wordt de status van de server als rood of groen weergegeven in de systeemconsole. Dit geeft aan of de servers correct communiceren met de cluster. De servers gebruiken communicatie tussen knooppunten om de andere machines in de cluster te pingen, en zodra een ping is ingesteld, wisselen de gegevens van de servers uit, zoals serverversie en configuratiebestanden.

Een serverstatus van rood kan de volgende oorzaken hebben:

-** Discrepantie in configuratiebestand: ** Matterbest probeert nog steeds de communicatie tussen knooppunten te proberen, maar de systeemconsole zal een rode status voor de server laten zien, omdat de functie voor hoge beschikbaarheid hetzelfde configuratiebestand nodig heeft om goed te kunnen functioneren.
-** Niet-overeenkomende serverversie: ** Matterbest probeert nog steeds de communicatie tussen knooppunten te proberen, maar de systeemconsole zal een rode status voor de server laten zien, omdat de functie voor hoge beschikbaarheid van dezelfde versie van Matterbest is geïnstalleerd op elke server in de cluster. Het wordt aanbevolen om op alle servers de 'nieuwste versie van Mattermore <https://mattermost.org/download/>' __ te gebruiken. Volg de upgradeprocedure in :doc: ` ../administration/upgrade ` voor elke server die moet worden geüpgraded.
-** Server is down: ** Als een communicatie tussen knooppunten een bericht niet verzendt, doet het een andere poging binnen 15 seconden. Als de tweede poging mislukt, wordt aangenomen dat de server down is. Er wordt een foutbericht naar de logboeken geschreven en de systeemconsole bevat een status van rood voor die server. De communicatie tussen knooppunten blijft in 15 seconden doorgaan met het pingen van de downserver. Als de server weer omhoog komt, worden er nieuwe berichten verzonden.

WebSocket-verbinding verbreken
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Wanneer een client WebSocket een verbinding ontvangt, zal het automatisch proberen om elke drie seconden een verbinding te herstellen met een backoff. Nadat de verbinding tot stand is gebracht, probeert de client alle berichten te ontvangen die zijn verzonden tijdens het verbreken van de verbinding.

App Continu Vernieuwen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Wanneer configuratie-instellingen worden gewijzigd via de systeemconsole, vernieuwt de client elke keer als een gebruiker
nects voor een andere app-server. Dit gebeurt omdat de servers verschillende ` `config.json ` ` bestanden in een High Availability-cluster hebben.

Wijzig de configuratie-instellingen rechtstreeks via ' `config.json ` ` ` ` volgende stappen <https: //docs.mattermost.com/deployment/cluster.html#updating-configuration-changes-while-operating-continuously> ` __.

Berichten Worden Pas Na Herladen Gepost
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Als u werkt in de modus voor hoge beschikbaarheid, moet u ervoor zorgen dat alle Mattermeeste toepassingenservers dezelfde versie van Matterbest uitvoeren. Als ze verschillende versies hebben, kan dit leiden tot een status waarbij de lagere versie-appserver geen aanvraag kan afhandelen en de aanvraag niet wordt verzonden totdat de frontend-toepassing wordt vernieuwd en naar een server wordt verzonden met een geldige Mattertiste versie. Symptomen om te zoeken naar omvatten verzoeken niet schijnbaar willekeurig of een enkele toepassingenserver met een drastische stijging van de goroutines en API-fouten.
