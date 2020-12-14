.. _ldap-group-sync:

AD/LDAP-groepen (E20)
== == == == == == == == == ==

Overzicht
--------

De groepsfunctie is handig voor organisaties die veel nieuwe gebruikers aan boord hebben of die gebruikers vaak aan boord hebben en die ervoor willen zorgen dat gebruikers worden toegevoegd aan standaardteams en -kanalen die voor hen relevant zijn. De groepsfunctie ondersteunt momenteel:

-Groepen maken door synchronisatie met uw AD/LDAP-systeemgroepen.-Syncing groepen naar vooraf gedefinieerde rollen in Matterbest.-AD/LDAP geneste groepen.-Met behulp van gesynchroniseerde groepen kunt u 'lidmaatschap van teams en privé-kanalen beheren <https://docs.mattermost.com/deployment/ldap-group-constrained-team-channel.html>' _.

Voor meer informatie over deze functie en toekomstige plannen lees ` dit forum post <https://forum.mattermost.org/t/ldap-group-sync-alpha-release/6351> ` __. Voor een technisch overzicht van de functie van Martin Kraft, die de ontwikkeling van de functie leidde, zie ` this blog post <https://developers.mattermost.com/blog/2019-06-05-ldap-nested-groups-modelling-and-representation-in-code/> ` _.

U kunt ook een video-overzicht bekijken over het toevoegen van gebruikers aan Mattermost met AD/LDAP op ` YouTube <https://www.youtube.com/watch?v=zyku2ibsG0M> ` _. .. raw:: html

   <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
      <iframe src="https://www.youtube.com/embed/zyku2ibsG0M" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 95%;"></iframe>
   </div>

Opmerkingen vooraf bij de installatie
----------------------

Als u synchronisatie met AD/LDAP hebt ingeschakeld, zijn alle groepen die overeenkomen met de standaardfilter ` ` (| (objectClass=group) (objectClass=groupOfNames) (objectClass=groupOfUniqueNames)) ` ` beschikbaar om te worden gekoppeld in de groepslijstweergave op ** Systeemconsole > Gebruikersbeheer > Groepen * * (of ** Systeemconsole > Toegangsbesturing > Groepen * * in versies ouder dan 5.12).

Het groepsfilter is een optionele configuratie-instelling die beschikbaar is onder ** Systeemconsole > AD/LDAP* *, en kunt u de groepen opgeven die toegang moeten hebben tot Matterbest. Het filter ** Group** is onafhankelijk van het filter ** User**, maar maakt gebruik van het kenmerk Base DN. Mogelijk moet u de basis-DN aanpassen om ervoor te zorgen dat groepsobjecten kunnen worden doorzocht in uw AD/LDAP-structuur.

De synchronisatie van groepen gebeurt met de synchronisatie van gebruikers, tijdens welke Mattermeest query's AD/LDAP voor bijgewerkte accountgegevens. Zie de ` Active Directory/LDAP Set up documentation <https: //docs.mattermost.com/deployment/sso-ldap.html?highlight = ldap#configure-ad-ldap-synchronization> ` __. voor meer informatie. De groepsfunctie heeft geen effect op de gebruikersverificatie voor Matterbest.

AD/LDAP-groepssynchronisatie inschakelen
--------------------------------------

Om deze functie in te schakelen, gaat u naar ** System Console > Groups * * (of ** System Console > Advanced > Experimental > Enable AD/LDAP Group Sync * * in versies ouder dan 5.12).


AD/LDAP-groepssynchronisatie gebruiken
-----------------------------------

Om sp te synchroniseren
ecific AD/LDAP-groepen voor Matterbest, geef het ` ` Group ID Attribute ` ` en de ` ` Group Display Name Attribute ` ` (bijv., "cn" for Common Name) onder ** System Console > Authentication > AD/LDAP* *.

