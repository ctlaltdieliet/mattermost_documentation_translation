== == == == == == == == == == == == = Mobile App-implementatiehandleiding
== == == == == == == == == == == == == =

################
Over deze handleiding ##################

********
Publiek
********

Leiders, Beheerders en/of Champions verantwoordelijk voor het in gebruik nemen van Matterbest mobiele apps in hun organisatie.

    ** Note:** Enkele in deze handleiding beschreven functies zijn alleen beschikbaar in Enterprise Edition E10 en/of E20.

*******************
Leerdoelen *******************

Deze handleiding bevat basisgegevens die nodig zijn bij de ontwikkeling van een plan voor een proof of concept en/of bedrijfsmobiele implementatie. 

Aan het einde van deze gids zult u inzicht hebben in de eisen op hoog niveau voor een succesvolle Mattermeest mobiele implementatie. 

Dit omvat:

-Kiezen hoe de Mattermeeste mobiele applicaties te verkrijgen en te verspreiden
-Het bepalen van het ideale mobiele implementatiemodel voor uw organisatie
-Het begrijpen van de resourcevereisten bij de keuze voor het bouwen van uw eigen Mattermeest mobiele apps

Technische implementatie gidsen zijn opgenomen als links om de informatie in deze gids beknopt te houden. .. _Ondersteuning:

*******
Ondersteuning
*******

Als u op elk punt extra hulp nodig hebt, kunt u de onderstaande methoden gebruiken.

** Gemeenschap **
    Ons hele team is actief binnen de ` public instance van Mattermeest <https://community.mattermost.com> ` _, plus u krijgt de steun van een van de beste open source communities rond.
** Documentatie**
    Wij koppelen aan een heleboel ` mobiele-specifieke documentatie <https://docs.mattermost.com/mobile/mobile-overview.html> ` _ in deze gids, maar wij moedigen u aan om ` al onze documentatie te controleren <https://docs.mattermost.com/> ` _.
** Forums**
    Voor meer informatie over het oplossen van problemen, ` open een nieuw onderwerp in onze forums <https://forum.mattermost.org/c/trouble-shoot> ` _ met stappen om uw probleem te reproduceren.
** GitHub**
    Bezoek ons op ` GitHub <https://github.com/mattermost/> ` _ om problemen te creëren in een van onze repositories.
** Enterprise Support * *
    Als u een abonnee van Enterprise Edition bent, kunt u een ondersteuningsticket openen in de " Enterprise Edition Support-portal <https://support.mattermost.com> ` _.

----

################################
Voordat u begint met de implementatie ##################################

Een succesvolle mobiele implementatie is een belangrijk onderdeel van uw ervaring met Matterbest.

Onze hoogste prioriteit is ervoor te zorgen dat je hebt wat je nodig hebt om succesvol te zijn, maar houd in gedachten dat elke verandering, zelfs gunstig, zal een impact hebben op uw gebruikers. Om uw succes te garanderen moet u de doelen voor uw mobiele implementatie identificeren.

U kunt bijvoorbeeld duizenden gebruikers in de hele wereld in gebruik nemen in minuten met de openbare Mattermeeste mobiele apps op Google Play en Apple App Store.

Natuurlijk zullen grote bedrijfsimplementaties meer tijd kosten, en de algemene doelstellingen voor uw implementatie zullen afhangen van vele factoren. We raden u aan een moment te nemen om te noteren hoe een succesvolle implementatie eruit ziet. Om te beginnen, vraag jezelf en je team wat je wilt bereiken, wat zijn uw wensen
Resultaten?

Dit kost een kleine hoeveelheid tijd vooraf. Maar, we hebben gezien het verschil dat dit maakt in succesvolle projecten.

Hieronder hebben we enkele belangrijke vragen toegevoegd om uzelf, uw team en alle andere belanghebbenden te vragen.

-Waarom hebben we besloten de Mattermeeste mobiele applicatie in te zetten?
-Wie zal, of moet, een belangrijke/kritische rol spelen in dit project?
Wie doet dit project?
Hoeveel tijd hebben we voor deze inzet?
-Moet, of zou, een eerste inzet een eenvoudiger pad?
-Kunnen we onze inzet spreiden, te beginnen met simpele eisen?
-Ga je een pilotomgeving uitvoeren, als dat zo is, met wie?
-Welke IT-of HR-beleid moet veranderen?

Wij raden aan ten minste één haalbaar en op tijd gebaseerd resultaat te bepalen.

Tegelijkertijd moet u beginnen na te denken over technische en veiligheidsvereisten. Een geweldige plek om te beginnen is met een implementatieplan. Dus, voel je vrij om ` gebruik van onze sjabloon beschikbaar <https://docs.mattermost.com/getting-started/implementation_plan.html> ` _ in de Mattermeeste documentatie. Begin ook met uw technische en beveiligingsteams met vragen zoals hieronder.

-Zijn er bekende beveiligings-of toegangsvereisten?
-Is een VPN-verbinding vereist?
-gebruiken we een EMM-provider (Enterprise Mobile Management)?

Nogmaals, dit betekent pauzeer voordat u springt in uw Mattermeest mobiele implementatie. Maar het zal het verschil maken in het verzekeren van een rendement op uw investering.

----

#################################
Matterbest mobile deployment primer ###############################

