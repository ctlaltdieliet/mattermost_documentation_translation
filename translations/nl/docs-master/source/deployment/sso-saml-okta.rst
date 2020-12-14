SAML configureren met Okta
== == == == == == == == == == == ==

Het volgende proces biedt stappen voor het configureren van SAML 2.0 met Okta voor Matterbest. .. Inhoud:
  :backlinks: boven: lokaal: .. include:: sso-saml-before-you-begin.rst

Een verbinding-app voor Mattermeest SSO instellen ------------------------------------------

1. Meld u aan bij Okta als beheerder.

2. Schakel over naar de ** Classic UI* *, met behulp van de drop-down in de linkerbovenhoek.

3. Ga naar ** Admin Dashboard > Toepassingen > Toepassing toevoegen * *.

4. Klik op ** Create New App * * en kies ** SAML 2.0 * * als teken op methode.

	.. image:: ../ ../source/images/okta_1_new_app.PNG

5. Enter ** Algemene instellingen * * voor de toepassing, inclusief ** App naam * * en ** App logo * * (optioneel). Het is raadzaam om het toepassingspictogram af te beelden op gebruikers, ook in de app Okta Mobile.

  Als u een Matterbest logo wilt gebruiken voor de toepassing, kunt u een ` op onze pagina downloaden <https://mattermost.org/brand-guidelines/> ` __.

	.. image:: ../ ../source/images/okta_2_general_settings.PNG

6. Enter ** SAML-instellingen * *, inclusief:
 -** Single teken op URL: ** ` ` https: //<your-mattermost-url>/login/sso/saml ` ` where ` ` https: //<your-mattermost-url>` ` moet meestal overeenkomen met de ` Matterbest Site URL <https: //docs.mattermost.com/administration/config-settings.html#site-url> ` __.
 -** Audience URI: ** Bijvoorbeeld ` ` matterit ` ` `
 -** Naam-ID-indeling: ** ` ` niet opgegeven ` `
 -** Toepassingsgebruikersnaam: ** ` ` E-mail ` `

	.. image:: ../ ../source/images/okta_3_initial_saml_settings.PNG

7. Voor het instellen van de versleuteling voor uw SAML-verbinding kiest u ** Geavanceerde instellingen afbeelden * *.

	.. image:: ../ ../source/images/okta_4_initial_saml_settings.PNG

8. Set ** Assertion Encryption * * as ** Encrypted** en upload het Service Provider Public Certificate dat u hebt gegenereerd in stap 2 naar het veld ** Encryption Certificate * *.

	.. image:: ../ ../source/images/okta_5_advanced_saml_settings.PNG

9. Voer kenmerkinstructies in, die worden gebruikt om kenmerken tussen Okta en Matterbest toe te wijzen. Voor meer informatie over de configureerbare kenmerken, raadpleegt u onze :ref: ` documentatie over de SAML-configuratie-instellingen <saml-enterprise>`. E-mail en gebruikersnaam attributen zijn vereist. Voor Mattermeeste servers die worden uitgevoerd 3.3 en eerder zijn ook de kenmerken voor de voornaam en de achternaam vereist.

	.. image:: ../ ../source/images/okta_6_attribute_statements.PNG

10. Klik op ** Next**. Stel vervolgens de parameters voor de Okta-ondersteuning in voor de toepassing. Aanbevolen instellingen:
 Ik ben een Okta klant die een interne app toevoegt * *
 Dit is een interne app die we gecreëerd hebben * *

	.. image:: ../ ../source/images/okta_7_support_configuration.PNG

11. Klik op ** Finish**. Klik op het volgende scherm op het tabblad ** Aanmelden * * en klik op ** Installatieinstructies bekijken * *.
  11.1 Selecteer de link ** Identity Provider metadata * * en kopieer de link vanuit de browser URL box. Dit wordt gebruikt tijdens de SAML-configuratiestappen in het volgende gedeelte. 

	.. image:: ../ ../source/images/okta_8_view_instructions.PNG

12. Let op ** Identity Provider Single Sign-On URL* * (ook bekend als ** SAML
SSO URL* *), en de Identity Provider Issuer, omdat beide nodig kunnen zijn om SAML voor Matterbest te configureren. Zorg er bovendien voor dat u het X.509-certificaatbestand downloadt en opslaat. Het kan nodig zijn om het te uploaden naar Matterbest in een latere stap.

	.. image:: ../ ../source/images/okta_9_view_instructions.PNG

SAML-aanmelding configureren voor Matterbest
--------------------------------------

Start de Mattermeeste server en meld u aan bij Matterbest als systeembeheerder. Ga naar ** System Console > Authentication > SAML* *, en plak de gekopieerde URL van de metagegevens van de ID-provider in het veld ** Identity Provider Metadata URL* * en selecteer ** Get SAML Metadata from IdP* *.

Hiermee worden de velden ** SAML SSO URL* * en het veld ** Identity Provider Issuer URL* * automatisch ingevuld en wordt het Public Certificate van de ID-provider ook gedownload van de server en lokaal ingesteld. 

U kunt ook de volgende velden handmatig invoeren:
 -** SAML SSO URL: ** ` ` Identity Provider Single Sign-On URL ` ` van Okta, eerder opgegeven.
 -** Identiteit Provider Uitgever URL: ** ` ` Identity Provider Issuer ` ` ` uit Okta, eerder opgegeven.
 -** Identity Provider Public Certificate: ** X.509 Openbaar certificaatbestand dat u hebt gedownload van Okta eerder. .. image:: ../ ../source/images/okta_10_mattermost_basics.PNG

