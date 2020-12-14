Veelgestelde vragen
--------------------------------

How to Bind Authentication to Id Attribute in plaats van E-mail
~ ~ ~ ~ > ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~

U kunt ook een ID-kenmerk gebruiken in plaats van een e-mail om de gebruiker te binden.  We raden aan een uniek ID te kiezen en niet in de loop van de tijd te veranderen.  

Door het configureren met een ID-kenmerk kunt u een e-mailadres opnieuw gebruiken voor een nieuwe gebruiker zonder dat de informatie van de oude gebruiker wordt weergegeven. Bijvoorbeeld, als een gebruiker met een e-mailadres joe.smith@mattermost.com ooit een werknemer was, kan een nieuwe werknemer met de naam Joe Smith dezelfde e-mail gebruiken. Deze configuratie is ook handig wanneer de naam van een gebruiker verandert en hun e-mail moet worden bijgewerkt. 

Dit proces is ontworpen met achterwaartse compatibiliteit met e-mailbinding. Dit is het proces dat wordt toegepast op nieuwe account-creaties en om rekening te houden met inloggen na de configuratie:

 -Een gebruiker die is geverifieerd met SAML is gebonden aan de SAML-servicegebruiker met behulp van het Id-kenmerk (zo lang als het is geconfigureerd) of gebonden door e-mail met behulp van de e-mail ontvangen van SAML.-Wanneer de gebruiker zich aanmeldt en de SAML-server reageert met een geldige authenticatie, dan gebruikt de server het veld "Id" van de SAML-authenticatie om de gebruiker te doorzoeken.-Als een gebruiker die aan dat ID gebonden is al bestaat, dan wordt het zich aangemeld als die gebruiker.-Als een gebruiker die aan dat ID gebonden is niet bestaat, dan zal het zich op de e-mail zoeken. gebruiker die aan het ID of de e-mail is gebonden, bestaat niet. Het maakt een nieuwe Mattermeeste account aan die aan het SAML-account gebonden is door ID en stelt de gebruiker in staat om zich aan te melden. 

 Opmerking: Bestaande accounts worden pas bijgewerkt nadat ze zich bij de server hebben aangemeld. 
 
Kan SAML via Microsoft ADFS worden geconfigureerd met Integrated Windows Authentication (IWA)?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~

-Ja, IWA wordt ondersteund door de browser, met ondersteuning toegevoegd aan iOS en Android mobiele apps in Q2/2019 (mobiele apps v1.18 en later).

Echter, IWA wordt niet ondersteund op de Mattermeeste Desktop Apps als gevolg van een beperking in Electron. Als een tijdelijke oplossing kunt u een snelkoppeling op het bureaublad van de browser voor snelle toegang tot Matterbest, net als een Desktop App.

Hoe migreer ik gebruikers van de ene verificatiemethode (bijv. e-mail) naar SAML?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~

Gebruik de :doc: ` mattermeeste gebruiker migrate_auth CLI opdracht <cli-user-migrate-auth>`.

Hoe verschilt SAML van OAuth 2.0 en OpenId Connect?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~

OAuth 2.0 is voornamelijk bedoeld voor gedelegeerde machtigingen, waarbij een app is gemachtigd voor toegang tot resources, zoals de lijst van contactpersonen van Google. Het gaat niet om authenticatie.

OpenID Connect is gebouwd bovenop OAuth 2.0, dat authenticatie ondersteunt en dus direct SSO.

SAML is als OpenID Connect, behalve meestal
gebruikt in bedrijfsinstellingen. OpenID Connect komt vaker voor in consumentenwebsites en web/mobile apps.

Meer informatie op https://hackernoon.com/demystifying-oauth-2-0-en-openid-connect-and-saml-12aa4cf9fdba.