Hoewel Matterbest biedt opties om mobiele implementatie zo eenvoudig mogelijk te maken, zal het tijd en iteratie nemen.

Deze primer dient als een introductie tot Mattermeest mobiele technologieën. Het is een aanvulling op onze technische documentatie en richt zich op drie hoofdgebieden:

-Technische vereisten
-Basiskenmerken en technologieën
-Problemen oplossen

Ongeacht uw expertise, adviseren wij het lezen van deze sectie voordat u begint met uw implementatie. En houd in gedachten, wij zijn hier om u te steunen.

**********************
Technische vereisten **********************

` Ondersteunde Mattermeeste Server Versies <https://github.com/mattermost/mattermost-mobile/blob/master/CHANGELOG.md> ` _ Minimumvereisten voor de Mattermeeste Server worden bijgehouden in onze documentatie (link hierboven). ** Echter, we raden aan de nieuwste versie * * van de Mattermeeste Server te draaien omdat het de meest recente features en alle toepasselijke beveiligingsupdates bevat.

    Als dit niet mogelijk is, raden wij u aan om op de meest recente ` Extended Support Release versie <https://docs.mattermost.com/administration/extended-support-release.html> ` _ van de Mattermeeste Server te zijn. Deze release heeft een aantal essentiële updates die zorgen voor compatibiliteit op een aantal gebieden, waaronder de Matterbest Push Notification Service (MPNS).

` Ondersteunde Apparaten/Mobile Device Requirements <https: //docs.mattermost.com/install/requirements.html#mobile-apps> ` _
    De basisvereisten voor mobiele apparatuur zijn vermeld in de bovenstaande link.

***************************************************
Openbare app store vs. aangepaste Mattermeeste apps *******************************************

    ** Note:** Deze gids gebruikt de term Public App Store als generiek voor de twee meest gebruikte toepassingswinkels: Apple App Store en Google Play Store.

De meest kritische beslissing die u in uw mobiele implementatie maakt, is of de apps die Matterbest geleverd wordt via Google Play en Apple App Store moeten worden gebruikt, of om aangepaste versies van de Mattermeeste apps te bouwen en te distribueren. Hieronder geven wij een zeer algemeen overzicht van deze opties.

Openbare app-opslag
== == == == == == == ==

Met behulp van de app gedistribueerd door Matterbest in Google Play en de Apple App Store vermindert sterk de inzet tijd en is onze aanbevolen aanpak. Belangrijke voordelen zijn:

-Gemakkelijker implementatie, gedreven door de behoeften van de gebruiker.
-Mogelijkheid om de Hosted Push Notification Service of HPNS te gebruiken.
-Apps automatisch bijgewerkt met de nieuwste functies, verbeteringen en security updates.

Aangepaste Mattermeeste apps
== == == == == == == == == == ==

Als u wilt om de toepassingen aan te passen, of niet wilt dat uw gebruikers het downloaden van de toepassing van de openbare app stores, moet u de apps zelf te bouwen. 

Omdat de apps een open source project zijn, zal het aanpassen van een vork, en uw team zal verantwoordelijk zijn voor het onderhoud van de vork, evenals het houden van de vork up-to-date met eventuele wijzigingen gemaakt door Matterbest.

Dit proces kan gecompliceerd zijn. Het zal ook sterk verhogen implementatietijd, niet alleen in eerste zin, maar wanneer de apps moeten worden bijgewerkt. 

Wij raden u aan om uw ontwikkelteam een kijkje te nemen in de documentatie om ervoor te zorgen dat ze de schaal en de vereisten van dit pad begrijpen. In het algemeen zal deze route een aantal uitdagingen, waaronder:

-Verkrijgen/verstrekken van certificaten voor uw aangepaste Mattermeeste toepassing
-Uw aangepaste Mattermeeste-toepassingen ondertekenen
-Distributie van uw applicaties via openbare of particuliere app stores

***************************************************
Matterendste Push Notification Service (MPNS) *******************************************

Het ontvangen van meldingen op een mobiel apparaat is een kernwaarde van elke mobiele implementatie.

Het vertegenwoordigt ook een rendement op uw inzet investering door middel van beter verbonden gebruikers. 

Een push-proxy is een sleuteltechnologie achter kennisoverdracht. Hiermee kunnen meldingen tussen de server en de mobiele toepassing worden ingeschakeld.

Mattermore biedt een zelfgehoste push-proxy die u kunt implementeren, de Matterbest Push Notification Service (MPNS). Dit is ook beschikbaar via een gehoste-by-Mattermeest optie, of Hosted Push Notification Service (HPNS).

    ** Note:** ` Alleen Matterste Enterprise Edition E10 <https://mattermost.com/pricing-self-managed/> ` _ of hoger kan worden gebruikt om toegang te krijgen tot onze Hosted Push Notification Service (HPNS)

Als u de Mattermeeste toepassingen gebruikt via Google Play en Apple App Store, is de HPNS alles wat u nodig hebt.

Onze Gehoste Push Notification Service biedt:

-Toegang tot
een openbare Hosted Push Notification Service (HPNS).
-Een expliciet ` privacybeleid <https://mattermost.com/data-processing-addendum/> ` _ voor de inhoud van niet-versleutelde berichten.
-versleutelde TLS-verbindingen:
    -Tussen HPNS en Apple Push Notification Services
    -HPNS en Google ' s Firebase Cloud Messaging-dienst
    -HPNS en uw Mattermeeste server