Bovendien kunt u het filter ** Group** opgeven dat wordt gebruikt om groepen op te halen. Als de filterconfiguratie ** Group** leeg is, worden alle groepen die overeenkomen met het standaardfilter ` ` (| (objectClass=group) (objectClass=groupOfNames) (objectClass=groupOfUniqueNames)) ` ` geretourneerd. .. Opmerking:
   Kenmerkwaarden voor ** Group ID* * and ** Group Display Name * * zijn hoofdlettergevoelig.

Groepssynchronisatie vindt plaats nadat de gebruikerssynchronisatie en de resultaten voor groepssynchronisatie beschikbaar zijn in de tabel met status synchonization (op de onderkant van de configuratiepagina ** AD/LDAP* *).

Nadat de AD/LDAP-groepen zijn gesynchroniseerd, gaat u naar ** System Console > User Management > Groups * * (of ** System Console > Access Control > Groups * * in versies vóór 5.12) om Mattermeeste groepen te koppelen en te configureren. .. image:: ../images/Group_filter.png .. Opmerking:

   Het synchronisatieproces maakt geen Mattermeeste groepen. De meeste groepen worden gemaakt wanneer u de AD/LDAP-groep "linkt" zoals beschreven in de volgende sectie ** Linking AD/LDAP groepen naar Mattermeeste groepen * *. Bestaande AD/LDAP-gebruikers worden toegevoegd aan de Mattermeeste groepen op de volgende synchronisatie en nieuwe gebruikers worden toegevoegd op hun eerste login.

Bij volgende synchronisaties en zodra groepen zijn gekoppeld:

 -Gebruikers die aan een AD/LDAP-groep zijn toegevoegd, worden toegevoegd aan de gekoppelde Mattermeeste-groep en aan teams en kanalen die voor die groep zijn geconfigureerd.
 -Mattermeeste groepen die zijn gekoppeld aan AD/LDAP-groepen die niet meer in uw filter zijn opgenomen, worden gewist.
 -Gebruikers die uit een AD/LDAP-groep zijn verwijderd, worden verwijderd uit de gekoppelde Matterbest-groep, maar hun kanaal-en teamlidmaatschap wordt alleen ingetrokken wanneer het kanaal of team wordt gesynchroniseerd met een AD/LDAP-groep. .. image:: ../images/Group_Group_Member_Sync.png

AD/LDAP-groepen koppelen aan Mattermeeste Groepen
-------------------------------------------------------

Groepen die zijn geretourneerd uit het standaardfilter of uw AD/LDAP-groepsfilter, zijn beschikbaar in een lijstweergave op de pagina Groepen. De koppelingsactie maakt Mattermeeste groepen die overeenkomen met de AD/LDAP-groep. AD/LDAP-groepen die zijn gekoppeld aan een Matterbest-groep worden afgebeeld in het pictogram ** Linked**. AD/LDAP-groepen die niet zijn gekoppeld aan een Matterbest-groep worden afgebeeld met het pictogram ** Niet gekoppeld * *. Een AD/LDAP-groep die niet is gekoppeld, maakt geen Mattermeeste groep. .. afbeelding:: ../images/Groups_listing.png

Groepen kunnen individueel door de knop Inline ** Linked** worden gekoppeld. U kunt het selectievakje naast de naam van de groep ook gebruiken om meerdere groepen te selecteren en te kiezen voor ** Geselecteerde groepen koppelen * *. Bij het selecteren van meerdere groepen met een mix van ** Linked** en ** Niet gekoppeld * * staat de bulkactie van de knop ** Link Geselecteerde Groepen * * tot alle geselecteerde items zijn gemarkeerd ** Linked**. Als u de bulkactie gebruikt, wordt het proces van het maken van Mattermeeste groepen van uw AD/LDAP-groepen versneld.

Als u een bericht ** Link mislukt * * ziet, klikt u op het bericht of selecteert u het vakje naast de naam van de groep om het inline koppelingsbericht weer te geven en het opnieuw te proberen. afbeelding:: ../images/LinkFailed.png

