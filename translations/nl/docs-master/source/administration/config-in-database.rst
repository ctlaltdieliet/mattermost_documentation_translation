Configuratie in de meest overeenkomende database
== == == == == == == == == == == == == == == == == == == ==

Er is een nieuwe configuratieoptie toegevoegd in de ` 5.10 release <https: //docs.mattermost.com/administration/changelog.html#configuration-database> ` _ om de database te gebruiken als de enkele bron van de waarheid voor de actieve configuratie van uw Mattermeest installatie. Dit wijzigt het binaire bestand Matterit van het lezen van het standaardbestand ` `config.json ` ` voor het lezen van de configuratie-instellingen die zijn opgeslagen in een configuratietabel in de database.

Matterbest heeft onze ` communityserver <https://community.mattermost.com> ` _ op deze optie gebruikt omdat de functie is vrijgegeven en beveelt het gebruik ervan aan voor: ' High Availability deployments <cluster>`.

Voordelen voor het gebruik van deze optie:

* Handig beheer van de configuratie verandert rechtstreeks van de System Console, zelfs in High Availability-implementaties en alleen-lezen-containerized omgevingen.
* Zorg ervoor dat alle servers in een implementatie met hoge beschikbaarheid dezelfde configuratie hebben, zelfs wanneer er nieuwe servers aan de cluster worden toegevoegd.
* Automatisch SAML-certificaten en sleutels implementeren op alle servers in de cluster.

Configuratie migreren naar de database
------------------------------------------------------

Deze instructies hebben betrekking op het migreren van de Matterste configuratie naar de database en het bijwerken van de ` ` systemd ` ` configuratie om het uit de database te laden. .. Opmerking:
  Deze instructies gaan ervan uit dat Mattermeeste server geïnstalleerd is op ` ` /opt/matterbest ` `. Als je Matterbest in een andere directory draait, moet je de paden aanpassen aan je omgeving.

Uw database-verbindingsreeks ophalen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De eerste stap is het ophalen van de verbindingsreeks voor de hoofddatabase. Er zijn verschillende manieren om dit te doen, maar de makkelijkste is om de ` ` mattermeest config get ` ` opdracht te gebruiken: .. code-blok :: bash

   sudo su matterbest cd /opt/mattermeeste bin/mattermeeste config get SqlSettings.DataSource

Voorbeeld van uitvoer: .. code-blok :: tekst

   SqlSettings.DataSource: "mmuser:really_secure_password@tcp (127.0.0.1:3306 )/mattermost?charset=utf8mb4,utf8\u0026readTimeout=30s \u0026writeTimeout=30s" .. Opmerking:
   Voer deze opdracht uit als de gebruiker * matterbest * en niet * root *. Als de Matterbest-binary wordt uitgevoerd als * root *, worden er fouten in de machtigingen veroorzaakt.

Een andere manier is om het bestand ` `config.json ` ` te bekijken en de waarde in ` `SqlSettings.DataSource ` ` te krijgen.

Als ` `SqlSettings.DataSource ` ` niet begint met ` ` postgres: // ` ` moet je ` ` mysql:// ` ` aan het begin toevoegen. Als u ` ` ` \u0026 ` ` vervangen door ` ` vervangen door ` ` & ` `.

Hier zijn twee voorbeelden van verbindingsreeksen:

** MySQL* * .. code-blok :: tekst

   mysql://mmuser:really_secure_password@tcp (127.0.0.1:3306 )/mattermost?charset=utf8mb4,utf8&readTimeout=30s&writeTimeout=30s

** PostgreSQL* * .. code-blok :: tekst

   postgres://mmuser:really_secure_password@localhost: 5432/mattermost?sslmode=disable &connect_timeout=10

Een omgevingsbestand maken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ Opmerking:
  Als je Matterbest in een hoge A runt ...
Deze stap moet op alle servers in de cluster worden uitgevoerd.

Maak het bestand ` `/opt/mattermost/config/mattermost.environment ` ` om de omgevingsvariabele ` ` MM_CONFIG ` ` in te stellen op de verbindingsreeks van de database. Bijvoorbeeld:

** MySQL* * .. code-blok :: tekst

   MM_CONFIG='mysql://mmuser:mostest@tcp (127.0.0.1:3306 )/mattermost?charset=utf8mb4,utf8&readTimeout=30s&writeTimeout=30s '

** PostgreSQL* * .. code-blok :: tekst

   MM_CONFIG= 'postgres://mmuser:mostest@localhost: 5432/mattermost_test?sslmode=disable &connect_timeout=10' .. Opmerking:
  Zorg ervoor dat u geen enkele aanhalingstekens in de verbindingsreeks van de database wilt plaatsen door een ` ` \ ` ` te plaatsen als deze ` ` \ '` `. Bijvoorbeeld: ` ` MM_CONFIG=' mysql://mmuser:it \ 's-a-password!@tcp(127.0.0.1:3306 )/mattermost?charset=utf8mb4,utf8&readTimeout=30s&writeTimeout=30s' ` ` .. code-blok :: tekst

   MM_CONFIG= 'mysql://mmuser:it \' s-a-password!@tcp(127.0.0.1:3306 )/mattermost?charset=utf8mb4,utf8&readTimeout=30s&writeTimeout=30s '

