SAML configureren met Microsoft ADFS voor Windows Server 2012
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

Het volgende proces biedt stappen om SAML 2.0 te configureren met Microsoft ADFS voor Matterbest. .. Inhoud:
  :backlinks: boven: lokaal: .. include:: sso-saml-before-you-begin.rst

De volgende basisvereisten zijn voor het gebruik van ADFS voor Matterbest:
 -Een Active Directory-instance waarin alle gebruikers een opgegeven e-mailadres en gebruikersnaam hebben. Voor Mattermost servers die worden uitgevoerd op 3.3 en eerder, moeten gebruikers ook hun voornaam en achternaam kenmerken opgegeven hebben.
 -Een Microsoft Server draait. De screenshots gebruikt in deze gids zijn van Microsoft Server 2012R2, maar soortgelijke stappen moet werken voor andere versies.
 -Een SSL certificaat om uw ADFS login pagina te tekenen.
 -ADFS geïnstalleerd op uw Microsoft Server. U vindt een gedetailleerde handleiding voor het in gebruik nemen en configureren van ADFS in ` dit artikel <https://msdn.microsoft.com/en-us/library/gg188612.aspx> ` __.

Let op de ADFS-installatie op de waarde van de ** SAML 2.0/W-Federation URL* * in ADFS Endpoints sectie, ook bekend als het ** SAML SSO URL Endpoint * * in deze handleiding. Als u de standaardinstellingen voor de installatie hebt gekozen, wordt dit ` ` /adfs/ls/ ` `.

Een vertrouwensrelatie toevoegen -------------------------

1. Ga in ADFS management zijbalk naar ** AD FS > Trust Relationships > Vertrouwend Party Trusts * * en klik op ** Add Relying Party Trust * *.

	.. image:: ../ ../source/images/adfs_1_add_new_relying_party_trust.PNG

2. Een configuratiewizard voor het toevoegen van een nieuw vertrouwensvenster. Klik in het scherm ** Welcome** op ** Start**.

	.. image:: ../ ../source/images/adfs_2_start_wizard.PNG

3. Selecteer in het venster ** Gegevensbron selecteren * * de optie ** Geef gegevens op over de vertrouwende partij * *.

	.. image:: ../ ../source/images/adfs_3_select_data_source.PNG

4. In het scherm ** Geef weergavenaam op * * op, typt u een * * Weergavenaam * * om het vertrouwen te herkennen, zoals ` ` Matterbest ` ` en voeg eventuele opmerkingen toe die u wilt maken.

	.. image:: ../ ../source/images/adfs_4_specify_display_name.PNG

5. Selecteer in het venster ** Profiel kiezen * * de optie ** AD FS-profiel * *.

	.. image:: ../ ../source/images/adfs_5_choose_profile.PNG

6. Laat in het venster ** Certificaat configureren * * de certificaatinstellingen op hun standaardwaarden staan.

	.. image:: ../ ../source/images/adfs_6_configure_certificate_default.PNG

Als u echter versleuteling wilt instellen voor uw SAML-verbinding, klikt u op de knop ** Browse** en uploadt u het openbaar certificaat van de serviceprovider.

	.. image:: ../ ../source/images/adfs_7_configure_certificate_encryption.PNG

7. In het venster ** Configure URL* * selecteert u ** Enable Support for the SAML 2.0 WebSSO protocol * * en typt u de ** SAML 2.0 SSO service URL* *, vergelijkbaar met ` ` https: //<your-mattermost-url>/login/sso/saml ` ` where ` `<your-mattermost-url>` ` moet meestal overeenkomen met de ` Matterbest Site URL <https: //docs.mattermost.com/administration/config-settings.html#site-url> ` __.

	.. image:: ../ ../source/images/adfs_8_configure_url.PNG

8. In het ** Configureren-ID
entifiers * * screen, voer het ** Relying party trust identifier * * (ook bekend als de ** Identity Provider Issuer URL* *) in van het formulier ` ` https: //<your-idp-url>/adfs/services/trust ` ` en klik op ** Add**.

	.. image:: ../ ../source/images/adfs_9_configure_identifiers.PNG

9. In het scherm ** Configure Multi-factor Authentication Now * *, kunt u verificatie met meerdere factoren inschakelen, maar dit valt buiten het bereik van deze handleiding.

	.. image:: ../ ../source/images/adfs_10_configure_mfa.PNG

10. In het scherm ** Kies Uitgifte van beslissingsmachtiging * * selecteert u de optie ** Alle gebruikers toestaan om toegang te krijgen tot deze vertrouwende partij * *.

	.. image:: ../ ../source/images/adfs_11_authorization.PNG

11. In het scherm ** Ready to Add Trust * * kunt u uw instellingen bekijken.

	.. image:: ../ ../source/images/adfs_12_ready_to_add_trust.PNG

