Geavanceerde machtigingen (E10/E20)
== == == == == == == == == == == == == == ==

Mattermeeste Admins kunnen geavanceerde machtigingen gebruiken om aan te passen welke gebruikers specifieke acties kunnen uitvoeren, zoals het maken van teams, het beheren van kanalen en het configureren van webhooks. Het Mattermeeste-machtigingssysteem is gebaseerd op een gewijzigde RBAC-architectuur (role-based access control), waarbij rollen worden gebruikt om te bepalen welke gebruikers de mogelijkheid hebben om verschillende acties uit te voeren.

Er zijn twee machtigingsschema's beschikbaar in Matterbest: 

* Systeemschema: Toestand machtigingen universeel in alle teams en kanalen.
* Team override-schema's: beheerders toestaan om machtigingen voor elk team aan te passen.

Dit document beschrijft de typen machtigingen die kunnen worden verleend aan gebruikers van Matterbest met behulp van programma's en kanaalinstellingen en rollen. De ` permissies backend documentatie <https://docs.mattermost.com/deployment/permissions-backend.html> ` _ biedt extra technische details rond permissies. .. Opmerking:

  Dit document is van toepassing op Mattermeeste Server versie 5.0 en hoger. Voor eerdere versies, zie ` permission settings available in the System Console > Policy page <https: //docs.mattermost.com/administration/config-settings.html#policy> ` __.


... Inhoud:
  :backlinks: boven: lokaal:
  
Machtigingen structuur
----------------------

De Matterbest System Console bevat een aantal elementen voor Admins voor het besturen van de machtigingen in hun systeem. 

Systeem (E10)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

*Beschikbaar in Enterprise Edition E10 en hoger *

U kunt de standaardmachtigingen instellen voor Systeembeheerders, Teambeheerders, Kanaalbeheerders, Gasten (indien ingeschakeld) en Alle leden. De machtigingen die worden verleend in de System Scheme gelden voor het gehele systeem, wat betekent:

-** Guests:** Als Gast-accounts zijn ingeschakeld, zijn de permissies van toepassing op gastgebruikers in alle kanalen, in alle teams.
-** Alle leden: ** Machtigingen zijn van toepassing op alle leden, inclusief Admins, in alle kanalen, in alle teams.
-** Channel Administrators: ** Machtigingen gelden voor alle Channel Admins in alle kanalen, in alle teams.
-** Teambeheerders: ** Machtigingen zijn van toepassing op alle teambeheerders, in alle teams.

Als u de standaardmachtigingen voor het systeem wilt vervangen in een specifiek team, moet u een Team Override-schema instellen.

U hebt toegang tot de System Scheme-interface in ** Systeemconsole > Gebruikersbeheer > Machtigingen > Systeemschema * * (of ** Systeemconsole > Geavanceerde machtigingen > Systeemschema * * in versies ouder dan 5.12). .. image:: ../images/system-scheme.png

Team-overschrijdingen (E20)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

*Beschikbaar in Enterprise Edition E20 *

Op systemen met meerdere ` Mattermeeste teams <https://docs.mattermost.com/help/getting-started/creating-teams.html> ` _, kan elk team op een unieke manier werken en samenwerken. Team Override Schemes geven Admins de flexibiliteit om de machtigingen aan de behoeften van elk team te kunnen aanpassen.

Wanneer u dit machtigingsschema gebruikt:

-De machtigingen die zijn verleend in een TeamOverride-schema zijn alleen van toepassing in de teams die aan de regeling zijn toegewezen.
-Het systeem is niet van toepassing op teams die worden toegevoegd aan een
Team Overschrijven.
-Teams kunnen slechts deel uitmaken van een Team Override Scheme.

U hebt toegang tot de interface van het team voor het vervangen van het team in ** System Console > Gebruikersbeheer > Machtigingen > Team Override Schema's * * (of ** Systeemconsole > Geavanceerde machtigingen > Machtigingen schema > Team Override schema * * in versies ouder dan 5.12). .. image:: ../images/team-scheme.png

Kanaalmachtigingen --------------------