2. Configureer Matterbest om de handtekening te controleren. De ** Service Provider Login URL* * is het ` ` Single-teken op URL ` ` dat u eerder in Okta hebt opgegeven.

	.. image:: ../ ../source/images/okta_11_mattermost_verification.PNG

3. Schakel versleuteling in op basis van de eerder gegeven parameters.

	.. image:: ../ ../source/images/okta_12_mattermost_encryption.PNG

4. Configureer Matterbest om SAML-aanvragen te ondertekenen met behulp van de Serviceverlener Private Key.

5. Stel kenmerken in voor de SAML Assertions, die worden gebruikt voor het bijwerken van gebruikersgegevens in Matterbest. Attributen voor e-mail en gebruikersnaam zijn vereist en moeten overeenkomen met de waarden die u eerder hebt ingevoerd in Okta. Zie :ref: ` documentatie over SAML configuratie-instellingen <saml-enterprise>` voor meer informatie.

Voor Mattermeeste servers die worden uitgevoerd op 3.3 en eerder, zijn de kenmerken voor de voornaam en de achternaam ook vereist.

	.. image:: ../ ../source/images/okta_13_mattermost_attributes.PNG

6. (Optioneel) Pas de tekst van de aanmeldknop aan.

	.. image:: ../ ../source/images/okta_14_mattermost_login_button.PNG

7. Klik op ** Save**.

8. (Optioneel) Als u First Name Attribute and Last Name Attribute hebt geconfigureerd, ga dan naar ** System Console * * > ** Site Configuration * * > ** Users and Teams * * (or ** System Console > General > Users and Teams * in versions prior to 5.12) and set ** Teammate Name Display * * to *Show first and achternaam *. Dit wordt aanbevolen voor een betere gebruikerservaring.

Eenmaal voltooid en om te bevestigen dat SAML SSO is ingeschakeld, kunt u het systeembeheerdersaccount overschakelen van e-mail naar SAML-verificatie via ** Account Settings > General > Sign-in Method > Switch to SAML SSO* * en meld u aan met uw SAML-legitimatiegegevens om de switch te voltooien.

Het is ook aanbevolen om een aankondiging te plaatsen voor uw gebruikers om uit te leggen hoe de migratie zal werken.

U kunt SAML ook configureren voor Okta door ` `config.json ` ` te bewerken om SAML in te schakelen op basis van :ref: ` SAML configuratie-instellingen <saml-enterprise>`. U moet de Mattermost server opnieuw starten om de wijzigingen van kracht te laten worden. .. include:: sso-saml-ldapsync.rst .. include:: sso-saml-faq.rst
