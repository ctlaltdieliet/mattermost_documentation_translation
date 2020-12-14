.. _guestaccounts:

Gastaccounts (Beta) (E10/E20)
== == == == == == == == == == == == == == == ==

Beschikbaar in ` Enterprise Edition E10 en hoger <https://mattermost.com/pricing-self-managed/> ` __.

Gasten Accounts zijn een manier om samen te werken met individuen (zoals leveranciers en aannemers) buiten uw organisatie door het controleren van hun toegang tot kanalen en teamleden. Bijvoorbeeld: Guest Accounts kan worden gebruikt om samen te werken met klanten over een ondersteuningskwestie of om te werken aan een websiteproject met middelen van een extern ontwerpbureau.

Gasten kunnen:

-Speld berichten naar kanalen
-Gebruik schuine commando &apos; s (met uitzondering van beperkte commando &apos; s zoals uitnodigen leden, hernoemen van kanalen, wijzigen headers, etc)
-Favoriete kanalen
-Mute kanalen
-Update hun account instellingen

Gasten kunnen niet:

-Ontdek de publieke zenders
-Deelnemen aan open teams
-Maak directe berichten of groepsberichten met leden die zich niet in hetzelfde kanaal bevinden
-Personen uitnodigen

Bovendien worden de gasten niet automatisch toegevoegd aan de standaard ` ` Town-square ` ` ` en ` ` Off-topic ` ` kanalen bij het aanmelden en moeten ze handmatig worden uitgenodigd/toegevoegd.

Gastaccounts inschakelen ------------------------

1. Navigeer naar ** Systeemconsole > Verificatie > Gasttoegang * *.
2. Instellen ** Schakel Guest Access * * in op ` ` True ` `.
3. (Optioneel) ** Whitelistische domeinen die acceptabel zijn voor Guest Access * *.
 -Hiermee kunnen de systeembeheerders een lijst van goedgekeurde gastdomeinen instellen. Als u teamdomeinbeperkingen hebt, moet u ook uw gastdomein toevoegen aan ** Teaminstellingen > Alleen gebruikers met een specifiek e-maildomein toestaan om deel te nemen aan dit team * *.
4. (Optioneel) ** Enforce Multi-Factor Authentication (MFA) voor uw gasten * *.
 -Als u MFA handhaaft voor uw gebruikers, kunt u desgewenst kiezen voor het afdwingen van MFA voor uw gastgebruikers.

Gastverificatie
---------------------

Gasten hebben toegang tot de Mattermeeste server via e-mail en worden geverifieerd met behulp van AD/LDAP of SAML 2.0.

Voordat u doorgaat, moet u ervoor zorgen dat de verificatiemethode die u wilt gebruiken correct is geconfigureerd op uw server en in Matterbest is ingeschakeld. Voor configuratiestappen en technische documentatie raadpleegt u ` Active Directory/LDAP Setup <https://docs.mattermost.com/deployment/sso-ldap.html> ` _ en ` SAML Single-Sign-On <https://docs.mattermost.com/deployment/sso-saml.html> ` _.

Het converteren van een gebruiker naar een gast verandert niet de kanalen waarin ze zich bevinden. Ze zullen echter worden beperkt door het ontdekken van extra kanalen en kunnen gebruikers van Message/Group Message/Group niet buiten de kanalen waar ze zich bevinden te vinden. Ze kunnen worden toegevoegd aan kanalen door systeembeheerders en andere rollen die de juiste machtigingen hebben om gasten uit te nodigen.

Gasten uitnodigen voor de Mattermeeste Server via e-mail
---------------------------------------------------

Gasten kunnen worden uitgenodigd in een of meer Mattermeeste kanalen binnen een team door System Admins en andere rollen die de juiste toestemming hebben om gasten uit te nodigen. Een gast kan worden uitgenodigd in kanalen op meerdere teams.

** Opmerking: ** Gastuitnodigingen worden herroepen na 48 uur per m
lid-e-mailuitnodiging. Als uw gast de uitnodiging binnen die periode niet heeft geaccepteerd, volg dan de onderstaande stappen om een uitnodiging aan de gast te verzenden.

Gasten uitnodigen in een of meer Mattermeeste kanalen:

1. E-mail inschakelen vanuit ** System Console > Signup > E-mailuitnodigingen inschakelen * *.
2. Navigeer naar ** Hoofdmenu > Uitnodigen * *. Dit is een nieuwe uitnodiging die uitnodigt om gasten en leden uit te nodigen en te consolideren ** E-mail verzenden * *, ** Get Team Invite Link * *, en ** Leden toevoegen aan het Team * *.
3. Selecteer ** Gasten Uitnodigen * *.
4. Voer het e-mailadres van de gast in.
5. Kies de kanalen waar de gast mee kan meedoen (exclusief beheerde teams).
6. (Optioneel) Voer een aangepast bericht in. image:: ../images/Guest_Invite_Screen.png

AD/LDAP-verificatie configureren
----------------------------------

Als deze optie is ingeschakeld, geeft het ** Guest Filter * * in Matterbest de externe gebruikers aan waarvan de AD/LDAP-rol ` ` gast ` ` is en die worden uitgenodigd om deel te nemen aan uw Mattertiste server. Deze gebruikers hebben de ` ` guest ` ` rol direct op het eerste teken-in plaats van de standaard gebruikersrol van de gebruiker. Hierdoor hoeft u de rol in de systeemconsole niet handmatig toe te wijzen.

1. Activeer Guest Access via ** System Console > Verificatie > Gasttoegang (Beta) * *.
2. Navigeer naar ** Systeemconsole > Verificatie > AD/LDAP* *.
3. Voltooi het veld ** Guest Filter * *.
4. Kies ** Save**.

Als een Mattermeeste gast de ` ` guest ` ` rol heeft verwijderd in het AD/LDAP systeem, zal het synchronisatieproces deze niet automatisch promovenen naar een rol van een lid-gebruiker. Dit gebeurt handmatig via ** System Console > Gebruikersbeheer * *. Als een gebruiker het kenmerk ** Gast heeft * * heeft toegevoegd, worden de gebruikersrol automatisch door de synchronisatieprocessen aan de gebruiker toegewezen.

Wanneer een gast zich aanmeldt zonder dat er een kanaal is toegewezen aan hun account, wordt het aangeraden contact op te nemen met een beheerder. 

SAML 2.0-verificatie configureren
------------------------------------

Als dit is ingeschakeld, geeft het ** Guest Attribute * * in Matterbest de externe gebruikers aan waarvan de SAML-bevestiging gast is en die worden uitgenodigd om deel te nemen aan uw Mattertiste server. Deze gebruikers hebben de ` ` guest ` ` rol direct op het eerste teken-in plaats van de standaard gebruikersrol van de gebruiker. Hierdoor hoeft u de rol in de systeemconsole niet handmatig toe te wijzen.

Als een Mattermeeste gastgebruiker de gastrol heeft verwijderd in het SAML-systeem, worden deze niet automatisch door de synchronisatieprocessen naar een gebruikersrol van een lid bevorderd. Dit gebeurt handmatig via ** System Console > Gebruikersbeheer * *. Als een gebruiker het kenmerk ** Gast heeft * * heeft toegevoegd, worden de gebruikersrol automatisch door de synchronisatieprocessen aan de gebruiker toegewezen.

1. Schakel Guest Access via ** System Console > Guest Access (Beta) * * in.
2. Navigeer naar ** Systeemconsole > Verificatie > SAML 2.0 * *.
3. Vul het veld ** Guest Attribute * * in.
4. Kies ** Save**.

Wanneer een gast zich aanmeldt zonder dat er een kanaal is toegewezen aan hun account, wordt het aangeraden contact op te nemen met een beheerder.

Instellingen voor gastmachtiging
-------------------------

In E10 en E20 kunt u ook bepalen welke gebruikers gasten kunnen uitnodigen. Standaard kunnen alleen de systeembeheerders gasten uitnodigen. Er zijn ` aanvullende machtigingen <https://docs.mattermost.com/deployment/advanced-permissions.html> ` _ in E20 die aangepast kunnen worden onder ** Systeemconsole > Geavanceerde machtigingen > Systeemschema * * om de mogelijkheden van een gast te bepalen:

 -Artikelen bewerken
 -Berichten verwijderen
 -Post-reacties
 -Maak private kanalen met leden die ze mogen samenwerken met

Gast-ID
---------------------