De interface voor kanaalmachtigingen is toegankelijk in ** System Console > User Management > Channels * *.

Kanaalmoderatie (E20)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Deze content is verplaatst naar ` Team en Channel Management <https://docs.mattermost.com/deployment/team-channel-management.html> ` _.

Aanvullende rollen (E20)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

*Beschikbaar in een toekomstige release van Enterprise Edition E20 *

Hiermee kunnen beheerders aanvullende machtigingen verlenen aan bepaalde gebruikers of aan een groep gebruikers op basis van het lidmaatschap van de AD/LDAP-groep. Machtigingen kunnen worden verleend binnen het bereik van kanalen, teams of systeemniveau.

Recepten
--------

In dit gedeelte vindt u enkele voorbeelden van algemene machtigingen voor teambeheer, kanaalbeheer en algemene machtigingen. 

Teambeheer
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Alleen beheerders, in het specifieke team, toestaan om leden toe te voegen * *

Voorbeeld: In Team A kunnen alleen Team-en System-beheerders nieuwe teamleden toevoegen. Als standaard voor alle andere teams, kunnen alle gebruikers nieuwe leden toevoegen en uitnodigen.

1. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Machtigingen * * (of ** Systeemconsole > Geavanceerde machtigingen * * in versies ouder dan 5.12).
2. Selecteer ** Schema bewerken * *.
3. In het venster ** Alle leden > Teams * * selecteert u het vakje ** Team-leden toevoegen * *. Hiermee wordt het systeem standaard ingesteld voor alle teams.
4. Kies ** Save**.
5. Selecteer de pijl terug om terug te gaan naar het menu ** Permission Schemes * * *.
6. Selecteer ** Nieuw team overschrijven regeling * *.
  i. Naam en beschrijving van de regeling. Bijvoorbeeld ` ` Authorized Personnel Only ` ` with description ` ` Restrict adding team members to Team and System Admins. ` ` ii. Selecteer ** Teams toevoegen * * om Team B toe te voegen aan de lijst ** Selecteer teams om machtigingen te vervangen * * lijst, zoek Team B en kies ** Add**. iii. Schakel in het venster ** Alle leden * * het selectievakje uit voor ** Team-leden toevoegen * *. iv. In het venster ** Teambeheerders * * selecteert u het vakje ** Team-leden toevoegen * *.
7. Kies ** Save**. 8. Selecteer de pijl terug om terug te gaan naar het menu ** Permission Schemes * *. 

Openbaar en particulier beheer van het Kanaal
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

** Beperken die de kanalen kunnen hernoemen en kanaalkoptekst en -doel bewerken * *

Voorbeeld: Als standaardwaarde voor het gehele systeem, kunt u de hernoemen van kanalen en het bewerken van headers en doeleinden beperken tot alleen de beheerders.

1. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Machtigingen * * (of ** Systeemconsole > Geavanceerde machtigingen * * in versies ouder dan 5.12).
2. Selecteer ** Schema bewerken * *.
3. In het venster ** Alle leden * * wordt het vakje voor ** Manage Public Channels > Manage Channel Settings * * ongedaan gemaakt.

De optie ** Kanaal-instellingen beheren * * is nu alleen beschikbaar voor ** Channel Administrators * *, ** Teambeheerders * * en ** Systeembeheerders * *. .. Opmerking:

  Machtigingen voor het hernoemen van kanalen, het bewerken van kanaalkop en het bewerken van het kanaaldoel zijn op dit moment gegroepeerd in een enkele machtiging. Deze worden in een toekomstige release opgesplitst in afzonderlijke machtigingen.

** Beperken wie kanalen kan maken, in specifieke teams * *

Voorbeeld: In Team C beperkt u het maken van openbare kanalen tot Admins. Als de standaard voor alle andere teams, laat iedereen toe om publieke kanalen te creëren.

1. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Machtigingen * * (of ** Systeemconsole > Geavanceerde machtigingen * * in versies ouder dan 5.12).
2. Selecteer ** Schema bewerken * *.
3. In het venster ** Alle leden * *, in het menu ** Manage Public Channels * *, selecteert u het vakje ** Create Channels * *. Hiermee wordt het systeem standaard ingesteld op het maken van openbare kanalen voor alle teams.
4. Kies ** Save**.
5. Selecteer de pijl om terug te gaan naar de interface ** Permission Schemes * *.
6. Selecteer ** Nieuw team overschrijven regeling * *.
  i. Naam en beschrijving van de regeling. Bijvoorbeeld: ` ` Contractor Scheme ` ` met beschrijving ` ` beperken public channel creation to Admins only ` `. ii. Selecteer ** Teams toevoegen * * om Team B toe te voegen aan de lijst ** Selecteer teams om machtigingen te vervangen * * lijst, zoek Team B en kies ** Add**. iii. Schakel in het venster ** Alle leden * * in de sectie ** Openbare kanalen beheren * * het selectievakje uit voor ** Kanalen maken * *. iv. In het venster ** Teambeheerders * *, in de sectie ** Openbare kanalen beheren * *, selecteert u het vakje ** Create Channels * *.
  
Openbare kanalen omzetten naar besloten kanalen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

** Laat alle leden om publieke kanalen om te zetten naar besloten kanalen * *

Voorbeeld: Stel de standaardinstelling in om alle leden, Team Admins en Channel Admins in staat te stellen openbare kanalen om te zetten in Private.

1. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Machtigingen * * (of ** Systeemconsole > Geavanceerde machtigingen * * in versies ouder dan 5.12).
2. Selecteer ** Schema bewerken * *.
3. In het venster ** Alle leden * * ontvinken u het vakje ** Openbare kanalen beheren > Kanalen converteren * *.

Deze machtiging wordt toegepast op alle andere rollen (met uitzondering van de gastrol). Als deze machtiging niet is ingeschakeld voor alle leden, moet deze handmatig worden toegepast op teambeheerders en kanaalbeheerders als dit vereist is.

Alleen kanalen lezen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Configureer een kanaal zodat leden kunnen post/reply/reageren maar de gasten kunnen alleen lezen en reactiont * *

1. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Kanalen * *.
2. Selecteer ** Bewerken ** naast de naam van het kanaal dat u wilt configureren.
3. In het venster ** Maken Posts * * wordt de selectie van ** Guests** ongedaan gemaakt.
4. In het venster ** Post Reacties * *, controleert u indien nodig de selectie van ** Guests**.
5. Kies ** Save**.

Het kanaal is beschikbaar voor alle leden en gasten om toegang te krijgen, maar de gasten kunnen alleen berichten lezen en erop reageren.

** Maak een mededelingenkanaal waar alleen kanaalbeheerders kunnen post. * *

1. Maak een nieuw kanaal (Public of Private).
2. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Kanalen * *.
3. Selecteer ** Bewerken ** naast de naam van het chann
El je gewoon gemaakt (je kan nodig hebben om te zoeken naar het).
4. In het venster ** Aanmaakacties maken * *, controleert u de selectie van de optie ** Guests** en ** Members**.
5. In het venster ** Post Reactions * *, controleert u de selectie van de optie ** Guests** en ** Members**.
6. Kies ** Save**.

Het kanaal is beschikbaar voor alle leden en gasten om toegang te krijgen, maar alleen admins kunnen posten.

Post Management
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Beperken wie berichten kan verwijderen * *

Voorbeeld: Als standaardwaarde voor het gehele systeem, kunt u het wissen van posts beperken tot alleen teambeheerders en systeembeheerders.

1. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Machtigingen * * (of ** Systeemconsole > Geavanceerde machtigingen * * in versies ouder dan 5.12).
2. Selecteer ** Schema bewerken * *.
3. In de vensters ** Alle leden * * en ** Kanaal Admininistrators * * in de sectie * * Posts wissen * *, ontvinken u de vakjes voor * * Eigen Posts wissen * * en * * Anderen wissen * *.
4. In de vensters van ** Channel Administrators * * en ** Team Administrators * *, in het gedeelte * * Delete Posts * *, selecteert u de vakjes voor * * Delete Eigen Posts * * and * * Delete Anderen ' Posts * *.

