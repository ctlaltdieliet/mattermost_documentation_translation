Herstel-en herstelbewerking == == == == == == == == == == == == == == == =

Opties om uw Mattermeeste server te beschermen tegen verschillende soorten storingen variëren van eenvoudige back-up tot geavanceerde noodherstel-implementaties en automatisering.

Backup maken
------

De status van uw Mattermeeste server bevindt zich in meerdere datastores die afzonderlijk moeten worden ondersteund en hersteld om uw systeem volledig te herstellen van storingen. 

U maakt als volgt een backup van de Mattermeeste server:

1. Maak een backup van uw Mattermeeste database met behulp van standaard MySQL of PostgreSQL procedures, afhankelijk van uw database versie.

      -` MySQL backup documentatie <https://dev.mysql.com/doc/refman/5.6/en/backup-types.html> ` __ is online beschikbaar. Gebruik de selector op de pagina om uw MySQL versie te kiezen.
      -` PostgreSQL back-updocumentatie <https://www.postgresql.org/docs/9.5/static/backup-dump.html> ` __ is online beschikbaar. Gebruik de navigatie bovenaan de pagina om uw PostgreSQL-versie te selecteren.
     
2. Maak een backup van de serverinstellingen die zijn opgeslagen in ` `config/config.json ` `.

      -Als u SAML-configuratie voor Matterbest gebruikt, worden uw SAML-certificaatbestanden opgeslagen in de ` ` config ` ` directory. Daarom wordt aanbevolen om een backup van de gehele directory te maken.
   
3. Maak een backup van bestanden die door uw gebruikers zijn opgeslagen met een van de volgende opties: 

     -Als u lokale opslag gebruikt met behulp van de standaarddirectory ` ` ./data '', maakt u een backup van deze directory.
     -Als u lokale opslag gebruikt met behulp van een niet-standaarddirectory die is opgegeven in de instelling ` ` Directory ` ` in ` `config.json ` `, backup van bestanden op die locatie.
     -Als u uw bestanden opslaat in S3, kunt u meestal de bestanden waar ze zich bevinden zonder backup te bewaren. Houd er rekening mee dat u een 'schone' backup moet maken die u nodig hebt om Matterbest te stoppen tijdens de duur van de backup, anders kunnen de database en de bestanden niet synchroon lopen.

Om een Matterbest-instance te herstellen vanaf een backup, herstelt u uw database, het bestand ``config.json ` ` bestand, en eventueel lokaal opgeslagen gebruikersbestanden naar de locaties waarvan ze een backup hebben gemaakt.

Herstel na calamiteiten -----------------

Een geschikt rampenherstelplan weegt de voordelen van het beperken van specifieke risico's tegen de kosten en complexiteit van het opzetten van een noodherstelinfrastructuur en automatisering.

Er zijn twee gemeenschappelijke benaderingen: 

Geautomatiseerde backup ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het automatiseren van backups voor een Matterigste server levert een kopie van de status van de server op een bepaald moment, die kan worden hersteld als een storing in de toekomst leidt tot verlies van gegevens. Opties zijn onder andere:

-Automatisering om periodiek een back-up van de Matterendste server, die kan omvatten alle onderdelen hierboven of een subset afhankelijk van wat je kiest om te beschermen.
-Automatisering om een server te herstellen van back-up, of het in gebruik nemen van een nieuwe server, om de hersteltijd te verminderen.
-Automatisering om te controleren of een back-up is succesvol geproduceerd om te beschermen tegen back-up storingen.
-Het opslaan van reservekopieën ter plaatse, ter bescherming tegen fysiek verlies van onlocatiesystemen.

Het herstellen van een fout met behulp van een backup is meestal een handmatig proces en
geen downtime veroorzaken. Het alternatief is het automatiseren van het herstel door gebruik te maken van een hoge beschikbaarheid.

Hoge beschikbaarheid-implementatie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De implementatie van Matterbest in ` High Availability mode <https://docs.mattermost.com/deployment/cluster.html> ` __ zorgt voor een snelle, geautomatiseerde herstel van een componentfout, zoals een specifieke server die uit de schijfruimte of een hardware probleem, door het draaien op redundante servers. Opties zijn onder andere:

-De implementatie van redundante Mattermeeste servers, ter bescherming tegen storingen in de Mattertiste server.
-Het in gebruik nemen van redundante databases, om te beschermen tegen storingen in de database.
-Het inzetten van redundante webproxy's, om te beschermen tegen storingen in de webproxy's.
-Het in gebruik nemen van redundante infrastructuur in een afzonderlijk fysiek datacenter om te beschermen tegen storingen in het primaire datacenter.