-Productie-level uptime verwachtingen
-Compatibiliteit met EMM-providers *

\ * *Bij gebruik van onze openbare app store applicaties en de AppConfig standard.*

Het hosten van uw eigen versie van de MPNS is een optie, maar vereist dat u de Matterbest app zelf te bouwen. De sectie ` Het kiezen van de juiste Mobile Deployment Model ' _ sectie van deze handleiding, evenals onze ` Mobile App Admin Documentatie <https://docs.mattermost.com/mobile/mobile-hpns.html> ` _ zijn de beste plaatsen om te beginnen.

****************************************************
Providers van Enterprise Mobile Management (EMM) *******************************************

EMM Providers ontwikkelen software die helpt enterprise teams te beheren veilige mobiele technologie-implementaties. Dit omvat het gebruik van mobiele apparaten en gebruiksklare toepassingen.

De meeste grote bedrijfsteams zijn bekend met ` Enterprise Mobile Management <https://en.wikipedia.org/wiki/Enterprise_mobility_management> ` _ providers of EMMs. Als dit een nieuwe term voor u is, bekijk ` Appendix B: EMM Provider List ` _ voor een lijst van aanbieders en relevante informatie.

Voor degenen die grotere implementaties nemen, nemen we aan dat u al een EMM-provider gebruikt.

AppConfig is nieuwere, meer moderne aanpak in vergelijking met de vorige standaard, app-verpakking.

AppConfig (ondersteund) vs. appconfiguratie (niet ondersteund)
== == == == == == == == == == == == == == == == == == == == == == == == == == == ==

    ** Note:** Matterbest ondersteunt alleen de AppConfig-standaard. Het biedt geen ondersteuning voor het inpakken van apps. Gebruik de app-verpakking op eigen risico.

Hier is ` een nuttig artikel <https://www.computerworld.com/article/3209907/app-wrapping-the-key-to-more-secure-mobile-app-management.html> ` _ het definiëren van AppConfig en app-verpakking. Laten we eerst naar AppConfig kijken.

AppConfig
---------

"Een gemeenschap gericht op het verstrekken van tools en beste praktijken rond native mogelijkheden in mobiele besturingssystemen om een meer consistente, open en eenvoudige manier om te configureren en beveiligde mobiele apps om mobiele adoptie in het bedrijfsleven te verhogen."-AppConfig.org

Dat klinkt geweldig, maar zijn er voordelen voor gebruikers?

Nogmaals, in de woorden van de AppConfig Community, " Gebruikers profiteren van onmiddellijke mobiele productiviteit en een naadloze out-of-the box-ervaring, en bedrijven profiteren van veilige werk-ready apps met een minimale setup vereist, terwijl het gebruik van bestaande investeringen in Enterprise Mobility Management (EMM), VPN, en identiteit oplossingen. Zet een andere manier, uw apps zijn eenvoudiger te configureren, veilig en te implementeren. "

Voor nu, focus op dat laatste deel, "... uw apps zijn eenvoudiger te configureren, veilig en te implementeren." AppConfig biedt het meest efficiënte en schaalbare pad voor succes. Als admin betekent dit een eenvoudiger implementatie en beheer van mobiele applicaties. En opnieuw, als het om Matterbest gaat, is het onze enige ondersteunde aanpak.

Toepassing (app)
-------------------------- Vanuit het artikel waarnaar we eerder verwijzen <https://www.computerworld.com/article/3209907/app-wrapping-the-key-to-more-secure-mobile-app-management.html> ` _, application (app) wrapping betreft "... het gebruik van een SDK van een EMM-leverancier die een ontwikkelaar of beheerder in staat stelt een API in gebruik te nemen die het beheer van beleidsdefinities mogelijk maakt." 

Bij het volgen van deze route zijn er twee opties:

** Optie 1 * *
    De EMM provider geeft je hun bibliotheken, en dan ga je naar de broncode voor de app. Met behulp van de bibliotheken "wikkel" de bron en repakket de toepassing. Deze aanpak zal leiden tot aanzienlijke ontwikkelingstijd en bijbehorende frustratie. Uiteindelijk moet je een app hebben die nu gewikkeld is met de EMM bibliotheken. De hoop, maar niet de garantie, is dat je een app hebt met een extra laag. Hiermee kunt u de app beheren en beveiligen op het mobiele apparaat van een gebruiker.

** Optie 2 * *
    De EMM-provider geeft u een tool voor het inpakken van de app. In meer moderne gevallen, het is een eenvoudig selectievakje in uw EMM-toepassing bij het configureren van de app. Deze tools injecteren dan alle benodigde code om het in te pakken. Dan bouwt de tool (of EMM provider) het weer op. Hiermee kunt u de nieuwe, ingepakte app distribueren. De ingepakte app heeft een laag waarmee u de app op het mobiele apparaat van een gebruiker kunt beheren en beveiligen. 

Tot voor kort is app-verpakking de gemeenschappelijke aanpak geweest. Het komt niet zonder risico's en uitdagingen om schaalbaarheid. 

De meeste moderne toepassingen volgen bijvoorbeeld continue ontwikkeling. Telkens wanneer een toepassing wordt gewijzigd, moet deze door het hierboven beschreven proces worden uitgevoerd. 

