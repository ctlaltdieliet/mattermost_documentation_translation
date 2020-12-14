Teamleden en kanaalleden beheren (E20)
== == == == == == == == == == == == == == == == == == == =

Systeembeheerders kunnen de kanaalconfiguratie in de systeemconsole beheren.

-** Management:** Beheer van synchronisatie, moderatie en lidmaatschapsinstellingen.
-** Promoveren/degraderen Team en Channel Admins: ** Team en Channel Admins kunnen worden gedegradeerd via de systeemconsole.
-** View kanaalleden: ** System Admins kunnen leden van een kanaal bekijken zonder dat ze lid hoeven te worden van het kanaal.
-** Aantal leden: ** Totaal aantal leden in een team of kanaal.
-** Archive channels: ** System Admins kunnen kanalen archiveren zonder dat ze lid hoeven te worden van het kanaal.

Teams
------

Voor het bekijken en beheren van teamgegevens gaat u naar ** System Console > Teams * *. Teams kunnen worden beheerd door ** Group Sync * * of ** Invite Only * *. Het type beheer dat wordt gebruikt, kan van invloed zijn op de beheeropties die voor dat team beschikbaar zijn.

Selecteer een team om de configuratieopties te bekijken.

Teamprofiel
~ ~ ~ ~ nopen ~ ~

De naam en beschrijving van het team.

Teambeheer ~ ~ ~ ~ ~ ~ ~ ~ ~ geven

-Als ** Sync Group Members * * is ingeschakeld, is de lijst ** Synced Groups * * zichtbaar en kunnen er extra groepen worden toegevoegd.
-Als ** Sync-groepsleden * * niet is ingeschakeld, kunnen er geen uitnogbeperkingen worden geselecteerd.

Groepen
~ ~ ~ geven

U kunt groepen toevoegen en verwijderen en groepsleden promoot of degraderen tot teambeheerders/Member-rollen.

Leden
~ ~ ~ ~ nten

Een lijst van alle leden in een kanaal is zichtbaar voor systeembeheerders. Leden kunnen worden toegevoegd en verwijderd uit de teamleden en worden gepromoveerd of gedegradeerd naar een teambeheer/lidrol. Gebruik de rol ** Filter** om uw zoekresultaten te verfijnen. U kunt een filter gebruiken of filters combineren om te zoeken op meerdere rollen:

-Gast
-Lid
-Teambeheer
-Systeembeheer

Kanalen
---------

Voor het bekijken en beheren van kanaalgegevens gaat u naar ** System Console > Channels * *. Kanalen kunnen worden beheerd door ** Group Sync * * of ** Handmatig uitnodigt * *. Het type beheer dat wordt gebruikt, kan van invloed zijn op de beheeropties die voor dat kanaal beschikbaar zijn. Gebruik de ** Filter** om uw zoekresultaten te verfijnen. U kunt een filter gebruiken of filters combineren om te zoeken op kanaal en type beheer:

-Openbare kanalen
-Eigen kanalen
-Gearchiveerde kanalen
-Kanalen die zijn gesynchroniseerd met een AD/LDAP-groep
-Kanalen met gebruikers die handmatig zijn uitgenodigd (niet gesynchroniseerd met LDAP)

Selecteer een kanaal om de configuratieopties te bekijken.

Profiel
~ ~ ~ geven

De naam en beschrijving van het kanaal. Om het kanaal te archiveren, selecteert u ** Archive Channel > Save * *. Het kanaal is nog steeds doorzoekbaar in de lijst ** Channels**. Als u het kanaal wilt uitpakken, selecteert u ** Unarchive Channel * * and ** Save**.

Kanaalbeheer ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ n~ ~ g

-Als ** Sync Group Members * * is ingeschakeld, is de lijst ** Synced Groups * * zichtbaar en kunnen er extra groepen worden toegevoegd.
-Als ** Sync-groepsleden * * niet is ingeschakeld, kunt u opgeven of het kanaal ** Private** of ** Public** is.

