.. _ldap-group-constrained-team-channel:

AD/LDAP-gesynchroniseerde groepen gebruiken om het lidmaatschap van een team of een besloten kanaal te beheren
------------------------------------------------------------------------------

De meeste groepen die zijn gemaakt met ` gesynchroniseerde AD/LDAP-groepen <https://docs.mattermost.com/deployment/ldap-group-sync.html> ` _ kunnen worden gebruikt om het lidmaatschap van private teams en private kanalen te beheren. Wanneer een team of een besloten kanaal wordt beheerd door gesynchroniseerde groepen, worden gebruikers toegevoegd en verwijderd op basis van hun lidmaatschap van de gesynchroniseerde AD/LDAP-groep.

U kunt bijvoorbeeld een AD/LDAP-groep hebben die uw ontwikkelteam bevat dat u wilt synchroniseren met een ontwikkelingsteam.  Als u deze functie gebruikt, worden nieuwe ontwikkelaars toegevoegd aan het team wanneer ze worden toegevoegd aan de gesynchroniseerde AD/LDAP-groep en worden ze uit het team verwijderd wanneer ze worden verwijderd uit de AD/LDAP-groep.

Op dezelfde manier kunt u een AD/LDAP-groep hebben die uw leiderschapsteam bevat dat u wilt synchroniseren met een besloten kanaal voor coördinatie en updates. Deze functie helpt bij het bepalen van het lidmaatschap van het kanaal, zodat gebruikers buiten de gesynchroniseerde groep niet per ongeluk aan het kanaal kunnen worden toegevoegd.

Voor teams die worden beheerd door gesynchroniseerde groepen, worden gebruikers buiten de groep beperkt tot:

 -Uitnodiging via een team uitnodigen link
 -Uitnodiging via een e-mail uitnodiging

Op persoonlijke kanalen die door gesynchroniseerde groepen worden beheerd, worden gebruikers buiten de groep beperkt van:

 -Uitnodiging door middel van een vermelding
 -Uitnodiging via de ` ` /invite ` ` slash opdracht
 -toegevoegd aan het kanaal met "leden toevoegen"

Gebruikers kunnen zichzelf verwijderen van teams en private kanalen die door gesynchroniseerde groepen worden beheerd.

Het beheren van het lidmaatschap van een team of een kanaal met gesynchroniseerde groepen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het lidmaatschap van een besloten team beheren met gesynchroniseerde groepen:

1. Navigeren naar ** Systeemconsole > Gebruikersbeheer > Teams * *. 2. Selecteer het team dat u wilt beheren met groepssynchronisatie.
3. Onder ** Team Management * *, enable ** Sync Group Members * *. Als ** Iedereen kan deelnemen aan dit team * * is ingeschakeld of als er specifieke e-maildomeinen zijn ingesteld, worden deze uitgeschakeld door de functie Sync-groepsleden.
4. Voeg een of meer groepen toe aan het team. Als er al groepen aan standaardgebruikers in het team zijn gekoppeld, zijn ze al aanwezig.
5. Bekijk de aankondiging in de voettekst van het scherm voor gebruikers die geen deel uitmaken van groepen die worden verwijderd uit het team op de volgende synchronisatie.
6. Klik op ** Save**. De leden worden bijgewerkt op de volgende geplande AD/LDAP-synchronisatie.

Als alternatief kunt u de CLI-tool gebruiken om het team in te stellen dat wordt beheerd door groepen:

1. Zorg ervoor dat er ten minste één groep aan het team is gekoppeld. U kunt standaardteams bekijken en toevoegen aan een groep via ** System Console > Gebruikersbeheer > Groepen > Groepsconfiguratie * *. Raadpleeg meer informatie over het toevoegen van standaardteams en -kanalen ' hier <https: //docs.mattermost.com/d
eployment/ldap-group-sync.html#add-default-teams-or-channels-for-the-group> ` _. Bovendien kunt u de CLI-tool gebruiken om te bekijken of er al een groep aan het team is gekoppeld door de CLI-opdracht voor het groepsteam uit te voeren <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-group-team-list> ` _.
2. Zorg ervoor dat ** Team-instellingen > Algemeen > elke gebruiker met een account op deze server toestaan om deel te nemen aan dit team * * is ingesteld op ` ` Nee ` `.
3. Converteer het team om het lidmaatschap van de groep te laten beheren door gesynchroniseerde groepen door het ` group team in te schakelen CLI-opdracht <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-group-team-enable> ` _.