De groep configureren
---------------------

AD/LDAP-groepen die zijn gekoppeld aan Mattermeeste groepen kunnen worden geconfigureerd om team en kanalen toe te voegen. Om de groep te configureren, selecteert u ** Configureren > Groepsconfiguratie * * en bekijkt u het groepsprofiel met de groepsnaam. Deze naam wordt automatisch toegewezen uit het kenmerk common name van de AD/LDAP-groep en is alleen-lezen.

Standaardteams of kanalen voor de groep toevoegen
------------------------------------------------------

Als u de teams en kanalen wilt toevoegen waarvan u wilt dat de groepsleden standaard worden geselecteerd, selecteert u ** Team toevoegen * * of ** Kanaal toevoegen * * uit de knop ** Team toevoegen of Kanaal * *. .. image:: ../images/Group_Configuration.png

Kanalen zijn genest onder het team waartoe ze behoren in het team en de kanaallijst.

Teams die voor iedereen toegankelijk zijn, worden aangegeven door: .. image:: ../images/open_team.png

Teams die niet voor iedereen toegankelijk zijn, worden aangegeven door: .. afbeelding:: ../images/private_team.png

Openbare kanalen worden aangegeven door: .. image:: ../images/public_channel.png

Privé-kanalen worden aangegeven door: .. image:: ../images/private_channel.png

Als er een team wordt toegevoegd, worden de ` ` Town Square ` ` ` en ` ` Off-Topic ` ` kanalen ook als standaard toegevoegd, evenals alle standaardkanalen die zijn ingesteld in de ' ExperimentalDefaultChannels config setting <https: //docs.mattermost.com/administration/config-settings.html?highlight=configuration%20settings#default-channels-experimental> ` __.

Wanneer er een kanaal wordt toegevoegd zonder het team expliciet in te stellen, wordt het team getoond in het ** Team en Channel lidmaatschap * * lijst, maar het zal niet specifiek aan de groep worden toegevoegd. Door deze afhankelijkheid wordt het team ook verwijderd wanneer het kanaal wordt verwijderd. Teams worden tussen haakjes geplaatst na de kanaalnaam in de kanaalselector.

U kunt rollen toewijzen aan groepsleden met behulp van de opties in de kolom ** Toegewezen rollen * *. Rollen worden bijgewerkt op de volgende geplande AD/LDAP-synchronisatie. 

Teams en kanalen synchroniseren
--------------------------------

Voor nieuwe gebruikers worden standaard teams en kanalen toegevoegd wanneer ze zich voor het eerst aanmelden. Voor bestaande gebruikers worden standaard teams en kanalen toegevoegd na de volgende geplande AD/LDAP-sychronisatie.

Het kan enkele seconden duren om alle team-en kanaallidmaatschappen te laden voor een gebruiker, afhankelijk van het aantal teams en kanalen waarvoor de groep standaard is ingesteld. In onze tests duurde het 6 seconden voor een organisatie met 200.000 gebruikers en 30.000 gekoppelde groepen. .. Opmerking:

   Gebruikers worden niet verwijderd uit het team of kanaal bij opeenvolgende synchronisaties van de AD/LDAP-groepen. Gebruikers moeten handmatig worden verwijderd uit het team of kanaal per de bestaande functionaliteit. Ze worden niet opnieuw toegevoegd als ze handmatig worden verwijderd of verwijderd. Een team of een besloten kanaal beheren met gesynchroniseerde groep
s, zie ` deze documentatie <https://docs.mattermost.com/deployment/ldap-group-constrained-team-channel.html> ` _. .. afbeelding:: ../images/Team_Channel_Membership_Sync.png

Geconfigureerde teams en kanalen uit een groep verwijderen
---------------------------------------------------

Als u een team of kanaal wilt verwijderen dat is geconfigureerd voor een groep, klikt u op ** Remove** rechts van het team of de kanaalnaam. Gebruikers die al deel uit maken van het team en het kanaal worden door deze actie niet uit dat kanaal verwijderd.

