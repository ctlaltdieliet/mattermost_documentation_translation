GitLab Single Sign-On
== == == == == == == == == == =

Configureer Matterbest om GitLab te gebruiken als single sign-on (SSO) service voor het aanmaken van het team, het maken van accounts en het aanmelden van gebruikers. .. Opmerking: Alleen de standaard GitLab SSO wordt officieel ondersteund. "Double SSO", waarbij GitLab SSO aan andere SSO-oplossingen wordt geketend, wordt niet ondersteund. Het kan mogelijk zijn om GitLab SSO te verbinden met AD, LDAP, SAML, of MFA add-ons in sommige gevallen, maar vanwege de speciale logica is vereist dat ze niet officieel worden ondersteund en zijn bekend om niet te werken aan sommige ervaringen. Als u een officiële AD-, LDAP-, SAML-of MFA-ondersteuning voor uw bedrijf hebt, moet u de optie 'Mattermeest Enterprise Edition <https://mattermost.com/pricing/>' __ als een optie beschouwen. 


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

1. In Team Edition navigeert u naar ** System Console > Authentication > Gitlab * * of in Enterprise Edition naar ** System Console > Authentication > OAuth 2.0 * *. Selecteer ` ` Gitlab ` ` in de *Select OAuth 2.0 service provider * dropdown en voeg andere verplichte velden toe.  Als alternatief kunt u op uw Matterste-server het *Application Id * en het *Secret * toevoegen aan de sectie *GitLab * in het bestand ` `config.json ` `:

  a. Open ` `config.json ` ` als root in een teksteditor. Het is meestal in ` ` /opt/mattermost/config ` ` maar misschien elders op je systeem.
  b. Zoek de sectie *GitLabSettings * op en voeg de volgende informatie toe of wijzig deze:

    .. code-block :: javascript

      "GitLabSettings": {
          "Enable": true, "Secret": "{ matterbest-app-secret-from-gitlab }", "Id": "{ mattermost-app-application-id-from-gitlab }", "Scope": "", "AuthEndpoint": "https: // { gitlab-site-name } /oauth/machtigen", "TokenEndpoint": "https: // { gitlab-site-name } /oauth/token", "UserApiEndpoint": "https: // { gitlab-site-name } /api/v4/user"
      }

    Voor ` ` { gitlab-site-name } ` ` gebruik de naam van je GitLab instantie. Als uw GitLab-instance niet is ingesteld voor SSL, moeten de eindpunten beginnen met wit
h ` ` http:// ` ` in plaats van ` ` https: // ` `. Als je GitLab zelf gebruikt als je OAuth provider, gebruik dan * gitlab.com *. Voor ` ` UserApiEndpoint ` ` gebruik ` ` https: // { gitlab-site-name } /api/v3/user ` ` als je GitLab v8.17.8 of eerder draait.

2. [ Optioneel] Om alle gebruikers te dwingen alleen SSO te ondertekenen, stelt u instellen ** Systeemconsole > Verificatie > E-mail > Aanmelding inschakelen met e-mail * * naar ` ` false ` ` of in de sectie *EmailSettings * van ` `config.json ` ` set *EnableSignUpWithEmail * in op ` ` false ` ` `.  

3. Start uw Matterigste server opnieuw op.

  Op Ubuntu 14.04 en RHEL 6: ` ` sudo restart matterbest ` `

  Op Ubuntu 16.04 en RHEL 7: ` ` sudo systemctl restart matterbest ` `

Nadat de server opnieuw is gestart, moeten gebruikers hun aanmeldingsmethode wijzigen voordat ze kunnen aanmelden bij GitLab.
