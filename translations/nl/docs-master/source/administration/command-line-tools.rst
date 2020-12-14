Opdrachtregeltools
== == == == == == == == ==

Vanuit de directory waar de Matterigste server is geïnstalleerd, is er een ` ` matterpopulairste ` ` opdracht beschikbaar voor het configureren van het systeem. Voor een overzicht van de Mattermeest command line interface (CLI), ` lees dit artikel <https: //medium.com/@santosjs/plugging-in-to-the-matterbest-cli-8cdcef2bd1f6> ` __ from Santos.

Deze ` ` mattermeest ` ` commando's omvatten:

** Algemeen Beheer * *

-Teams maken
-Gebruikers maken
-rollen toewijzen aan gebruikers
-Gebruikerswachtwoorden resetten
-Gebruikers uitnodigen voor teams

** Uitgebreid beheer * *

-Permanent verwijderen van gebruikers (gebruik cautiously-database back-up aanbevolen voor gebruik)
-Permanent verwijderen van teams (gebruik cautiously-database back-up aanbevolen voor gebruik)

** Geavanceerde automatisering * *

-Kanalen maken
-Gebruikers uitnodigen voor kanalen
-Het verwijderen van gebruikers van kanalen
-Lijst van alle kanalen voor een team
-Herstellen van eerder verwijderde kanalen
-Het openbaar/privé-type van een kanaal wijzigen
-Aanmeldingsopties worden gemigreerd
-multi-factor-verificatie opnieuw instellen voor een gebruiker
-voorbeeldgegevens maken ** Diagnostics**

-Analyseren van de database voor relationele consistentie .. Inhoud:
    :backlinks: boven: lokaal:

De CLI (^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Om de CLI-opdrachten uit te voeren, moet u zich in de hoofddirectory van Mattermost hebben. Bij een standaardinstallatie van Mattermost is de hoofddirectory ` ` /opt/mattermost ` `. Als u ons standaard ` installatieproces < ../guides/administrator.html#installing-mattermost> ' __ hebt gevolgd, moet u de opdrachten uitvoeren als de gebruiker ` ` mattermost ` `. De naam van het uitvoerbare bestand is ` ` matterbest ` `, en het is te vinden in de ` ` /opt/mattermost/bin ` ` directory.

** Bijvoorbeeld, om de meest overeenkomende versie op een standaard installatie van Matterste te krijgen: ** .. code-blok :: bash

    cd /opt/mattermost/ sudo -u mattermeeste bin/mattermeeste versie .. Opmerking:
   Zorg ervoor dat u de Matterbest uitvoert als de ` ` mattermeest ` ` user. Het uitvoeren als ` ` root ` ` gebruiker (bijvoorbeeld) kan leiden tot complicaties met de permissies als de binaire initiates plugins en toegang tot verschillende bestanden bij het uitvoeren van CLI-opdrachten. Het uitvoeren van de server als ` ` root ` ` kan leiden tot het eigendom van de plugins en bestanden die worden overschreven, evenals andere mogelijke permissies fouten.
  
Als u CLI-opdrachten uitvoert op een Mattermeeste-installatie met de configuratie die is opgeslagen in de database, moet u mogelijk de verbindingsreeks van de database als volgt doorgeven: .. code-block :: bash bin/matterbest -- config="postgres: //mmuser:mostest@localhost: 5432/mattermost_test?sslmode=disable \u0026connect_timeout=10 "

Met behulp van de CLI op GitLab Omnibus
-------------------------------

Op GitLab Omnibus moet je in de volgende directory staan als je CLI-opdrachten uitvoert: ` ` /opt/gitlab/embedded/service/mattermost ` `. Ook moet je de commando's uitvoeren als de gebruiker * mattermost * en de locatie van het configuratiebestand opgeven. Het uitvoerbare bestand is ` ` /opt/gitlab/embedded/bin/mattermost ` `.

** Bijvoorbeeld, om de meest overeenkomende versie op GitLab Omnibus te krijgen: ** .. code-blok :: bash

    cd /opt/gitlab/em
bedded/service/mattermost sudo /opt/gitlab/embedded/bin/chpst -e /opt/gitlab/etc/mattermost/env -P -U mattermost: mattermost -u mattermost: mattermost /opt/gitlab/embedded/bin/mattermost -- config=/var/opt/gitlab/mattermost/config.json versie .. Opmerking:
  De voorbeeldopdrachten in de documentatie zijn bedoeld voor een standaardinstallatie van Matterbest. Je moet de commando's aanpassen zodat ze werken op GitLab Omnibus.

Werken met de CLI voor Docker-installatie
-------------------------------

Bij het installeren van Docker is de ` ` /mattermost/bin ` ` directory toegevoegd aan ` ` PATH ` `, zodat je de CLI direct kunt gebruiken met de ` ` docker exec ` ` opdracht. De containernaam mag ` ` mattermostdocker_app_1 ` ` zijn als u Matterbest hebt geïnstalleerd met ` `docker-compose.yml ` `.

** Bijvoorbeeld, om de meest overeenkomende versie op een Docker te installeren: ** .. code-blok :: bash

    docker exec -it <your-mattermost-container-name> mattermeest versie

Werken met de CLI voor Docker-preview
-------------------------------

De bovenstaande documentatie en de onderstaande naslag voor opdrachten zijn ook van toepassing op het 'Matterbest docker preview image <https://github.com/mattermost/mattermost-docker-preview>' __.

Het hoogste punt 3.6 en later ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De nieuwe CLI-tool wordt ondersteund in Matterbest 3.6 en hoger. Voor het bekijken van de beschikbare opdrachten in het oude CLI-tool, raadpleegt u 'Mattermeest 3.5 en eerder' _. .. Opmerking:
  Voor Matterbest 4.10 en eerder gebruikten de commando's het ` ` platform ` ` uitvoerbare bestand in plaats van ` ` matterit ` `. Bijvoorbeeld, om de Matterste versie te controleren, zou men ` ` ./platform versie ` ` draaien in plaats van ` ` ./matterbest version ` `. Notes:

-Parameters in CLI-opdrachten zijn orderspecifiek.
-Als speciale tekens (` `! ` `, ` ` | ` `, ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` `
-De naam van het team en de naam van het kanaal verwijzen naar de handvatten, niet de weergavenamen. Dus in de url ` ` https: //community.mattermost.com/core/channels/town-square ` ` ` team naam zou ` ` core ` ` ` en channel name zou ` ` town-square ` `. .. punt:
   Als u het maken van gebruikers automatisch via de CLI-tool met SMTP automatisch maakt, worden e-mails verzonden naar alle nieuwe gebruikers die zijn gemaakt. Als u een dergelijk laadscript uitvoert, is het het beste om SMTP uit te schakelen of testaccounts te gebruiken, zodat nieuwe e-mails voor het maken van accounts niet onbedoeld worden verzonden naar mensen in uw organisatie die ze niet verwachten.

mattermeest
----------

  Beschrijvingen voor het configureren en beheren van uw Matterbest-instance en -gebruikers.

  Opties .. code-blok :: geen

      -c, -- config { string } configuratiebestand voor gebruik. (standaard "config.json ")
      --disableconfigwatch { boolean } Wanneer waar, wordt het bestand config.json niet automatisch opnieuw geladen wanneer een ander proces het wijzigt (standaard "false")

  Onderliggende opdrachten
    -` mattermeeste kanaal ` _-Beheer van kanalen
    -` matterbest opdracht ` _-Beheer van slash-opdrachten
    -` matterbest config ` _-Werken met het configuratiebestand
    -` matterbest export ` _-Nalevingsexportopdrachten
    -` mattermeest groep ` _-Beheer van Mattermeeste groepen
    -` matterbest help ` _-Genereer volledige documentatie voor de CLI
    -` mattermeest importeren ' _-Gegevens importeren
    -` mattermeest jobserver ` _-Start de Matterste taakserver
    -` mattermeest ldap ` _-AD/LDAP-gerelateerde hulpprogramma's
    -` matterbest license ` _-Licentieopdrachten
    -` matterste logs ` _-Voor menselijk leesbare logs
    -` mattermeeste permissies ` _-Beheer van het toestemmingen systeem
    -` matterbest plugin ` _-Beheer van plugins
    -` matterbest reset ` _-Reset de database naar de eerste status
    -` mattermeest rollen ` _-Beheer van gebruikersrollen
    -` mattermeeste sampledata ` _-Voorbeeldgegevens genereren
    -` matterste server ` _-De Mattermeeste server uitvoeren
    -` mattermeeste team ` _-Beheer van teams
    -` mattermeest gebruiker ` _-Beheer van gebruikers
    -` mattermeest versie ` _-versiegegevens afbeelden
    -` mattermeest webhook ` _-Beheer van webhaken

mattermeeste kanaal
------------------

  Beschrijvingen voor kanaalbeheer.

  Onderliggende opdrachten
    -` matterbest channel add ` _-Gebruikers toevoegen aan een kanaal
    -` mattermeeste kanaal archief ` _-Archief een kanaal
    -` matterbest channel create ` _-Een kanaal aanmaken
    -` matterbest channel delete ` _-Een kanaal verwijderen
    -` matterbest channel list ` _-Lijst alle kanalen op opgegeven teams
    -` mattermeest channel modify ` _-Wijzig het public/private type van een kanaal
    -` matterbest channel move ` _-Verplaats een kanaal naar een ander team
    -` mattermeeste kanaal verwijderen ' _-Gebruikers uit een kanaal verwijderen
    -` matterbest channel hernoemen ' _-Hernoem een kanaal
    -` matterbest channel restore ` _-Een kanaal uit het archief herstellen
    -` matterbest channel search ` _-Zoek een kanaal op naam .. _kanaalwaarde-opmerking: .. Opmerking:
    ** { channel } waarde * *

    Voor de opdrachten * add*, * archive*, * delete*, * remove * and * restore *, kunt u de waarde * { channels } * waarderen door { team }: { channel } met behulp van de team-en channel-URL 's of met behulp van kanaal-ID' s. In de volgende URL is de waarde * { channels } * bijvoorbeeld * mijnteam:mychannel*:

    ` ` https: //example.com/myteam/channels/mychannel ` `

    Ook moeten het team en de kanaalnamen in de URL in kleine letters worden geschreven.

mattermeest kanaal toevoegen
~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl channel add <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-add> ` __.


Beschrijving gebruikers toevoegen aan een kanaal. Als u meerdere gebruikers toevoegt, gebruikt u een door spaties gescheiden lijst.

 Formaat .. code-blok :: geen

      mattermeeste kanaal toevoegen { kanaal } { gebruikers }

 Voorbeelden .. code-blok :: geen

      bin/mattermeeste kanaal toevoegen 8soyabwthjnf9qibfztje5a36h user@example.com gebruikersnaam bin/mattermeeste kanaal toevoegen myteam: mychannel user@example.com gebruikersnaam mattermeeste kanaal archief
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ Opmerking:

   Deze opdracht wordt opnieuw uitgevoerd
laced in een toekomstige release met het mmctl-commando ` mmctl channel archive <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-archive> ` __.


Beschrijving Archief een kanaal. Gearchiveerde kanalen zijn niet toegankelijk voor gebruikers, maar blijven in de database. Voor het herstellen van een kanaal uit het archief, zie ` matterbest channel restore ` _. Kanalen kunnen worden opgegeven door { team }: { channel } met behulp van het team en de kanaalnamen of met behulp van kanaal-ID ' s.

  Formaat .. code-blok :: geen

      mattermeest kanaal archief { kanalen }

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste kanaal archief 8soyabwthjnf9qibfztje5a36h bin/mattermeeste channel archief myteam: mychannel

mattermeeste kanaal maken
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-kanaal van het mmctl-kanaal <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-create> ` __.


Beschrijving Een kanaal maken.

 Formaat .. code-blok :: geen

     mattermeeste kanaal maken

 Voorbeelden .. code-blok :: geen

      bin/mattermeeste channel create -- team myteam -- name mynewchannel --display_name "My New Channel"
      bin/mattermeeste channel create -- team myteam -- name mynewprivatechannel --display_name "My New Private Channel" -- private

 Opties .. code-blok :: geen

      --display_name string Channel Display Name -- header string Channel header -- name string Channel Name -- private Create a private channel.
      -- purpose string Kanaal doel -- team string Team naam of ID mattermeeste kanaal verwijderen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Beschrijving Permanent verwijderen een kanaal samen met alle gerelateerde informatie, met inbegrip van berichten uit de database. Kanalen kunnen worden opgegeven door { team }: { channel } met behulp van het team en de kanaalnamen of met behulp van kanaal-ID ' s.

  Formaat .. code-blok :: geen

      mattermeeste kanaal wissen { kanalen }

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste kanaal verwijderen 8soyabwthjnf9qibfztje5a36h bin/mattermeeste kanaal verwijderen myteam: mychannel

mattermeeste kanaallijst
~ ~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl channel list <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-list> ` __.


Beschrijving Alle kanalen in een opgegeven team. Persoonlijke kanalen worden toegevoegd met ` ` (private) ` ` ` en gearchiveerde kanalen worden toegevoegd met ` ` (gearchiveerd) ` `.

  Formaat .. code-blok :: geen

      mattermeeste kanaallijst { teams }

  Voorbeeld .. code-block :: geen

      bin/mattermeeste channel lijst myteam mattermeeste kanaal wijzigen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Beschrijving Het openbaar/persoonlijk type van een kanaal wijzigen.

  Formaat .. code-blok :: geen

      mattermeeste kanaal wijzigen

  Voorbeeld .. code-block :: geen

      bin/mattermeeste channel modify myteam: mychannel -- username myusername -- private

  Opties .. code-blok :: geen

          -- username [ REQUIRED] Gebruikersnaam van de gebruiker die de privacy van het kanaal verandert.
          -- public Change een besloten kanaal openbaar te maken.
          -- private Change een openbaar kanaal om privé te zijn.

mattermeeste kanaalverplaatsing
~ ~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-kanaalverplaatsing van het mmctl-kanaal <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-move> ` __.

Beschrijving Verplaats kanalen naar een ander team. De opdracht controleert of alle gebruikers in het kanaal deel uitmaken van het doelteam. Inkomende/uitgaande webhooks worden samen met het kanaal verplaatst. Kanalen kunnen worden opgegeven met '` [ team]: [ channel] ` ` of met behulp van kanaal-ID' s.

  Formaat .. code-blok :: geen

      mattermeeste kanaalverplaatsing

  Voorbeeld .. code-block :: geen

      bin/matterbest channel move newteam 8soyabwthjnf9qibfztje5a36h -- username mijnusername bin/mattermeeste channel move newteam myteam: mychannel -- username mijngebruikersnaam

  Opties .. code-blok :: geen

          -- username [ REQUIRED] Gebruikersnaam van de gebruiker die het team verplaatst.
          --remove-gedeactiveerde gebruikers [ OPTIONEEL] Wanneer u het kanaal verplaatst, verwijdert u alle gedeactiveerde gebruikers die de verplaatsing kunnen voorkomen.

mattermeest kanaal verwijderen
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl channel remove <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-remove> ` __.

Beschrijving verwijderen van gebruikers van een kanaal.

  Formaat .. code-blok :: geen

      mattermeeste kanaal verwijderen { kanaal } { gebruikers }

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste kanaal verwijderen 8soyabwthjnf9qibfztje5a36h user@example.com username bin/mattermeeste channel remove myteam: mychannel user@example.com username bin/mattermeeste channel remove myteam: mychannel -- all-users

  Opties .. code-blok :: geen

          -- all-users string Verwijder alle gebruikers van het kanaal.

mattermeeste kanaalnaam wijzigen
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-kanaalnaam van het mmctl-kanaal <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-rename> ` __.

De naam van een kanaal wijzigen. Kanalen kunnen worden opgegeven door * { team }: { channel } * met behulp van het team en de kanaalnamen of met behulp van kanaal-ID ' s.

  Formaat .. code-blok :: geen

      mattermeeste kanaalnaam wijzigen { channel } newchannelname --display_name "Nieuwe weergavenaam"

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste kanaal naam 8soyabwthjnf9qibfztje5a36h newchannelname --display_name "Nieuwe weergavenaam"
      bin/mattermeeste channel hernoemen myteam: mychannel newchannelname --display_name "New Display Name"

  Opties .. code-blok :: geen

      --display_name string Channel Display Name mattermeeste kanaal herstellen
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ' mmctl channel restore <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-restore> ` __.

Beschrijving Herstel een kanaal uit het archief. Kanalen kunnen worden opgegeven door { team }: { channel } met behulp van het team en de kanaalnamen of met behulp van kanaal-ID ' s.

  Formaat .. code-blok :: geen

      mattermeeste kanaal herstellen { kanalen }

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste kanaal herstellen 8soyabwthjnf9qibfztje5a36h bin/mattermeeste kanaal herstellen myteam: mychannel

mattermeeste kanaal zoeken
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ' mmctl channel search <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-search> ` __.

Beschrijving Zoeken naar een kanaal op kanaalnaam. Retourneert de weergavenaam van het kanaal, het kanaal-ID en geeft aan of het persoonlijk of gearchiveerd is. Persoonlijke kanalen worden toegevoegd met ` ` (private) ` ` ` en gearchiveerde kanalen worden toegevoegd met ` ` (gearchiveerd) ` `.

  Formaat .. code-blok :: geen

      mattermeest kanaal zoeken { channelName }

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste channel search mychannel bin/mattermeeste channel search -- team myteam mychannel bin/mattermeeste channel search -- team f1924a8db44ff3bb41c96424cdc20676 mychannel

  Opties .. code-blok :: geen

      -- Team Team Naam of Team ID mattermeestopdracht ------------------

  Beschrijvingen voor het beheer van de schuine streep naar rechts.

  Onderliggende opdrachten
    -` matterbest command create ` _-Maak een aangepaste slash opdracht voor een specifiek team.
    -` matterbest command delete ` _-Verwijder een slash opdracht.
    -` matterbest command list ` _-Lijst alle opdrachten op opgegeven teams of alle teams standaard.
    -` matterbest command modify ` _-Wijzig een slash opdracht.
    -` matterbest command move ` _-Verplaats een slash opdracht naar een ander team.
    -` matterbest command show ` _-Toon een aangepaste slash opdracht.

mattermeest opdracht maken
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht met de opdracht 'mmctl' create <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-command-create> ` __.

Beschrijving Een aangepaste slash-opdracht voor een opgegeven team maken.

  Formaat .. code-blok :: geen

      mattermeest opdracht maken

  Voorbeelden .. code-blok :: geen

       bin/matterbest opdracht create myteam -- title MyCommand --description "My Command Description" -- trigger-word mycommand -- url http://localhost: 8000/my-slash-handler -- creator myusername -- response-username my-bot-username -- icon http://localhost: 8000/my-slash-handler-bot-icon.png -- autocomplete -- post

  Opties .. code-blok :: geen

          -- title string Command Title --description string Command Description -- trigger-word string [ REQUIRED] Command Trigger Word -- url string [ REQUIRED] Opdracht Callback URL
          -- creator stri
ng [ REQUIRED] Username van de maker van de opdracht -- response-gebruikersnaam string Command Response Username -- icon string Command-pictogram URL
          -- autocomplete bool Show commando in autocomplete lijst -- autocompleteDesc string Short command beschrijving voor autocomplete lijst -- autocompleteHint string Command argumenten weergegeven als hulp in autocomplete lijst -- post bool Use POST methode voor callback URL matterbest opdracht verwijderen
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ' mmctl command delete <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-command-delete> ` __.

Beschrijving Een schuine streep naar rechts wissen. Opdrachten kunnen worden opgegeven met de opdracht-ID.

  Formaat .. code-blok :: geen

      matterbest opdracht wissen { commandID }

  Voorbeelden .. code-blok :: geen

       bin/mattermeeste opdracht commandID matterbest opdracht wissen
~ ~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ' mmctl command list <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-command-list> ` __.


Beschrijving Alle opdrachten op opgegeven teams of alle teams standaard.

  Formaat .. code-blok :: geen

      mattermeest opdrachtlijst { team }

  Voorbeelden .. code-blok :: geen

       bin/mattermeest command list myteam mattermeeste opdracht wijzigen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Een schuine streep naar rechts wijzigen. Opdrachten kunnen worden opgegeven met de opdracht-ID. .. Opmerking:
    Alleen velden die u wilt wijzigen, moeten worden opgegeven.  Wanneer u de maker van de opdracht wijzigt, moet de opgegeven nieuwe maker de machtiging hebben om opdrachten te maken.


  Formaat .. code-blok :: geen

      mattermeeste opdracht wijzigen { commandID }

  Voorbeelden .. code-blok :: geen

       bin/matterbest opdracht wijzigen commandID -- title MyModifiedCommand --description "My Modified Command Description" -- trigger-word mycommand -- url http://localhost: 8000/my-slash-handler -- creator myusername -- response-username my-bot-username -- icon http://localhost: 8000/my-slash-handler-bot-icon.png -- autocomplete -- post

  Opties .. code-blok :: geen

          -- title string Command Title --description string Command Description -- trigger-word string Command Trigger Word -- url string Command Callback URL
          -- creator van de maker van de opdracht van de schepper van de opdrachtnemer -- antwoord-gebruikersnaam tekenreeks opdrachtantwoord gebruikersnaam -- pictogram URL voor pictogramstring
          -- autocomplete bool Toon commando in autocomplete lijst -- autocompleteDesc string Short command beschrijving voor autocomplete lijst -- autocompleteHint string Command argumenten weergegeven als hulp in autocomplete lijst -- post bool Use POST methode voor callback URL, anders gebruik GET methode mattermeeste opdracht verplaatsen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Een schuine streep naar links verplaatsen naar een ander team. Opdrachten kunnen worden opgegeven door { team }: { command-trigger-word } of met behulp van opdracht-ID ' s.

  Formaat .. code-blok :: geen

      mattermeest opdracht verplaatsen

  Voorbeelden .. code-blok :: geen

      bin/mattermost opdracht verplaatsen newteam oldteam:command-trigger-word bin/matterbest opdracht verplaatsen newteam o8soyabwthjnf9qibfztje5a36h

mattermeest opdrachtprogramma
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Toon een aangepaste slash-opdracht. Opdrachten kunnen worden opgegeven met de opdracht-ID. Retourneert opdracht-ID, team-ID, triggerwoord, weergavenaam en gebruikersnaam voor maker.

  Formaat .. code-blok :: geen

      opdracht show { commandID }

  Voorbeelden .. code-blok :: geen

      bin/mattermeest-opdrachtopdracht-ID

mattermeest config
-----------------

  Beschrijvingen voor het beheren van het configuratiebestand.

  Onderliggende opdracht
    -` matterbest config get ` _-Ophalen van de waarde van een config instelling door zijn naam in punt notatie.
    -` matterbest config migrate ` _-Migreer een bestandsgebaseerde configuratie naar (of vanuit) een database-gebaseerde configuratie.
    -` matterbest config reset ` _-Hiermee wordt de waarde van een configuratie ingesteld met de naam in de puntnotatie of een instelling.
    -` matterbest config set ` _-Stel de waarde van een config instelling in op zijn naam in de punt notatie.
    -` matterbest config show ` _-Print de huidige mat meest configuratie in een eenvoudig te lezen formaat.
    -` matterbest config validate ` _-Valideren het configuratiebestand.

mattermeest config get
~ ~ ~ ~ ~ ~ ~ ~ A Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ' mmctl config get <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-config-get> ` __.

Beschrijving Ophalen van de waarde van een configuratie-instelling met de naam in de punt-notatie.

  Formaat .. code-blok :: geen

      mattermeest configuratie ophalen { config.name }

  Voorbeelden .. code-blok :: geen

       bin/mattermeest config get SqlSettings.DriverName

 Opties .. code-blok :: geen

          -- path string Optioneel subpad; standaard is de waarde in de URL van de site. mattermeest config migreren
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Migrate a file-based configuration to (or from) a database-based configuration. Richt de Mattermeeste server op de doelconfiguratie om er gebruik van te maken. Als u SAML gebruikt, controleer dan of de SAML-certificaten en -sleutels toegankelijk zijn voor migratie naar de database. .. Opmerking:
    Als er geen parameter ' ` from ` ` is opgegeven, wordt de opdracht teruggevallen naar wat is opgegeven in -- config.

  Formaat .. code-blok :: geen

      mattermeest configuratie migreren { configuratie om te lezen } { config om te schrijven }

  Voorbeelden .. code-blok :: geen

       bin/matterbest config migrate path/to/config.json "postgres: //mmuser:mostest@dockerhost: 5432/mattermost_test?sslmode=disable &connect_timeout=10" matterbest config reset
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Resets de waarde van een config instelling door de naam in punt notatie of een instelling sectie om de standaardwaarde. Accepteert meerdere waarden voor arrayinstellingen. Als er geen parameters zijn opgegeven, worden alle configuratie-instellingen gereset.

  Formaat .. code-blok :: geen

      matterbest config reset { config.name } { instelling van sectie }

  Voorbeelden .. code-blok :: geen

       bin/mattermeest config reset SqlSettings.DriverName LogSettings Options .. code-block :: geen

        -- bevestigen bevestigen dat u de configuratie-instelling echt wilt resetten en dat er een backup is gemaakt.

mattermeest configuratie set
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Stel de waarde in van een configuratie-instelling met de naam in de punt-notatie. Accepteert meerdere waarden voor arrayinstellingen.

  Formaat .. code-blok :: geen

      mattermeest configuratieset { config.name } { instelling van nieuwe waarde }

  Voorbeelden .. code-blok :: geen

       bin/mattermeest config set SqlSettings.DriverName mysql

 Opties .. code-blok :: geen

          -- path string Optioneel subpad; standaard is de waarde in de URL van de site. mattermeest config show
~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht 'mmctl config <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-config-show>' __.

Beschrijving Print de huidige mat meest configuratie in een eenvoudig te lezen formaat.

  Formaat .. code-blok :: geen

      mattermeest config show

  Voorbeelden .. code-blok :: geen

       bin/mattermeest config show matterbest config valideren
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving zorgt ervoor dat het configuratiebestand de volgende eigenschappen heeft:

    -Is geldige JSON.
    -Heeft kenmerken van het juiste type, zoals * bool*, * int* en * str *.
    -Alle ingangen zijn geldig. U kunt bijvoorbeeld controleren of de items onder de maximumlengte liggen.

    Formaat .. code-blok :: geen

        matterbest config valideren

    Voorbeeld .. code-block :: geen

        bin/matterbest config valideren

mattermeest exporteren
-----------------

  Beschrijvingen voor het exporteren van gegevens voor naleving en voor het samenvoegen van meerdere Mattermeeste instances.

  Onderliggende opdrachten
    -` mattermeest export action ' _-Exporteer gegevens van Matterbest in Actiance XML formaat.  Vereist een E20-licentie
    -` mattermeeste export bulk ` _-Export gegevens naar een bestand compatibel met de Matterbest ` Bulk Import formaat <https://docs.mattermost.com/deployment/bulk-loading.html> ` __
    -` matterbest export csv ` _-Exporteer gegevens van Matterbest in CSV-formaat. Vereist een E20-licentie
    -` matterbest export global-relay-zip ` _-Export gegevens van Matterbest in een zip-bestand met e-mails naar Global Relay te sturen voor foutopsporing en het testen van doeleinden. Vereist een E20-licentie
    -` matterbest export schedule ` _-Plan een export job mattermeeste export actieteit
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Exportgegevens van Matterbest in de XML-indeling Actiance.

  Formaat .. code-blok :: geen

      mattermeest exportactieteit

  Voorbeeld .. code-block :: geen

      bin/mattermeest exportactie -- exportFrom=1513102632

  Opties .. code-blok :: geen

          -- exportFrom string Unix timestamp (milliseconden sinds epoch, UTC) om gegevens van te exporteren.

mattermeest export bulk
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Exporteer de exportgegevens naar een bestand dat compatibel is met het Matterbest 'Bulk Import format <https://docs.mattermost.com/deployment/bulk-loading.html>' __.

  Formaat .. code-blok :: geen

      mattermeest export bulk

  Voorbeeld .. code-block :: geen

      bin/mattermeest export bulk file.json -- all-teams

  Opties .. code-blok :: geen

	  -- all-teams bool [ REQUIRED] Exporteer alle teams van de server.

mattermeest export csv
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Exportgegevens van Matterbest in CSV-indeling.

  Formaat .. code-blok :: geen

      mattermeest export csv

  Voorbeeld .. code-block :: geen

      bin/mattermeest export csv -- exportFrom=1513102632

  Opties .. code-blok :: geen

          -- exportFrom string Unix timestamp (seconden sinds epoch, UTC) om gegevens van te exporteren.

mattermeest export global-relay-zip
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

  Exportgegevens van Matterbest in een zip-bestand met e-mails die alleen naar Global Relay kunnen worden verzonden voor foutopsporing en testdoeleinden. Dit archief bevat geen informatie in Global Relay.

  Formaat .. code-blok :: geen

      mattermeest export global-relay-zip

  Voorbeeld .. code-block :: geen

      bin/mattermeest export global-relay-zip -- exportFrom=1513102632

  Opties .. code-blok :: geen

          -- exportFrom string Unix timestamp (seconden sinds epoch, UTC) om gegevens van te exporteren.

mattermeest exportplanning
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Een exporttaak in een indeling die geschikt is voor het importeren in een archiefsysteem van een derde partij.

  Formaat .. code-blok :: geen

      mattermeest exportplanning

  Voorbeeld .. code-block :: geen

      bin/matterbest export schedule -- format=actiance -- exportFrom=1513102632

  Opties .. code-blok :: geen

          -- format string Output bestandsindeling. Momenteel wordt alleen ` ` actiantie ` ` ondersteund.
          -- exportFrom string Unix timestamp (seconden sinds epoch, UTC) om gegevens van te exporteren.
          -- timeoutSeconds tekenreeks instellen hoe lang de export moet worden uitgevoerd voordat de timeout wordt uitgevoerd.

mattermeeste groep
------------------------

  Beschrijving van opdrachten voor het beheren van Mattermeeste groepen.  Voor meer informatie over Mattermeeste groepen zie ` deze documentatie. <https://docs.mattermost.com/deployment/ldap-group-sync.html> ` _

  Onderliggende opdrachten
    -` mattermeest groepskanaal ` _-Beheer van de meeste groepen verbonden met kanalen
    -` mattermeeste groep team ` _-Beheer van Mattermeeste groepen gekoppeld aan teams mattermeeste groepskanaal
------------------------ .. Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl group channel <https: //docs.mattermost.com/administra
tion/mmctl-cli-tool.html#mmctl-group-channel> ` __.


Beschrijvingen voor het beheren van Mattermeeste groepen die aan een kanaal zijn gekoppeld.

  Onderliggende opdrachten
    -` matterbest group channel enable ' _-Hiermee kan groepsbeperking op het opgegeven kanaal
    -` mattermeest groepskanaal uitschakelen ' _-Hiermee schakelt u de groepsvoorwaarde uit op het opgegeven kanaal
    -` matterbest group channel list ` _-Lijsten de groepen die geassocieerd worden met een kanaal
    -` mattermeest groepskanaalstatus ` _-Hiermee wordt de status van de groepsvoorwaarde afgebeeld van het opgegeven kanaalmattermeest groepskanaal.
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ .. Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl group channel enable <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-channel-enable> ` __.

Beschrijving Hiermee schakelt u groepsvoorwaarde in op het opgegeven kanaal. Wanneer een kanaal groep beperkt is, wordt kanaallidmaatschap beheerd door gekoppelde groepen in plaats van beheerd door het handmatig toevoegen en verwijderen van gebruikers. Opmerking:
  Om een groepsvoorwaarde op een bepaald kanaal in te schakelen, moet u al ten minste één groep hebben. Zie ' AD/LDAP Group documentation <https: //docs.mattermost.com/deployment/ldap-group-sync.html#add-default-teams-or-channels-for-the-group> ` _ voor meer informatie over het koppelen van een groep aan een kanaal.

  Formaat .. code-blok :: geen

      mattermeest groepskanaal schakelt { team }: { channel } in

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste groepskanaal schakelt myteam in: mychannel

mattermeest groepskanaal uitschakelen
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ .. Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl group channel disable <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-channel-disable> ` __.

Beschrijving Disables group constraint op het opgegeven kanaal.

  Formaat .. code-blok :: geen

      mattermeest groepskanaal uitschakelen { team }: { channel }

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste groepskanaal uitschakelen myteam: mychannel

mattermeest groepskanaallijst
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ .. Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl group channel list <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-channel-list> ` __.

Beschrijving De groepen die aan een kanaal zijn gekoppeld.

  Formaat .. code-blok :: geen

      mattermeest groepskanaallijst { team }: { channel }

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste group channel list myteam: mychannel


mattermeest groepskanaalstatus
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ .. Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ` mmctl group channel status <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-channel-status> ` __.

Beschrijving De status van de groepsvoorwaarde van het opgegeven kanaal. Retourneert "Ingeschakeld" als kanaallidmaatschap wordt beheerd door gekoppelde groepen.  Retourneert "Uitgeschakeld" als het kanaallidmaatschap wordt beheerd door gebruikers handmatig toe te voegen en te verwijderen.

  Formaat .. code-blok :: geen

      mattermeest groepskanaalstatus { team }: { channel }

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste groepchannel status myteam: mychannel

mattermeest groepsteam
------------------------ .. Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl group team <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-team> ` __.

Beschrijvingen voor het beheren van Mattermeeste groepen die aan een team zijn gekoppeld.

  Onderliggende opdrachten
    -` matterbest group team enable ' _-Hiermee kan groepsbeperking worden ingesteld voor het opgegeven team
    -` matterbest group team uitschakelen ' _-Hiermee schakelt u de groepsvoorwaarde uit voor het opgegeven team
    -` matterbest group team list ` _-Lijsten de groepen die bij een team horen
    -` matterbest group team status ` _-Hiermee wordt de status van de groepsvoorwaarde afgebeeld van het opgegeven teamteamgroepsteam
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ .. Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl group team enable <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-team-enable> ` __.

Beschrijving Hiermee schakelt u groepsvoorwaarde in voor het opgegeven team. Wanneer een team beperkt is, wordt teamlidmaatschap beheerd door gekoppelde groepen in plaats van beheerd door handmatig uitnodigen en verwijderen van gebruikers. Opmerking:
  Om een groepsvoorwaarde in te schakelen voor een specifiek team, moet u al ten minste één groep hebben gekoppeld. Zie ' AD/LDAP Group documentation <https: //docs.mattermost.com/deployment/ldap-group-sync.html#add-default-teams-or-channels-for-the-group> ` _ voor meer informatie over het koppelen van een groep aan een team.

  Formaat .. code-blok :: geen

      mattermeest groepsteam inschakelen { team }

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste groep team inschakelen myteam mattermeeste groep team uitschakelen
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ .. Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl group team disable <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-team-disable> ` __.

Beschrijving Hiermee schakelt u de groepsvoorwaarde uit voor het opgegeven team.

  Formaat .. code-blok :: geen

      mattermeest groepsteam uitschakelen { team }

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste group team uitschakelen myteam matterbest groep team lijst
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ .. Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ' mmctl group team list <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-team-list> ` __.

Beschrijving De groepen die aan een team zijn gekoppeld.

  Formaat .. code-blok :: geen

      mattermeest groepsteamlijst { team }

  Voorbeelden .. code-blok :: geen

      bin/mattermeest groep team lijst myteam


mattermeeste groepstatus van het team
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ .. Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ` mmctl group team status <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-team-status> ` __.

Beschrijving De status van de groepsvoorwaarde van het opgegeven team. Retourneert "Ingeschakeld" als teamlidmaatschap wordt beheerd door gekoppelde groepen.  Retourneert "Uitgeschakeld" als het teamlidmaatschap wordt beheerd door gebruikers handmatig uit te nodigen en te verwijderen.

  Formaat .. code-blok :: geen

      mattermeest groeps-teamstatus { team }

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste groepsteam status myteam

mattermeest hulp
---------------

  Beschrijving Genereren van volledige documentatie in Markdown-indeling voor de Mattermeeste command line tools.

  Formaat .. code-blok :: geen

      mattermeest hulp { outputdir }

mattermeest importeren
-----------------

  Beschrijving importgegevens in Matterbest.

  Onderliggende opdracht
    -` mattermeeste import bulk ` _-Importeer een Mattermeeste Bulk importbestand.
    -` mattermeest import slack ` _-Import een team uit Slack. mattermeeste import bulk
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving importeren gegevens uit een Mattermeeste Bulk importbestand.

  Formaat .. code-blok :: geen

      matterbest import bulk { file }

  Opties .. code-blok :: geen

          -- apply Save the import data to the database. Voorzichtig gebruiken-dit kan niet worden omgedraaid.
          -- Valideren de importgegevens zonder wijzigingen aan te brengen in het systeem.
          -- werknemers int hoeveel werknemers tijdens het uitvoeren van de import worden uitgevoerd. (standaard 2)

  Voorbeeld .. code-block :: geen

      bin/mattermeest import bulk bulk-file.jsonl

mattermeest importspeling
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Import een team uit een Slack export zip-bestand.

  Formaat .. code-blok :: geen

      mattermeest importeerspeling { team } { file }

  Voorbeeld .. code-block :: geen

      bin/matterbest import slack myteam slack_export.zip

matterigste integriteit
--------------------

  Beschrijving Controleer de integriteit van het databaseschema en de referentiële integriteit van kanalen, schuine streep naar rechts, webhaken, posts, schema's, sessies, gebruikers en teams. Dit proces kan tijdelijk van invloed zijn op de prestaties van het live systeem en dient tijdens daluren te worden gebruikt.

  Formaat .. code-blok :: geen

      matterigste integriteit

  Voorbeeld .. code-block :: geen

      bin/meest integriteit -- bevestigen -- verbose

  Opties .. code-blok :: geen

          -- bevestig Optioneel. Sla het bevestigingsbericht over dat aangeeft dat de volledige integriteitscontrole de systeemprestaties tijdelijk kan schaden. Dit wordt niet aanbevolen in productieomgevingen.
	  -- verbose Outputs een gedetailleerd rapport van het aantal en type losse records, inclusief ID's (indien aanwezig).


... _command-line-tools-mattermeest-jobserver:

mattermeest jobserver
--------------------

  Beschrijving Start de Matterste taakserver.

  Formaat .. code-blok :: geen

      mattermeest jobserver

  Voorbeeld .. code-block :: geen

      bin/mattermeest jobserver

mattermeest ldap
---------------

  Beschrijvingen voor het configureren en synchroniseren van AD/LDAP.

  Onderliggende opdracht
    -` mattermeest ldap idmigrate ` _-Het LDAP-ID-kenmerk migreren naar een nieuwe waarde
    -` mattermeest ldap sync ` _-Synchroniseren nu mattermeeste ldap idmigrate
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving LDAP-ID-kenmerk migreren naar nieuwe waarde.

    Voer dit hulpprogramma uit om de waarde van uw ID-kenmerk te wijzigen zonder dat uw gebruikers hun accounts verliezen. Nadat u de opdracht hebt uitgevoerd, kunt u het ID-kenmerk wijzigen in de nieuwe waarde in uw ` `config.json ` `. Bijvoorbeeld, als uw huidige ID-kenmerk ` ` sAMAccountName ` ` was en u het wilde wijzigen in ` ` objectGUID ` `, zou u:

    1. Wacht op een off-piektijd als uw gebruikers niet worden beïnvloed door een herstart van de server.
    2. Voer de opdracht ` ` matterbest ldap idmigrate objectGUID ` ` uit.
    3. Bewerk uw ` `config.json ` ` en wijzig uw ` ` IdAttribute ` ` veld naar de nieuwe waarde ` ` objectGUID ` ` `.
    4. Start de Matterigste server opnieuw op.

  Formaat .. code-blok :: geen

      matterbest ldap idmigrate { attribute }

  Voorbeeld .. code-block :: geen

      bin/matterbest ldap idmigrate objectGUID mattermeeste ldap sync
~ ~ ~ ~ ~ ~ ~ ~ ~ A .. Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ' mmctl ldap sync <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-ldap-sync> ` __.

Beschrijving Alle AD/LDAP-gebruikers nu synchroniseren.

  Formaat .. code-blok :: geen

      mattermeeste ldap-synchronisatie

  Voorbeeld .. code-block :: geen

      bin/mattermeeste ldap-synchronisatie

mattermeeste licentie
------------------

  Beschrijving van opdrachten voor het beheren van licenties.

  Onderliggende opdracht
    -` mattermeeste licentie uploaden ` _-Upload een licentie.

mattermeeste licentie-upload
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ' mmctl license upload <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-license-upload> ` __.

Beschrijving Upload een licentie. Deze opdracht vervangt de huidige licentie als er al een licentie is geüpload.

  Formaat .. code-blok :: geen

      mattermeeste licentie uploaden { license }

  Voorbeeld .. code-block :: geen

      bin/mattermeest licentie uploaden /pad/naar/license/mylicensefile.mattermeest-licentie .. Opmerking:
  De Matterendste server moet opnieuw worden gestart nadat u een licentiebestand hebt geüpload om de wijzigingen van kracht te laten worden. Voor clusterinstellingen moet het licentiebestand ook worden geüpload naar elk knooppunt.

mattermeeste logboeken
------------------ .. Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ` mmctl logs <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-logs> ` __.

Beschrijving Toont Mattermeeste Logs in een menselijk leesbare indeling.

  Formaat .. code-blok :: geen

      mattermeeste logboeken

  Voorbeeld .. code-block :: geen

      bin/mattermeeste logboeken -- logrus

  Opties .. code-blok :: geen

          -- logrus Geeft Mattermeeste logs weer in ` logrus format <https://github.com/sirupsen/logrus> ` _. Else, de standaarduitvoer wordt geretourneerd.


mattermeeste machtigingen
----------------------

  Beschrijvingen voor het beheren van geavanceerde machtigingen.

  Onderliggende opdrachten
    -` mattermeeste machtigingen exporteren ` _-Export Schemes en Rollen.
    -` mattermeeste machtigingen importeren ' _-Invoerschema's en rollen van een exportmachtiging.
    -` mattermeeste machtigingen reset ` _-Reset het machtigingen systeem naar de standaard toestand op nieuwe installaties.

mattermeeste machtigingen exporteren
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Ng~

  Description Prints om een jsonl representatie van Schema's en Rollen uit een Mattermeeste instantie stdout. Wordt gebruikt voor het exporteren van rollen en schema's van de ene Matterinstance naar de andere. De uitvoer is een jsonl-representatie met elke regel met een json-representatie van een schema en de bijbehorende rollen. De uitvoer is bedoeld om te worden gebruikt als invoer van ` mattermeeste machtigingen importeren '.

  Formaat .. code-blok :: geen

      mattermeeste machtigingen exporteren

  Voorbeeld .. code-block :: geen

      bin/mattermeeste permissies exporteren > my-permissions-export.jsonl

mattermeeste machtigingen importeren
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Ng~

  Beschrijving Maakt rollen en schema's op een Matterbest-instance van een jsonl-invoerbestand in de indeling die wordt uitgevoerd door ` mattermeeste machtigingen exporteren '.

  Formaat .. code-blok :: geen

      mattermeeste machtigingen importeren { bestand }

  Voorbeeld .. code-block :: geen

      bin/mattermeeste machtigingen importeren my-permissions-export.jsonl

mattermeeste toestemmingen resetten
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Reset machtigingen voor alle gebruikers, met inbegrip van Admins, naar hun standaard toestand op nieuwe installaties. Opmerking: ** hiermee worden alle aangepaste schema's * * gewist.

  Formaat .. code-blok :: geen

      mattermeeste toestemmingen resetten

  Voorbeeld .. code-block :: geen

      bin/mattermeeste toestemmingen resetten

  Opties .. code-blok :: geen

          -- bevestigen bevestigen dat u het machtigingssysteem echt opnieuw wilt instellen en er is een DB-backup uitgevoerd.

mattermeeste plugin
-----------------

  Beschrijvingen voor het beheren van plugins.

  Onderliggende opdrachten
    -` matterbest plugin add ` _-plugins toevoegen aan uw Mattertiste server.
    -` matterbest plugin delete ` _-Verwijder eerder geüploade plugins.
    -` matterbest plugin uitschakelen ` _-Uitschakelen plugins.
    -` matterbest plugin enable ` _-Enable plugins voor gebruik.
    -` mattermeeste plugin lijst ` _-List plugins geïnstalleerd op uw Mattermeeste server.

mattermeeste plugin toevoegen
~ ~ ~ ~ ~ ~ ~ ~ A Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ' mmctl add <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-plugin-add> ` __.

Beschrijving Voeg plugins toe aan uw Mattertiste server. Als u meerdere plugins toevoegt, gebruikt u een door spaties gescheiden lijst.

  Formaat .. code-blok :: geen

      mattermeeste plugin toevoegen { plugin tar-bestand }

  Voorbeeld .. code-block :: geen

      bin/matterbest plugin add hovercardexample.tar.gz pluginexample.tar.gz

mattermeeste plugin verwijderen
~ ~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt vervangen in een futur
De release met de mmctl-opdracht ` mmctl plugin delete <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-plugin-delete> ` __.

Beschrijving Verwijder eerder geüploade plugins van uw Mattertiste server. Als u meerdere plugins wist, gebruik dan een door spaties gescheiden lijst.

  Formaat .. code-blok :: geen

      mattermeeste plugin wissen { plugin_id }

  Voorbeeld .. code-block :: geen

      bin/mattermeeste plugin delete hovercardexample pluginvoorbeeld mattermeeste plugin uitschakelen
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ` mmctl plugin disable <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-plugin-disable> ` __.

Beschrijving Uitschakelen van plugins. Uitgeschakelde plugins worden onmiddellijk verwijderd uit de gebruikersinterface en afgemeld van alle sessies. Als u meerdere plugins uitschakelt, gebruikt u een door spaties gescheiden lijst.

  Formaat .. code-blok :: geen

      matterbest plugin uitschakelen { plugin_id }

  Voorbeeld .. code-block :: geen

      bin/mattermeeste plugin uitschakelen hovercardexample pluginvoorbeeld mattermeeste plugin inschakelen
~ ~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-plugin voor de mmctl-plugin <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-plugin-enable> ` __.

Beschrijving Enable plugins voor gebruik op uw Mattermeeste server. Als u meerdere plugins inschakelt, gebruikt u een door spaties gescheiden lijst.

  Formaat .. code-blok :: geen

      matterbest plugin inschakelen { plugin_id }

  Voorbeeld .. code-block :: geen

      bin/mattermeeste plugin inschakelen hovercardexample pluginvoorbeeld mattermeeste plugin lijst
~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl plugin list <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-plugin-list> ` __.

Beschrijving Alle actieve en inactieve plugins geïnstalleerd op uw Mattermeeste server.

  Formaat .. code-blok :: geen

      mattermeeste plugin lijst

  Voorbeeld .. code-block :: geen

      bin/mattermeeste plugin lijst

mattermeest reset
----------------

  Beschrijving Volledig wissen van de database waardoor het verlies van alle gegevens. Dit resets Matterbest tot zijn oorspronkelijke staat.

  Formaat .. code-blok :: geen

      mattermeest reset

  Opties .. code-blok :: geen

          -- bevestigen bevestigen dat u alles wilt wissen en er is een DB-backup uitgevoerd.

mattermeeste rollen
----------------

  Beschrijvingen voor het beheren van gebruikersrollen.

  Onderliggende opdrachten
    -` mattermeest rollen-lid ` _-Systeembeheermachtigingen verwijderen van een gebruiker
    -` mattermeest rollen system_admin ` _-Maak een gebruiker in een System Admin mattermeest rollen lid
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Verwijder de machtigingen voor systeembeheer van een gebruiker.

  Formaat .. code-blok :: geen

      mattermeest rollen lid { gebruikers }

  Voorbeeld .. code-block :: geen

      bin/mattermeest rollen lid user1

mattermeest rollen systeem\_admin
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Ng~

  Beschrijving Bevorderen van een gebruiker naar een systeembeheerder.

  Formaat .. code-blok :: geen

      mattermeest rollen system_admin { users }

  Voorbeeld .. code-block :: geen

      bin/mattermeest rollen system_admin user1

mattermeeste sampledata
---------------------

  Beschrijving .. versiontoegevoegd:: 4.7
      Voorbeeldgegevens genereren en de meest overeenkomende database vullen. Ondersteund in Mattermeest v4.7 en later.

      De opdracht genereert één gebruiker als systeembeheerder met een gebruikersnaam ` ` sysadmin ` ` en wachtwoord ` ` Sys@dmin-sample1 ` ` `. Andere gebruikers worden gegenereerd na een index, bijvoorbeeld met de gebruikersnaam ` ` user-1 ` ` ` en wachtwoord ` ` SampleUs@r-1 ` ` `.

  Formaat .. code-blok :: geen

      mattermeeste sampledata

  Voorbeeld .. code-block :: geen

      bin/mattermeeste sampledata -- seed 10 -- teams 4 -- gebruikers 30

  Opties .. code-blok :: geen

          -u, -- users int Het aantal monstergebruikers. (standaard 15)
              -- profile-images string Optioneel. Pad naar map met afbeeldingen om willekeurig als gebruikersprofiel te kiezen.
          -t, -- teams int Het aantal voorbeeldteams. (standaard 2)
              -- teamlidmaatschappen int Het aantal voorbeeldteamlidmaatschappen per gebruiker. (standaard 2)
              --kanalen-per-team int Het aantal monsterkanalen per team. (standaard 10)
              -- channel-lidmaatschappen int Het aantal monsterkanaallidmaatschappen per gebruiker in een team. (standaard 5)
              --postings-per-kanaal int Het aantal sample post per kanaal. (standaard 100) --direct-kanalen int Het aantal directe berichtenkanalen van het monster. (standaard 30)
              -- group-channels int The number of sample group message channels. (standaard 15)
              --postings-per-direct-kanaal int Het aantal sample posts per direct bericht kanaal. (standaard 15)
              --posts-per-groep-kanaal int Het aantal sample post per groep berichtenkanaal. (standaard 30)
          -s, -- seed int Seed gebruikt voor het genereren van willekeurige gegevens (verschillende zaden genereren verschillende gegevens). (standaard 1)
          -b, -- bulk string Optioneel. Pad om een JSONL-bestand te schrijven in plaats van in de database te laden.
          -w, -- werknemers int hoeveel werknemers tijdens het importeren moeten worden uitgevoerd. (standaard 2)

mattermeeste server
-----------------

  Beschrijving Voert de Mattermeeste server uit.

  Formaat .. code-blok :: geen

      mattermeeste server

mattermeeste team
---------------

  Beschrijvingen om teams te beheren.

  Onderliggende opdrachten
    -` mattermeeste team toevoegen ` _-Gebruikers toevoegen aan een team.
    -` mattermeeste team archief ` _-Archief teams gebaseerd op naam.
    -` mattermeeste team maken ` _-Maak een team.
    -` mattermeeste team delete ` _-Verwijder een team.
    -` mattermeeste teamlijst ` _-Lijst van alle teams.
    -` mattermeeste team modify ` _-Wijzig het openbaar/private type van een team.
    -` mattermeeste team verwijderen ` _-Verwijder gebruikers uit een team.
    -'mattermeeste team hernoemen' _-Hernoem een team.
    -` matterbest team restore ` _-Herstel een eerder gearchiveerd team.
    -` mattermeeste team zoeken ` _-Zoeken naar teams gebaseerd op naam. .. _teamwaarde-opmerking: .. Opmerking:
    ** { teamnaam } waarde * *

    Voor de opdrachten * add*, * delete* en * remove * kunt u de waarde * { teamnaam } * bepalen op basis van de URL's die u gebruikt voor toegang tot uw instance van Matterbest. In de volgende URL is de waarde * { teamnaam } * bijvoorbeeld * mijnteam*:

    ` ` https: //example.com/myteam/channels/mychannel ` `

    Ook moeten het team en de kanaalnamen in de URL in kleine letters worden geschreven.

mattermeeste team toevoegen
~ ~ ~ ~ ~ ~ ~ A Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl team toevoegen <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-add> ` __.

Beschrijving gebruikers toevoegen aan een team. Voordat u deze opdracht uitvoert, gaat u naar de :ref: ` note about { team-name } <team-value-note>`.

  Formaat .. code-blok :: geen

      mattermeeste team toevoegen { teamnaam } { gebruikers }

  Voorbeeld .. code-block :: geen

      bin/mattermeeste team toevoegen mijnteam user@example.com gebruikersnaam mattermeeste team archief
~ ~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl team archive <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-archive> ` __.


Beschrijving Archive teams op basis van naam. Voordat u deze opdracht uitvoert, gaat u naar de :ref: ` note about { team-name } <team-value-note>`.

  Formaat .. code-blok :: geen

      mattermeest teamarchief { team }

  Voorbeelden .. code-blok :: geen

       bin/mattermeeste team archief team1

mattermeeste team maken
~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl team create <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-create> ` __.

Beschrijving Een team maken.

  Formaat .. code-blok :: geen

      mattermeeste team maken

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste team create -- name mynewteam --display_name "My New Team"
      bin/mattermeeste teams maken -- name private --display_name "My New Private Team" -- private

  Opties .. code-blok :: geen

          --display_name string Team Weergavenaam -- email string Administrator Email (iedereen met deze e-mail is automatisch een teamadmin)
          -- name string Team Naam -- private Maak een besloten team.

mattermeeste team wissen
~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl team delete <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-delete> ` __.

Beschrijving Permanent verwijderen een team samen met alle gerelateerde informatie, met inbegrip van berichten uit de database. Voordat u deze opdracht uitvoert, gaat u naar de :ref: ` note about { team-name } <team-value-note>`.

  Formaat .. code-blok :: geen

      mattermeeste team wissen { teamnaam }

  Voorbeeld .. code-block :: geen

      bin/mattermeeste team verwijderen mijnteam

  Opties .. code-blok :: geen

          -- bevestigen bevestigen dat u het team echt wilt wissen en er is een DB-backup uitgevoerd.

mattermeeste teamlijst
~ ~ ~ ~ ~ ~ ~ ~ ~ A .. Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl team list <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-list> ` __.

*Ondersteund in Mattermeest v4.10 en hoger *

  Beschrijving Alle teams op de server.

  Formaat .. code-blok :: geen

      mattermeeste teamlijst

  Voorbeeld .. code-block :: geen

      bin/mattermeeste teamlijst mattermeeste team wijzigen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Het openbaar/persoonlijk type van een team wijzigen.

  Formaat .. code-blok :: geen

      mattermeeste team wijzigen [ team] [ vlag]

  Voorbeeld .. code-block :: geen

      bin/mattermeeste team myteam -- private bin/mattermeeste team myteam -- public

mattermeeste team verwijderen
~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl team remove <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-remove> ` __.

Beschrijving verwijderen van gebruikers uit een team. Voordat u deze opdracht uitvoert, gaat u naar de :ref: ` note about { team-name } <team-value-note>`.

  Formaat .. code-blok :: geen

      mattermeeste team verwijderen { teamnaam } { gebruikers }

  Voorbeeld .. code-block :: geen

      bin/mattermeeste team verwijderen mijnteam user@example.com gebruikersnaam mattermeeste team hernoemen
~ ~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-teamnaam van het mmctl-team <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-rename> ` __.

Beschrijving Hernoemen van een team.

  Formaat .. code-blok :: geen

      mattermeeste teamnaam wijzigen naam { team } newteamname --display_name "Nieuwe weergavenaam"

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste team hernoemen mijnteam newteamname --display_name "New Display Name"

  Opties .. code-blok :: geen

      --display_name string Team Display Naam mattermeeste team herstellen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Herstel een eerder gearchiveerd team.

  Formaat .. code-blok :: geen

      mattermeeste team herstellen { team }

  Voorbeeld .. code-block :: geen

      bin/mattermeeste team herstellen mijnteam mattermeeste team zoeken
~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ' mmctl team search <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-search> ` __.

Beschrijving Zoeken naar teams gebaseerd op naam. Voordat u deze opdracht uitvoert, gaat u naar de :ref: ` note about { team-name } <team-value-note>`.

  Formaat .. code-blok :: geen

      mattermeeste team zoeken { team }

  Voorbeelden .. code-blok :: geen

       bin/mattermeeste team zoeken team1

mattermeeste gebruiker
---------------

  Beschrijvingen om gebruikers te beheren.

  Onderliggende opdrachten

    -` mattermeeste gebruiker activeren ` _-Een gebruiker activeren
    -` mattermeeste gebruiker converteren ` _-Converteer een gebruiker naar een bot, of een bot naar een gebruiker
    -` matterbest user create ` _-Een gebruiker aanmaken
    -` mattermeeste gebruiker deactiveren ` _-Deactiveren van een gebruiker
    -` matterbest user delete ` _-Verwijder een gebruiker en alle berichten
    -` mattermeeste user deleteall ` _-Verwijder alle gebruikers en alle berichten
    -` mattermeeste user email ` _-Een e-mail van een gebruiker instellen
    -` matterbest user invite ` _-Stuur een gebruiker een e-mail uitnodiging naar een team
    -` mattermeeste gebruiker migrate_auth ` _-Mass migreert alle gebruikersaccounts naar een nieuw verificatietype
    -` matterbest user password ` _-Het wachtwoord van een gebruiker instellen
    -` mattermeest user resetmfa ` _-Schakel MFA uit voor een gebruiker
    -` matterbest user search ` _-Zoeken naar gebruikers op basis van gebruikersnaam, e-mailadres of gebruikers-ID
    -` matterbest user verify ` _-Controleer het e-mailadres van een nieuwe gebruiker ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ out

mattermeeste gebruiker activeren
~ ~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ` mmctl user activate <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-activate> ` __.

Beschrijving activeren gebruikers die zijn gedeactiveerd. Als u meerdere gebruikers activeert, moet u een door spaties gescheiden lijst gebruiken.

  Formaat .. code-blok :: geen

      mattermeeste gebruiker activeren { e-mails, gebruikersnamen, userIds }

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste gebruiker activeren user@example.com bin/mattermeeste gebruiker activeren gebruikersnaam1 gebruikersnaam2

mattermeeste gebruiker converteren
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Converteer een gebruiker naar een bot, of converteer een bot naar een gebruikersaccount.

  Formaat .. code-blok :: geen

      mattermeeste gebruiker converteren { emails, usernames, userIds } -- bot OR mattermeeste gebruiker converteren { bot_id } -- user -- email { email_address }--password { new_password }

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste gebruiker converteren user@example.com -- bot bin/mattermeeste gebruiker converteren gebruikersnaam1 gebruikersnaam2 -- bot bin/meeste gebruiker convert old_bot -- user -- email real_user@example.com--password Password1


  Opties .. code-blok :: geen

          -- bot string Converteer gebruiker naar bot.  Ondersteunt het omzetten van meerdere bots tegelijk, gebruik maken van een ruimte-gescheiden lijst.
          -- user string Convert bot naar gebruiker.  Ondersteunt het converteren van 1 account per opdracht. De geconverteerde gebruiker heeft de rol van ` system_user ` set.

mattermeeste gebruiker maken
~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ` mmctl user create <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-create> ` __.


Beschrijving Een gebruiker maken.

  Formaat .. code-blok :: geen

      mattermeeste gebruiker maken

  Voorbeelden .. code-blok :: geen

      bin/matterbest user create -- email user@example.com -- username userexample--password Password1
      bin/matterbest user create -- firstname Joe -- system_admin -- email joe@example.com -- username joe--password Password1

  Opties .. code-blok :: geen

          -- email string Email -- firstname string First Name -- lastname string Last Name -- locale string Locale (ex: en, fr)
          -- nickname string Nickname--password string Password -- system_admin Maak de gebruiker een systeembeheerder -- gebruikersnaam string Gebruikersnaam mat meest gebruiker deactiveer
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ` mmctl user deactiveren <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-deactivate> ` __.

Beschrijving Deactiveren van een gebruiker. Gedeactiveerde gebruikers worden onmiddellijk afgemeld van alle sessies en kunnen zich niet aanmelden.

  Formaat .. code-blok :: geen

      mattermeeste gebruiker deactiveren { e-mails, gebruikersnamen, userIds }

  Voorbeelden .. code-blok :: geen

      bin/matterbest user deactiveren user@example.com bin/mattermeeste gebruiker deactiveren gebruikersnaam

  .. opmerking:
    Gebruikers die via deze CLI-opdracht worden gedeactiveerd, kunnen Matterbest blijven gebruiken als ze al zijn aangemeld, totdat de gebruikerscache handmatig is verwijderd of na 30 minuten automatisch wordt verwijderd. Gebruikers die gedeactiveerd zijn als ze niet zijn aangemeld, kunnen zich niet opnieuw aanmelden bij Matterbest.

    Als u de sessie van een gedeactiveerde gebruiker onmiddellijk wilt beëindigen, moet u alle caches in ** Systeemconsole > Webserver > Alle Caches * * opschonen na het uitvoeren van deze opdracht.

    U kunt ook de ` API-opdracht <https: //api.mattermost.com/#tag/users%2Fpaths%2F ~ 1users ~ 1%7Buser_id%7D%2Fdelete> ` _ gebruiken om een gebruikersaccount te deactiveren en de sessie onmiddellijk te beëindigen.

mattermeeste gebruiker wissen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Permanent verwijderen van een gebruiker en alle gerelateerde informatie, met inbegrip van berichten uit de database.

    De inhoud van de bestandsopslag wordt niet gewist. U kunt handmatig alle uploads van bestanden voor een bepaalde gebruiker wissen als uploads het veld ` ` CreatorId ` ` bevatten. Avatars voor gebruiker worden opgeslagen in ` ` data/users/<userid>/profile.png ` `.

  Formaat .. code-blok :: geen

      matterbest gebruiker wissen { gebruikers }

  Voorbeeld .. code-block :: geen

      bin/mattermeeste gebruiker verwijderen user@example.com

  Opties .. code-blok :: geen

          -- bevestigen bevestigen dat u de gebruiker echt wilt wissen en er is een DB-backup uitgevoerd.

mattermeest gebruiker deleteall
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Permanent verwijderen alle gebruikers en alle gerelateerde informatie, met inbegrip van berichten.

    De inhoud van de bestandsopslag wordt niet gewist. U kunt handmatig alle uploads en avatars verwijderen. Alle uploads bevatten het veld ` ` CreatorId ` ` en de gebruikeravatars worden opgeslagen in ` ` data/users/<userid>/profile.png ` `.

  Formaat .. code-blok :: geen

      mattermeest gebruiker deleteall

  Voorbeeld .. code-block :: geen

      bin/mattermeest gebruiker deleteall

  Opties .. code-blok :: geen

          -- bevestigen bevestigen dat u de gebruiker echt wilt wissen en een DB-backup is perfo geweest
rmed.

mattermeeste gebruikeremail
~ ~ ~ ~ ~ ~ ~ ~ A Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door het mmctl-commando ` mmctl user email <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-email> ` __.


Beschrijving Set a user's email.

  Formaat .. code-blok :: geen

       mattermeest user email { user } { new email }

  Voorbeeld .. code-block :: geen

      bin/mattermeest gebruiker e-mail user@example.com newuser@example.com

mattermeest gebruiker uitnodigen
~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ` mmctl user invite <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-invite> ` __.


Beschrijving Stuur een gebruiker een e-mail uit te nodigen voor een team. U kunt een gebruiker uitnodigen voor meerdere teams door de teamnamen of team-ID's op te geven.

  Formaat .. code-blok :: geen

      mattermeest gebruiker uitnodigen { e-mail } { teams }

  Voorbeelden .. code-blok :: geen

      bin/mattermeeste gebruiker uitnodigen user@example.com mijnteam bin/mattermeeste gebruiker uitnodigen user@example.com mijnteam1 mijnteam2

mattermeeste gebruiker migrate_auth
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ .. _cli-user-migrate-auth:

  Beschrijving Migreert alle bestaande Mattermeeste gebruikersaccounts van de ene verificatieprovider naar de andere. U kunt bijvoorbeeld uw verificatieprovider upgraden van e-mail naar AD/LDAP of van AD/LDAP naar SAML. In de uitvoer worden alle accounts afgebeeld die niet zijn gemigreerd. Deze accounts kunnen worden geblokkeerd vanwege de filters in uw AD/LDAP-configuratie in de systeemconsole.

** Migreren naar AD/LDAP* *

  Parameters
    -` ` from_auth ` `: De verificatieservice van waaruit gebruikersaccounts worden gemigreerd. Ondersteunde opties: ` ` email ` `, ` ` gitlab ` ` `, ` ` saml ` ` `.

    -` ` to_auth ` `: De verificatieservice om gebruikersaccounts te migreren. Ondersteunde opties: ` ` ldap ` `.

    -` ` match_field ` ` `: Het veld dat gegarandeerd hetzelfde is in beide verificatieservices. Bijvoorbeeld, als de gebruikers e-mails consistent zijn ingesteld op e-mail. Ondersteunde opties: ` ` email ` ` `, ` ` username ` `.

  Formaat .. code-blok :: geen

      mattermeeste gebruiker migrate_auth { from_auth } ldap { match_field }

  Voorbeeld .. code-block :: geen

      bin/mattermeeste gebruiker migrate_auth email ldap e-mail Opties .. code-blok :: geen

      -- force duplicaatvermeldingen op de AD/LDAP-server negeren.
      --dryRun een simulatie van het migratieproces uitvoeren zonder de database te wijzigen.

** Migreren naar SAML* *

*Ondersteund in Matterbest v4.8 en later *

  Parameters

    -` ` from_auth ` `: De verificatieservice van waaruit gebruikersaccounts worden gemigreerd. Ondersteunde opties: ` ` email ` `, ` ` gitlab ` `. ` ` ` ldap ` ` `.

    -` ` to_auth ` `: De verificatieservice om gebruikersaccounts te migreren. Ondersteunde opties: ` ` saml ` ` `.

    -` ` users_file ` `: Het pad van een JSON-bestand met de gebruikersnamen en e-mails van alle gebruikers om naar SAML te migreren. De gebruikersnaam en e-mail moeten dezelfde zijn als in uw SAML-serviceprovider. Bovendien moet de e-mail overeenkomen met het e-mailadres van het Mattermost gebruikersaccount. Hieronder volgt een voorbeeld van het gebruikersbestand:

    .. code-blok :: json

        {
          "user1@email.com": "username.one", "user2@email.com": "username.two"
        }

  Gebruikers van bestandsgenerering Genereren van ` ` users_file ` ` is afhankelijk van hoe het systeem is geconfigureerd en welke SAML service provider wordt gebruikt. Hieronder vindt u twee voorbeeldscripts voor OneLogin en Okta service providers. Voor ADFS kunt u het AD/LDAP-protocol gebruiken om de gebruikers rechtstreeks te extraheren en naar een JSON-bestand te exporteren.

    Nadat u de ` ` users_file ` ` hebt gegenereerd, kunt u het bestand handmatig bijwerken om een lijst te verkrijgen van de meest overeenkomende gebruikersaccounts die u naar SAML wilt migreren. Houd er rekening mee dat gebruikers die zijn opgenomen in ` ` users_file ` ` die nog niet bestaan in Matterbest worden genegeerd tijdens het migratieproces.

    OneLogin:

    .. code-block :: python

        van onelogin.api.client import OneLoginClient import json

        client_id = invoer ("Client-ID:")
        client_secret = invoer ("Geheim:")
        region = input ("Region (us, eu):")

        client = OneLoginClient (client_id, client_secret, regio)

        toewijzing = { } voor gebruiker in client.get_users (): mapping [ user.email] = user.username

        met bestand ("saml_users.json "," w") als fd:
            json.dump (toewijzing, fd)

    Okta's:

    .. code-block :: python

        uit okta import UsersClient import json

        base_url = invoer ("Basis url (voorbeeld: https://example.okta.com):")
        api_token = invoer ("API-token:")

        usersClient = UsersClient (base_url, api_token)

        gebruikers = usersClient.get_paged_users (limit=25)

        toewijzing = { }

        voor gebruiker in users.result: mapping [ user.profile.email] = user.profile.login

        terwijl niet users.is_last_page (): users = usersClient.get_paged_users (url=users.next_url) voor gebruiker in users.result: mapping [ user.profile.email] = user.profile.login

        met bestand ("saml_users.json "," w") als fd:
            json.dump (toewijzing, fd)

    ADFS:

    .. code-block :: python

        import ldap import json import getpass

        ldap_host = input ('Ldap Host (voorbeeld ldap://localhost: 389):')
        base_dn = input ('Base DN (voorbeeld dc = mm, dc = test, dc = com):')
        bind_dn = invoer ('Bind-DN (voorbeeld ORGANIZATION\username):') wachtwoord = getpass.getpass ('Wachtwoord: ')
        user_object_class = invoer ('gebruikersobjectklasse (voorbeeld organizationalPerson):')
        gebruikersnaam_veld = invoer (veld Gebruikersnaam (voorbeeld sAMAccountName): ')
        mail_field = input ('Mail field (voorbeeld mail):')

        l = ldap.initialize (ldap_host)
        l.simple_bind_s (bind_dn, wachtwoord)
        page_control = ldap.controls.libldap.SimplePagedResultsControl (True, size=1000, cookie = '') r = l.search_ext (base_dn, ldap.SCOPE_SUBTREE, '(objectClass =' + user_object_class + ')', [ gebruikersnaam_veld, mail_field], serverctrls = [ pagina_control])

        toewijzing = { } terwijl True: rtype, rdata, rmsgid, serverctrls = l.result3 (r)

            voor dn, item in rdata: indien mail_field in entry and len (entry [ mail_field]) > = 1 en gebruikersnaam_veld in entry en len (item [ gebruikersnaam_veld]) > = 1: mapping [ entry [ mail_field] [ 0] .decode ('utf-8')] = item [ gebruikersnaam_veld] [ 0] .decode ('utf-8')

            besturingselementen = [ control for control in serverctrls if control.controlType == ldap.controls.libldap.SimplePagedResultsControl.controlType] if not controls:
                print ('The server negeert RFC 2696 control') break if not controls [ 0] .cookie: break page_control.cookie = controls [ 0] .cookie r = l.search_ext (base_dn, ldap.SCOPE_SUBTREE, '(objectClass =' + user_object_class + ')', [ username_field, mail_field], serverctrls = [ page_control])

        met open ("saml_users.json "," w") als fd:
            json.dump (toewijzing, fd)

  Formaat .. code-blok :: geen

      mattermeeste gebruiker migrate_auth { from_auth } saml { users_file }

  Voorbeeld .. code-block :: geen

      bin/mattermeeste gebruiker migrate_auth email saml users.json

  Opties .. code-blok :: geen

      -- automatisch alle gebruikers zonder { users_file } automatisch migreren. Hiermee wordt ervan uitgegaan dat de gebruikersnamen en e-mails identiek zijn tussen de Matteristen en de SAML-services.
      --dryRun een simulatie van het migratieproces uitvoeren zonder de database te wijzigen. Nuttig om te testen of de migratie resulteert in fouten. U kunt deze optie gebruiken met of zonder { users_file }.

mattermeeste gebruikerswachtwoord
~ ~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ' mmctl user reset_password <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-reset-password> ` __.


Beschrijving Het wachtwoord van een gebruiker instellen.

  Formaat .. code-blok :: geen

      mattermeest gebruikerswachtwoord { gebruiker } { wachtwoord }

  Voorbeeld .. code-block :: geen

      bin/mattermeeste gebruikerswachtwoord user@example.com Password1

mattermeest gebruikersresetmfa
~ ~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ` mmctl user resetmfa <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-resetmfa> ` __.


Beschrijving Schakelt multi-factor verificatie uit voor een gebruiker. Als de MFA-handhaving is ingeschakeld, wordt de gebruiker gedwongen MFA opnieuw in te schakelen met een nieuw apparaat zodra ze zich aanmelden.

  Formaat .. code-blok :: geen

      matterbest user resetmfa { users }

  Voorbeeld .. code-block :: geen

      bin/meest gebruiker resetmfa user@example.com

mattermeeste gebruiker zoeken
~ ~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ ~ > Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ` mmctl user search <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-search> ` __.


Beschrijving Zoeken voor gebruikers op basis van gebruikersnaam, e-mailadres of gebruikers-ID.

  Formaat .. code-blok :: geen

      matterbest gebruiker zoeken { gebruikers }

  Voorbeeld .. code-block :: geen

      bin/mattermeeste gebruiker zoeken user1@example.com user2@example.com

mattermeest gebruikersverificatie
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Het e-mailadres van een nieuwe gebruiker controleren.

  Formaat .. code-blok :: geen

      mattermeest gebruiker controleren { gebruikers }

  Voorbeeld .. code-block :: geen

      bin/mattermeest gebruiker controleren user1

mattermeest versie
------------------ .. Opmerking:

   Deze opdracht wordt in een toekomstige release vervangen door de mmctl-opdracht ' mmctl versie <https: //docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-version> ` __.


Beschrijving De meest overeenkomende versie-informatie.

  Formaat .. code-blok :: geen

      mattermeest versie

mattermeest webhook
------------------

  Beschrijvingen om webhooks te beheren.

  Onderliggende opdrachten
    -` mattermeest webhook create-incoming ` _-Maak een inkomende webhook binnen een specifiek kanaal.
    -` mattermeest webhook create-uitgaande ` _-Maak een uitgaande webhook binnen een specifiek kanaal.
    -` mattermeest webhook delete ` _-Verwijder inkomende en uitgaande webhooks.
    -` mattermeest webhook lijst ` _-Lijst alle webhaken.
    -` matterbest webhook modify-incoming ` _-Wijzig een bestaande inkomende webhook door de titel, beschrijving, kanaal of pictogram-URL te wijzigen.
    -` matterbest webhook modify-uitgaande ` _-Wijzig een bestaande uitgaande webhook door de titel, beschrijving, kanaal, pictogram, URL, inhoudstype en triggers te wijzigen.
    -` mattermeest webhook move-uitgaande ` _-Verplaats een bestaande uitgaande webhook met een ID.
    -` mattermeest webhook show ` _-Toon informatie over een webhook door het verstrekken van het webhook ID. mattermeest webhook create-inkomend
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

  Beschrijving Een binnenkomende webhook maken binnen een specifiek kanaal.

  Formaat .. code-blok :: geen

      mattermeeste webhook maken-inkomend

  Voorbeelden .. code-blok :: geen

       bin/mattermost webhook create-incoming -- channel [ channelID] -- user [ userID] --display-name [ display-name] --description [ webhookDescription]--lock-to-channel -- icon [ iconURL]

  Opties .. code-blok :: geen

          -- kanaal-ID kanaal
          -- Gebruikers-ID gebruikerstekenreeks
          --display-name string Inkomende webhook weergavenaam --description string Inkomende webhook beschrijving--lock-to-channel boolean (True/False) Inkomende webhook vergrendelen aan kanaal -- icon [ iconURL] Pictogram URL-URL mattermeest webhook create-uitgaande
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

  Beschrijving Een uitgaande webhook maken waarmee externe berichten van een bepaald kanaal kunnen worden geplaatst.

  Formaat .. code-blok :: geen

      mattermeest webhook create-uitgaande

  Voorbeelden .. code-blok :: geen

       bin/mattermost webhook create-uitgaande -- team myteam -- channel mychannel -- user myusername --display-name mijnwebhook --description "My cool webhook" -- trigger-when start -- trigger-word "build" -- icon http://localhost: 8000/my-slash-handler-bot-icon.png -- url http://localhost: 8000/my-webhook-handler -- content-type "application/json"

       bin/mattermost webhook create-uitgaande -- team myotherteam -- channel mychannel -- user myusername --display-name myotherwebhook --description "My cool webhook" -- trigger-if exact -- trigger-word "build" -- trigger-word "test" -- trigger-word "derde-trigger" -- icon http://localhost: 8000/my-slash-handler-bot-icon.png -- url http://localhost: 8000/my-webhook-handler -- url http://example.com -- content-type "application/json"

  Opties .. code-blok :: geen

          -- team string [ REQUIRED] Team naam of ID
          -- channel string Channel naam of ID
          -- user string [ REQUIRED] Gebruiker gebruikersnaam, e-mail of ID
          --display-name string [ REQUIRED] Outgoing webhook display name --description string Outgoing webhook description -- trigger-words stringArray [ REQUIRED] Words to trigger webhook -- trigger-when string [ REQUIRED] When to trigger webhook (exact: for first word matches a trigger word exact, start: for first word starts with a trigger word) (default "exact")
          -- icon [ iconURL] Pictogram URL
          -- url stringArray [ REQUIRED] Callback URL's -- content-type tekenreeks Content-type -- h, -- help Help voor maken-uitgaande

mattermeest webhook delete
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

   Beschrijving inkomende en uitgaande webhaken verwijderen. Als u meerdere webhaken verwijdert, gebruikt u een door spaties gescheiden lijst.

   Formaat .. code-blok :: geen

       mattermeeste webhook delete [ webhookID]

   Voorbeelden .. code-blok :: geen

        bin/mattermeeste webhook delete ggwpz8c1oj883euk98wfm9n1cr

mattermeest webhook-lijst
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Lijst alle webhaken.

  Formaat .. code-blok :: geen

      mattermeest webhook-lijst { team }

  Voorbeelden .. code-blok :: geen

       bin/mattermeest webhook lijst team1
       bin/mattermeest webhook lijst

  Opties .. code-blok :: geen

          -- team string Specifiek team resultaten om terug te keren.  Als dit niet is opgegeven, worden alle teams opgenomen.

mattermeeste webhook wijzigen-inkomend
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

  Beschrijving Een bestaande inkomende webhook wijzigen door de titel, beschrijving, kanaal of pictogram-URL te wijzigen.

  Formaat .. code-blok :: geen

      mattermeest webhook modify-incoming { webhookId }

  Voorbeelden .. code-blok :: geen

       bin/mattermost webhook modify-incoming [ webhookID] -- channel [ channelID] --display-name [ displayName] --description [ webhookDescription]--lock-to-channel -- icon [ iconURL]

  Opties .. code-blok :: geen

          -- kanaal-ID kanaal
          --display-name string Binnenkomende webhook weergavenaam --description string Inkomende webhook beschrijving--lock-to-channel boolean (True/False) Inkomende webhook vergrendelen voor kanaal -- icon [ iconURL] Pictogram URL-URL mattermost webhook modify-uitgaande
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

  Beschrijving Een bestaande uitgaande webhook wijzigen door de titel, beschrijving, kanaal, triggerwoorden, pictogram-URL, callback-url of contenttype te wijzigen.

  Formaat .. code-blok :: geen

      mattermeest webhook modify-uitgaande { webhookId }

  Voorbeelden .. code-blok :: geen

       bin/mattermost webhook modify-outgoing [ webhookId] -- channel [ channelId] --display-name [ displayName] --description "New webhook description" -- icon http://localhost: 8000/my-slash-handler-bot-icon.png -- url http://localhost: 8000/my-webhook-handler -- content-type "application/json" -- trigger-word test -- trigger-wanneer start "

  Opties .. code-blok :: geen

          -- kanaal-ID kanaal
          --display-name string Inkomende webhook weergavenaam --description string Inkomende webhook beschrijving -- trigger-word string array Word (s) om webhook te activeren -- trigger-wanneer tekenreeks Wanneer om te triggeren webhook (exacte: voor het eerste woord komt overeen met een trigger woord precies, start: voor het eerste woord begint met een trigger woord) ")
         -- icon [ iconURL] Pictogram URL
	  -- url [ callbackURL] Callback-URL
	  -- content-type tekenreeks Content type mattermeest webhook move-uitgaande
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

  Beschrijving Verplaats een bestaande uitgaande webhook naar een ander team door het ID op te geven. Als de uitgaande webhook wordt geactiveerd door een trefwoord, dan is het afmelden van een kanaal optioneel.  Als de uitgaande webhook wordt gekoppeld aan een specifiek kanaal voordat u wordt verplaatst, moet er binnen het nieuwe team een kanaal worden opgegeven.

  Formaat .. code-blok :: geen

      mattermeest webhook move-uitgaande { webhookId }

  Voorbeelden .. code-blok :: geen

       bin/mattermeest webhook move-uitgaande newteam oldteam: [ webhookId] -- channel [ channelId of channelName]

  Opties .. code-blok :: geen

          -- kanaalstring kanaal-ID of kanaalnaam


mattermeest webhook show
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Toon informatie over een webhook door het verstrekken van het webhook ID. Retourneert weergavenaam, kanaal-ID en team-ID voor zowel inkomende als uitgaande webhaken.  Daarnaast retourneert callback URL, gebruikersnaam en pictogram URL voor uitgaande webhooks.

  Formaat .. code-blok :: geen

      mattermeest webhook show { webhookId }

  Voorbeelden .. code-blok :: geen

       bin/mattermeeste webhook show [ webhookId]

Maximaal 3,5 en eerder ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als u ` ` ./platform -help ` ` typt, maakt u documentatie voor de CLI-tool. Om de Help-documentatie in GitLab omnibus terug te geven, typt u

    .. code-blok :: geen

      sudo -u mattermost /opt/gitlab/embedded/bin/mattermost -- config=/var/opt/gitlab/mattermost/config.json -help Notes:

-Parameters in CLI-opdrachten zijn orderspecifiek.
-Als speciale tekens (` `! ` `, ` ` | ` `, ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` `
-De naam van het team en de naam van het kanaal verwijzen naar de handvatten, niet de weergavenamen. Dus in de url ` ` https: //community.mattermost.com/core/channels/town-square ` ` ` team naam zou ` ` core ` ` ` en channel name zou ` ` town-square ` ` .. tip :: Als je het automatiseren van de gebruiker maken door middel van de CLI tool met SMTP ingeschakeld, e-mails worden verzonden naar alle nieuwe gebruikers gemaakt. Als u een dergelijk laadscript uitvoert, is het het beste om SMTP uit te schakelen of testaccounts te gebruiken, zodat nieuwe e-mails voor het maken van accounts niet onbedoeld worden verzonden naar mensen in uw organisatie die ze niet verwachten.

CLI-documentatie:

::

  Mattermeeste opdrachten voor het configureren van het systeem

  NAAM: platform -- platformconfiguratietool

  USAGE: platform [ opties]

  VLAGGEN:
      -config="config.json " Pad naar het configuratiebestand

      -username = "someuser " Gebruikersnaam gebruikt in andere opdrachten

      -license="ex.mattermost-license " Pad naar uw licentiebestand

      -email="user@example.com " E-mailadres gebruikt in andere opdrachten

      -password = "mypassword " Wachtwoord gebruikt in andere commando's

      -team_name = "name " De teamnaam die in andere opdrachten wordt gebruikt

      -channel_name = "name " De kanaalnaam die in andere opdrachten wordt gebruikt

      -channel_header = "string " De kanaalkop gebruikt in andere commando's

      -channel_purpose = "string " Het kanaal doel gebruikt in andere commando's

      -channel_type = "type " Het kanaaltype dat in andere opdrachten wordt gebruikt, is
                                          "O"-openbaar kanaal
                                          "P"-private kanaal

      -role = "system_admin "De rol die wordt gebruikt in andere opdrachten geldige waarden zijn" "-De lege rol is standaard gebruikersmachtigingen" system_admin "-vertegenwoordigt een systeembeheerder die toegang heeft tot alle teams en configuratie-instellingen.
  OPDRACHTEN:
      -create_team Maakt een team.  Het vereist de vlag -teamnaam en -e-mail om een team te maken.
          Voorbeeld: platform -create_team -team_name = "name "-email="user@example.com"

      -create_user Maakt een gebruiker.  Het vereist de -email en-password vlag, en -team_name en -username zijn optioneel om een gebruiker te maken.
          Voorbeeld: platform -create_user -team_name = "name "-email="user@example.com" -password = "mypassword "-username = "user"

      -invite_user Nodigt een gebruiker uit voor een team per e-mail. Het vereist de -teamnaam en -email vlaggen.
          Examen
ple: platform -invite_user -team_name = "name "-email="user@example.com"

      -join_team Voegt een gebruiker toe aan het team.  Hiervoor zijn de vlaggen -email en -team_name vereist.  Mogelijk moet u zich afmelden van uw huidige sessie voor het nieuwe team dat moet worden toegepast.
          Voorbeeld: platform -join_team -email="user@example.com "-team_name = "name"

      -assign_role wijst de rol toe aan een gebruiker.  Hiervoor is de vlag -role en -email vereist.  Mogelijk moet u zich afmelden van uw huidige sessies voor de nieuwe rol die moet worden toegepast.
          Voorbeeld: platform -assign_role -email="user@example.com "-role = "system_admin"

      -create_channel Maak een nieuw kanaal in het opgegeven team. Het vereist de -email, -team_name, -channel_name, -channel_type vlaggen. Optioneel kunt u de -channel_header en -channel_purpose instellen.
          Voorbeeld: platform -create_channel -email="user@example.com "-team_name = "name" -channel_name = "channel_name "-channel_type = "O"

      -join_kanaal voegt een gebruiker toe aan het kanaal.  Het vereist de -email, -channel_name en -team_name vlaggen.  Mogelijk moet u zich afmelden van uw huidige sessie voor het nieuwe kanaal dat moet worden toegepast.  Vereist een bedrijfslicentie.
          Voorbeeld: platform -join_channel -email="user@example.com "-team_name = "name" -channel_name = "channel_name "

      -leave_channel Verwijdert een gebruiker uit het kanaal.  Het vereist de -email, -channel_name en -team_name vlaggen.  Mogelijk moet u zich afmelden van uw huidige sessie om het kanaal te verwijderen.  Vereist een bedrijfslicentie.
          Voorbeeld: platform -leave_channel -email="user@example.com "-team_name = "name" -channel_name = "channel_name "

      -list_channels geeft een overzicht van alle kanalen voor een bepaald team.
                                         Het zal toevoegen ' (gearchiveerd) ' naar de naam van het kanaal indien gearchiveerd.  Hiervoor is de vlag -teamnaam vereist.  Vereist een bedrijfslicentie.
          Voorbeeld: platform -list_channels -team_name = "name "

      -restore_channel herstelt een eerder gewist kanaal.
                                        Hiervoor is de vlag -channel_name vlag en -team_name vereist.  Vereist een bedrijfslicentie.
          Voorbeeld: platform -restore_channel -team_name = "name "-channel_name = "channel_name"

      -reset_password Resets het wachtwoord voor een gebruiker.  Het vereist de -email en-password vlag.
          Voorbeeld: platform -reset_password -email="user@example.com "-password = "newpassword"

      -reset_mfa schakelt multi-factor verificatie uit voor een gebruiker.  Het vereist de -email of -username vlag.
          Voorbeeld: platform -reset_mfa -username = "someuser "

      -reset_database Volledig wist de database waardoor het verlies van alle gegevens. Dit zal Matterbest resetten naar de oorspronkelijke staat. (let op: dit zal je configuratie niet wissen.)

          Voorbeeld: platform -reset_database

      -permanent_delete_user Permanent wist een gebruiker en alle gerelateerde informatie met inbegrip van berichten uit de database.  Het vereist de -email vlag.  Het kan nodig zijn om de server opnieuw te starten om het cache-voorbeeld te ongeldig te maken: platform -permanent_delete_user -email="user@example.com "

      -permanent_delete_all_users Permanent wist alle gebruikers en alle gerelateerde informatie met inbegrip van berichten uit de database.  Hiervoor is de vlag -team_name en -email vereist.  Mogelijk moet u de server opnieuw starten om het cache-voorbeeld te ongeldig te maken: platform -permanent_delete_all_users -team_name = "name "-email="user@example.com"

      -permanent_delete_team verwijdert permanent een team samen met alle gerelateerde informatie, inclusief berichten uit de database.
                                        Hiervoor is de vlag -teamnaam vereist.  Mogelijk moet u de server opnieuw starten om de cache ongeldig te maken.
          Voorbeeld: platform -permanent_delete_team -team_name = "name "

      -upload_license Uploads een licentie voor de server. Vereist de vlag -license.

          Voorbeeld: platform -upload_license -license=" /path/to/license/example.mattermost-license "

      -migrate_accounts Migreert accounts van de ene verificatieprovider naar de andere.
                                        Vereist -from_auth -to_auth en -match_field vlaggen. Ondersteunde opties voor -from_auth: email, gitlab, saml. Ondersteunde opties voor -to_auth: ldap. Ondersteunde opties voor -match_field: e-mail, gebruikersnaam. In de uitvoer worden alle accounts afgebeeld die niet zijn gemigreerd.

          Voorbeeld: platform -migrate_accounts -from_auth email -to_auth ldap -match_field gebruikersnaam

      -upgrade_db_30 Upgrades de database van een versie 2.x schema naar versie 3 zie https://mattermost.org/upgrading-to-mattermost-3-0/

          Voorbeeld: platform -upgrade_db_30 -version de huidige versie van het Matterste-platform afbeelden -Help Hiermee beeldt u deze Help-pagina af


Probleemoplossing ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het uitvoeren van een opdracht hangt af en is niet compleet
-------------------------------------------------------

Als u de zoekindexering van Bleve hebt ingeschakeld, schakelt u deze tijdelijk uit in ** System Console > Experimental > Bleve * * en voert u de opdracht opnieuw uit. U kunt ook optioneel de nieuwe ' mmctl Command Line Tool <https://docs.mattermost.com/administration/mmctl-cli-tool.html> ` _ gebruiken.

Bleve ondersteunt niet meerdere processen die dezelfde index openen en manipuleren. Als de Matterigste server actief is, zal een poging om de CLI uit te voeren dus worden vergrendeld bij het openen van de indeces.

Als u de zoekindexering van Bleve niet gebruikt, voel u dan vrij om te posten in ons ` Troubleshooting forum <https://mattermost.org/troubleshoot/> ` __ om hulp te krijgen.
