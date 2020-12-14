Handleiding voor ingebruikname van desktop app
== == == == == == == == == == == == == == =

Mattermeeste desktop applicaties zijn beschikbaar voor Windows, Mac en Linux besturingssystemen.

U kunt de apps rechtstreeks downloaden van onze downloadpagina <https: //mattermost.com/download/#mattermostApps> ` __ en bezoek onze ` installation guides <https://docs.mattermost.com/install/desktop.html> ` __ voor hulp bij het instellen en oplossen van tips.

Deze pagina biedt een gids over hoe u uw eigen Matterbest Desktop App aanpassen en distribueren, en hoe u de officiële Windows Desktop App kunt distribueren naar eindgebruikers, vooraf geconfigureerd met de server-URL en andere app-instellingen. .. Inhoud:
  :diepte: 1 :lokaal:
  :backlinks: item

Aangepaste buildconfiguratie
---------------------------

U kunt uw eigen Matterste Desktop-toepassing aanpassen en distribueren door ` src/common/config/buildConfig.js <https://github.com/mattermost/desktop/blob/master/src/common/config/buildConfig.js> ` __ te configureren.

1. Configureer het bestand ` buildConfig.js ` van de Desktop App. Er zijn meerdere parameters die u kunt configureren om de gebruikerservaring aan te passen:

` defaultTeams '
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Lijst van server-URL's en hun weergavenamen toegevoegd aan de desktop-app standaard, die de gebruiker niet kan wijzigen. Gebruikers kunnen nog steeds servers toevoegen " via de pagina Server Management <https: //docs.mattermost.com/help/apps/desktop-guide.html#server-management> ` __ tenzij ` ` enableServerManagement ` ` is ingesteld op false. Verwacht een array van sleutel-waardeparen.

  Voorbeeld .. code-block :: geen

      defaultTeams: [
        {
          naam: 'voorbeeld', url: 'https: //example.com'
        }, {
          naam: 'matterbest', url: 'https: //www.mattermost.com '
        }
      ]

` helpLink '
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving De URL van de Help-documentatie in Help > Meer informatie over de menubalk. Als er geen is opgegeven, wordt de menuoptie verborgen. Verwacht een tekenreeks.

  Voorbeelden .. code-blok :: geen

      helpLink: 'https: //about.mattermost.com/default-desktop-app-documentatie/'
      helpLink: ''

` enableServerManagement '
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

  Beschrijving Bepaalt of gebruikers servers kunnen toevoegen, bewerken of verwijderen op de pagina-instellingenpagina. Als deze eigenschap is ingesteld op false, moet ten minste één server worden opgegeven voor ` ` defaultTeams ` ` ` of anders kunnen gebruikers geen interactie hebben met servers. Verwacht een booleaans, true of false.

  Voorbeelden .. code-blok :: geen

      enableServerManagement: true

2. Om de toepassing te bouwen, volgt u de 'Matterste Desktop Development Guide <https://github.com/mattermost/desktop/blob/master/docs/development.md>' __.

Windows App: Pre-Configuration en Silent Deployment
------------------------------------------------------

U kunt de officiële Windows Desktop App automatisch distribueren naar eindgebruikers, vooraf geconfigureerd met de server-URL. U kunt ook alle ` app-instellingen <https: //docs.mattermost.com/help/apps/desktop-guide.html#app-options> ` __ instellen, behalve de optie ** Start app bij aanmelden * *.

1. Downloa
d het meest recente Windows-installatieprogramma van de ` Matterbest download page <https: //mattermost.com/download/#mattermostApps> ` __.

2. Verplaats het uitvoerbare bestand naar een gemeenschappelijke plaats, zoals een bestandsserver.

3. Een batchbestand maken in Windows:

  1. Open een teksteditor naar keuze, zoals Notepad of Notepad + +.
  2. Kopieer en plak de volgende opdrachten in het tekstbestand:

    .. code-blok :: geen


      rem "Stap 1: Matterste Desktop App automatisch installeren op de lokale schijf van de gebruiker" start /wait \\SERVER \shared_folder\mattermost-setup-4.3.1-win64.exe -- silent

      rem "Stap 2: Eerste config.json genereren in de configuratiedirectory van de gebruiker"
      (
        echo {
        echo "versie": 1, echo "teams": [
        echo {
        echo "name": "community", echo "url": "https: //community.mattermost.com/core" echo } echo], echo "showTrayIcon": false, echo "trayIconTheme": "light", echo "minimizeToTray": false, echo "meldingen": {
        echo "flashWindow": 0, echo "bounceIcon": false, echo "bounceIconType": 'informational', echo }, echo "showUnreadBadge": true, echo "useSpellChecker": true, echo "enableHardwareAcceleration": true, echo "autostart": true, echo "spellCheckerLocale": 'en-US', echo }) > %APPDATA%\Mattermost\config.json

    .. opmerking:
      In plaats van deze opdracht te gebruiken om de Desktop-app te installeren in een gedeelde map, kunt u het uitvoerbare bestand ook kopiëren naar de map voordat u deze uitvoert. Hierdoor kan de gedeelde map alleen lezen-alleen-permissies vereisen.

  3. Sla het tekstbestand op met de extensie ` ` .bat ` `. Bijvoorbeeld: ```mattermeest-app-install.bat ` `.
  4. Gebruik standaardtools voor softwareactivabeheer om het batchbestand te distribueren en in gebruik te nemen op elke gebruiker.

Eenmaal uitgevoerd, wordt de desktop-app toegevoegd aan de lokale directory van de gebruiker, samen met het vooraf geconfigureerde config.json-bestand. Het installatieprogramma maakt een snelkoppeling voor de Desktop App in het menu start van de gebruiker; als een zip-versie wordt gebruikt, moet u de snelkoppeling handmatig maken.

Windows App: Het verwijderen van de app
------------------------------------------------------

Als u de app automatisch wilt verwijderen van de computer van een gebruiker, kunt u de volgende opdracht uitvoeren:

  .. code-block :: geen %userprofile%\AppData\local\Programs\mattermost-desktop \ Uninstall Mattermost.exe /currentuser /S .. opmerking:::
      De exe moet worden gesloten wanneer deze opdracht wordt uitgevoerd