Er is ook functionaliteit en compatibiliteitsrisico. Dit is een bekend probleem voor de Mattermeeste toepassing en appinpaktools.

Deze incompatibiliteit is geen probleem met de toepassing Matterbest. Het resultaat van de eigen aard van de tools van de provider. Om de zaken nog erger te maken, is er geen enkele actie om problemen op het gebied van verenigbaarheid aan te pakken.

In het einde, dit stelt app inwikkelen in een negatief licht. Dit is de reden waarom de ` AppConfig Community <https://www.appconfig.org> ` _ kwam samen om een standaard te maken. AppConfig is een moderne, efficiënte en schaalbare benadering van enterprise mobile management. In dat opzicht zijn de meeste toepassingsvoordelen van de toepassing rond deze standaard.

******************
Mobiele VPN-opties ******************

Met een VPN (Virtual Private Network) kan een apparaat buiten een firewall toegang krijgen tot content binnen de firewall alsof het zich in hetzelfde netwerk bevonden. De meeste bedrijfsteams zijn bekend met VPN's. Wij zullen hier niet in detail treden.

Er zijn VPN-opties die afhankelijk zijn van de eisen van uw organisatie. U moet ook rekening houden met de eisen/behoeften van uw gebruikers. Dit kan van invloed zijn op uw aanpak voor mobiele implementatie.

Voor de Matterbest mobiele applicatie zullen we twee opties bespreken: een apparaat VPN of per-app VPN.

    ** Note:** We stellen voor ' na onze aanbevolen stappen <https://docs.mattermost.com/mobile/mobile-appstore-install.html> ` _ om uw inzet te beveiligen.

* * Apparaat VPN* *
    Dit is niet zo gebruikelijk, vooral in het geval van Bring Your Own Device (BYOD) scenario's. In deze optie worden alle internetverkeersroutes door het VPN opgegeven in het profiel. Dit kan problemen veroorzaken voor persoonlijke toepassingen.

** Per-app VPN* *
    In tegenstelling, de meer algemene aanpak is het gebruik van een per-app VPN. Dit zorgt voor een verbinding met het VPN wanneer dat nodig is (on-demand). Bijvoorbeeld wanneer u een bepaalde app gebruikt.

Ongeacht de gemeenschappelijkheid van beide opties hierboven, Mattermeeste biedt ondersteuning voor beide. Omdat Matterbest de AppConfig-standaard ondersteunt, zijn beide opties compatibel met EMM-providers.

    ** Note:** Wil je verbinding maken via een corporate proxy server? Als dit het geval is, " review onze FAQ <https: //docs.mattermost.com/mobile/mobile-faq.html#how-do-i-receive-mobile-push-notification-if-my-it-policy-requires-the-use-of-a-corporate-proxy-server> ` _ voor architectuur, probleemoplossing en beste praktijken.

----

##########################################
Het juiste mobiele implementatiemodel kiezen ############################################

Op dit punt zou je moeten lezen door de inzet primer. Het biedt een grote hoeveelheid context voor de principes en best practices die volgen. Deze volgende sectie is bedoeld om u te helpen kiezen voor een van de twee aanbevolen implementatiemodellen.

*****************************************
Werken met de openbare app-stores *************************************************

* * Gewenste Resultaten: **

-Snelle uitrol van de Mattermeest mobiele applicatie
-Gebruikers toestaan om de toepassing te installeren op hun apparaat
-Zorgen voor een hoog niveau van beveiliging en gecontroleerde toegang
-Gebruik bestaande, interne processen en tools

Wij raden u een van deze opties aan als u:

-Het testen van de mobiele toepassingen
-Service-servers in gebruik nemen met behulp van geen push-berichten, of berichten van Matterbest's ` TPNS <https: //docs.mattermost.com/overview/faq.html#tpns> ` _ (Test Push Notification Service)
-Enterprise Edition-servers in gebruik nemen met behulp van push-berichten van Matterbest's ` HPNS <https://docs.mattermost.com/mobile/mobile-hpns.html> ' _ (Hosted Push Notification Service)

De mobiele toepassingen van Mattermeeste werken met onze gehoste versie van de Mattermeeste Push Notification Service (MPNS). Dit is het eenvoudiger pad. De Mattermeeste mobiele toepassingen kunnen worden ingezet met of zonder EMM provider. Deze opties worden hieronder nader toegelicht. 

    ** Note:** HPNS is compatibel met EMM providers.

** Optie 1 * *-Public App Store Installatie (Makkelijkst)

-Gebruikers downloaden van toepassing via Apple App Store of Google Play
-Gebruikers URL invoeren voor uw gehoste Mattermeeste Server

*Advantages: * Zeer eenvoudig, mobiele implementatie kan worden gedaan door elke individuele gebruiker

*Disadvantages: * Geen extra EMM-beveiligingsfuncties

** Optie 2 * *-Openbare App Store-Insta
llatie met EMM Provider (Easy)

-De EMM provider duwt de Matterbest app naar de EMM geregistreerde apparaten
-De best practices/vereisten van uw organisatie uitbreiden via uw EMM-provider

*Advantages: * Gemakkelijk, mobiele implementatie gebeurt automatisch naar geregistreerde apparaten, app beveiliging en configuratie kan worden onderhouden via uw EMM-provider

