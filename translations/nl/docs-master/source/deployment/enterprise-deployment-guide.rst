#########################
Bedrijfsimplementatiehandleiding #########################

== == == == == == == == Over Deze Gids
== == == == == == == ==

********
Publiek
********

IT-leiders, systeembeheerders en/of projectmanagers. Opmerking:
    Sommige functies die in deze handleiding worden beschreven, zijn alleen beschikbaar voor Enterprise Edition E10 en/of E20. We zullen specifieke licenties selecteren die nodig zijn wanneer van toepassing.

*******************
Leerdoelen *******************

Deze handleiding bevat basisgegevens die nodig zijn bij de ontwikkeling van een plan voor een proof of concept en/of productieniveau van Matterbest op productieniveau.

Het zal niet in de technische implementatie duiken, maar zal naar alle relevante documentatie verwijzen.

Aan het einde van deze handleiding moet u inzicht krijgen in de eisen op hoog niveau voor een succesvolle Mattermeeste Enterprise-implementatie.

Dit omvat:

-Het kiezen van de implementatie van de Mattermeeste Server-toepassing.
-Migreren van andere ChatOps platforms.
-Integratie van Mattermeeste met bestaande Single Sign-On (SSO) providers.
-Eerste stappen/beste praktijken voor onboarding gebruikers.

*******
Ondersteuning
*******

Als u op elk punt extra hulp nodig hebt, zijn we klaar om te helpen, gewoon bereiken met behulp van een van deze methoden:

-` Community <https://community.mattermost.com/> ` _-Onze hele organisatie gebruikt Matterbest, plus u krijgt de steun van een van de beste open source communities rond.
-Documentatie-Wij linken naar vele delen van onze ` Beheerder documentatie <https://docs.mattermost.com/guides/administrator.html> ` _ in deze gids, maar moedigen u aan om een kijkje te nemen op ` al onze documentatie <https://docs.mattermost.com> ` _.
-Enterprise Support-Als u een abonnee van Enterprise Edition bent, kunt u een ondersteuningsticket openen in de Support-portal van Enterprise Edition. .. Aanbeveling:
    Ga naar de ` Mattermeest Community-server <https://community.mattermost.com/> ' _ en maak een account aan. Join kanaal ` Vraag iets <https://community.mattermost.com/core/channels/ask-anything> ` _ om niet alleen de ervaring Matterbest meteen maar ook voor ondersteuning als je vast te zitten op elk punt in deze gids.

== == == == == == == == == == == == == == == == Voordat U Begint Met Uw Implementatie
== == == == == == == == == == == == == == == ==

****************************************
Wat maakt Mattermeest anders? ********************************

Mattermeeste is een high-trust messaging platform voor enterprise gebruik. Als ondernemingen komen in alle vormen en maten, Matterbest is gebouwd om een optimale ervaring voor alle klanten.

De opkomst van ` ChatOps <https://mattermost.com/chatops> ` _ betekent dat Matterbest niet langer een instrument is dat voornamelijk door ontwikkelaars wordt gebruikt. In feite heeft het de mogelijkheid om de communicatie voor vele soorten teams te verbeteren door middel van een veelheid van ` integraties <https://integrations.mattermost.com> ` _, extensies en maatwerk.

Hier is een voorbeeld van de soorten integraties die onze klanten in gebruik nemen:

-Confluence
-Docker
-GitHub/GitLab
Jira
-Outlook
-Trello

Ik neem dit verder, want Mattermore is een ope.
n de brontoepassing, kan het op vele manieren worden aangepast aan uw organisatorische behoeften.

***************
Verdere lezing ***************

Mattermeest schaling
------------------

Om uw Matterste-installatie te laten groeien door een team te ondersteunen bij het ondersteunen van een bedrijf, zijn er twee soorten ` scaling <https://docs.mattermost.com/deployment/scaling.html> ' _ nodig.

** Technical Scaling: ** Of gebruikt voor teams of bedrijven, de Mattermeeste server is ontworpen om tienduizenden gebruikers te ondersteunen op een enkele server met geschikte hardware. Wij ondersteunen het uitvoeren van Mattermeeste Server op meerdere ` Linux distributies en on-premises cloud solutions <https: //docs.mattermost.com/guides/administrator.html#installing-mattermost> ` _.

