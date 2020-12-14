== == == == == == == == == == == == = SAML Single Sign-On
== == == == == == == == == == == == =

Enkelvoudige aanmelding (Single Sign-On, SSO) is een manier waarop gebruikers zich kunnen aanmelden bij meerdere toepassingen met een enkel gebruikers-ID en wachtwoord zonder dat ze opnieuw hun legitimatiegegevens hoeven in te voeren. Met de SAML-standaard kunnen identiteitsproviders legitimatiegegevens doorgeven aan serviceproviders. Matterbest kan worden geconfigureerd om te fungeren als SAML 2.0 -serviceprovider. 

Matterbest kan worden geconfigureerd om te fungeren als SAML 2.0 -serviceprovider. De integratie SAML Single Sign-On biedt de volgende voordelen:

-** Single sign-on. * * Gebruikers kunnen zich aanmelden bij Matterbest met hun SAML referenties.
-** Centralized identity management. * * Mattermeeste accounts trekken automatisch gebruikersattributen van SAML bij login, zoals volledige naam, e-mail en gebruikersnaam.
-** Automatisch account-provisioning. * * Mattermeeste gebruikersaccounts worden automatisch de eerste keer dat een gebruiker zich aanmeldt met hun SAML-legitimatiegegevens op de Matterendste server gemaakt.
-** Sync groepen naar vooraf gedefinieerde rollen in Mattermost. * * Wijs team-en kanaalrollen toe aan groepen via LDAP Group Sync.
-** Nalevingsuitlijning met beheerdersbeheer. * * Beheerder toegang beheren tot Matterbest in de systeemconsole met behulp van SAML-kenmerken.

SAML Single sign-on (Single Sign-On, SSO) zelf ondersteunt geen periodieke updates van gebruikerskenmerken of automatische deprovisioning. Er kan echter SAML met AD/LDAP-synchronisatie worden geconfigureerd om deze gebruiksvoorbeelden te ondersteunen.

Voor meer informatie over SAML, zie ` dit artikel van Varonis <https://www.varonis.com/blog/what-is-saml/> ` _, en ` dit conceptuele voorbeeld van DUO <https://duo.com/blog/the-beer-drinkers-guide-to-saml> ` _.

Matterbest ondersteunt officieel Okta, OneLogin en Microsoft ADFS als identiteitsproviders (IDPs), zie de links hieronder voor meer informatie over het configureren van SAML met deze providers.

 -` Okta SAML-configuratie <https://docs.mattermost.com/deployment/sso-saml-okta.html> ` _
 -` OneLogin SAML-configuratie <https://docs.mattermost.com/deployment/sso-saml-onelogin.html> ` _
 -` Microsoft ADFS SAML Configuration for Windows Server 2012 <https: //docs.mattermost.com/deployment/sso-saml-adfs.html#configure-saml-with-microsoft-adfs-for-windows-server-2012 > ` _
 -` Microsoft ADFS SAML Configuration for Windows Server 2016 <https://docs.mattermost.com/deployment/sso-saml-adfs-msws2016.html> ` _

Naast de officieel ondersteunde identiteitsproviders kunt u ook SAML configureren voor een aangepaste IdP. Klanten hebben bijvoorbeeld met succes Azure AD, DUO, PingFederate, Keycloak en SimpleSAMLphp als aangepaste IdPs ingesteld. Omdat we niet tegen deze identiteitsproviders testen, is het belangrijk dat u nieuwe versies van Matterbest in een stagingomgeving test om te bevestigen dat het werkt met uw identiteitsprovider. U kunt ook MFA instellen op uw SAML-provider voor extra beveiliging.

SAML-kenmerken gebruiken om rollen toe te passen
------------------------------------

U kunt kenmerken gebruiken om rollen toe te wijzen aan opgegeven gebruikers bij aanmelding. Voor toegang tot de SAML-kenmerkinstellingen navigeert u naar ** System Console > SAML 2.0 * *.

Gebruikersnaam Attri
bute
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

(Optioneel) Voer een SAML-bevestigingsfilter in om te gebruiken bij het zoeken naar gebruikers.

1. Navigeer naar ** Systeemconsole > Verificatie > SAML* *.
2. Vul het veld ** Username Attribute * * in.
3. Kies ** Save**.

Wanneer de gebruiker de Matterbest URL opent, loggen ze in met dezelfde gebruikersnaam en wachtwoord die ze gebruiken voor de organisatie logins.

