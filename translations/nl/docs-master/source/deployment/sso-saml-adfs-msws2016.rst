SAML configureren met Microsoft ADFS met Microsoft Windows Server 2016
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

Dit document bevat stappen voor het configureren van SAML 2.0 met Microsoft ADFS voor Mattermost en Microsoft Windows Server 2016. .. Inhoud:
  :backlinks: boven: lokaal: .. include:: sso-saml-before-you-begin.rst

Vereisten
-------------------------
 -Een Active Directory-instance waarin alle gebruikers de kenmerken e-mail en gebruikersnaam hebben opgegeven. Voor Mattermost servers die worden uitgevoerd op 3.3 en eerder, moeten gebruikers ook hun voornaam en achternaam kenmerken opgegeven hebben.
 -Een actieve Microsoft Server. De screenshots gebruikt in deze gids zijn van Microsoft Server 2012R2, maar soortgelijke stappen moet werken voor andere versies.
 -Een SSL certificaat om uw ADFS login pagina te tekenen.
 -ADFS geïnstalleerd op uw Microsoft Server. U vindt een gedetailleerde handleiding voor het in gebruik nemen en configureren van ADFS in ` dit artikel <https://msdn.microsoft.com/en-us/library/gg188612.aspx> ` __.

Open op uw ADFS-installatie de ADFS-console. Selecteer ** Service** en vervolgens ** Eindpunten **. Zoek in de kolom ** Type** naar ` ` SAML 2.0/WS-Federation`` en nok de waarde van ** URL Path * * kolom. Dit staat ook bekend als het ** SAML SSO URL-eindpunt * * in deze handleiding. Als u de standaardinstellingen voor de installatie hebt gekozen, wordt dit ` ` /adfs/ls ` `.

Een vertrouwensrelatie toevoegen -------------------------

1. Open de ADFS management snap-in en selecteer ** AD FS > Vertrouwende Partij Trusts > Add Vertrouwend Party Trust * * op de rechter zijbalk. U kunt ook met de rechtermuisknop klikken op ** Vertrouwende Party Trusts * * en kies ** Relying Party Trust * toevoegen uit het contextmenu.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_add-new-vertrouwend-party-trust_000.png

2. In het scherm ** Welcome** van de configuratiewizard kiest u ** Claims bewust * * en selecteert u ** Start**.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_add-new-trust-party-trust_001.png

3. Kies in het venster ** Gegevensbron selecteren * * de optie ** Geef gegevens op over de vertrouwende partij * *.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_add-new-vertrouwend-party-trust_002.png

4. In het scherm ** Geef weergavenaam op * * op in een * * Weergavenaam * * (bijv. ` ` Matterbest ` `). U kunt optionele notities toevoegen.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_add-new-vertrouwend-party-trust_003.png

5. Laat in het venster ** Certificaat configureren * * de certificaatinstellingen op hun standaardwaarden staan.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_add-new-vertrouwend-party-trust_004.png

Als u versleuteling wilt instellen voor uw SAML-verbinding, selecteert u ** Browse** en uploadt u het openbare certificaat van de serviceprovider.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_add-new-vertrouwend-party-trust_005.png

6. In het venster ** Configure URL* * selecteert u ** Enable Support for the SAML 2.0 WebSSO protocol * * en typt u de ** SAML 2.0 SSO service URL* * in de volgende indeling: ` ` https: //<your-mattermost-url>/login/sso/saml ` ` where ` ` ` ` moet meestal overeenkomen met de ` Matterbest Site URL <https: //docs.mattermost.com/administr
ation/config-settings.html#site-url> ` __.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_add-new-vertrouwend-party-trust_006.png

7. Geef in het scherm ** Configure Identifiers * * het ID van de "Relying Party Trust" * * op. Geeft aan welke claims worden aangevraagd. De notatie ** SAML 2.0 SSO-service URL* * moet ` ` https: //<your-mattermost-url>/login/sso/saml ` zijn, waarbij ` ``` ` overeenkomt met uw ` Matterbest Site-URL <https: //docs.mattermost.com/administration/config-settings.html#site-url> ` _. Kies vervolgens ** Next**. 

	.. image:: ../ ../source/images/SSO-SAML-ADFS_add-new-vertrouwend-party-trust_007.png

	.. image:: ../ ../source/images/SSO-SAML-ADFS_add-new-vertrouwend-party-trust_008.png

Deze tekenreeks moet overeenkomen met de tekenreeks ** Service Provider Identifier * *. Voor meer informatie over het ID van de Relying Party en hoe prefixovereenkomsten worden toegepast, zie ` deze documentatie <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/technical-reference/how-uris-are-used-in-ad-fs> ` _.

Voeg uw ** SAML 2.0 SSO-service URL* * van boven dezelfde manier toe.

