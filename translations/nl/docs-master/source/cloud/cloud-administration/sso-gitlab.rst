GitLab Single Sign-On
== == == == == == == == == == =

Configureer Matterbest om GitLab te gebruiken als single Sign-on (SSO) service voor het aanmaken van het team, het maken van accounts en het aanmelden van gebruikers. .. Opmerking: Alleen de standaard GitLab SSO wordt officieel ondersteund. "Double SSO", waarbij GitLab SSO aan andere SSO-oplossingen wordt geketend, wordt niet ondersteund. Het kan mogelijk zijn om GitLab SSO te verbinden met AD, LDAP, SAML, of MFA add-ons in sommige gevallen, maar vanwege de speciale logica is vereist dat ze niet officieel worden ondersteund en zijn bekend om niet te werken aan sommige ervaringen. 


Stap 1: Voeg een OAuth-toepassing toe aan uw GitLab-account -------------------------------------------------------

1. Meld je aan bij je GitLab account en ga naar ` ` https: // { gitlab-site-name } /profile/applications ` `. For * { gitlab-site-name } * gebruik de naam van je GitLab instantie. Als je GitLab zelf gebruikt als je OAuth provider, gebruik dan * gitlab.com *.
2. Een nieuwe toepassing toevoegen:

  a. Typ *Matterbest * in het veld ** Name**.
  b. Voeg in het veld ** Redirect URI* * de volgende twee regels toe met behulp van uw eigen waarde voor * { matterbest-site-name } *.

    .. code-blok :: tekst

      https:// { matterbest-site-name } /login/gitlab/compleet
      https:// { mattermost-site-name } /signup/gitlab/complete

     Als uw GitLab-instance niet is ingesteld voor SSL, moeten uw URI's beginnen met ` ` http:// ` ` in plaats van ` ` https: // ` `.
  c. Selecteer geen opties onder ** Scopes**.

3. Klik op ** Save toepassing * *.

Houd het GitLab venster open omdat je het *Application Id * en *Secret * nodig hebt wanneer je Matterbest configureert.

Stap 2: Configureer Matterbest voor GitLab SSO -------------------------------------------------------

1. Navigeer naar ** Systeemconsole > Verificatie > OAuth 2.0 * *. Selecteer ` ` Gitlab ` ` in de *Select OAuth 2.0 service provider * dropdown en voeg andere verplichte velden toe. 2. Voeg het toepassings-ID toe. 3. Voeg de Toepassingsgeheime sleutel toe. 4. Voeg de Gitlab Sire URL toe. Als je GitLab subsysteem niet is ingesteld voor SSL, moeten de eindpunten beginnen met ` ` http:// ` ` in plaats van ` ` https: // ` `. Als je GitLab zelf gebruikt als je OAuth provider, gebruik dan * gitlab.com *.
5. Voeg de UserApiEndpoint toe. Gebruik ` ` https: // { gitlab-site-name } /api/v3/user ` ` als je GitLab v8.17.8 of eerder draait.
6. [ Optioneel] Om alle gebruikers te dwingen alleen SSO te ondertekenen, stelt u instellen ** Systeemconsole > Verificatie > E-mail > Inschakelen inschakelen met e-mail * * naar ` ` false ` ` `

Gebruikers moeten hun aanmeldingsmethode veranderen voordat ze kunnen aanmelden bij GitLab.