*Disadvantages: * Geen aanpassing van de app

*********************************************
Aangepaste builds van de mobiele apps distribueren *************************************

* * Gewenste Resultaten * *:

-Onderhouden volledige controle over de distributie van applicaties
-Verander de look, feel en mogelijkheden van de Mattermeest mobiele applicatie
-Uw eigen MPNS in gebruik nemen om te voldoen aan specifieke organisatorische eisen

Dit model is moeilijker en wordt aanbevolen voor organisaties die de HPNS niet (of niet willen) gebruiken. Vaak wordt dit bepaald door beveiligings-en toegangsvereisten, niet de grootte van uw organisatie.

Zowel Google als Apple vereisen handtekeningen van de toepassing en push-proxy die overeenkomen. Dit betekent dat als u de toepassingen bouwt, u uw eigen instance van MPNS moet hosten.

Het bouwen van de apps kan een betrokken proces zijn. Dit vereist dat u de skillset hebt om verpakte apps te onderhouden en in gebruik te nemen. Een deel van dit proces omvat, maar is niet beperkt tot:

-Verkrijgen/verstrekken van certificaten voor uw aangepaste Mattermeeste toepassing
-Uw aangepaste Mattermeeste-toepassingen ondertekenen
-Distributie van uw applicaties via openbare of particuliere app stores

Het bijhouden van uw aangepaste apps up-to-date met functies en security updates zal uw verantwoordelijkheid.

Om te begrijpen wat er aan de hand is, laat u uw ontwikkelteam lezen op onze documentatie <https://developers.mattermost.com/contribute/mobile/build-your-own/> ` _.

    ** Opmerking: ** Als van Matterbest 5.18 kunnen klanten van E20 gegevens naar HPNS sturen. Met deze optie wordt een bericht met alleen een ID verzonden. Zodra de mobiele client dit ID ontvangt, wordt de inhoud van het bericht van de server geladen. De inhoud van het bericht wordt dus nooit doorgegeven via APNS/FCM.

----

#################################################
Mobiele implementatie via openbare appstores (aanbevolen) ###################################################

Om verder te kunnen gaan, moet er een Mattermost Server geïnstalleerd en toegankelijk zijn. Dit geldt ook voor het gebruik van de gehoste versie van de Matterbest pushproxy (HPNS).

*********************************
Toegang tot de mobiele toepassingen *********************************

De Mattermeeste mobiele applicatie is beschikbaar voor zowel Android-als iOS-apparaten. Op dit moment is het net zo eenvoudig als uw gebruikers de toepassing downloaden en ` verwijzen naar uw Mattermeeste Server-URL <https: //docs.mattermost.com/help/getting-started/signing-in.html#ios-setup> ` _.

    ** Note:** De Matterbest mobiele apps worden ondertekend en hebben certificaten die zijn gekoppeld aan Matterbest en de openbare app stores. Dit betekent dat ze niet zullen werken als u particulier de Mattermeeste Push Proxy Service.

` Matterbest for Android Devices <https://play.google.com/store/apps/details?id=com.mattermost.rn&hl=en_US> ` _ (via Google Play) ` Matterbest of iOS Devices <https://apps.apple.com/us/app/mattermost/id1257222717> ` _ (via Apple App Store)

Als u geen aanvullende beveiliging wilt (of nodig hebt) die via een EMM-provider wordt geleverd, is uw implementatie voltooid. Vraag uw gebruikers naar de ` beschikbare documentatie <https://docs.mattermost.com/guides/user.html> ` _.

De sub-secties hieronder dienen als een gids op hoog niveau om dit implementatiemodel te begrijpen. Indien nodig, wijzen wij op de documentatie voor technisch onderwijs.

    ** Note:** We raden u ten minste aan onze aanbevolen stappen te volgen om uw implementatie te beveiligen.

****************************************************
Een EMM-provider gebruiken met openbare store-apps ********************************************

EMM-providers helpen beveiligingsparameters uit te breiden tot de Mattermeeste mobiele toepassingen. De AppConfig-standaard maakt dit mogelijk. ` Review de Matterbest AppConfig Values Documentation <https: //docs.mattermost.com/mobile/mobile-appconfig.html#mattermost-appconfig-values> ` _ voor een volledige lijst van beschikbare parameters.  

Bij het volgen van deze route dient u rekening te houden met:

-Wat is het mobiele beleid, is het bedrijf-eigendom, BYOD of beide?
-Weet u welke apparaten worden gebruikt als BYOD?
-Wat voor besturingssysteem wilt u beginnen met testen?
-Een voorbeeldconfiguratie maken en vervolgens validatietests uitvoeren op elk configuratie-item

**********************************
Matterbest configureren voor gebruik HPNS **********************************

Het configureren van uw Mattermeeste Server voor het gebruik van de Mattermeeste HPNS is een enkel configuratie-item. Dit wordt behandeld in onze ` Hosted Push Notification Service documentation <https://docs.mattermost.com/mobile/mobile-hpns.html> ` _. 

Vervolgens moeten uw gebruikers de mobiele toepassing installeren op hun apparaat. Indien gewenst kunt u de beveiligingsmogelijkheden verder configureren met behulp van een EMM-provider.