Gebruikers van de groep bekijken
------------------------------------

Gebruikers die zijn aangemeld en Matterbest hebben benaderd, zijn zichtbaar in de ledenlijst van het groepsobject. Leden zijn alleen-lezen op dit moment en nieuwe leden kunnen worden toegevoegd via het beheer in uw AD/LDAP-systeem. .. image:: ../images/Group_Members.png

Gebruikers kunnen worden verwijderd uit de Matterbest-groep bij opeenvolgende synchronisaties. Ze worden echter niet verwijderd uit teams en kanalen, tenzij het team of het kanaal groepsgesynchroniseerd is. Opmerking:

   Wanneer een lid zichzelf handmatig uit een kanaal verwijdert, wordt die actie gevolgd in de tabel ** Channel Member History * *. Gebruikers worden niet opnieuw toegevoegd aan kanalen waaruit ze zichzelf eerder hebben verwijderd.

AD/LDAP-gebruikers uitschakelen en opnieuw activeren
-----------------------------------------

Als een gebruiker wordt verwijderd uit een AD/LDAP-groep en later opnieuw wordt toegevoegd, worden deze opnieuw gebruikt in de teams en kanalen die in de groep zijn geconfigureerd. Als een gebruiker in AD/LDAP wordt gedeactiveerd of gefilterd uit het AD/LDAP-gebruikersfilter, worden deze verwijderd uit de groep en verliezen ze de toegang tot Matterbest. Als die gebruiker wordt gereactiveerd, krijgen ze weer toegang tot de teams en kanalen, evenals eventuele extra teams en kanalen die worden toegevoegd aan de Mattermeeste groepsconfiguratie.

Groepen beheren
---------------

Als een groep eenmaal is geconfigureerd, kunnen de standaardteams en kanalen worden gewijzigd via de optie ** Edit** in de groepslijstweergave.

Groepen wissen
---------------

Mattermeeste groepen kunnen worden verwijderd door uw AD/LDAP-groepsfilter aan te passen om de groep te verwijderen of door de groep los te koppelen van de groepenlijst. Als u de groep weer toevoegt door het AD/LDAP-groepsfilter opnieuw aan te passen en de groep opnieuw te koppelen aan de groepconfiguratiepagina, zijn de vorige team-en kanaalconfiguraties beschikbaar.

AD/LDAP-gesynchroniseerde groepen gebruiken om het lidmaatschap van een team of een besloten kanaal te beheren
-------------------------------------------------------------------------------

De meeste groepen die zijn gemaakt met gesynchroniseerde AD/LDAP-groepen kunnen worden gebruikt voor het beheren van het lidmaatschap van private teams en private kanalen. Wanneer een team of een besloten kanaal wordt beheerd door gesynchroniseerde groepen, worden de gebruikers toegevoegd en verwijderd op basis van hun lidmaatschap van de gesynchroniseerde AD/LDAP-groep. .. Opmerking:

   Het is niet mogelijk om gasten toe te voegen aan teams en kanalen die worden beheerd met behulp van groepen.

U kunt bijvoorbeeld een AD/LDAP-groep hebben die uw ontwikkelteam bevat dat u wilt synchroniseren met een ontwikkelingsteam. Als u deze functie gebruikt, worden nieuwe ontwikkelaars toegevoegd aan het team wanneer ze worden toegevoegd aan de gesynchroniseerde AD/LDAP-groep en worden ze uit het team verwijderd wanneer ze worden verwijderd uit de AD/LDAP-groep.

Op dezelfde manier kunt u een AD/LDAP-groep hebben die uw leiderschapsteam bevat dat u wilt synchroniseren met een besloten kanaal voor coördinatie en updates.

Deze functie helpt bij het besturen van het lidmaatschap van het kanaal, zodat gasten en gebruikers buiten de gesynchroniseerde groep niet per ongeluk aan het kanaal kunnen worden toegevoegd.