** Functional Scaling: ** Scaling van een team naar een onderneming is als het gaan van een "virtueel kantoor" naar een "virtuele campus". Geavanceerde functies, zoals enterprise authenticatie, granulaire permissies, compliance en auditing, en geavanceerde rapportage worden steeds belangrijker als organisaties groeien dan teams.

Mattermeeste licentieverlening
--------------------

Mattermeeste Enterprise Edition wordt geleverd met twee licentieopties: Enterprise E10 en Enterprise E20.

De E10-licentie is geschikt voor kleinere organisaties met minder behoefte aan automatisering en compliance, terwijl de E20-licentie functies biedt zoals AD/LDAP, SAML 2.0, geautomatiseerde nalevingsexport en teamspecifieke machtigingen. U vindt hier een volledige vergelijking ` hier <https://mattermost.com/pricing-feature-comparison> ` _.

Zodra u Matterbest hebt geïnstalleerd en gebruikt, activeert u uw Enterprise E20-proeflicentie via ** Hoofdmenu > Systeemconsole > Edition en licentie * * en selecteert u ** Start trial * *. .. Opmerking:
    U kunt uw Matterste Enterprise-abonnementen kopen en beheren met onze ` Customer Portal <https://customers.mattermost.com/login> ` _ of u kunt contact opnemen met ons Sales team door contact op te nemen met sales@mattermost.com.

Clientgebruik
------------

Afhankelijk van uw omgeving en uw gebruikers hebt u verschillende opties bij het in gebruik nemen van Matterbest: web browser, ` desktop <https://docs.mattermost.com/install/desktop.html> ` _, ` mobile <https://docs.mattermost.com/mobile/mobile-overview.html> ` _, of alle drie. Wij ` bieden binaries <https: //mattermost.com/download/#mattermostApps> ` _ voor MS Windows, macOS, Linux, iOS en Android. Afhankelijk van uw organisatiebeleid kunnen deze platforms echter variëren.

== == == == == == == == == == Implementatie Eerste Stappen
== == == == == == == == == == ==

De implementatie van Matterbest met een bedrijfsomgeving is geen klein project. Afhankelijk van uw use case moeten meerdere fysieke machines worden ingesteld met Mattermeeste server, een proxy en een database, terwijl duizenden gebruikers via AD/LDAP moeten worden geïmporteerd. Terwijl wij ernaar streven om dit zo eenvoudig mogelijk te maken zal het tijd en iteratie nemen.

***********************
Bepaal uw gebruik Zaak ***********************

Zoals hierboven vermeld is het essentieel voor een succesvolle implementatie om uw specifieke use case te kennen. Om te beginnen probeer je de volgende vragen te beantwoorden:

-Hoeveel gebruikers zullen gebruik maken van Mattermeest op de eerste inzet en is dit aantal gaat drastisch te verhogen in de nabije toekomst?
-Welke klanten zullen in gebruik zijn?
-Migreert u van een bestaand ChatOps of een ander communicatieplatform?
-Gebruikt u een identiteitsprovider voor enkelvoudige aanmelding en zo ja, welke?
-Welke nalevingsvereisten moet je ontmoeten?
-Wat zijn de beveiligingseisen van uw organisatie?

************************
Uw implementatie voorbereiden ************************

Technische Voorschriften
----------------------

De hardwarevereisten voor de Mattermeeste server en database ` groeien op basis van het aantal gebruikers <https://docs.mattermost.com/install/requirements.html> ` _.

Afhankelijk van welke clients uw gebruikers zullen werken met extra lezen kan nodig zijn:
-U gaat gebruik maken van de web-app-geen verdere lezing nodig.
-U gaat de desktop app gebruiken-lees ook ` Desktop Application Install Guides <https://docs.mattermost.com/install/desktop.html> ` _.
-U gaat de mobiele app gebruiken-lees ook ` Mobile App Deployment Guide <https://docs.mattermost.com/deployment/mobile-app-deployment.html> ` _.

Migratie
---------

Bij het migreren van een bestaande oplossing is het belangrijk om vooruit te plannen. We raden aan om te beginnen met een kleine dataset-beperkte gebruikers en content-om de tijd besteed foutopsporing te verminderen en ervoor te zorgen dat alle velden correct worden geïmporteerd, voordat het nemen van een grote import.

Wij bieden onze klanten gemakkelijk om migratieoplossingen te gebruiken voor vele scenario's:

-Matterbest-Migreren van Matterbest Team Edition is gebruikelijk en vereist alleen dat u een upgrade uitvoert naar de meest recente Enterprise Edition <https: //docs.mattermost.com/administration/upgrade.html#upgrading-team-edition-to-enterprise-edition> ` _ en voeg uw licentiesleutel toe.
-Slack-Er is ondersteuning voor twee methoden van het importeren van gegevens van Slack.
    -Voor kleine datasets met weinig gebruikers en zonder bijlagen kan de ` Matterbest web app worden gebruikt <https: //docs.mattermost.com/administration/migrating.html?highlight = speling#migrating-van-speling-met-de-matterbest-web-app> ` _.
    -Als het mogelijk is, raden we het gebruik van ` Matterbest CLI voor het migratieproces <https: //docs.mattermost.com/administration/migrating.html?highlight = slack#migrating-from-slack-using-the-matterbest-cli> ` _.
-HipChat-Wij raden u aan ' Group Export Dashboard <https://docs.mattermost.com/administration/hipchat-migration-guidelines.html> ` _ te gebruiken om uw gegevens te exporteren in combinatie met het ` Matterbest Bulk Load Tool <https://docs.mattermost.com/deployment/bulk-loading.html> ` _.
-Jabber-U kunt ` BrightScout's Extract, Transform and Load (ETL) <https://github.com/Brightscout/mattermost-etl> ` _ tool gebruiken om te migreren van Jabber.
-Bespoke Messaging Solutions-Matterbest is ontworpen om besprak messaging-oplossingen te vervangen en extra ` security features te bieden <https://docs.mattermost.com/overview/security.html> ` _, maar te migreren van besprak boodschappers kan blijken te zijn uitdagend, omdat de gegevens voor
De mat van dergelijke gereedschappen is onvoorspelbaar. Toch bieden we ` meerdere tools <https: //docs.mattermost.com/administration/migrating.html?highlight = speling#bringing-data-from-bespoke-solutions-into-mattermost> ` _ om migratie te proberen en veel succesvolle migraties met onze klanten te hebben gehad. .. Opmerking:
    Als uw gegevens in de besprak messenger niet essentieel zijn, raden wij u aan een harde schakelaar aan te raden na een periode waarin beide systemen parallel lopen.

Enkelvoudige aanmelding
--------------

Matterbest kan optreden als een ` SAML 2.0 <https://docs.mattermost.com/deployment/sso-saml.html> ` _ provider dus het opzetten van Single Sign-On is een eenvoudige zaak.

Wij ondersteunen deze SSO-services:

-` OneLogin <https://docs.mattermost.com/deployment/sso-saml-onelogin.html> ` _
-` Okta <https://docs.mattermost.com/deployment/sso-saml-okta.html> ` _
-` GitLab <https://docs.mattermost.com/deployment/sso-gitlab.html> ` _
-` Google People API <https://docs.mattermost.com/deployment/sso-google.html> ` _
-` AD/LDAP <https://docs.mattermost.com/deployment/sso-ldap.html> ` _
-` Azure Active Directory en Office 365 <https://docs.mattermost.com/deployment/sso-office.html> ` _
-` Microsoft ADFS <https://docs.mattermost.com/deployment/sso-saml-adfs-msws2016.html> ` _

Naleving
----------

Wanneer u aan de nalevingsvereisten moet voldoen-met name bij het werken met proxy's-zorg er dan voor dat u vooruit wilt plannen om te voorkomen dat de infrastructuur opnieuw wordt ontworpen terwijl u Matterbest in gebruik neemt. Hier is hoe Mattermeest ondersteunt uw compliance behoeften:

-Uitgaande Proxy-In sommige scenario's, zoals het bewaken van het uitgaande verkeer of het bepalen welke websites kunnen worden weergegeven in de link previews, kunt u wensen ` gebruik Matterbest achter een proxy <https://docs.mattermost.com/install/outbound-proxy.html> ` _.
-Electronic Discovery-Electronic Discovery (eDiscovery) is het proces van het zoeken van elektronische gegevens om te worden gebruikt als bewijs in een juridische zaak. We hebben de ` eDiscovery documentatie <https://docs.mattermost.com/administration/ediscovery.html> ` _ om te helpen.
-Compliance exporteren-Met deze functie kunt u 'Nalevingsexporten <https://docs.mattermost.com/administration/compliance-export.html>' _ maken op basis van de systeemconsole, die alle berichten bevat.
-Data Retention-Standaard biedt Matterbest een onbeperkte zoekgeschiedenis waarin alle berichten zonder vervaldatum worden opgeslagen. Deze standaardwaarden kunnen worden gewijzigd door het instellen van het bericht "Retention and File Retention <https://docs.mattermost.com/administration/data-retention.html>" _ voor een bepaalde tijdsduur in de systeemconsole.
-Aangepaste servicevoorwaarden-Als uw organisatie het gebruik van ` custom ToS <https://docs.mattermost.com/administration/custom-terms-of-service.html> ' _ vereist, kan dit worden gedaan in de systeemconsole.

Beveiliging
--------

Veiligheid is een grote zorg met betrekking tot het selecteren van de juiste instrumenten. Mattermeeste software wordt voortdurend gecontroleerd op veiligheid door ontwikkelaars, IT-beheerders, en security-onderzoekers. In tegenstelling tot SaaS-oplossingen kan Matterbest worden geïmplementeerd op-premises in uw privé cloud die u volledige controle over niet alleen de software, maar ook de hardware kant. Hier is een niet-uitputtende lijst van onze veiligheidskenmerken:

-Private cloud-implementatie
-Beveiligde mobiele apps
-Transmissiebeveiliging
-Integriteit en audit controles
-Verificatiewaarborgen
-Toegangsbeleid
-Meer details over dit onderwerp zijn beschikbaar op de sectie 'Matterigste beveiliging <https://docs.mattermost.com/overview/security.html>' _ in onze documentatie.
-HIPAA und FINRA-Matterbest kan worden geïmplementeerd ` Health Insurance Portability and Accountability Act-HIPAA <https: //docs.mattermost.com/overview/security.html#hipaa-compliance> ` _ and ` Financial Industry Regulatory Authority-FINRA <https: //docs.mattermost.com/overview/security.html#finra-compliance> ` _ compliant.
-Certificaat-Based Authentication-` Certificate-Based Authentication <https://docs.mattermost.com/deployment/certificate-based-authentication.html> ` _ is beschikbaar als experimentele functie.
-Multi-factor authenticatie-Matterbest ondersteunt ` multi-factor authenticatie <https://docs.mattermost.com/deployment/auth.html> ` _.

== == == == == == == == == == == == == == Gebruiker Onboarding en Aanneming
== == == == == == == == == == == == == ==

************************
Integraties en plugins ************************

Bij de eerste blik overwegen ` integrations <https://integrations.mattermost.com> ` _ en ` plugins <https://docs.mattermost.com/administration/plugins.html> ` _ als onderdeel van de implementatie lijkt misschien contra-intuïtief. Maar het zijn essentiële onderdelen van het adoptieproces, waarbij uw organisatie wordt gemachtigd om de door elke afdeling gebruikte hulpmiddelen beter te begrijpen.

Bij het kiezen van integraties en plugins voor uw implementatie, richt u zich op die welke waarde voor de organisatie brengen. Bijvoorbeeld, als uw organisatie meestal werkt op afstand de Zoom-plugin kan essentieel zijn, terwijl een enkele office organisatie niet nodig heeft, maar sterk afhankelijk van Outlook-integratie.

*************
Kennisgevingen
*************

Kennisgevingen hebben betekenis gekregen in ons dagelijks leven. Moderne besturingssystemen hebben allemaal een manier om de aandacht van de gebruiker te richten op belangrijke gebeurtenissen van specifieke apps. Er zijn drie verschillende soorten meldingen in Matterbest: desktop-, e-mail-en mobiele push-meldingen. Mattermeesten zal u op de hoogte van berichten met een van deze kenmerken:

-Directe Berichten.
-Uw gebruikersnaam of voornaam wordt vermeld in een kanaal.
-Een kanaal waarin u zich bevindt, wordt gemeld met @channel, @hereof @all.
-Elk van uw geconfigureerde trefwoorden <https: //docs.mattermost.com/help/settings/account-settings.html#words-die-trigger-mentions> ` _ worden gebruikt. Opmerking:
    Alle meldingsgedrag kan globaal worden gecontroleerd of individueel per kanaal. Desktop-, e-mail-en mobiele push-meldingen hebben afzonderlijke instellingen.