**********************************
Bijwerken via de openbare store-apps **************************

Hoewel geen deel van uw eerste mobiele implementatie, moet u overwegen een strategie voor het bijwerken wanneer nieuwe versies van de Mattermeeste mobiele toepassingen beschikbaar zijn. Tegelijkertijd moet u alle compatibiliteitsvereisten voor de mobiele apps en de Mattermeeste Server controleren. 

Wij raden u bijvoorbeeld aan:

-Controleer de compatibiliteitsvereisten
-Versies valideren die verbinding maken met server
-Server bijwerken
-Update apps

Het is vaak gemakkelijker om de mobiele apps te upgraden. Echter, niet alle verstrekte updates zijn compatibel met alle eerdere versies van de Mattermeeste server.

Raadpleeg voor meer informatie de ` Matterbest mobile app changelog <https://github.com/mattermost/mattermost-mobile/blob/master/CHANGELOG.md> ` _ en ` Mattermsot server changelog <https://docs.mattermost.com/administration/changelog.html> ` _.

    ** Note:** Alleen het bijwerken van de mobiele apps, of het bijwerken van de mobiele apps voor de Mattermeeste server, kan leiden tot onverenigbaarheid.

----

#################################
Mobiele implementatie via aangepaste builds #################################

Het kiezen van dit model betekent dat je hebt besloten om de mobiele applicaties die Matterbest beschikbaar heeft gemaakt niet via de openbare app stores te gebruiken. 

Dit betekent ook dat u deze toepassingen moet onderhouden. Onderhoud omvat het opnieuw opbouwen en opnemen van voorzieningen en/of beveiligingsupdates. Anders komen uw toepassingen niet overeen met de functionaliteit van onze openbare toepassingen en kunnen ze niet compatibel zijn met toekomstige versies van de Mattermeeste Server.

Tot slot betekent deze optie ook dat u de gehoste versie van de Matterbest Push Notification Service (MPNS) niet kunt gebruiken.

Een eerste stap voor dit implementatiemodel is ` review the documentation <https://developers.mattermost.com/contribute/mobile/> ` _. Uw ontwikkelteam moet voldoen aan de eisen voor het bouwen van de toepassingen. Deze documentatie bevat informatie over het bouwen, compileren en ondertekenen. Het bevat ook informatie voor het aanpassen van de apps.

We hebben een aantal aanbevolen secties hieronder.

-Developer Setup
-Bouw Je Eigen App
-Push-berichten

*********************************
Distributie via een app store *********************************

Zodra u uw eigen apps hebt gebouwd, moet u ze distribueren. Er zijn twee opties:

Optie 1-Enterprise App Store via EMM Provider (meest voorkomende en aanbevolen): 

-Dit is de meest gebruikelijke manier voor klanten om hun apps te distribueren
-Eenmaal toegevoegd aan uw eigen Enterprise App Store, kunnen gebruikers downloaden van de EMM-catalogus, of u kunt de EMM-provider gebruiken om de toepassing te pushen naar het apparaat van de gebruiker

Optie 2-Apple App Store en Google Play (minder vaak):

-Om een app te verzenden naar de officiële app stores, moet u de app te verzenden naar Apple/Google voor review
-Dit is hetzelfde proces dat Mattermeeste maakt gebruik maken van de apps beschikbaar voor iedereen
-Dit proces komt vaker voor als u op zoek bent naar wit label de app om Mattermeest branding te verwijderen

**************************************************************
Een EMM-provider gebruiken met uw aangepaste Mattermeeste apps ******************************************************

Als u een EMM-provider gebruikt, let er dan op dat Matterbest geen app-inpakpapier ondersteunt. In plaats daarvan gebruiken we de AppConfig standaard.

In sommige gevallen is er een onverenigbaarheid met de app-inpaken React Native toepassingen. Reageren Native is de technologie die wordt gebruikt om de Mattermeeste mobiele toepassingen te ontwikkelen. De Matterbest mobiele app werkt niet goed wanneer u de app-inpakpapier gebruikt. In feite, een meerderheid van de app wrappers EMMs bieden geen ondersteuning voor WebSocket verbindingen.

App-verpakking is nog vaak een optie tijdens de EMM-configuratie. Nogmaals, AppConfig is de enige ondersteunde methode voor het beveiligen van Mattermeeste mobiele toepassingen via een EMM provider.

AppConfig-opties variëren per EMM-provider en het bijbehorende apparaat. U kunt de beschikbare opties bekijken in onze ` AppConfig Values-documentatie <https: //docs.mattermost.com/mobile/mobile-appconfig.html#mattermost-appconfig-values> ` _.

    ** Note:** In Bijlage B hebben we een lijst van populaire EMM-aanbieders en bijvoorbeeld documentatie waar beschikbaar.

Als onderdeel van het configureren van uw EMM-oplossing dient u rekening te houden met:

-Wat is het mobiele beleid, is het bedrijf-eigendom, BYOD of beide?
-Weet u welke apparaten worden gebruikt als BYOD?
-Wat voor besturingssysteem wilt u beginnen met testen?
-Een voorbeeldconfiguratie maken en vervolgens validatietests uitvoeren op elk configuratie-item

************************************************************
De MPNS configureren voor uw aangepaste Mattermeeste-apps ****************************************************

