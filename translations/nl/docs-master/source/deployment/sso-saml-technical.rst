== == == == == == == == == == == == == == == == == == == == == == == == == == = SAML Single-Sign-On (E20): Technische Documentatie
== == == == == == == == == == == == == == == == == == == == == == == == == == = .. _sso-saml-technisch:

Security Assertion Markup Language (SAML) is een open standaard waarmee identiteitsproviders (IdP), net als OneLogin, legitimatiegegevens kunnen doorgeven aan serviceproviders (SP), zoals Matterbest.

In eenvoudigere termen betekent dit dat u een set legitimatiegegevens kunt gebruiken om u aan te melden bij veel verschillende sites. Met een SAML identity provider account, kunt u inloggen op Mattermeeste en andere sites veilig met dezelfde account.

Het belangrijkste voordeel is dat het helpt beheerders te centraliseren gebruikersbeheer door te bepalen welke sites gebruikers toegang hebben tot met hun SAML identity provider referenties.

Vanaf v5.20 ondersteunt Mattermeeste met behulp van een enkele metagegevens-URL om configuratiegegevens voor de ID-provider op te halen met behulp van uw SSO-URL voor het genereren van een IdP-metagegevens-URL. Het XML-bestand voor de IdP-metagegevens bevat het IdP-certificaat, het entiteits-ID, de omleidings-URL en de afmeldings-URL. 

Met behulp van deze URL wordt de SAML SSO-URL en de URL-velden van de ID-provider automatisch in het configuratieproces gevuld en wordt het Public Certificate van de ID-provider ook gedownload van de server en lokaal ingesteld. 

Dit wordt momenteel ondersteund voor Okta en Microsoft ADFS server 2012 en 2016. OneLogin-ondersteuning wordt in een toekomstige release toegevoegd. 

Voor gedetailleerde stappen bekijkt u de :doc: ` SAML configureren met Okta <sso-saml-okta>`, :doc: ` SAML configureren met Microsoft ADFS voor Windows Server 2012 <sso-saml-adfs>`, en :doc: ` SAML configureren met Microsoft ADFS met Microsoft Windows Server 2016 <sso-saml-adfs-msws2016>` documentatie. 

... Inhoud:
  :backlinks: boven: lokaal:

SAML-providers
------------------------------------------------------

** Identity Providers (IdP) * *: Een identiteitsprovider voert de verificatie uit. Wanneer een gebruiker klikt om zich aan te melden, bevestigt de ID-provider wie de gebruiker is, en stuurt hij gegevens naar de serviceprovider met de juiste machtiging om toegang te krijgen tot de site.

*Examples*: OneLogin, Okta, Microsoft Active Directory (ADFS) of Azure.

** Service Providers (SP) * *: Een serviceprovider krijgt verificatie-en machtigingsinformatie van een IdP. Eenmaal ontvangen, geeft het de gebruiker toegang tot het systeem en logt de gebruiker in.

*Examples*: Matterbest, Zendesk, Zoom, Salesforce.

SAML-aanvraag (AuthNRequest)
------------------------------------------------------

Wanneer Matterbest een SP-geïnitieerde SAML-opdrachtstroom initieert, wordt er een binding (** HTTP-Redirect**) gegenereerd aan de IdP die een XML-payload bevat als een base64-reeks. code-blok :: geen

 BM441nuRIzjZ4L4xngbgbgbgbgjdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdqbdq

AuthNRequests kan ook worden ondertekend door Matterbest in v5.14 en later, in welk geval de XML-payload vergelijkbaar is met: .. code-block :: XML

  <samlp :AuthnRequest xmlns:samlp="urn:oasis: namen: tc: SAML:2.0 :protocol " xmlns: sam
