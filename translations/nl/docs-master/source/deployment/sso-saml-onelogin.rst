SAML configureren met OneLogin
== == == == == == == == == == == == == == =

Het volgende proces biedt stappen om SAML 2.0 te configureren met OneLogin voor Matterbest. .. Inhoud:
  :backlinks: boven: lokaal: .. include:: sso-saml-before-you-begin.rst

Een OneLogin Connection-app maken voor Mattermeest SSO ---------------------------------------------------

1. Voeg een SAML-testconnector-app toe.
  a. Meld u aan bij OneLogin als beheerder.
  b. Ga naar ** Apps > Apps toevoegen * *.
  c. Zoek naar "SAML Test Connector" en kies ** SAML Test Connector (IdP) w/encrypt**.

  .. image:: ../ ../source/images/onelogin_1_new_app.png

  d. In het veld * * Weergavenaam * * geeft u een naam op voor de toepassing en uploadt u het pictogram van een app. U kunt het Matterbest-logo gebruiken voor het pictogram, dat u kunt downloaden van ` Branding Guidelines <https://mattermost.org/brand-guidelines/> ` __ pagina.

  .. image:: ../ ../source/images/onelogin_2_basic_configuration.png

  e. Zorg ervoor dat de optie ** Zichtbaar in portal * * is ingeschakeld.
  f. Klik op ** Save**.

2. Configureer de app.
  a. Selecteer het tabblad ** Configuration** en voer de volgende waarden in:
    -** Recipient**: ` ` https: //<your-mattermost-url>/login/sso/saml ` ` where ` ` https: //<your-mattermost-url>` ` moet meestal overeenkomen met de ` Matterbest Site URL <https: //docs.mattermost.com/administration/config-settings.html#site-url> ` __.
    -** ACS (Consumer) URL Validator * *: ` ` https: \/ \/<your-mattermost-url>\/login \/sso \/saml ` `
    -** ACS (Consumer) URL* *: ` ` https: //<your-mattermost-url>/login/sso/saml ` `

  .. image:: ../ ../source/images/onelogin_3_configuration_1.png

  b. Plak de openbare sleutel die u eerder hebt gegenereerd in het veld ** SAML-versleuteling * *.

  .. image:: ../ ../source/images/onelogin_4_configuration_2.png

  c. Kies ** Save**.

3. Voer de kenmerkparameters in.

  Kenmerkparameters toewijzen kenmerken tussen OneLogin en Matterbest. Voor meer informatie over de configureerbare kenmerken, raadpleegt u onze :ref: ` documentatie over SAML-configuratie-instellingen <saml-enterprise>`.

  De kenmerken *E-mail * en *Username * zijn vereist. Voor Mattermeeste servers met versie 3.3 en eerder zijn ook de kenmerken *FirstName * en *LastName * vereist.

  a. Selecteer het tabblad ** Parameters**.
  b. Selecteer ** Parameter toevoegen * *.

  .. image:: ../ ../source/images/onelogin_5_parameters_add.png

  c. Geef in het veld ** Veldnaam * * een kenmerkparameter op zoals ` ` Email ` `.
  d. Selecteer de optie ** Opnemen in SAML-bevestiging * *.
  e. Kies ** Save**.

  .. image:: ../ ../source/images/onelogin_6_parameters_add_2.png

  f. Kies ** Edit**.
  g. Selecteer in het veld ** Value** de OneLogin-waarde die overeenkomt met de kenmerkparameter.

  .. image:: ../ ../source/images/onelogin_7_parameters_add_3.png

  h. Herhaal stap b tot en met g om het kenmerk *Username * en alle andere kenmerken toe te voegen die u nodig hebt.

    Nadat u alle kenmerken hebt toegevoegd die u wilt gebruiken, moet de parameterlijst lijken op de volgende afbeelding:

    .. image:: ../ ../source/images/onelogin_8_parameters_add_4.png