Een correct geïmplementeerde High Availability-implementatie schakelt automatisch over naar een redundant systeem als een enkele server mislukt. Hoge beschikbaarheid beschermt niet tegen storingen zoals gegevensbeschadiging, omdat fouten zich zouden verspreiden naar redundante systemen.

Een "complete" hersteloplossing voor calamiteiten zou beschermen tegen zowel real-time hardwarestoringen die gebruikmaken van hoge beschikbaarheid, gegevenscorruptiestoringen met behulp van automatisering en storingen in het primaire datacenter door het aanbieden van zowel externe backup als offsite redundante infrastructuur. Omdat de complexiteit van een volledige oplossing voor herstel na calamiteiten hoog is, is het voor de klanten gebruikelijk dat zij rekening houden met de afwegingen in kosten en complexiteit ten opzichte van de verwachte risico's en de hersteltijden.

Failover vanaf enkelvoudige aanmelding-bij uitvoer ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Wanneer enkelvoudige aanmelding met Mattermeeste Enterprise Edition wordt gebruikt, kan een storing aan uw SSO-provider een gedeeltelijke storing op uw Matterste-instance veroorzaken.

** Wat gebeurt er tijdens een SSO-storing? **

-** De meeste mensen kunnen zich nog steeds aanmelden. * * Standaard, wanneer een gebruiker zich aanmeldt bij Mattermost ontvangen ze een sessietoken van 30 dagen (de duur kan worden geconfigureerd in de systeemconsole). Tijdens een SSO-storing kunnen gebruikers met geldige sessiekens doorgaan met het gebruik van Mattermeest ononderbroken.
-** Sommige personen kunnen zich niet aanmelden. * * Tijdens een SSO-storing zijn er twee situaties waarin een gebruiker zich niet kan aanmelden:
  
  * Gebruikers waarvan het sessietoken tijdens de storing vervalt
  * Gebruikers proberen zich aan te melden bij nieuwe apparaten

In elk geval kan de gebruiker de SSO-provider niet bereiken en kan de gebruiker zich niet aanmelden. In dit geval zijn er verschillende mogelijke verzakkingen:  

Configureer uw SSO-provider voor hoge beschikbaarheid ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als u een self-hosted single sign-on provider gebruikt, zijn er verschillende opties beschikbaar voor ` High Availability configuraties die uw systeem beschermen tegen ongeplande uitval <https://docs.microsoft.com/en-us/microsoft-identity-manager/pam/high-availability-disaster-recovery-considerations-bastion-environment> ` __.

Voor verificatieproviders op basis van SaaS, terwijl u nog steeds afhankelijk bent van service uptime, kunt u redundantie instellen in bronsystemen waaruit gegevens worden opgehaald. Met de verificatieservice OneLogin SaaS kunt u bijvoorbeeld ` High Availability LDAP-connectiviteit <https://support.onelogin.com/hc/en-us/articles/204262680-High-Availability-for-LDAP> ' (High Availability LDAP-connectiviteit) instellen om de kans op een storing verder te verkleinen.

Stel uw eigen IDP in om een geautomatiseerde of handmatige SSO-failoveroptie te bieden ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Maak een aangepaste ID-provider voor SAML-verificatie die verbinding maakt met zowel een actieve als een standby-verificatieoptie, die handmatig of automatisch kan worden ingeschakeld in het geval van een storing.

In deze configuratie moet de beveiliging zorgvuldig worden bekeken om te voorkomen dat de standby-SSO-optie de verificatieprotocollen verzwakt.

Een handmatige failoverplan voor SSO-uitval instellen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Wanneer gebruikers de SSO-provider van uw organisatie niet kunnen bereiken tijdens een storing, wordt er een foutbericht afgebeeld waarin ze worden gestuurd om contact op te nemen met uw ondersteuningslink (gedefinieerd in uw systeemconsole-instellingen).

Zodra er contact is opgenomen met een SSO-storing, kunnen ze tijdelijk een gebruikersaccount wijzigen van SSO naar e-mail-wachtwoord met behulp van de systeemconsole, en kan de eindgebruiker het wachtwoord gebruiken om het account te claimen, totdat de SSO-uitval is beëindigd en het account kan worden teruggeconverteerd naar SSO.

Als de beheerder niet in staat is zich aan te melden bij de systeemconsole vanwege de SSO-uitval, kunnen ze hun verificatiemethode omzetten in een e-mail-wachtwoord om toegang te krijgen met het ` command line tool <https://docs.mattermost.com/administration/command-line-tools.html> ' __.

Wanneer de uitval voorbij is, is het cruciaal om iedereen terug te schakelen naar SSO van email-wachtwoord om consistentie en veiligheid te handhaven.