l="urn:oasis: namen: tc: SAML:2.0 :assertion "xmlns:samlsig="https: //www.w3.org/2000/09/xmldsig#" ID="_u5mpjadp1fdozfih4cj8ap4brh" Version="2.0 "ProtocolBinding="urn:oasis:names:tc: SAML:2.0 :bindings:HTTP-POST" AssertionConsumerServiceURL="http://localhost: 8065/login/sso/saml " IssueInstant=" 2019-06-08T16:00:31Z">
      <saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">https://www.okta.com/exkoxukx1D8OIfY03356</saml:Issuer>
      <samlsig:Signature Id="Signature1">
          <samlsig:SignedInfo>
              <samlsig :CanonicalizationMethod Algorithm="https://www.w3.org/2001/10/xml-exc-c14n#"></samlsig:CanonicalizationMethod>
              <samlsig:SignatureMethod Algorithm="https://www.w3.org/2000/09/xmldsig#rsa-sha1"></samlsig:SignatureMethod>
              <samlsig:Reference URI="#_u5mpjadp1fdozfih4cj8ap4brh">
                  <samlsig:Transforms>
                      <samlsig:Transform Algorithm="https://www.w3.org/2000/09/xmldsig#enveloped-signature"></samlsig:Transform>
                  </samlsig:Transforms>
                  <samlsig:DigestMethod Algorithm="https://www.w3.org/2000/09/xmldsig#sha1"></samlsig:DigestMethod>
                  <samlsig:DigestValue></samlsig:DigestValue>
              </samlsig:Reference>
          </samlsig:SignedInfo>
          <samlsig:SignatureValue></samlsig:SignatureValue>
          <samlsig:KeyInfo>
              <samlsig:X509Data>
                  <samlsig:X509Certificate>MIIFmzCCA4OgAwIBAgIJAIusvV3gZIwiMA0GCSqGSIb3DQEBCwUAMGIxCzAJBgNVBAYTXvIEFsdG8xEzARBgNVBAoMCk1hdHRlcm1vc3QxDzANBgcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcvcbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbdvcvcvcvcvcvcvcvcvcvcbtbtbtbtbdvcvcvcvcvcbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbbtb0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0cT8rPsjowzjtjowzjtbddbjtbddbjt1bddbjt1bddbjt1bdgbbbdgbgbgbdgbgbgbgbgbgbgbgcbbbddbbbddbbbddbbbddbbbddbbbddbbbbddbbbbddbbbbddbbbbddbbbbddbbbbddbbbbddbbbbddbbbbddbbbbbddbbbbddbbbbbddbbbbddbbbbbddbbbbbddbbbbbbbbbbddbbbbbddbbbbbbbbbddbbbbbbbbbbddbbbbbbbbbd2bbbbbbbbd2bbbbbbd2bbbbbbbd2bbbbbbbbbd2bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbd0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0bb0b0b0b0R + cycgx0aMrWZoyzOzP7NCTM5MNE41C48xeGviyCtUID4xiBow + xo6IDUaiCoUVjhz579ore8ic70a19DD0qHy4SpBvrUwcbkgn6HjYlLC/k8nF9W9WlgbU61Jv3q4kZxxq4kZxxq4kedGH-FgbbgbgbgcvbgbgbgcgcgcvbgbgbgbgcgcgcgcgcvbgbWbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbbtbbtbbtbtbtbtb0b1Owg4bfd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0blbdbd0blbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbd0bdbdbdbdbdbdbdbd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bd0bdbdbd0bd0bd0bd0bd0bdbd0bd0bdbdbd0bd0bd0bd0bd0bd0bd0bdbdbd0bd0bd0bd0bd0bdbd0bd0bd0bd0bd0bdbd0bd0bdbdbd0bd0bd0bd0bd0bdbd0bd0bdbd0bd0bdbdbd0bd0bdbd0bd0bdoCWfdi + WyBQJGWcIp2OTC1XyWHv7JsY3lo04 + </samlp:AuthnRequest></samlsig:KeyInfo>
      </samlp:AuthnRequest></samlp:AuthnRequest></samlp:AuthnRequest>

SAML-antwoorden
------------------------------------------------------------

Er zijn verschillende typen SAML-responsen die door de IdP naar de SP worden verzonden. De respons bevat de bevestiging met het NameID en de kenmerken van een gebruiker.

Hieronder vindt u een overzicht van de verschillende soorten reacties. Elk responstype wordt volledig ondersteund, behalve wanneer de SAML-bevestiging wordt ondertekend terwijl de SAML-respons zelf niet is: .. csv-table ::
    :header: "Signed SAML Response", "Signed SAML Assertion", "Encrypted SAML Assertion", "Ondersteund door Matterbest"

    "Ja", "Ja", "Ja", "Ja"
    "Ja", "Ja", "Nee", "Ja"
    "Ja", "Nee", "Ja", "Ja"
    "Ja", "Nee", "Nee", "Ja"
    "Nee", "Ja", "Ja", "Gedeeltelijk, validatie van bevestiging handtekening wordt niet ondersteund"
    "Nee", "Ja", "Nee", "Gedeeltelijk, validatie van bevestiging handtekening wordt niet ondersteund"
    "Nee", "Nee", "Ja", "Ja"
    "Nee", "Nee", "Nee", "Ja"