Het bouwen en distribueren van de Matterbest mobiele apps vereist dat u een instance van de MPNS in gebruik neemt.

Als onderdeel van het proces van het bouwen van de toepassingen moet u de toepassingen ondertekenen. U moet ook het juiste certificaat verkrijgen voor zowel Android als iOS. Als dit niet gebeurt, kunnen de toepassingen niet interactief werken met uw instance van de MPNS.

Als dat eenmaal is voltooid, kunt u doorgaan met de implementatie van uw MPNS-instance.

De documentatie over de installatie en configuratie van uw MPNS vindt u hieronder.

-` Push Notification Service Installation <https://developers.mattermost.com/contribute/mobile/push-notifications/service/> ` _
-` Admin Configuration for Push Notifications <https: //docs.mattermost.com/administration/config-settings.html#push-notification-contents> ` _
-` Aanvullende FAQs <https://docs.mattermost.com/mobile/mobile-faq.html#> ` _

********************************************
Bijwerken van uw aangepaste Mattermeeste apps ************************************

Hoewel geen deel van uw eerste mobiele implementatie, moet u overwegen een strategie voor het bijwerken wanneer nieuwe versies van de Mattermeeste mobiele toepassingen beschikbaar zijn. Wij raden u aan uw aangepaste Mattermeeste apps bij te werken voor alle beveiligings-of servicereleases. Op hetzelfde moment, als u de apps hebt bijgewerkt, voorafgaand aan distributie, moet u de compatibiliteitsvereisten voor de mobiele apps en de Mattermeeste Server controleren. 

    ** Note:** Alleen het bijwerken van de mobiele apps, of het bijwerken van de mobiele apps voor de Mattermeeste server, kan leiden tot onverenigbaarheid.

----

####################################
Bijlage A: Problemen oplossen en veelgestelde vragen ####################################

Wij raden u aan om onze ' Mobile FAQ <https://docs.mattermost.com/mobile/mobile-faq.html> ` _ en ` Mobile Troubleshooting documentation <https://docs.mattermost.com/mobile/mobile-troubleshoot.html> ` _ te bekijken. De meest voorkomende vragen zijn daar beantwoord. Echter, het is belangrijk om uit te roepen een paar gemeenschappelijke items klanten lopen in.

***************************************
Gegevensbeveiliging op mobiele apparaten *******************************

-` Hoe wordt gegevens verwerkt op een apparaat nadat een account is verwijderd? <https: //docs.mattermost.com/mobile/mobile-faq.html#how-is-data-afgehandeld-on-mobile-devices-after-a-user-account-is-deactivated> ` _
-` Welke post metagegevens worden verzonden in mobiele push-berichten? <https: //docs.mattermos
t.com/mobile/mobile-faq.html#what-post-metadata-is-sent-in-mobile-push-notifications> ` _
-` Wat zijn mijn opties voor het beveiligen van de mobiele apps? <https: //docs.mattermost.com/mobile/mobile-faq.html#what-zijn-mijn-opties-voor-beveiligen-de-mobile-apps> ` _
-` Wat zijn mijn opties voor het beveiligen van push-berichten? <https: //docs.mattermost.com/mobile/mobile-faq.html#what-zijn-mijn-opties-voor-beveiligen-push-notificaties> ` _

***********************
Bedrijfsproxyservers ***********************

' Hoe ontvang ik mobiele push-meldingen als mijn IT-beleid het gebruik van een bedrijfsproxyserver vereist? <https: //docs.mattermost.com/mobile/mobile-faq.html#how-do-i-receive-mobile-push-notification-if-my-it-policy-requires-the-use-of-a-corporate-proxy-server> ` _

-` Matterbest implementeren met beperkte postproxy-relay in DMZ of een betrouwbare cloud-omgeving <https: //docs.mattermost.com/mobile/mobile-faq.html#deploy-matterbest-with-connection-restricted-post-proxy-relay-in-dmz-or-a-trusted-cloud-environment> ` _
-` Whitelist Matterbest push notification proxy om uw corporate proxy server te omzeilen <https: //docs.mattermost.com/mobile/mobile-faq.html#whitelist-matterbest-push-notification-proxy-to-bypass-uw-corporate-proxy-server> ` _
-` Run App Store versies van de Mattermeeste mobiele apps <https: //docs.mattermost.com/mobile/mobile-faq.html#run-app-store-versions-of-the-matterbest-mobile-apps> ` _

----

###########################
Bijlage B: Lijst van EMM-providers #############################

We hebben een lijst samengesteld van de meest populaire EMM-providers en de bijbehorende Unified Endpoint Management-tools die ze gebruiken. In twee gevallen (Blackberry Dynamics en MobileIron) hebben we ook de bijbehorende documentatie ontwikkeld die is ontwikkeld door het Mattermeeste team.

********************************************
Blackberry Dynamics (Blackberry UEM) ************************************

" BlackBerry UEM is een multiplatform EMM-oplossing die een uitgebreid apparaat, app en content management biedt met geïntegreerde beveiliging en connectiviteit, en helpt u bij het beheren van iOS-, macOS-, Android-, Windows-10-en BlackBerry 10-apparaten voor uw organisatie. BlackBerry UEM is opgenomen in de ` BlackBerry Secure UEM & Productivity Suites <https://www.blackberry.com/us/en/products/blackberry-secure-uem-suites.html> ` _-Choice Suite, Freedom Suite en Limitless Suite. "