Voor teams die worden beheerd door gesynchroniseerde groepen, zijn de gasten en gebruikers buiten de groep beperkt tot:

 -Uitnodiging via een team uitnodigen link
 -Uitnodigingen via een e-mail uitnodigen

Op persoonlijke kanalen die worden beheerd door gesynchroniseerde groepen, worden de gasten en de leden van de groep buiten de groep beperkt van:

 -Uitnodiging door middel van een vermelding
 -Uitnodiging via de ` ` /invite ` ` slash opdracht
 -toegevoegd aan het kanaal met "leden toevoegen"

Gebruikers kunnen zichzelf verwijderen van teams en private kanalen die door gesynchroniseerde groepen worden beheerd.

Het beheren van het lidmaatschap van een team of een kanaal met gesynchroniseerde groepen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het lidmaatschap van een besloten team beheren met gesynchroniseerde groepen:

1. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Teams * *. Selecteer het team dat u wilt beheren met groepssynchronisatie.
2. Onder ** Team Management * *, enable ** Sync Group Members * *. Als ** Iedereen kan deelnemen aan dit team * * is ingeschakeld of als er specifieke e-maildomeinen zijn ingesteld, worden deze uitgeschakeld door de functie Sync-groepsleden.
3. Voeg een of meer groepen toe aan het team. Als er al groepen aan standaardgebruikers in het team zijn gekoppeld, zijn ze al aanwezig.
4. Bekijk de aankondiging in de voettekst van het scherm voor gebruikers die geen deel uitmaken van groepen die worden verwijderd uit het team op de volgende synchronisatie.
5. Klik op ** Save**. De leden worden bijgewerkt op de volgende geplande AD/LDAP-synchronisatie.

Als alternatief kunt u de CLI-tool gebruiken om het team in te stellen dat wordt beheerd door groepen:

1. Zorg ervoor dat er ten minste één groep aan het team is gekoppeld. U kunt standaardteams bekijken en toevoegen aan een groep via ** System Console > Gebruikersbeheer > Groepen > Groepsconfiguratie * *. Zie meer informatie over het toevoegen van standaard teams en kanalen ` hier <https: //docs.mattermost.com/deployment/ldap-group-sync.html#add-default-teams-or-channels-for-the-group> ` _. Daarnaast kunt u de CLI-tool gebruiken om te bekijken of er al een groep aan het team is gekoppeld door de ' group team list CLI command <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-group-team-list> ` _ uit te voeren.
2. Zorg ervoor dat ** Team-instellingen > Algemeen > elke gebruiker met een account op deze server toestaan om deel te nemen aan dit team * * is ingesteld op ` ` Nee ` `.
3. Converteer het team om het lidmaatschap van de groep te laten beheren door gesynchroniseerde groepen door het ` group team in te schakelen CLI-opdracht <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-group-team-enable> ` _.

Het lidmaatschap van een besloten kanaal beheren met gesynchroniseerde groepen:

1. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Kanalen * *. Selecteer het kanaal dat u wilt beheren met groepssynchronisatie.
2. Onder ** Channel Management * *, enable ** Sync Group Members * *. Controleer of het kanaal is ingesteld op ` ` private ` `.
3. Voeg een of meer groepen toe aan het kanaal. Als er al groepen aan standaardgebruikers in het kanaal zijn gekoppeld, zijn ze al aanwezig.
4. Bekijk de aankondiging in de voettekst van het scherm voor gebruikers die geen deel uitmaken van groepen die worden verwijderd uit het kanaal op de volgende synchronisatie.
5. Klik op opslaan. De leden worden bijgewerkt op de volgende geplande AD/LDAP-synchronisatie.

U kunt ook de CLI-tool gebruiken om een besloten kanaal in te stellen voor beheer door groepen:

1. Zorg ervoor dat er ten minste één groep aan het kanaal is gekoppeld. U kunt standaardkanalen bekijken en toevoegen aan een groep via ** System Console > Gebruikersbeheer > Groepen > Groepsconfiguratie * *. Zie meer informatie over het toevoegen van standaard teams en kanalen ` hier <https: //docs.mattermost.com/deployment/ldap-group-sync.html#add-default-teams-or-channels-for-the-group> ` _. Daarnaast kunt u de CLI-tool gebruiken om te bekijken of er al een groep aan het kanaal is gekoppeld door het uitvoeren van de CLI-opdracht voor het groepskanaal <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-group-team-list> ` _.
2. Converteer het team zodat het lidmaatschap wordt beheerd door gesynchroniseerde groepen door het uitvoeren van de CLI-opdracht <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-group-channel-enable> ` _.

Rollen aan groepsleden toewijzen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Groepsleden kunnen vooraf gedefinieerde rollen toegewezen krijgen door systeembeheerders, die tijdens de geplande sychronisatie binnen de groep worden toegepast. De rollen zijn:

-Lid (standaard)
-Teambeheer (in teams)
-Kanaalbeheerder (in kanalen)

De machtigingen voor elke rol kunnen worden bekeken en gewijzigd in ** Systeemconsole > Machtigingen * *.

** Om de rol Team Admin in te stellen in een gesynchroniseerde groep * *

1. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Teams * *.
2. Selecteer ** Bewerken ** naast het team dat u wilt configureren.
3. Zorg ervoor dat ** Sync Group Members * * is ingeschakeld.
4. Kies ** Groep toevoegen * * om een of meer groepen toe te voegen aan het team. Als er al groepen aan standaardgebruikers in het team zijn gekoppeld, zijn ze al aanwezig.
5. Selecteer de pijl naast de huidige rol in de kolom ** Roles** om de optie ** Team Admin * * af te beelden en te selecteren.
6. Herhaal indien nodig voor alle andere gesynchroniseerde groepen die u hebt toegevoegd.
7. Kies ** Save**.

Rollen worden bijgewerkt op de volgende geplande AD/LDAP-synchronisatie.

** Om de rol Channel Admin in te stellen in een gesynchroniseerde groep * *

1. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Kanalen * *.
2. Selecteer ** Bewerken ** naast het team dat u wilt configureren.
3. Zorg ervoor dat ** Sync Group Members * * is ingeschakeld.
4. Kies ** Groep toevoegen * * om een of meer groepen toe te voegen aan het team. Als er al groepen zijn assoc
Als u de standaardgebruikers in het team hebt opgegeven, zijn ze al aanwezig.
5. Selecteer de pijl naast de huidige rol in de kolom ** Roles** om de optie ** Channel Admin * * af te beelden en te selecteren.
6. Herhaal indien nodig voor alle andere gesynchroniseerde groepen die u hebt toegevoegd.
7. Kies ** Save**.

Rollen worden bijgewerkt op de volgende geplande AD/LDAP-synchronisatie.

** Note:**
Leden die zijn gesynchroniseerd als onderdeel van een groep, kunnen hun rol niet wijzigen via ** Leden bekijken * * in Matterbest.

Groepen toevoegen of verwijderen uit teams ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Nadat het beheer van het team is geconverteerd om te worden beheerd door gesynchroniseerde groepen, kan een team of systeembeheerder extra groepen toevoegen vanuit ** Hoofdmenu > Groepen toevoegen aan team * *. Dit voegt gebruikers toe aan de volgende AD/LDAP-synchronisatie en alle nieuwe gebruikers aan de groep worden toegevoegd aan het team bij volgende synchronisaties. Teambeheerders kunnen het team niet naar het openbaar wijzigen door het inschakelen van ** Team-instellingen > Alle gebruikers met een account op deze server toestaan om deel te nemen aan dit team * *.

Team-of systeembeheerders kunnen groepen ook uit een team verwijderen uit ** Hoofdmenu > Groepen beheren * *. Hiermee wordt de groep losgekoppeld van het team. Gebruikers worden verwijderd op de volgende AD/LDAP-synchronisatie.

