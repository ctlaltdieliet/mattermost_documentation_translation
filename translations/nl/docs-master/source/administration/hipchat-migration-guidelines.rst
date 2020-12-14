Migreren van HipChat naar Matterbest
== == == == == == == == == == == == == == == == == == =

U kunt HipChat-gebruikers en berichten migreren naar Matterbest met behulp van de volgende richtlijnen.

Stap 1: Stel uw Matterste Instance -----------------------------------------
-` Ga naar de meest downloadpagina van <https://mattermost.com/download/> ` __ om Matterbest in uw omgeving te installeren met behulp van een van de installatiehandleidingen voor Linux binaire installatie, Docker-installatie of diverse georkestreerde installaties. 

Vragen? Bezoek onze ` troubleshooting forum <https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150> ` __ voor hulp. 

Stap 2: Exporteer uw gegevens van HipChat Data Center of HipChat Server
------------------------------------------------------------------------

HipChat Server/HipChat Data Server:
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Als u in staat bent om HipChat Server of HipChat Data Center te upgraden naar de nieuwste versie, raden wij u aan met behulp van Group Export Dashboard uw gegevens te exporteren. Als u niet kunt upgraden, raadpleegt u de onderstaande procedure voor de opdrachtregelinterface. 

*Werken met het groepsexportdashboard: *

#. Meld u aan bij uw Hipchat-server (bijv. hipchat.yourcompany.com).
#. Klik op ** Serverbeheer > Exporteren * *.
#. Selecteer de gegevens die u wilt exporteren.
#. In het veld ** Password** en ** Wachtwoord bevestigen * * maakt u een wachtwoord om uw archiefbestanden te beveiligen (Bewaar dit wachtwoord omdat het nergens anders wordt opgeslagen).
#. Klik op ** Export**. Als de export eenmaal is uitgevoerd, ontvangt u een e-mail met een link om het bestand te downloaden.

*Als u het Export Dashboard van Group Export niet kunt gebruiken, gebruikt u de opdrachtregelinterface om te exporteren: *

#. Ga naar **CLI* *.
#. Typ ` ` hipchat export -- export -p uw_wachtwoord ` ` `.
#. Als de export eenmaal is uitgevoerd, ontvangt u een e-mail met een link om het bestand te downloaden.

Meer gedetailleerde instructies zijn te vinden op de ` documentatie <https://confluence.atlassian.com/hipchatdc3/export-data-from-hipchat-data-center-913476832.html> ` __ en ` knowledge base <https://confluence.atlassian.com/hipchatkb/exporting-from-hipchat-server-or-data-center-for-data-portability-950821555.html> ` __.


Stap 3: Importeer uw gegevens in Mattermeeste ----------------------------------------

1. Volg de ' Matterthe Bulk Load Tool <https://docs.mattermost.com/deployment/bulk-loading.html> ` __ gids voor het importeren van uw gegevens in Matterbest. Bestanden die worden geëxporteerd uit HipChat moeten worden geconverteerd naar de indeling die vereist is voor Matterbest. Gelieve ` contact met ons op <https://mattermost.zendesk.com/hc/en-us/requests/new> ` __ als u hulp nodig hebt in de conversie. 

2. U wordt ook aangemoedigd om de HipChat import tool gemaakt door Herzum te gebruiken: https://github.com/herzum/HC2MM.

Als u geïnteresseerd bent in het bijdragen of testen van een community bijgedragen oplossing, laat het ons weten op info@mattermost.com, Twitter of Mattermeeste forums op https://forum.mattermost.org.

3. U kunt ook 'contact opnemen met Matterbest <https://mattermost.com/contact-us/>' __ voor partneraanbevelingen voor uw regio om u te helpen bij het importeren. 
  
Ste
p 4: Aanboord van uw gebruikers in Matterbest
--------------------------------------------- Nadat u gebruikers hebt geïmporteerd, kunt u een mededeling verzenden via e-mail of via uw oude systeem (of beide) om gebruikers te laten weten hoe u zich kunt aanmelden bij Matterbest met hun oude accounts of hoe u nieuwe accounts kunt maken. ** Aankondiging van de meest onboarding in uw vorige berichtensysteem: **
 
Gebruik de volgende berichtsjabloon om gebruikers van de migratie te waarschuwen::, we verplaatsen communicatie naar een nieuwe Mattertiste server. U kunt uw nieuwe account starten door naar de [ uw nieuwe locatie, bijvoorbeeld ` ` https: //yourcompany.com/mattermost ` ` `] te gaan, te klikken op ** I vergat mijn wachtwoord * * en het invoeren van de e-mail die u op dit systeem hebt gebruikt op de pagina Wachtwoord opnieuw instellen om nieuwe legitimatiegegevens in te stellen. Uw bericht geschiedenis en kanalen moeten dragen van dit systeem in Matterbest. Nog vragen? Laat het ons weten.

** Aankondiging van Mattermeeste onboarding met behulp van e-mail met behulp van gebruikersnaam/password:**

#. Een lijst ophalen van e-mailadressen van personen in het nieuwe systeem door een databasequery op Matterbest uit te voeren. Voer ` ` SELECT Email FROM Users ` ` uit van MySQL of PostgreSQL databases. #. Pas de e-mailsjabloon van de migratie-sjabloon (<https://docs.mattermost.com/administration/migration-announcement-email-template.html>) aan om gebruikers te laten weten hoe ze hun oude accounts kunnen terughalen of nieuwe accounts kunnen starten.

Gebruikers aan boord die SSO gebruiken in Matterbest
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

U kunt er ook voor kiezen om SSO (Single Sign-on) in te stellen met Matterbest als u een Enterprise-versie gebruikt.  

#. Configureer ` Active Directory/LDAP <https://docs.mattermost.com/deployment/sso-ldap.html> ` __ of 'SAML Single Sign-on <https://docs.mattermost.com/deployment/sso-saml.html>' __ van de ** System Console * *.
#. Pas de berichtsjablonen hierboven aan om verwijzingen naar "wachtwoord reset" te verwijderen en geef aan welke SSO-systeemlegitimatiegegevens Matterbest hebben geconfigureerd.