12. Selecteer in het scherm ** Finish** de optie ** Open het dialoogvenster Claim-regels bewerken voor deze vertrouwende partij bij het sluiten van de wizard * * en klik op ** Close**. U kunt nu de configuratiewizard afsluiten en de editor ** Claim Rules * * wordt geopend.

	.. image:: ../ ../source/images/adfs_13_finish_trust.PNG

Claimregels maken ------------------

1. Klik in de editor ** Issuance Transform Rules * * van de editor ** Claim Rules * * op de knop ** Regel toevoegen ... * *. Met deze actie wordt een wizard voor het toevoegen van een reactieregel voor transformatie (**) geopend.

	.. image:: ../ ../source/images/adfs_14_claim_rules_editor.PNG

2. In het venster ** Kies regeltype * * selecteert u ** LDAP-kenmerken verzenden als claims * * in het vervolgkeuzemenu en vervolgens op ** Next**.

	.. image:: ../ ../source/images/adfs_15_choose_rule_type.PNG

3. Voer in het venster ** Claim-regel configureren * * een ** Claim-regelnaam * * van uw keuze in, selecteer ** Active Directory * * als het ** Kenmerkbestand * * en doe het volgende:
  -In de kolom ** LDAP-kenmerk * * selecteert u ` ` E-Mail-Adressen ` `. Van het ** Uitgaande Claim Type * *, type ` ` E-mail ` ` `.
  -In de kolom ** LDAP-kenmerk * * selecteert u ` ` Given-Name ` `. Van het ** Uitgaande Claim Type * *, typ ` ` FirstName ` `.
  -In de kolom ** LDAP-kenmerk * * selecteert u ` ` Surname ` `. Van het ** Uitgaande Claim Type * *, type ` ` LastName ` `.
  -In de kolom ** LDAP-kenmerk * * selecteert u ` ` SAM-Account-Name ` `. Van het ** Uitgaande Claim Type * *, type ` ` Gebruikersnaam ` ` `.

Voor Matterste 3.4 en hoger zijn de kenmerken *FirstName * en *LastName * optioneel.

Klik vervolgens op ** Finish** om de regel toe te voegen.

Houd er rekening mee dat de items in de kolom ** Uitgaande Claim Type * * kunnen worden gekozen om iets anders te zijn. Ze kunnen streepjes bevatten, maar geen spaties. Merk op dat ze zullen worden gebruikt om de corresponderende velden in Mattermeest later in kaart te brengen.

	.. image:: ../ ../source/images/adfs_16_configure_claim_rule.PNG

4. Maak een nieuwe regel door te klikken op de knop ** Regel toevoegen * *.

5. In het venster ** Kies regeltype * * selecteert u ** Transform een inkomende Claim * * in het vervolgkeuzemenu en klikt u op ** Next**.

	.. image:: ../ ../source/images/adfs_17_transformation_of_incoming_claim.PNG

6. Voer in het venster ** Claim-regel configureren * * een ** Claim-regelnaam * * van uw keuze in.
  -Selecteer *Name ID* voor het type ** Inkomende claim * *.
  -Selecteer *Unspecified * voor de notatie ** Inkomende naam * *.
  -Selecteer *E-Mail Address * for the ** Outgoing claim type * *.

Selecteer bovendien de optie ** Pass door alle claimwaarden * * optie. Klik dan op ** Finish**.

	.. image:: ../ ../source/images/adfs_18_configure_incoming_claim.PNG

7. Klik op ** Finish** om de claimregel te maken, en vervolgens **OK* * om het maken van regels af te ronden.

8. Open Windows PowerShell als beheerder en voer de volgende opdracht uit:

  ` ` Set-ADFSRelyingPartyTrust -TargetName <display-name> -SamlResponseSignature "MessageAndAssertion" ` `