4. Kopieer de SSO
informatie.
  a. Selecteer het tabblad **SSO* *.
  b. Kopieer de waarden in de velden ** Issuer URL* * and ** SAML 2.0 Endpoint (HTTP) * * en sla ze op voor gebruik.

  .. image:: ../ ../source/images/onelogin_9_sso.png

  c. Klik op ** Details weergeven * * om het X.509-certificaat te bekijken.
  d. Zorg ervoor dat de optie ** X .509 PEM* * is geselecteerd in de vervolgkeuzelijst.

  .. image:: ../ ../source/images/onelogin_10_sso_certificate.png

  e. Klik op **DOWNLOAD* * en sla het bestand op in een handige locatie voor later gebruik.
5. Sla al uw wijzigingen op.

SAML-aanmelding configureren voor Matterbest --------------------------------------

1. Start Matterendste server en meld u aan bij Matterbest als systeembeheerder. Ga naar ** Systeemconsole > Verificatie > SAML* *.
  a. Plak in het veld ** SAML SSO URL* * de waarde voor het OneLogin *SAML 2.0 Endpoint (HTTP) * dat u eerder hebt gekopieerd.
  b. Plak in het veld ** Identity Provider Issuer URL* * de waarde voor het OneLogin *Issuer URL* dat u eerder hebt gekopieerd.
  c. Upload in het veld ** Identity Provider Public Certificate * * het bestand OneLogin X.509 PEM dat u eerder hebt gedownload.

  .. image:: ../ ../source/images/okta_10_mattermost_basics.PNG

2. Configureer Matterbest om de handtekening te controleren.
  a. Klik in het veld ** Handtekening controleren * * op ** True**.
  b. In de publicatie ** Service Provider Login URL* * typt u ` ` https//<your-mattermost-url>/login/sso/saml ` `.

  .. image:: ../ ../source/images/okta_11_mattermost_verification.PNG

3. Configureer Matterbest om SAML-aanvragen te ondertekenen met behulp van de Serviceverlener Private Key.

4. Schakel versleuteling in.
  a. Klik in het veld ** Versleuteling inschakelen * * op ** True**.
  b. Upload de persoonlijke sleutel die u eerder hebt gegenereerd in het veld ** Service Provider Private Key * *.
  c. Upload in het veld ** Service Provider Public Certificate * * de openbare sleutel die u eerder hebt gegenereerd.

  .. image:: ../ ../source/images/okta_12_mattermost_encryption.PNG

5. Stel kenmerken in voor de SAML Assertions, die worden gebruikt voor het bijwerken van gebruikersgegevens in Matterbest.

  Het veld ** Email Atttribute * * en het veld ** Username Attribute * * zijn verplicht en moeten overeenkomen met de waarden die u eerder hebt opgegeven toen u de SAML-testconnector op OneLogin hebt geconfigureerd.

  Voor Mattermeeste servers met versie 3.3 en eerder zijn ook de kenmerken *FirstName * en *LastName * vereist.

  .. image:: ../ ../source/images/okta_13_mattermost_attributes.PNG

6. (Optioneel) Pas de tekst van de aanmeldknop aan.

7. Klik op ** Save**.

8. (Optioneel) Als u First Name Attribute en Last Name Attribute hebt geconfigureerd, ga dan naar ** System Console > Site Configuration > Users and Teams * * (or ** System Console > General > Users and Teams * in versions prior to 5.12) and set ** Teammate Name Display * * to *Show first and achternaam *. Dit wordt aanbevolen voor een betere gebruikerservaring.

Om te bevestigen dat SAML SSO met succes is ingeschakeld, schakelt u uw systeembeheerdersaccount uit van e-mail naar SAML-verificatie via ** Account Settings > General > Sign-in Method > Switch to SAML SSO* * en meld u aan met uw SAML-legitimatiegegevens om de switch te voltooien.

Het wordt ook aanbevolen om een mededeling te posten aan gebruikers waarin wordt aangegeven hoe de migratie zal werken.

U kunt SAML ook configureren voor OneLogin door ` `config.json ` ` te bewerken om SAML in te schakelen gebaseerd op :ref: ` SAML configuratie-instellingen <saml-enterprise>`. U moet de Mattermost server opnieuw starten om de wijzigingen te activeren. .. include:: sso-saml-ldapsync.rst .. include:: sso-saml-faq.rst
