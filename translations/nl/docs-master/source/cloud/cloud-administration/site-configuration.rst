Vestigingsconfiguratie
== == == == == == == == ==

Banner voor mededeling
-------------------

Er is een annoncering beschikbaar waarmee System Admins een bericht kunnen afbeelden dat zichtbaar is voor alle gebruikers op het systeem. .. afbeelding:: ../ ../images/omroepcement-banner-1106x272.png
  :breedte: 1106
  :hoogte: 272
  :alt: Hiermee wordt de annoncering van de annoncering afgebeeld boven aan het scherm van de gebruiker.

Standaard kunnen gebruikers de banner verwijderen totdat ze zich opnieuw aanmelden of totdat u de banner bijwerkt. U kunt de banner bijwerken door de tekst van de banner te wijzigen of door de banner opnieuw in te schakelen nadat deze is uitgeschakeld. U kunt ook de kleur van de tekst en de achtergrondkleur bepalen. Met een instelling in de systeemconsole kunt u voorkomen dat gebruikers de banner niet kunnen missen.

** Om de banner in te schakelen * *:

1. Open ** Systeemconsole > Siteconfiguratie * *.
2. Voor ** Aankondiging Banner inschakelen * *, selecteert u ** true**.
3. Voer in het veld ** Banner-tekst * * de tekst in van de mededeling die u wilt maken.
4. Stel de achtergrond en tekstkleuren in.
5. Om te voorkomen dat gebruikers de banner niet missen, selecteert u in de sectie ** Afwijzing van banner toestaan * * door ** false** te selecteren.
6. Kies ** Save**.

In-Productberichten
------------------

Mattermeest in-product kennisgevingen houden gebruikers en beheerders op de hoogte van de nieuwste product verbeteringen, functies en releases. .. afbeelding:: ../ ../images/notices.png

Mededelingen van de beheerder ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Beheerdersberichten worden gebruikt om systeembeheerders op de hoogte te stellen wanneer er een nieuwe serverversie beschikbaar is, of als een serverupgrade wordt aanbevolen als gevolg van het beëindigen van de levenscyclus van ondersteuning. Systeembeheerders kunnen ook berichten ontvangen over de aanbevolen opties voor serverconfiguratie om de gebruikerservaring van hun implementatie te optimaliseren.

Beheerdersberichten kunnen worden uitgeschakeld in de pagina ** System Console > Notices * *.

Berichten van eindgebruiker berichten ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Eindgebruikersberichten worden gebruikt om gebruikers en beheerders van nieuwe functies te informeren en wanneer er nieuwe desktopversies beschikbaar zijn. Ze kunnen worden uitgeschakeld in ** System Console > Kennisgevingen * *.

FAQ's ^ ^ ^ ^

Zijn kennisgevingen standaard ingeschakeld?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Vragen

Kennisgevingen worden standaard ingeschakeld voor alle Mattermeeste gebruikers. Systeembeheerders kunnen ervoor kiezen om de berichten van beheerders of eindgebruikers in ** Systeemconsole > Kennisgevingen * * uit te schakelen.

Krijg ik nog steeds berichten als mijn server luchtvrij is?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Nee, de Mattermeeste server vereist een verbinding met het internet om berichten te ontvangen.

Hoe vaak krijgen gebruikers een bericht?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Kennisgevingen worden gebruikt om het bewustzijn van nieuwe functies te verhogen als onderdeel van onze maandelijkse release cadence. Gebruikers ontvangen alleen kennisgevingen die specifiek op hen van toepassing zijn. Als een gebruiker bijvoorbeeld al de meest recente versie van de Desktop App uitvoert, ontvangen ze geen upgradebericht.

Emoji
-----

Er zijn drie verschillende instellingen waarmee u emoji kunt besturen.

1. ** Schakel Emoji Picker: ** Een emoji picker die gebruikers in staat stelt om emojis te selecteren als reactie of gebruik in berichten. De emoji picker met een groot aantal inschakelen
van Custom Emojis kan de prestaties vertragen.
2. ** Schakel Aangepaste Emoji: ** U kunt bepalen of de Custom Emoji optie in het hoofdmenu, waar gebruikers kunnen gaan om aangepaste emoji te maken, is toegankelijk.
3. ** beperken custom emoji Maken: ** U kunt instellen welke rol is in staat om Custom Emoji te maken van ** Hoofdmenu > Custom Emoji * * (alle gebruikers, Systeem-en Team-beheerders, of Systeembeheerders).