** Beperken wie posts kan bewerken * *

Voorbeeld: Als de standaardwaarde voor het gehele systeem, alleen gebruikers toestaan om hun eigen berichten te bewerken voor vijf minuten na het plaatsen.

1. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Machtigingen * * (of ** Systeemconsole > Geavanceerde machtigingen * * in versies ouder dan 5.12).
2. Selecteer ** Schema bewerken * *.
3. In het venster ** Alle leden * *, ** Channel Administrators * * en ** Team Administrators * *, in de sectie ** Posts beheren * *, selecteert u het vakje ** Bewerken Posts * *.
4. Selecteer in elk venster de knop voor de versnelling om de globale tijdslimiet in te stellen op ` ` 300 ` ` seconden. .. Opmerking:

  De tijdslimiet voor het bewerken van de post is een ` globale configuratievariabele <https: //docs.mattermost.com/administration/config-settings.html#post-edit-time-limit> ` __ ` ` PostEditTimeLimit ` ` `, dus het instellen van een tijdslimiet na bewerken is van toepassing op alle teams en rollen.

Integratiebeheer
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Beperken van het beheer van webhooks en slash-opdrachten * *

Voorbeeld: Als de standaardwaarde voor het gehele systeem is het alleen mogelijk om systeembeheerders integraties te maken, te bewerken en te wissen.

1. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Machtigingen * * (of ** Systeemconsole > Geavanceerde machtigingen * * in versies ouder dan 5.12).
2. Selecteer ** Schema bewerken * *.
3. In de vensters ** Alle leden * * en ** Teambeheerders * *, in de sectie ** Integraties en aanpassingen * *, ontvink u de vakjes voor ** Inkomende webhaken beheren * *, ** Beheren van uitgaande webhaken * * en ** Beheren van schuine streep beheren * *. .. Opmerking:

  Machtigingen voor het maken, bewerken en wissen van integraties zijn momenteel gegroepeerd voor elk integratietype. Deze worden in een toekomstige release opgesplitst in afzonderlijke machtigingen.

Beheertools
--------------------

Er zijn een aantal CLI-tools beschikbaar voor beheerders om te helpen bij het configureren en oplossen van het machtigingssysteem:

1. ` Reset naar standaardmachtigingen <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-permissions-reset> ` __: Alle machtigingen voor de standaard op nieuwe installaties opnieuw instellen.
2. ` Export machtigingsschema's <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-permissions-export> ` __: Hiermee exporteert u de System Scheme en alle Team Override-schema's naar een jsonl-bestand.
3. ` Import machtigingsschema's <https: //docs.mattermost.com/administration/command-line-tools.html#mattermost-permissions-import> ` __: Importeert de System Scheme en alle Team Override-schema's aan uw Mattermeeste-instance van een jsonl-invoerbestand in de indeling die wordt uitgevoerd door ` ` mattermeeste machtigingen exporteren ` `.

Backend-infrastructuur
----------------------

Technische beheerders of ontwikkelaars die op zoek zijn naar een beter begrip van de permissies backend kunnen verwijzen naar onze :doc: ` permissions-backend ` technische documentatie.

-** Permission:** De mogelijkheid om bepaalde acties uit te voeren. Er worden machtigingen verleend aan rollen.
-** Roles:** Een set van machtigingen. Gebruikers of groepen worden toegewezen aan rollen.
-** Group:** Een groep gebruikers, meestal gesynchroniseerd vanuit AD/LDAP. Groepen worden toegewezen aan rollen in de context van teams, kanalen of systeembreed.
-* * Standaardrollen: ** Alle leden, Gasten (indien ingeschakeld), Channel Admins, Team Admins, System Admins.
-** Systeemschema: ** Een set standaardrollen die systeembreed toepassen.
-** Team Override schema: ** Een set standaardrollen die alleen van toepassing zijn in het opgegeven team. Machtigingen voor rollen in een teamschema vervangen rollen in het systeemschema.
-** System-wide:** geldt voor het gehele systeem, inclusief alle teams waarvan de gebruiker lid is.
-** Team-wide:** Geldt alleen in een specifiek team.