Zie voor voorbeeld XML-antwoorden voor elk type, zie de ` OneLogin SAML response voorbeelden <https://www.samltool.com/generic_sso_res.php> ` _.

Technische beschrijving van SAML-synchronisatie met AD/LDAP
------------------------------------------------------------

Als deze optie is ingeschakeld, treedt SAML-synchronisatie met AD/LDAP in fasen op:

1. Alle huidige LDAP-gebruikers ophalen uit de Matterbest-database met ` `Users.AuthService ` ` ingesteld op ` ` ldap ` `. Dit is een SQL-query die is opgegeven voor de Matterbest-database: ` ` SELECT * FROM Users WHERE AuthService = 'ldap ' ` `.
2. Alle huidige SAML-gebruikers ophalen uit de Matterendste database met ` `Users.AuthService ` ` ingesteld op ` ` saml ` ` `. Dit is een SQL-query die is opgegeven voor de Matterbest-database: ` ` SELECT * FROM Users WHERE AuthService = 'saml ' ` `.
3. Haal alle huidige LDAP-gebruikers van de LDAP-server zoals gedefinieerd door ` `LdapSettings.UserFilter ` `. Dit is een ` LDAP-query <https://github.com/mattermost/mattermost-server/blob/master/scripts/ldap-check.sh> ' __ die wordt opgegeven voor de LDAP-server. Gebruikers worden opgehaald in batches zoals gedefinieerd door ` `LdapSettings.MaxPageSize ` `.
4. LDAP-kenmerken bijwerken. Probeer voor elke bestaande Mattermeeste-gebruiker die is opgehaald in stap 1 een overeenkomst te vinden met de lijst van LDAP-gebruikers uit stap 3. Om overeenkomsten te vinden, wordt het veld 'Users.AuthData' 'van de Mattermeeste gebruiker vergeleken met de LDAP-instelling' ` 'LdapSettings.IdAttribute'.

 -Als een kenmerk van de gebruiker is gewijzigd, wordt dat kenmerk gekopieerd van de LDAP-server en wordt de gebruiker gemarkeerd als bijgewerkt.
 -Als het corresponderende ` `LdapSettings.IdAttribute ` ` niet wordt gevonden, wordt verondersteld dat de gebruiker wordt verwijderd van de LDAP-server, en gedeactiveerd van Matterbest door instelling
het veld ` `Users.DeleteAt ` ` op een geldige tijdsaanduiding.

5. SAML-kenmerken bijwerken. Probeer voor elke bestaande Mattermeeste-gebruiker die is opgehaald in stap 2 een overeenkomst te vinden met de lijst van LDAP-gebruikers uit stap 3. Om overeenkomsten te vinden, wordt " `SamlSettings.Email ` ` vergeleken met de LDAP-instelling ` ` ` LdapSettings.EmailAttribute ` `.

 -Als een kenmerk van de gebruiker is gewijzigd, wordt dat kenmerk gekopieerd van de LDAP-server en wordt de gebruiker gemarkeerd als bijgewerkt.
 -Als het corresponderende ` `LdapSettings.EmailAttribute ` ` niet wordt gevonden, wordt de gebruiker verondersteld te worden verwijderd van de LDAP-server en gedeactiveerd van Matterbest door het veld ` `Users.DeleteAt ` ` in te stellen op een geldige tijdsaanduiding.

Veelgestelde vragen
------------------------------------------------------------

Hoe kan ik een XML-bestand voor SAML-metagegevens verkrijgen dat door Matterbest wordt geconsumeerd?
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

U kunt het XML-bestand verkrijgen door het API Mattermeest RESTful API aan te roepen op ` ` /api/v4/saml/metadata ` `.

Voor andere nuttige SAML API-aanroepen raadpleegt u de ` API reference <https: //api.mattermost.com/#tag/SAML> ` _.