Bestanden delen en downloaden
--------------------------

Er zijn drie verschillende instellingen waarmee u het delen van bestanden en het downloaden van bestanden in uw werkgebied en op mobiele apparaten kunt beheren.

1. ** Gemeenschappelijk gebruik van bestanden toestaan: ** Als de configuratie is ingesteld op ** false**, is het delen van bestanden uitgeschakeld. Alle bestands-en afbeeldingsuploads op berichten zijn niet toegestaan voor alle clients en apparaten, inclusief mobiel.
2. ** Uploaden van bestanden toestaan op mobiel: ** Als de configuratie is ingesteld op ** false**, wordt het uploaden van bestanden op mobiele apps uitgeschakeld. Alle bestands-en afbeeldingsuploads op berichten zijn niet toegestaan voor alle clients en apparaten, inclusief mobiel.
3. ** Downloads van bestanden toestaan op mobiel: ** Als de configuratie is ingesteld op ** false**, schakelt u bestandsdownloads uit op mobiele apps. Gebruikers kunnen nog steeds bestanden downloaden van een mobiele webbrowser.

Lokalisatie
------------

Matterbest kan worden gelokaliseerd in 16 talen. U kunt de standaardtaal instellen voor nieuwe gebruikers en pagina's waar de gebruiker zich niet heeft aangemeld en welke talen beschikbaar zijn voor gebruikers in ** Accountinstellingen > Afbeelden > Talen * *. 

Nieuwe talen worden automatisch toegevoegd standaard. U kunt nieuwe talen toevoegen met behulp van de dropdown menu handmatig als ze beschikbaar. Als u handmatig nieuwe talen toevoegt, moet u de standaardtaal van de client toevoegen voordat u de instelling opslaat.

Kennisgevingen
-------------

Er zijn zeven verschillende instellingen waarmee u meldingen kunt instellen.

1. ** Toon @channel en @all -bevestigingsvenster: ** Gebruikers worden gevraagd om te bevestigen wanneer @channel en @all worden gepost in kanalen met meer dan vijf leden.
2. ** Inhoud van e-mailmeldingen: ** U kunt de inhoud van de e-mailmeldingen opgeven.-** Stuur volledige berichtinhoud * * bevat de naam van de afzender en het kanaal in e-mailberichten.-** Stuur een generieke beschrijving met alleen de naam van de afzender * * bevat de naam van het team en de naam van de persoon die het bericht heeft verzonden. Geen informatie over kanaalnaam of berichtinhoud, is opgenomen in e-mailmeldingen. Dit wordt meestal gebruikt om nalevingsredenen als Mattermeeste vertrouwelijke informatie bevat en het beleid dicteert dat het niet in e-mail kan worden opgeslagen.
3. ** Bericht weergavenaam: ** Stel de naam in die wordt weergegeven op het e-mailaccount dat wordt gebruikt bij het verzenden van e-mailberichten van Mattermeeste-systeem.
4. ** Bericht van adres: ** Stel het adres in op het e-mailaccount dat wordt gebruikt bij het verzenden van e-mailberichten van binnen Matterbest. Zodat u geen berichten mist, zorg er dan voor dat u deze waarde wijzigt in een e-mail die uw systeembeheerder ontvangt, bijvoorbeeld "admin@yourcompany.com".
5. ** Bericht antwoordadres: ** Stel het e-mailadres in dat wordt gebruikt in de header Reply-To, bij het verzenden van e-mailberichten van Matterbest.
6. ** Postadres voor notificatie: ** Stel de naam en het postadres in dat wordt afgebeeld in de voettekst van e-mailmeldingen van Matterbest, zoals *ABC Corporation, 565 Knight Way, Palo Alto, California, 94305, USA*. Als het veld leeg wordt gelaten, worden de organisatienaam en het postadres niet afgebeeld.
7. ** Inhoud van push-berichten: ** U kunt configureren welke informatie wordt verstrekt in push-berichten.-** Algemene beschrijving met alleen de naam van de afzender * * bevat alleen de naam van de persoon die het bericht heeft verzonden, maar geen informatie over kanaalnaam of berichttekst.-** Algemene beschrijving met afzender en kanaalnamen * * bevat namen van gebruikers en kanalen, maar geen specifieke gegevens uit de tekst van het bericht.-** Volledige berichtinhoud verzonden in de melding payload * * verzendt fragmenten uit berichten die aanleiding geven tot meldingen met details en kunnen vertrouwelijke informatie bevatten die in berichten wordt verzonden.- ** Alleen push-berichten * * betekent dat volledige inhoud van het bericht wordt opgehaald van de server na ontvangst. De payload van de melding die is doorgegeven via de Apple Push Notification-service of de Firebase Cloud Messaging-service bevat geen berichtinhoud. In plaats daarvan bevat het een uniek bericht-ID dat wordt gebruikt om berichtinhoud op te halen van de server wanneer een push-bericht wordt ontvangen door een apparaat via een app-extentie van een meldingsservice op iOS of een uitbreidbaar meldingspatroon op Android. Als de server niet kan worden bereikt, wordt er een generiek push-bericht afgebeeld zonder de berichtinhoud of de naam van de afzender. Voor klanten die ervoor kiezen om de Mattermeeste mobiele toepassing in een beveiligde container te laten teruglopen, zoals BlackBerry Dymanics, MobileIron, AirWatch of andere oplossingen, moet de container de inhoud van het bericht ophalen uit het unieke bericht-ID wanneer u push-berichten ontvangt. Als de container niet in staat is de fetch uit te voeren, kan de inhoud van de push-berichten niet worden ontvangen door de mobiele toepassing van de klant zonder de inhoud van het bericht door te geven via de service Apple Push Notification of de Firebase Cloud Messaging-service.