-` BlackBerry Website <https://www.blackberry.com/us/en/products/blackberry-uem> ` _
-` BlackBerry Matterendste Documentatie <https://docs.mattermost.com/mobile/mobile-blackberry.html> ` _
-` Blackberry Documentation and Help Materials <https://docs.blackberry.com/en/endpoint-management/blackberry-uem/12_11> ` _

**********
MobileIron
**********

" MobileIron Unified Endpoint Management (UEM) biedt de basis voor het eerste mobiel-centrische, nulvertrouwen enterprise security framework van de industrie. In tegenstelling tot andere UEM-oplossingen stelt MobileIron UEM de bedrijfsmobiele beveiliging in het midden van uw onderneming en stelt u in staat om er op te bouwen met het inschakelen van technologieën zoals 'zero sign-on (ZSO) <https://www.mobileiron.com/en/products/access> ` _ user-en apparaatverificatie, multi-factor authenticatie (MFA) en' mobile threat detection (MTD) <https://www.mobileiron.com/en/products/mobile-threat-defense> ` _. "

-` MobileIron Website <https://www.mobileiron.com/en/products/uem> ` _
-` MobileIron Matterbest Documentation <https://docs.mattermost.com/mobile/mobile-mobileiron.html> ` _-` MobileIron Support (requires login) <https://help.mobileiron.com/s/login/?startURL=%2Fs%2F&ec=302> ` _

****
Fyde
****

" Veilig toegang Matterit's messaging-platform om productieve teamsamenwerking mogelijk te maken. Onze connectionless, modern alternatief voor VPN helpt het beperken van het risico door het beveiligen van private cloud-netwerk van directe toegang door niet-beheerde apparaten. "

-` Fyde voor Mattermost Use Case <https://www.fyde.com/use-cases/fyde-for-mattermost> ` _
-` Fyde Documentation <https://fyde.github.io/docs/> ` _

************************************************
Werkruimte Eén (voorheen VMware AirWatch) ****************************************

"Empower medewerkers met een gepersonaliseerde" elke app, elk apparaat " ervaring en hen te betrekken van de eerste dag met een virtuele assistent die gemeenschappelijke taken versnelt. Met modern management en Zero Trust security, samen met data-driven inzichten en automatisering, kan IT verenigen siloed teams, het beschermen van zakelijke apps en gegevens, en met vertrouwen zorgen voor de boeiende ervaringen die moderne werkkrachten vraag. "

-` Workspace One Website <https://www.air-watch.com/why-workspace-one-airwatch/> ` _
-` werkruimte Een Help-portal <https://my.workspaceone.com/> ` _

***********************************************
Citrix Endpoint Management (voorheen XenMobile) ***********************************************

" Als je nog steeds op meerdere platforms vertrouwt om eindpunten te zien, is het tijd voor een verandering. Nu meer dan ooit, IT moet een manier om te beheren en monitoren van mobiele, traditionele en IoT eindpunten zonder te raadplegen tientallen verschillende dashboards en rapporten. Met de meerderheid van de medewerkers werken weg van de desks 50-60% van de tijd, 1 de apparaten en apps die ze toegang zijn zo gevarieerd als de tools beschikbaar om ze te beheren. Omdat de diversiteit van de eindgebruikeropties een all-time high-` BYOD <https://www.citrix.com/digital-workspace/byod.html> ` _, ` Office 365 <https://www.citrix.com/digital-workspace/optimize-microsoft-ems-intune.html> ` _ en frequente ` Windows 10 updates <https://www.citrix.com/digital-workspace/windows-10.html> ` _ allemaal een rol spelen bereikt-je hebt een geconsolideerde console nodig. Maak een enkele weergave van gebruikers met meerdere apparaten met UEM om apparaatconfiguraties, gegevensbeveiliging en gebruiksbeleid te verenigen ... allemaal op één centrale locatie. "

` Citrix Endpoint Website <https://www.citrix.com/products/citrix-endpoint-management/> ` _ ` Citrix Endpoint Management Documentation <https://docs.citrix.com/en-us/citrix-endpoint-management.html> ` _

****************
Microsoft InTune ****************

" Microsoft Intune is een cloud-gebaseerde service die zich richt op mobiel apparaatbeheer (MDM) en mobiel applicatiebeheer (MAM). Intune is opgenomen in Microsoft ' s ` Enterprise Mobility + Security (EMS) suite <https://www.microsoft.com/microsoft-365/enterprise-mobility-security> ` _, en stelt gebruikers in staat om productief te zijn terwijl uw organisatie gegevens beschermd. Het integreert met andere diensten, waaronder Microsoft 365 en Azure Active Directory (Azure AD) om te controleren wie toegang heeft, en wat ze hebben toegang tot, en Azure Information Protection voor gegevensbescherming. Wanneer u het gebruikt met Microsoft 365, kunt u uw personeel om productief te zijn op al hun apparaten, terwijl het houden van uw organisatie de informatie beschermd. "

-` InTune Website <https://docs.microsoft.com/en-us/intune/fundamentals/what-is-intune> ` _
-` Microsoft InTune Documentation <https://docs.microsoft.com/en-us/intune-user-help/use-managed-devices-to-get-work-done> ` _