waarbij <display-name> de naam is die u hebt opgegeven in stap 7. In ons voorbeeld is het ` ` matterit ` ` `.

Met deze actie wordt de handtekening toegevoegd aan SAML-berichten, waardoor verificatie is geslaagd.

Certificaat van ID-provider exporteren
-------------------------------------

Vervolgens exporteren we het certificaat van de identiteitsprovider, dat later wordt geüpload naar Matterbest om de SAML-configuratie af te ronden.

1. In ADFS management zijbalk, ga naar ** AD FS > Service > Certificaten * * en dubbel klik op het certificaat onder ** Token-signing**. U kunt ook met de rechtermuisknop op het veld klikken en vervolgens op ** Certificaat bekijken * * klikken.

	.. image:: ../ ../source/images/adfs_19_export_idp_cert_start.PNG

2. Ga in het scherm ** Certificate** naar het tabblad ** Details** en klik op ** Kopiëren naar bestand * *, en vervolgens op **OK* *. Dit opent een ** Certificate Export Wizard * *.

	.. image:: ../../source/images/adfs_20_export_idp_cert_copy.PNG

3. Klik in het venster ** Certificate Export Wizard * * op ** Next**. Selecteer vervolgens de optie ** Base-64 gecodeerde X.509 (.CER) * * en klik nogmaals op ** Next**.

	.. image:: ../ ../source/images/adfs_21_export_idp_cert_wizard.PNG

4. Klik in het scherm ** Certificate Export Wizard * * op ** Browse** om de locatie op te geven van het ID van het ID-providercertificaat dat moet worden geëxporteerd, en geef de bestandsnaam op.

	.. image:: ../ ../source/images/adfs_21-2_export_idp_cert_wizard.PNG

5. Klik op ** Save**. In het venster ** Certificate Export Wizard * * controleert u of het pad correct is en klikt u op ** Next**.

6. Klik in het venster ** De wizard Certificaat exporteren * *, klik op ** Finish** en vervolgens op **OK* * om te bevestigen dat de export is geslaagd.

	.. image:: ../ ../source/images/adfs_21-3_export_idp_cert_wizard.PNG

SAML-aanmelding configureren voor Matterbest
--------------------------------------

Maak een metagegevens-URL door "FederationMetadata/2007-06/FederationMetadata.xml" toe te voegen aan de root-URL van de ADFS-server, bijvoorbeeld: ` ` https: //<adfs.domain.com>/federationmetadata/2007-06/FederationMetadata.xml> ` ` ` `.

Start vervolgens Mattermeeste server en meld u aan bij Matterbest als systeembeheerder. Ga naar ** System Console > Authentication > SAML* *, plak de metagegevens-URL in het veld ** Identity Provider Metadata URL* * en selecteer ** Get SAML Metadata from IdP* *.

Hiermee worden de velden ** SAML SSO URL* * en het veld ** Identity Provider Issuer URL* * automatisch ingevuld en wordt het Public Certificate van de ID-provider ook gedownload van de server en lokaal ingesteld.

U kunt ook de volgende velden handmatig invoeren:
  -** SAML SSO URL* *: ** SAML
2.0/W-Federatie URL* * ADFS-eindpunt dat u eerder hebt gekopieerd.
  -** ID provider emittent uRL* *: ` ` vertrouwend partijtrust-ID ` ` van ADFS die u eerder hebt opgegeven.
  -** Identity Provider Public Certificate * *: ` ` X.509-Public Certificate ` ` ` die u eerder hebt gedownload.

	.. image:: ../ ../source/images/adfs_22_mattermost_basics.PNG

2. Configureer Matterbest om de handtekening te controleren. De ** Service Provider Login URL* * is de SAML 2.0 SSO-service-URL die u eerder hebt opgegeven in ADFS.

	.. image:: ../ ../source/images/adfs_23_mattermost_verification.PNG

3. Schakel versleuteling in door de Service Provider Private Key en Service Provider Public Certificate te uploaden die u eerder hebt gegenereerd.

	.. image:: ../ ../source/images/adfs_24_mattermost_encryption.PNG

4. Configureer Matterbest om SAML-aanvragen te ondertekenen met behulp van de Serviceverlener Private Key.

5. Stel kenmerken in voor de SAML Assertions, die worden gebruikt voor het bijwerken van gebruikersgegevens in Matterbest. Kenmerken voor e-mail en gebruikersnaam zijn vereist en moeten overeenkomen met de waarden die u eerder hebt opgegeven in ADFS. Zie :ref: ` documentatie over SAML configuratie-instellingen <saml-enterprise>` voor meer informatie.

Voor Mattermeeste servers die worden uitgevoerd op 3.3 en eerder, zijn de kenmerken voor de voornaam en de achternaam ook vereist.

	.. image:: ../ ../source/images/adfs_25_mattermost_attributes.PNG

6. (Optioneel) Pas de tekst van de aanmeldknop aan.

  .. image:: ../ ../source/images/adfs_26_mattermost_login_button.PNG

7. Klik op ** Save**.

8. (Optioneel) Als u First Name Attribute en Last Name Attribute hebt geconfigureerd, ga dan naar ** System Console > Site Configuration > Users and Teams * * (or ** System Console > General > Users and Teams * in versions prior to 5.12) and set ** Teammate Name Display * * to ** Show first and achternaam * *. Dit wordt aanbevolen voor een betere gebruikerservaring.

Als u wilt bevestigen dat SAML SSO is ingeschakeld, schakelt u het systeembeheerdersaccount uit van e-mail naar SAML-verificatie via ** Account Settings > General > Sign-in Method > Switch to SAML SSO* * en meld u aan met uw SAML-legitimatiegegevens om de switch te voltooien.

Het is ook aanbevolen om een aankondiging te plaatsen over hoe de migratie zal werken aan gebruikers.

U kunt SAML ook configureren voor ADFS door ` `config.json ` ` te bewerken om SAML in te schakelen op basis van :ref: ` SAML configuratie-instellingen <saml-enterprise>`. U moet de Mattermost server opnieuw starten om de wijzigingen van kracht te laten worden. .. include:: sso-saml-ldapsync.rst .. include:: sso-saml-faq.rst