Ten slotte voert u deze opdracht uit om de machtigingen voor uw Mattermeeste-directory te controleren: .. code-blok :: bash

   sudo chown -R matterbest: mattermeest /opt/matterbest

Wijzig het Matterbest ` ` systemd ` ` bestand ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Zoek eerst het ` `mattermost.service ` ` bestand met: .. code-blok :: bash

   sudo systemctl status mattermost.service

De tweede regel van de uitvoer heeft de locatie van de '`mattermost.service `'. .. code-blok :: tekst

      Geladen: geladen (/lib/systemd/system/mattermost.service; ingeschakeld; leverancier vooraf: ingeschakeld)

Bewerk dit bestand als * root * om de onderstaande tekst toe te voegen net boven de regel die begint met ` ` ExecStart ` ` ` \: .. code-block :: tekst

   EnvironmentFile=/opt/mattermost/config/mattermost.environment

Hier is een compleet ` `mattermost.service ` ` ` bestand met de ` ` EnvironmentFile ` ` regel toegevoegd: .. code-blok :: tekst

   [ Eenheid]
   Beschrijving = Matterbest
   After=network.target
   After=mysql.service
   Requires=mysql.service

   [ Service]
   Type=notify
   EnvironmentFile=/opt/mattermost/config/mattermost.environment
   ExecStart=/opt/mattermost/bin/matterbest
   TimeoutStartSec=3600
   Restart=altijd
   RestartSec=10
   WorkingDirectory=/opt/matterbest
   Gebruiker=matterbest
   Groep=mattermeest
   LimitNOFILE = 49152

   [ Installeren]
   WantedBy=mijnsql.service .. Opmerking:
  Als u PostgreSQL gebruikt als uw database, moet de ` `mysql.service ` ` worden vervangen door ` `postgresql.service ` `. De eenvoudigste manier om het maken van een fout te vermijden is om alleen de ` ` EnvironmentFile ` ` regel toe te voegen en niet het hele voorbeeld te kopiëren.

Configuratie migreren van ` `config.json ` ` ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ Opmerking:
  Als u een High Availability-cluster gebruikt, moet u dit alleen uitvoeren op een enkele server in de cluster.

De opdracht voor het migreren van de configuratie naar de database moet altijd worden uitgevoerd als de * mattermeeste * gebruiker. .. code-blok :: bash

   sudo su matterbest cd /opt/mattermeeste bin/mattermeeste config migrate ./config/config.json 'mysql://mmuser:mostest@tcp (127.0.0.1:3306 )/mattermost?charset=utf8mb4,utf8&readTimeout=30s&writeTimeout=30s' .. waarschuwing:
   Bij het migreren van configuratie zal Matterbest de configuratie overnemen van alle ` ` MM_ * ` ` ` omgevingsvariabelen die in de huidige shell zijn ingesteld.  Zie ` Omgevingsvariabelen <https: //docs.mattermost.com/administration/config-settings.html#configuration-settings> ` _
   
Net als bij het omgevingsbestand moet u eventuele enkele aanhalingstekens in de verbindingsreeks van de database ontsnappen. Ook worden alle bestaande SAML-certificaten gemigreerd naar de database, zodat ze beschikbaar zijn voor alle servers in de cluster.

Als de configuratie in de database is ingeschakeld, worden eventuele wijzigingen in de configuratie vastgelegd in de tabellen ` ` Configurations ` ` en ` ` ConfigurationFiles ` `. Bovendien wordt ' `ClusterSettings.ReadOnlyConfig ` ` genegeerd, zodat de systeemconsole volledig kan worden gebruikt.

Als u configuratie-instellingen hebt die op een server per server moeten worden ingesteld, moet u deze als omgevingsvariabelen toevoegen aan het ` `mattermost.environment ` ` bestand. Deze moeten op hun eigen lijn, en je moet ze goed te ontsnappen.

Controleer of de configuratie correct is gemigreerd ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Configuraties worden opgeslagen in de tabel ` ` Configuraties ` ` in de database. Om te controleren of u de configuratie hebt gemigreerd, voert u de volgende query uit: .. code-block :: sql

   SELECTEER * VAN CONFIGURATIES WAAR ACTIEF = 1;

Er moet precies één regel worden geretourneerd en het ` ` Waarde ` ` veld voor die regel moet overeenkomen met het ` `config.json ` ` bestand.

Herlaad ` ` systemd ` ` files en herstart Matteres ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ Opmerking:
  Als u Mattermost in High Availability draait, moet deze stap worden uitgevoerd op alle servers in de cluster.

Ten slotte voert u deze opdrachten uit om de daemon opnieuw te laden en Matterbest opnieuw te starten met de nieuwe omgevingsvariabele ` ` MM_CONFIG `. .. code-blok :: tekst

   sudo systemctl-daemon herladen sudo systemctl restart matterbest

Voortschrijdend ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als u problemen met uw configuratie in de database uitvoert, kunt u teruggaan naar het bestand ` `config.json ` ` door de ` ` MM_CONFIG `-regel in ` `/opt/mattermost/config/mattermost.environment ` uit te geven en Matterbest opnieuw te starten met ` ` systemctl restart matterbest ` `.

Problemen oplossen
-----------------

Server kan ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden

Als u de vlag ` ` --disableconfigwatch ` ` niet daadwerkelijk in een bestand aanwijst, wordt de server niet gestart met een passend foutbericht.