Gasten worden geïdentificeerd met een ** Guest** badge. Deze badge is zichtbaar op verschillende plaatsen op de interface en mobiele apps zoals op het profiel van een gast en naast hun naam op gebruikerslijsten, waaronder @mentions en quick switcher lists. Wanneer de gasten aan een kanaal worden toegevoegd, informeert een systeembericht andere kanaalleden dat de toegevoegde gebruiker een gast is.

Kanalen met de gasten zullen hun header automatisch bijgewerkt met een bericht met de vermelding: * Dit kanaal heeft gasten *. .. afbeelding:: ../images/Guest_Badges.png

Gasten beheren
---------------

Het toevoegen van gasten aan extra kanalen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Gebruikers met de toestemming om gasten uit te nodigen kunnen ** uitnodigden Gasten * * naar extra kanalen. Er wordt een systeebericht in de kanalen geplaatst om andere leden te laten weten dat er een gastgebruiker is toegevoegd.

Het verwijderen van gasten uit kanalen en teams ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

U kunt de gasten uit een kanaal verwijderen via ** Leden beheren * *, of door de opdrachten ` ` /kick ` ` of ` ` /remove ` ` te gebruiken.

Wanneer een gast van alle kanalen in een team is verwijderd, en als ze tot andere teams behoren, zullen ze standaard in het laatste kanaal van het laatste team dat ze hebben benaderd. Als ze worden verwijderd uit alle kanalen op alle teams, ze zullen worden genomen om een scherm hen te laten weten dat ze geen kanalen toegewezen.

Bevordering en Demoting Gebruikersrollen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Systeembeheerders kunnen een gast degraderen door hun rol in ** Systeemconsole > Gebruikersbeheer > Gebruikers * * te updaten. De gedegrateerde gebruiker behoudt hun bestaande kanaal-en teamlidmaatschappen, maar blijft beperkt tot het ontdekken van openbare kanalen en werkt samen met gebruikers buiten de kanalen waarin ze zich bevinden.  Dit is handig als u al samenwerkt met externe aannemers en hun mogelijkheden in uw Mattermeeste-instance wilt beperken.

Systeembeheerders kunnen een gast ook promovenen door hun rol bij te werken in ** Systeemconsole > Gebruikersbeheer > Gebruikers * *.

** Opmerking: ** U kunt de lijst in ** Systeemconsole > Gebruikersbeheer > Gebruikers * * filteren om alle gasten op het systeem te bekijken.

Gastaccounts uitschakelen
------------------------

Om de functie Guest Accounts uit te schakelen, gaat u naar ** System Console > Authentication > Guest Access (Beta) > Enable Guest Access * * en selecteert u ` ` False ` `. In versies ouder dan 5.18 blijven de huidige Guest Accounts actief totdat de gastgebruikers handmatig ' ` inactief ` ` zijn gemarkeerd in ** System Console > Gebruikersbeheer > Gebruikers * *.

Vanaf 5.18, als je ons bent
AD/LDAP en de Guest Access-instelling is uitgeschakeld, het gastfilter en bestaande gastgebruikers in de systeemconsole worden gedeactiveerd. Bovendien kunnen er geen nieuwe gasten worden uitgenodigd of toegevoegd met behulp van het filter als verificatiemethode. Als de legitimatiegegevens van een eerdere gast overeenkomen met het gebruikersfilter (het enige filter dat actief is als de gasttoegang uitgeschakeld is), worden deze opnieuw geactiveerd en gepromoveerd naar een gebruiker bij de volgende aanmelding.

Om de functie Guest Accounts uit te schakelen, gaat u naar ** System Console > Authentication > Guest Access (Beta) > Enable Guest Access * * en selecteert u ` ` False ` `. In versies ouder dan 5.18 blijven de huidige Guest Accounts actief totdat de gastgebruikers handmatig ' ` inactief ` ` zijn gemarkeerd in ** System Console > Gebruikersbeheer > Gebruikers * *.

Op dezelfde manier worden de instellingen voor Guest Access voor SAML, wanneer de instellingen voor de Guest Access uitgeschakeld zijn, gedeactiveerd als het gastkenmerk en de bestaande gastgebruikers in de systeemconsole zijn uitgeschakeld. Bovendien kunnen geen nieuwe gasten worden uitgenodigd of toegevoegd met het kenmerk als verificatiemethode. Als de legitimatiegegevens van een eerdere gast overeenkomen met het gebruikerskenmerk (het enige kenmerk dat actief is wanneer gasttoegang is uitgeschakeld), worden deze opnieuw geactiveerd en gepromoveerd naar een gebruiker bij de volgende aanmelding.