Het lidmaatschap van een besloten kanaal beheren met gesynchroniseerde groepen:

1. Navigeren naar ** Systeemconsole > Gebruikersbeheer > Kanalen * *. 2. Selecteer het kanaal dat u wilt beheren met groepssynchronisatie.
3. Onder ** Channel Management * *, enable ** Sync Group Members * *. Controleer of het kanaal is ingesteld op ` ` private ` `.
4. Voeg een of meer groepen toe aan het kanaal. Als er al groepen aan standaardgebruikers in het kanaal zijn gekoppeld, zijn ze al aanwezig.
5. Bekijk de aankondiging in de voettekst van het scherm voor gebruikers die geen deel uitmaken van groepen die worden verwijderd uit het kanaal op de volgende synchronisatie.
6. Klik op ** Save**. De leden worden bijgewerkt op de volgende geplande AD/LDAP-synchronisatie.

U kunt ook de CLI-tool gebruiken om een besloten kanaal in te stellen voor beheer door groepen:

1. Zorg ervoor dat er ten minste één groep aan het kanaal is gekoppeld. U kunt standaardkanalen bekijken en toevoegen aan een groep via ** System Console > Gebruikersbeheer > Groepen > Groepsconfiguratie * *. Zie meer informatie over het toevoegen van standaard teams en kanalen ` hier <https: //docs.mattermost.com/deployment/ldap-group-sync.html#add-default-teams-or-channels-for-the-group> ` _. Daarnaast kunt u de CLI-tool gebruiken om te bekijken of er al een groep aan het kanaal is gekoppeld door het uitvoeren van de CLI-opdracht voor het groepskanaal <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-group-team-list> ` _.
2. Converteer het team zodat het lidmaatschap wordt beheerd door gesynchroniseerde groepen door het uitvoeren van de CLI-opdracht <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-group-channel-enable> ` _.

Groepen toevoegen of verwijderen uit teams ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Nadat het beheer van het team is geconverteerd om te worden beheerd door gesynchroniseerde groepen, kan een team of systeembeheerder extra groepen toevoegen vanuit ** Hoofdmenu > Groepen toevoegen aan team * *.  Dit voegt gebruikers toe aan de volgende AD/LDAP-synchronisatie en alle nieuwe gebruikers aan de groep worden toegevoegd aan het team bij volgende synchronisaties. Teambeheerders kunnen het team niet naar het openbaar wijzigen door het inschakelen van ** Team-instellingen > Alle gebruikers met een account op deze server toestaan om deel te nemen aan dit team * *.

Team-of systeembeheerders kunnen groepen ook uit een team verwijderen uit ** Hoofdmenu > Groepen beheren * *. Hiermee wordt de groep losgekoppeld van het team. Gebruikers worden verwijderd op de volgende AD/LDAP-synchronisatie.

De systeembeheerder kan ook groepen verwijderen uit ** Systeemconsole > Gebruikersbeheer > Teams > Teamconfiguratie > Synced-groepen * *.

Groepen toevoegen of verwijderen uit persoonlijke kanalen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Nadat het beheer van het kanaal is geconverteerd om te worden beheerd door gesynchroniseerde groepen, kan een team of systeembeheerder extra groepen toevoegen vanuit ** Channel Menu > Groepen toevoegen aan kanaal * *. Dit zal gebruikers toevoegen aan de volgende AD/LDAP-synchronisatie en eventuele nieuwe gebruikers aan de groep worden toegevoegd aan het kanaal bij volgende synchronisaties.

Team-of systeembeheerders kunnen groepen ook uit een team verwijderen uit ** Hoofdmenu > Groepen beheren * *. Hiermee wordt de groep losgekoppeld van het team. Gebruikers worden verwijderd op de volgende AD/LDAP-synchronisatie.

De systeembeheerder kan ook groepen verwijderen uit ** System Console > User Management > Channels > Channel Configuration > Synced Groups * *.