De systeembeheerder kan ook groepen verwijderen uit ** Systeemconsole > Gebruikersbeheer > Teams > Teamconfiguratie > Synced-groepen * *.

Groepen toevoegen of verwijderen uit persoonlijke kanalen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Nadat het beheer van het kanaal is geconverteerd om te worden beheerd door gesynchroniseerde groepen, kan een team of systeembeheerder extra groepen toevoegen vanuit ** Channel Menu > Groepen toevoegen aan kanaal * *. Dit zal gebruikers toevoegen aan de volgende AD/LDAP-synchronisatie en eventuele nieuwe gebruikers aan de groep worden toegevoegd aan het kanaal bij volgende synchronisaties.

Team-of systeembeheerders kunnen groepen ook uit een team verwijderen uit ** Hoofdmenu > Groepen beheren * *. Hiermee wordt de groep losgekoppeld van het team. Gebruikers worden verwijderd op de volgende AD/LDAP-synchronisatie.

De systeembeheerder kan ook groepen verwijderen uit ** System Console > User Management > Channels > Channel Configuration > Synced Groups * *.

Het beheren van de leden ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Gebruikers worden automatisch uit het team of het besloten kanaal verwijderd wanneer ze worden verwijderd uit een gesynchroniseerde AD/LDAP-groep die het lidmaatschap van dat team of dat kanaal beheert. Bovendien worden gebruikers die niet in de gesynchroniseerde groepen voorkomen, niet meer toegevoegd via de ` ` /invite ` ` en worden de stromen binnen een kanaal vermeld.

Een gebruiker kan zichzelf uit het team of uit het besloten kanaal verwijderen wanneer het wordt beheerd door gesynchroniseerde groepen. Ze kunnen worden toegevoegd door gebruikers die gemachtigd zijn om leden voor een team of een besloten kanaal te beheren met behulp van de schuine streep naar rechts of door de gebruiker in een kanaal te vermelden.

Als de gebruiker wordt verwijderd uit een gesynchroniseerde groep en later wordt aangepast aan de groep, kunnen ze handmatig worden toegevoegd aan het team of Private kanaal zoals hierboven vermeld. .. opmerking:: Gebruikers worden niet automatisch toegevoegd door de AD/LDAP-synchronisatie zodra ze zichzelf verwijderen of door de LDAP-gesynchroniseerde groep worden verwijderd.

Het uitschakelen van groep gesynchroniseerd beheer van teams en particuliere kanalen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als u het beheer van leden door gesynchroniseerde groepen in een team wilt verwijderen, schakelt u ** Sync Group Members * * onder ** System Console > User Management > Teams > Team Management * * uit, of start u het ` group team disable CLI command <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-group-team-disable> ` _.

Om het beheer van leden te verwijderen door gesynchroniseerde groepen in een kanaal, schakelt u ** Sync Group Members * * onder ** Systeemconsole > Gebruikersbeheer > Kanalen > Kanaalbeheer * * uit, of voert u het ` group channel disable CLI command <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-group-channel-disable> ` _.

Veelgestelde vragen
----------------------------

Waarom kunnen mijn bestaande gebruikers niet de teams en kanalen zien waar ze zijn gesynchroniseerd? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Bestaande Mattermeeste gebruikers die lid zijn van gekoppelde Mattermeeste groepen worden toegevoegd aan teams en kanalen op de volgende geplande synchronisatietaak die wordt uitgevoerd na teams en kanalen worden toegevoegd aan de Mattermeeste groep. U kunt handmatig een synchronisatie starten vanuit ** System Console > Authentication > AD/LDAP > AD/LDAP Synchronize Now * *.

Hoe werken geneste groepen met AD/LDAP Group Sync? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Gebruikers binnen geneste groepen worden opgenomen als leden van bovenliggende groepen. Het groepsfilter dat u opgeeft, kan elk type AD/LDAP-groep op uw systeem bevatten. Het ` ` member ` ` AD/LDAP-kenmerk wordt gebruikt om geneste groepen te bepalen die tot een bovenliggende groep behoren.