U kunt afzonderlijke gastaccounts uitschakelen in ** Systeemconsole > Gebruikersbeheer * * via ** Leden beheren * *. Vanaf versie 5.18, wanneer een enkele gastaccount is uitgeschakeld of de functie is uitgeschakeld, wordt de gast gemarkeerd als ` ` inactief ` `, afgemeld van Matterbest, en alle sessies worden ingetrokken.

Het herstellen van gastaccounts
--------------------------

Wanneer Guest Access opnieuw is ingeschakeld voor AD/LDAP, wordt het gastfilter opnieuw ingesteld. 

Nieuwe gebruikers die overeenkomen met het gastfilter worden geverifieerd als nieuwe gastgebruikers bij aanmelding.

Eerdere gastgebruikers worden geactiveerd met de volgende synchronisatie. Als hun legitimatiegegevens nog steeds overeenkomen met de gastfilter, behouden ze hun gaststatus. Als ze niet meer overeenkomen met de gastfilter maar wel overeenkomen met het gebruikersfilter, worden ze niet automatisch gepromoveerd aan de gebruiker bij aanmelding-dit moet handmatig gebeuren. Als een vorige gast werd gereactiveerd als een lid gebruiker toen Guest Access werd uitgeschakeld, en nu worden geïdentificeerd door de Guest Filter opnieuw, zullen ze automatisch worden gedegradeerd naar Gast op hun login.

Op dezelfde manier wordt het SAML Guest Attribute voor SAML, wanneer Guest Access opnieuw is ingeschakeld, opnieuw ingesteld. Nieuwe gebruikers die overeenkomen met het gastkenmerk worden geverifieerd als nieuwe gastgebruikers bij aanmelding.

Eerdere gastgebruikers worden geactiveerd met de volgende synchronisatie.  Als hun legitimatiegegevens nog steeds overeenkomen met het gastkenmerk, behouden ze hun gaststatus. Als ze niet meer overeenkomen met het gastkenmerk maar wel overeenkomen met het gebruikersfilter, worden ze niet automatisch gepromoveerd aan de gebruiker bij aanmelding. Dit moet handmatig gebeuren. Als een vorige gast is gereactiveerd als een lid-gebruiker wanneer de gast toegang is uitgeschakeld, en nu worden geïdentificeerd door de Guest Attribute nogmaals, zullen ze automatisch worden gedegradeerd naar Gast op hun login.

Veelgestelde vragen
---------------------------

Hoe moet ik rekening houden met de rekeningen van de gast? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Gasten worden als gebruikerszetel in rekening gebracht.

Waarom heeft Mattermeeste geen enkele-kanaals gasten? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

We wilden de samenwerking met externe gasten voor de breedste use cases ondersteunen zonder de toegang van gasten tot kanalen te beperken. In de toekomst kunnen we overwegen het toevoegen van single-channel gasten.

Kan ik een vervaldatum voor de gasten instellen? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Op dit moment kun je dat niet. Deze functie kan later worden toegevoegd.

Kan de MVO selectief worden toegepast? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als MFA wordt afgedwongen voor uw gebruikers, kan deze worden toegepast op Guest Accounts. Gasten kunnen MFA configureren in ** Accountinstellingen > Beveiliging * *. Als MFA niet wordt afgedwongen voor uw gebruikers, kan het niet worden toegepast op Guest Accounts.

Waarom is de Guest Account functie in Beta? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De Guest Account functie is in beta terwijl wij reageren op feedback van onze klanten op de functie.

Is de Score Accounts functie is beoordeeld door een externe beveiligingsfirma? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De functie Guest Account is gecontroleerd door het Matterbest Security Team. We hebben geen externe, stevige beoordeling gepland, maar zal deze functie in toekomstige beoordelingen.

Hoe kan ik de identiteit van mijn gasten valideren? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Gasten kunnen worden geverifieerd via SAML en/of AD/LDAP om ervoor te zorgen dat alleen de genoemde gast kan aanmelden. U kunt ook domeinen witelist via ** System Console > Guest Access > Whitelisted Guest Domains * *.

Kan ik de mogelijkheden van de gasten om inhoud te uploaden beperken? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Het is momenteel niet mogelijk om de upload/download functionaliteit selectief uit te schakelen omdat het een configuratie voor de hele server is.