Posten
-----

Er zijn vijf verschillende instellingen waarmee u content in posts kunt beheren.

1. ** Link Previews inschakelen: ** Link previews zijn voorbeelden van gekoppelde website-content, afbeeldingslinks en YouTube-video's die worden afgebeeld onder posts als deze beschikbaar zijn. Gebruikers kunnen previews van de website voor zichzelf in-of uitschakelen via ** Accountinstellingen > Afbeelden > Website Link Previews * *. U kunt ook uitschakelen van alle website link previews, beeld link previews, en YouTube-previews door het veranderen van deze instelling op false.
2. ** Enable SVGs:** Bepaalt of gebruikers de mogelijkheid hebben om previews van SVG-bestandsbijlagen en SVG-beeldlinks te bekijken.
3. ** enable LaTeX rendering: ** Controls users ' ability to render LaTeX code.
4. ** Aangepaste URL-schema's: ** Een lijst van URL-schema's die worden gebruikt voor het automatisch koppelen van berichttekst. HTTP, HTTPS, FTP, tel en mailto maken altijd links.
5. ** Google API-sleutel: ** Matterbest biedt de mogelijkheid om YouTu in te bedden
zijn video's van URL's die worden gedeeld door eindgebruikers. Stel deze sleutel in en voeg YouTube Data API v3 toe als een service aan uw sleutel om de weergave van titels voor ingebedde YouTube-videovoorbeelden mogelijk te maken. Zonder de sleutel zullen YouTube-previews nog steeds worden gemaakt op basis van hyperlinks die in berichten of reacties verschijnen, maar ze zullen de video-titel niet tonen. Als Google detecteert dat het aantal weergaven uiterst hoog is, kunnen ze de toegang tot inbedden insluiten. Mocht dit gebeuren, dan kunt u de gasklep verwijderen door zich te registreren voor een Google Developer Key en deze in te voeren op dit veld volgens deze instructies: https://www.youtube.com/watch?v=Im69kzhpR3I. Uw Google Developer Key wordt gebruikt in JavaScript op de client. Met behulp van een Google API-sleutel kan Matterbest detecteren wanneer een video niet meer beschikbaar is en de post weergeven met een Video niet gevonden label.

Openbare koppelingen
------------

Als u Public File Links in staat stelt, kunnen gebruikers openbare links genereren naar bestanden en afbeeldingen voor het delen buiten het meest overeenkomende systeem met een openbare URL.