Leden beheren ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Gebruikers worden automatisch uit het team of het besloten kanaal verwijderd wanneer ze worden verwijderd uit een gesynchroniseerde AD/LDAP-groep die het lidmaatschap van dat team of dat kanaal beheert. Bovendien worden gebruikers die niet in de gesynchroniseerde groepen voorkomen, niet meer toegevoegd via de ` ` /invite ` ` en worden de stromen binnen een kanaal vermeld.

Een gebruiker kan zichzelf uit het team of uit het besloten kanaal verwijderen wanneer het wordt beheerd door gesynchroniseerde groepen. Ze kunnen worden toegevoegd door gebruikers die gemachtigd zijn om leden voor een team of een besloten kanaal te beheren met behulp van de schuine streep naar rechts of door de gebruiker in een kanaal te vermelden.

Als de gebruiker wordt verwijderd uit een gesynchroniseerde groep en later wordt aangepast aan de groep, kunnen ze handmatig worden toegevoegd aan het team of private kanaal zoals hierboven vermeld. .. opmerking:: Gebruikers worden niet automatisch toegevoegd door de AD/LDAP-synchronisatie zodra ze zichzelf verwijderen of door de LDAP-gesynchroniseerde groep worden verwijderd.

Het uitschakelen van groep gesynchroniseerd beheer van teams en particuliere kanalen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als u het beheer van leden door gesynchroniseerde groepen in een team wilt verwijderen, schakelt u ** Sync Group Members * * onder ** System Console > User Management > Teams > Team Management * * uit, of start u het ` group team disable CLI command <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-group-team-disable> ` _.

Om het beheer van leden te verwijderen door gesynchroniseerde groepen in een kanaal, schakelt u ** Sync Group Members * * onder ** Systeemconsole > Gebruikersbeheer > Kanalen > Kanaalbeheer * * uit, of voert u het ` group channel disable CLI command <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-group-channel-disable> ` _.

FAQ's ^ ^ ^ ^

** Waarom worden geen openbare kanalen ondersteund met deze functie? **

Openbare kanalen zijn beschikbaar voor alle leden om te ontdekken en toe te treden. Het beheren van het lidmaatschap met gesynchroniseerde groepen verwijdert de mogelijkheid voor openbare kanalen om toegankelijk te zijn voor gebruikers in het team. Private kanalen vereisen doorgaans een meer gecontroleerd lidmaatschap management, die ik
s waarom deze functie van toepassing is op Private kanalen. Groepen kunnen worden toegewezen aan openbare teams en openbare kanalen zoals beschreven in ` this documentation <https: //docs.mattermost.com/deployment/ldap-group-sync.html#add-default-teams-or-channels-for-the-group> ` _.

* * Heeft een team met zijn lidmaatschap beheerd door groepen hebben enig effect op Public channel toegang? **

Alleen gebruikers die lid zijn van groepen die zijn gesynchroniseerd met het team, zijn in staat om openbare kanalen te ontdekken en aan te sluiten. Private kanalen kunnen ook worden beheerd door gesynchroniseerde groepen wanneer een team wordt beheerd door gesynchroniseerde groepen.

** Waarom worden gebruikers niet aan teams of kanalen aangepast nadat ze zijn verwijderd en vervolgens weer worden toegevoegd aan de LDAP-groep? **

De implementatie van groepsverwijderingen maakt momenteel geen onderscheid tussen gebruikers die zichzelf hebben verwijderd of die door het LDAP-synchronisatieproces zijn verwijderd. Ons ontwerp optimaliseert gebruikers die zichzelf hebben verwijderd van een team of kanaal. In de toekomst kunnen we de mogelijkheid voor beheerders toevoegen om gebruikers opnieuw toe te voegen die zijn verwijderd, en zelfs te voorkomen dat gebruikers een team of kanaal verlaten.

Bovendien worden LDAP-gebruikers die niet toegankelijk zijn voor Matterbest op basis van filters, verwijderd uit de groepen en uit de teams en kanalen van de groep. Als ze werden verwijderd uit teams en kanalen dan zullen ze niet opnieuw worden toegevoegd aan die teams en kanalen op het worden vervolgens opnieuw toegankelijk voor Matterbest.
