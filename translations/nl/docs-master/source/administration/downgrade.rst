Mattermeeste Server downgraden
== == == == == == == == == == == == == == =

In de meeste gevallen kunt u Mattermeeste Server downgraden met dezelfde stappen als :doc: ` upgrade '. De binaire bestanden zijn te vinden in de :doc: ` version-archive `. We raden u niet aan om meer dan één versie terug te brengen van uw huidige installatie.

Downgrade van 5.0 naar 4.10
---------------------------

Tijdens het upgraden van versie 5.0 wordt een migratie uitgevoerd om nieuwe functies in te schakelen van het ` advanced permissions system <https://docs.mattermost.com/deployment/advanced-permissions.html> ` __. Hierdoor wordt de database gewijzigd op een manier die niet langer compatibel is met Matterendste server 4.10. Als u moet downgraden van 5.0 of hoger naar 4.10, is het noodzakelijk om de onderstaande stappen te volgen.

U moet de volgende informatie verzamelen voordat u de upgrade start:

Bestaande installatiedirectory-* { install-path } *
  Als u niet weet waar Mattermeeste Server is geïnstalleerd, gebruikt u de opdracht ` ` whereis matterbest '. De uitvoer moet vergelijkbaar zijn met */opt/mattermost/bin/matterbest *. De installatiedirectory is alles vóór het laatste voorval van de reeks */matterbest *. In dit voorbeeld is * { install-path } * ` ` /opt ` `.
Locatie van uw lokale opslagdirectory De lokale opslagdirectory bevat alle bestanden die gebruikers aan hun berichten hebben gekoppeld. Als u de locatie niet weet, opent u de System Console en gaat u naar ** Bestanden > Opslag * * en leest u de waarde in ** Lokale opslagdirectory * *. Relatieve paden zijn relatief ten opzichte van de ` ` matterste ` ` directory. Als de lokale opslagdirectory bijvoorbeeld ` ` ./data/ ` ` is, is het absolute pad ` ` { install-path } /mattermost/data ` `.
Eigenaar en groep van installatiedirectory-* { owner } * en * { group } *
  Gebruik de opdracht ` ` ls -l { install-path } /mattermost/bin/matterbest ` ` om de eigenaar en de groep op te halen.

#. In een terminalvenster op de server waarop Mattermeeste Server wordt gehost, gaat u naar uw hoofddirectory. Indien aanwezig, wis de bestanden en directory's die mogelijk nog steeds bestaan uit een vorige download.

   .. code-blok :: sh

     cd ~ a

#. Stop Matterendste Server.

   Op Ubuntu 14.04 en RHEL 6:

   .. code-blok :: sh

     sudo service-mattermeeste stoppen

   Op Ubuntu 16.04 en RHEL 7:

   .. code-blok :: sh

     sudo systemctl stop matterbest
     

     
#. Maak een backup van uw gegevens en toepassingen.

   a. Maak een backup van uw database met de standaardprocedures van uw organisatie voor het maken van een backup van MySQL of PostgreSQL.

   b. Maak een backup van uw toepassing door te kopiëren naar een archiefmap (bijv. ` ` matterbest-back-YYYY-MM-DD-HH-mm ` `).

   .. code-block :: sh cd { install-path } sudo cp -ra mattermeeste/mattermost-back-$ (datum + '%F-%H-%M')/
    

#. Maak verbinding met uw CLI voor databases en voer de volgende SQL-instructies uit om de wijzigingen in de database te herstellen die door de migratie zijn gemaakt. De opdrachten kunnen tot een paar minuten duren voor het uitvoeren van grote installaties.

    .. code-blok :: sh

      UPDATE Teams SET SchemeId = NULL;
      UPDATE-kanalen SET SchemeId = NULL;

      UPDATE TeamMembers SET Rollen = CONCAT (Rollen, ' team_user '), SchemeUser = NULL w
hier SchemeUser = true;
      UPDATE TeamMembers SET Rollen = CONCAT (Rollen, ' team_admin '), SchemeAdmin = NULL waarbij SchemeAdmin = true;

      UPDATE ChannelMembers SET Roles = CONCAT (Rollen, ' channel_user '), SchemeUser = NULL waar SchemeUser = true;
      UPDATE ChannelMembers SET Roles = CONCAT (Rollen, ' channel_admin '), SchemeAdmin = NULL waar SchemeAdmin = true;

      UPDATE TeamMembers SET SchemeUser = NULL, SchemeAdmin = NULL;
      UPDATE ChannelMembers SET SchemeUser = NULL, SchemeAdmin = NULL;

      DELETE uit systemen WHERE Name = 'migration_advanced_permissions_phase_2 ';
 

#. Mattermeeste server starten.

   Op Ubuntu 14.04 en RHEL 6:

   .. code-blok :: sh

     sudo service matterbest start

   Op Ubuntu 16.04 en RHEL 7:

   .. code-blok :: sh

     sudo systemctl start matterbest