Als deze optie is uitgeschakeld, wordt de optie Openbare koppeling ophalen verborgen in de gebruikersinterface van de afbeeldingspreview. Iedereen die een eerder gegenereerde openbare link probeert te bezoeken, ontvangt een foutbericht waarin wordt gezegd dat de openbare links zijn uitgeschakeld. Wanneer teruggeschakeld wordt naar True, werken oude openbare links opnieuw, tenzij het Public Link-zout opnieuw is gegenereerd.

Gebruikers en teams
---------------

Er zijn zeven verschillende instellingen waarmee u gebruikers en teams kunt beheren.

1. ** Max Gebruikers Per Team: ** Het Max Gebruikers Per Team verwijst naar de grootte van de * teamsite *, dat is een werkruimte een * team van mensen * ingewoontes. Een team van mensen wordt beschouwd als een kleine organisatie waar mensen nauw samenwerken in de richting van een specifiek gemeenschappelijk doel en dezelfde etiquette delen. In de fysieke wereld, een team van mensen kan meestal zitten rond een tafel om een maaltijd te hebben en hun project te bespreken. De standaard maximum van 50 mensen, is aan het uiterste einde van een enkel team van mensen. Op dit punt zijn organisaties vaker 'meerdere teams van mensen' en investeringen in het expliciet definiëren van etiquette, zoals channel organisatie of het draaien van beleidsfuncties in Enterprise Edition, worden vaak gebruikt om de hoge niveaus van de productiviteit te schalen in een team van mensen die Matterbest gebruiken om meerdere teams van mensen.
2. ** Max Kanalen Per Team: ** Stel het maximum aantal kanalen per team in, inclusief zowel actieve als verwijderde kanalen.
3. ** Schakel gebruikers in om Direct Message-kanalen te openen met: ** U kunt configureren of gebruikers een gebruiker kunnen berichten op het meeste werkgebied of alleen gebruikers in het team dat zij lid zijn van de teams waarvan de gebruiker lid is. Deze instelling past de gebruikers terug in het menu Directe berichten Meer en CTRL/CMD + K kanaal switcher toont alleen gebruikers van het huidige team. Deze instelling is alleen van invloed op de UI, niet op machtigingen op de server. Een Direct Message-kanaal kan bijvoorbeeld met iedereen op de server worden gemaakt, ongeacht deze instelling.
4. ** Teammat-naamweergave: ** Geeft aan hoe namen standaard worden afgebeeld in de gebruikersinterface. Let op: gebruikers kunnen deze instelling overschrijven in ** Account Settings > Display > Teammate Name Display * *.-** Toon gebruikersnaam * * toont de gebruikersnaam van de gebruiker.-** Toon roepnaam * * als er een bestaat geeft de bijnaam van de gebruiker weer. Als de gebruiker geen roepnaam heeft, wordt de volledige naam afgebeeld. Als de gebruiker geen volledige naam heeft, wordt de gebruikersnaam weergegeven.-** Show first and achternaam * * geeft de volledige naam van de gebruiker weer. Als de gebruiker geen volledige naam heeft, wordt de gebruikersnaam afgebeeld. Aanbevolen bij gebruik van SAML of LDAP als de kenmerken voor de voornaam en achternaam zijn geconfigureerd.
5. ** Gebruikers toestaan om gearchiveerde kanalen (Beta) te bekijken: ** Hiermee kunnen gebruikers content bekijken, delen en zoeken naar content van kanalen die zijn gearchiveerd. Gebruikers kunnen alleen de content bekijken in kanalen waarvan ze lid waren voordat het kanaal werd gearchiveerd.
6. ** Email Address afbeelden: ** Wanneer ingesteld op ** false** verbergt deze instelling het e-mailadres van gebruikers van andere gebruikers in de gebruikersinterface, inclusief Team Admins. Dit is ontworpen voor het beheren van teams waar gebruikers hun contactgegevens privé houden. Systeembeheerders kunnen nog steeds e-mailadressen in de gebruikersinterface zien.
7. ** Toon volledige naam: ** WHen ingesteld op false, deze instelling verbergt de volledige naam van gebruikers van andere gebruikers, waaronder Team Admins. Dit is ontworpen voor het beheren van teams waar gebruikers hun contactgegevens privé houden. Systeembeheerders kunnen nog steeds volledige namen in de gebruikersinterface zien.