8. In het scherm ** Kies toegangscontrole beleid * * selecteert u het toegangsbesturingsbeleid dat geschikt is voor uw omgeving. Deze handleiding gaat uit van de standaardwaarden ** Iedereen * * en een niet-geselecteerd vak.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_add-new-vertrouwend-party-trust_009.png

9. In het scherm ** Ready to Add Trust * * kunt u uw instellingen bekijken.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_add-new-vertrouwend-party-trust_010.png

10. In het scherm ** Finish** select ** Configure claims issuance policy for this application * * and then ** Close**.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_add-new-vertrouwend-party-trust_011.png

Claimregels maken ------------------

1. In het tabblad ** Issuance Transform Rules * * van de editor ** Claim Rules * *, kiest u ** Regel toevoegen ... * *.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_create-claim-rules_001.png

2. In het venster ** Kies regeltype * * selecteert u ** LDAP-kenmerken verzenden als claims * * in het vervolgkeuzemenu en vervolgens op ** Next**.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_create-claim-rules_002.png

3. Geef in het venster ** Claim-regel configureren * * een ** Claim-regelnaam * * van uw keuze op, selecteer ** Active Directory * * als ** Kenmerkbestand * * en voeg de volgende toewijzing toe:
  -In de LDAP-kenmerkkolom ** select** ` ` E-Mail-Adressen ` `. Van het type uitgaand claimtype, ** type** ` ` E-mail ` `
  -In de LDAP-kenmerkenkolom ** select** ` ` Given-Name ` `. Van het type Uitgaande Claim, ** type** ` ` FirstName ` `
  -In de LDAP-kenmerkenkolom ** select** ` ` Surname ` `. Van het type uitgaand claimtype, ** type** ` ` LastName ` `
  -In de LDAP-kenmerkenkolom ** select** ` ` SAM-Account-Name ` `. Van het type uitgaand claimtype, ** type** ` ` Gebruikersnaam ` `

Voor Matterste 3.4 en hoger zijn de kenmerken *FirstName * en *LastName * optioneel.

Selecteer ** Finish** om de regel toe te voegen.

De items in de kolom ** Uitgaande Claim Type * * kunnen worden gewijzigd en de items kunnen streepjes maar geen spaties bevatten. Deze worden gebruikt om de corresponderende velden in Matterbest toe te wijzen.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_create-claim-rules_003.png

4. Selecteer ** Regel toevoegen * * om een nieuwe regel te maken.

5. In het venster ** Kies regeltype * * selecteert u ** Transform een inkomende Claim * * in het vervolgkeuzemenu en klikt u op ** Next**.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_create-claim-rules_004.png

6. Voer in het venster ** Claim-regel configureren * * een ** Claim-regelnaam * * van uw keuze in.
  -Selecteer *Naam ID* voor het type ** Inkomende claim * *
  -Selecteer *Unspecified * voor de notatie ** Inkomende naam-ID * *
  -Selecteer *E-Mail Address * for the ** Outgoing claim type * *

Selecteer de optie ** Pass door alle claimwaarden * * en klik op ** Finish**.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_create-claim-rules_005.png

7. Klik op ** Finish** om de claimregel te maken, en vervolgens **OK* * om het maken van regels af te ronden.

8. Open Windows PowerShell als beheerder en voer de volgende opdracht uit:

  ` ` Set-ADFSRelyingPartyTrust -TargetName <display-name> -SamlResponseSignature "MessageAndAssertion" ` `

waarbij *<display-name>* de naam is die u hebt opgegeven in stap 4 van *Add a Relying Party Trust *. In ons voorbeeld is het ` ` matterit ` ` `.

Met deze actie wordt de handtekening toegevoegd aan SAML-berichten, waardoor verificatie is geslaagd.

Certificaat van ID-provider exporteren
-------------------------------------

Vervolgens exporteren we het certificaat van de identiteitsprovider, dat later wordt geüpload naar Matterbest om de SAML-configuratie af te ronden.

1. Open de ADFS management snap-in, selecteer ** AD FS > Service > Certificaten * * en dubbelklik op het certificaat onder ** Token-signing**. U kunt ook met de rechtermuisknop op het veld klikken en in het contextmenu op ** Certificaat bekijken * * klikken.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_export-id-provider-cert_001.png

2. In het scherm ** Certificate** opent u het tabblad ** Details**, selecteer ** Kopiëren naar bestand * * en vervolgens **OK* *.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_export-id-provider-cert_003.png

3. Klik in het venster ** Certificate Export Wizard * * op ** Next**.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_export-id-provider-cert_004.png

	Selecteer vervolgens de optie ** Base-64 gecodeerde X.509 (.CER) * * en klik nogmaals op ** Next**.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_export-id-provider-cert_005.png

4. Klik in het scherm ** Certificate Export Wizard * * op ** Browse** om de locatie op te geven van het ID van het ID-providercertificaat dat moet worden geëxporteerd, en geef de bestandsnaam op.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_export-id-provider-cert_006.png

5. Klik op ** Save**. In het venster ** Certificate Export Wizard * * controleert u of het pad correct is en klikt u op ** Next**.

6. Klik in het venster ** De wizard Certificaat exporteren * *, klik op ** Finish** en vervolgens op **OK* * om te bevestigen dat de export is geslaagd.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_export-id-provider-cert_007.png

SAML-aanmelding configureren voor Matterbest
--------------------------------------

Maak een metagegevens-URL door "FederationMetadata/2007-06/FederationMetadata.xml" toe te voegen aan de root-URL van de ADF
S-server, bijvoorbeeld: ` ` https: //<adfs.domain.com>/federationmetadata/2007-06/FederationMetadata.xml> ` ` ` `.

Start vervolgens Mattermeeste server en meld u aan bij Matterbest als systeembeheerder. Ga naar ** System Console > Authentication > SAML* *, plak de metagegevens-URL in het veld ** Identity Provider Metadata URL* * en selecteer ** Get SAML Metadata from IdP* *.

Hiermee worden de velden ** SAML SSO URL* * en het veld ** Identity Provider Issuer URL* * automatisch ingevuld en wordt het Public Certificate van de ID-provider ook gedownload van de server en lokaal ingesteld.

U kunt de volgende velden selecteren:
  -Instellen ** Inloggen inschakelen met SAML 2.0 * * naar ` ` true ` ` `.
  -Set ** Enable Synchronizing SAML Accounts With AD/LDAP* * to suit your environment.
  -Instellen ** overschrijven van SAML-bindgegevens met AD/LDAP-informatie * * voor uw omgeving.