Hoe beheer ik een team of een besloten kanaal met gesynchroniseerde groepen? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

U kunt dit doen door het team-of kanaalbeheer in te stellen op gesynchroniseerde groepen in plaats van een groep in te stellen op een team of kanaal. Zie ` deze documentatie <https://docs.mattermost.com/deployment/ldap-group-constrained-team-channel.html> ` _ voor meer informatie.

Hoe gebruik ik AD/LDAP Group Sync met SAML? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

U kunt AD/LDAP Group Sync gebruiken met SAML door 'SAML Synchronization met AD/LDAP <https: //docs.mattermost.com/deployment/sso-saml-okta.html#configure-saml-synchronisatie-met-ad-ldap>' _. U hoeft de aanmelding met LDAP niet in te schakelen voor deze functie.

Het is echter essentieel dat het unieke ID-ID dat u hebt gekozen als uw kenmerk in uw directoryservice (AD/LDAP) hetzelfde is voor zowel de SAML-als de AD/LDAP-configuratie.

Als bijvoorbeeld ` ` ObjectGUID ` ` is gekozen als het Mattermeest ID in uw AD/LDAP-configuratie, moet een kenmerk dat dezelfde waarde heeft ook worden toegewezen aan het ID-kenmerk in uw SAML-bevestiging. We raden ook aan dat het ID-attribuut dat u selecteert uniek en onveranderend is (zoals een ` ` ` GUID ` ` `).

Waarom worden geen openbare kanalen ondersteund met gesynchroniseerde groepen? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Openbare kanalen zijn beschikbaar voor alle leden om te ontdekken en toe te treden. Het beheren van het lidmaatschap met gesynchroniseerde groepen verwijdert de mogelijkheid voor openbare kanalen om toegankelijk te zijn voor gebruikers in het team. Voor besloten kanalen is doorgaans een meer bestuurde lidmaatschapsbeheer vereist. Dit is de reden waarom deze functie van toepassing is op besloten kanalen. Groepen kunnen worden toegewezen aan openbare teams en openbare kanalen zoals beschreven in ` this documentation <https: //docs.mattermost.com/deployment/ldap-group-sync.html#add-default-teams-or-channels-for-the-group> ` _.

Heeft een team met een door groepen beheerd lidmaatschap enig effect op de toegang van het openbaar kanaal? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Alleen gebruikers die lid zijn van groepen die zijn gesynchroniseerd met het team, zijn in staat om openbare kanalen te ontdekken en aan te sluiten.  Private kanalen kunnen ook worden beheerd door gesynchroniseerde groepen wanneer een team wordt beheerd door gesynchroniseerde groepen.

Waarom worden gebruikers niet tot teams of kanalen aangepast nadat ze zijn verwijderd en later opnieuw aan de LDAP-groep zijn toegevoegd? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De implementatie van groepsverwijderingen maakt momenteel geen onderscheid tussen gebruikers die zichzelf hebben verwijderd of die door het LDAP-synchronisatieproces zijn verwijderd. Ons ontwerp optimaliseert gebruikers die zichzelf hebben verwijderd van een team of kanaal. In de toekomst kunnen we de mogelijkheid voor beheerders toevoegen om gebruikers opnieuw toe te voegen die zijn verwijderd, en zelfs te voorkomen dat gebruikers vertrekken, een team of kanaal.

Bovendien worden LDAP-gebruikers die niet toegankelijk zijn voor Matterbest op basis van filters, verwijderd uit de groepen en uit synced-teams en kanalen van de groep. Als ze werden verwijderd uit teams en kanalen dan zullen ze niet opnieuw worden toegevoegd aan die teams en kanalen nadat ze vervolgens opnieuw toegankelijk zijn voor Matterbest.