Kanaalmoderatie (E20)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Ng~

*Beschikbaar in Enterprise Edition E20 .*

Vanaf v5.22 staan de moderatie-instellingen van het kanaal de beheerders toe om acties binnen bepaalde kanalen te beperken. Deze
acties omvatten:

-** Make-kanaal read-only:** De mogelijkheid voor Admins om posten in opgegeven kanalen uit te schakelen.
-** Beperken reacties: ** Schakel de mogelijkheid voor leden en gasten uit om reacties te posten.
-** Restrict kanaal vermeldt: ** Schakel de mogelijkheid uit voor gebruikers om kanaalbrede vermeldingen te posten (@all/channel/hier) in opgegeven kanalen.
-** Channel member management: ** Alleen Admins hebben de mogelijkheid om kanaalleden in de opgegeven kanalen toe te voegen en te verwijderen.

Deze instellingen worden gewijzigd in ** Systeemconsole > Gebruikersbeheer > Kanalen * *. .. opmerking: Deze instellingen zijn alleen van toepassing op gasten en leden. Systeem-, team-en kanaalbeheerders worden niet beïnvloed. Als u het plaatsen van mogelijkheden aan een bepaald lid wilt verlenen, moet u dit lid eerst promovenen naar Channel Admin.

De beschikbaarheid van moderatie-instellingen voor kanalen kan ook worden beïnvloed door bestaande configuraties van systeem-en teammachtigingen. Als er bestaande configuraties zijn die de kanaalinstellingen overschrijven die u wilt toepassen, wordt deze aangegeven in de gebruikersinterface. Deze instellingen kunnen vervolgens worden aangepast in het desbetreffende venster in de sectie ** Permissions** van de systeemconsole.

** Configureer een kanaal zodat leden kunnen post/reply/reageren maar de gasten kunnen alleen lezen en reactiont * *

1. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Kanalen * *.
2. Selecteer ** Bewerken ** naast de naam van het kanaal dat u wilt configureren.
3. In het venster ** Maken Posts * * wordt de selectie van ** Guests** ongedaan gemaakt.
4. In het venster ** Post Reacties * *, controleert u indien nodig de selectie van ** Guests**.
5. Kies ** Save**.

Het kanaal is beschikbaar voor alle leden en gasten om toegang te krijgen, maar de gasten kunnen alleen berichten lezen en erop reageren.

** Maak een mededelingenkanaal waar alleen Kanaalbeheerders kunnen posten (alleen-lezen). * *

1. Maak een nieuw kanaal (Public of Private).
2. Navigeer naar ** Systeemconsole > Gebruikersbeheer > Kanalen * *.
3. Selecteer ** Bewerken ** naast de naam van het kanaal dat u zojuist hebt gemaakt (mogelijk moet u er naar zoeken).
4. In het venster ** Aanmaakacties maken * *, controleert u de selectie van de optie ** Guests** en ** Members**.
5. In het venster ** Post Reactions * *, controleert u de selectie van de optie ** Guests** en ** Members**.
6. Kies ** Save**.

Het kanaal is beschikbaar voor alle leden en gasten om toegang te krijgen, maar alleen Admins kunnen posten.

Groepen
~ ~ ~ geven

U kunt groepen toevoegen en verwijderen en groepsleden promoot of degraderen tot teambeheerders/Member-rollen.

Leden
~ ~ ~ geven

Een lijst van alle leden in een kanaal is zichtbaar voor systeembeheerders. Leden kunnen worden toegevoegd en verwijderd uit de teamleden en worden gepromoveerd of gedegradeerd naar een teambeheer/lidrol. Gebruik de rol ** Filter** om uw zoekresultaten te verfijnen. U kunt een filter gebruiken of filters combineren om te zoeken op meerdere rollen:

-Gast
-Lid
-Kanaalbeheerder
-Systeembeheer