Gastkenmerk
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Als deze optie is ingeschakeld, geeft het Guest Attribute in Matterbest de externe gebruikers aan waarvan de SAML-bevestiging gast is en die worden uitgenodigd om deel te nemen aan uw Mattertiste server. Deze gebruikers hebben de rol Gast onmiddellijk toegepast op eerste teken-in plaats van de standaard gebruikersrol lid. Hierdoor hoeft u de rol in de systeemconsole niet handmatig toe te wijzen.

Als een Mattermeeste Guest-gebruiker de gastrol heeft verwijderd in het SAML-systeem, worden deze niet automatisch door de synchronisatieprocessen naar een gebruikersrol van een lid bevorderd. Dit gebeurt handmatig via ** System Console > Gebruikersbeheer * *. Als een lid-gebruiker het gastkenmerk heeft toegevoegd, worden de gebruikersrol automatisch door de synchronisatieprocessen aan de gebruiker toegewezen.

1. Schakel Guest Access via ** System Console > SAML 2.0 * * in.
2. Navigeer naar ** Systeemconsole > Verificatie > SAML 2.0 * *.
3. Vul het veld Guest Attribute in.
4. Kies ** Save**.

Wanneer een gast zich aanmeldt voor de eerste keer worden ze gepresenteerd met een standaard landingspagina totdat ze worden toegevoegd aan kanalen.

Zie de ` Guest Accounts documentation <https://docs.mattermost.com/deployment/guest-accounts.html> ` _ voor meer informatie over deze functie.

Beheerderskenmerk
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

(Optioneel) Het kenmerk in de SAML-verklaring voor het aanduiden van systeembeheerders. De gebruikers die door de query zijn geselecteerd, hebben toegang tot uw Mattermeeste server als systeembeheerders. Systeembeheerders hebben standaard toegang tot de meest overeenkomende systeemconsole.

Bestaande leden die door dit kenmerk worden aangegeven, worden bij eerstvolgende aanmelding gepromoveerd van sectie naar Systeembeheer. De volgende aanmelding is gebaseerd op sessielengtes in ** Systeemconsole > SessieLengten * *. Het wordt aanbevolen dat gebruikers handmatig worden gedegradeerd naar leden in ** Systeemconsole > Gebruikersbeheer * * om ervoor te zorgen dat de toegang onmiddellijk wordt beperkt.

1. Navigeer naar ** Systeemconsole > Verificatie > SAML 2.0 * *.
2. Instellen ** Beheerkenmerk inschakelen * * naar ** true**.
3. Voltooi het veld ** Beheerkenmerk * *.
4. Kies ** Save**.

** Note:** Als het Admin-kenmerk is ingesteld op ` ` false ` ` is de rol van de lid als System Admin behouden. Als het kenmerk echter wordt verwijderd/gewijzigd, worden de systeembeheerders die via het kenmerk zijn gepromoveerd, gedegradeerd tot leden en behouden ze geen toegang tot de systeemconsole. Als dit kenmerk niet in gebruik is, kunnen de systeembeheerders handmatig worden gepromoveerd/gedegradeerd in ** Systeemconsole > Gebruikersbeheer * *.

Configuratiehulp
-------------------------

Wij staan open voor hulp bij het configureren van uw eigen IdP door het beantwoorden van de meest technische configuratievragen en het werken met uw IdP-provider ter ondersteuning van het oplossen van problemen, aangezien deze betrekking hebben op de Mattermeeste SAML-configuratie-instellingen. Wij kunnen echter niet garanderen dat uw verbinding met Matterbest zal werken.

Als u wilt helpen bij het ophalen van een gebruikersbestand voor uw aangepaste IdP, raadpleegt u deze ` documentatie <https://github.com/icelander/mattermost_generate_user_file> ` _.

Voor technische documentatie over SAML, zie ' SAML Single-Sign-On: Technical Documentation <https://docs.mattermost.com/cloud/cloud-administration/saml-technical.html> ` _.

Houd er rekening mee dat we misschien niet in staat zijn om te garanderen dat uw verbinding zal werken met Matterbest, maar we zullen overwegen verbeteringen aan onze functie als we in staat zijn. U kunt meer informatie vinden over het verkrijgen van ondersteuning ` hier <https://mattermost.com/support/> ` _ en aanvragen indienen voor officiële ondersteuning van een bepaalde provider op ons ` feature idea forum <https://mattermost.uservoice.com> ` _.