Als u niet van plan bent een metagegevens-URL te gebruiken, kunt u de volgende velden handmatig opgeven:
  -Voor ** SAML SSO URL* * gebruikt u de ` ` SAML 2.0/W-Federation URL ADFS Endpoint ` ` die u aan het begin van het proces hebt gekopieerd.
  -Voor ** Identity Provider Issuer URL* * gebruikt u het ` ` Relying party trust identifier ` ` van ADFS.
  -Voor ** Identity Provider Public Certificate * * gebruikt u het ` ` X.509-openbaar certificaat ` `.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_configure-saml_001.png

2. Configureer Matterbest om de handtekening te controleren.
  -Set ** Controleer Handtekening * * naar ` ` true ` ` `.
  -Voor ** Service Provider Login URL* * gebruikt u de ` ` SAML 2.0 SSO-service-URL ` ` die u hebt opgegeven in ADFS.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_configure-saml_002.png

3. Schakel versleuteling in.
  -Instellen ** Schakel versleuteling * * in op ` ` true ` `.
  -Voor ** Service Provider Private Key * * gebruikt u de Service Provider Private Key die bij het starten van dit proces is gegenereerd.
  -Voor ** Serviceverlener Public Certificate * * gebruikt u het openbaar certificaat van de serviceprovider dat u aan het begin van dit proces hebt gegenereerd.
  -Stel ** Sign Request * * in om uw omgeving aan te passen.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_configure-saml_003.png

4. Stel kenmerken in voor de SAML Assertions, die worden gebruikt voor het bijwerken van gebruikersgegevens in Matterbest. Kenmerken voor e-mail en gebruikersnaam zijn vereist en moeten overeenkomen met de waarden die u eerder hebt opgegeven in ADFS. Zie :ref: ` documentatie over SAML configuratie-instellingen <saml-enterprise>` voor meer informatie.

Voor Mattermeeste servers die worden uitgevoerd op 3.3 en eerder, zijn de kenmerken voor de voornaam en de achternaam ook vereist.

	.. image:: ../ ../source/images/SSO-SAML-ADFS_configure-saml_004.png

5. Klik op ** Save**.

6. (Optioneel) Als u First Name Attribute and Last Name Attribute hebt geconfigureerd, ga dan naar ** System Console > Site Configuration > Users and Teams * * (or ** System Console > General > Users and Teams * in versions prior to 5.12) and set ** Teammate Name Display * * to ** Show first and achternaam * *. Dit wordt aanbevolen voor een betere gebruikerservaring.

Je bent klaar! Als u wilt bevestigen dat SAML SSO is ingeschakeld, schakelt u het systeembeheerdersaccount uit van e-mail naar SAML-verificatie via ** Account Settings > General > Sign-in Method > Switch to SAML SSO* * en meld u aan met uw SAML-legitimatiegegevens om de switch te voltooien.

Het is ook aanbevolen om een aankondiging te plaatsen over hoe de migratie zal werken aan gebruikers.

U kunt SAML ook configureren voor ADFS door ` `config.json ` ` te bewerken om SAML in te schakelen op basis van :ref: ` SAML configuratie-instellingen <saml-enterprise>`. U moet de Mattermost server opnieuw starten om de wijzigingen van kracht te laten worden. .. include:: sso-saml-faq.rst .. include:: sso-saml-ldapsync.rst
