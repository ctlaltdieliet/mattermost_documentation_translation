.. _auth_mfa:

Verificatie met meerdere factoren
== == == == == == == == == == == == == =

Verificatie met meerdere factoren (MFA) is een secundaire laag van gebruikersverificatie die wordt toegepast op uw Mattermeeste-server.

Als MFA is ingeschakeld, moeten gebruikers een beveiligde eentijdcode opgeven naast hun gebruikersnaam en wachtwoord om zich bij Matterbest aan te melden. MFA is handig in organisaties met specifieke beveiligings-en nalevingsbeleidsdefinities. Het kan ook worden gebruikt in organisaties waar Matterbest niet achter een firewall staat en geen toegang heeft tot bestaande MFA-infrastructuur.

Matterbest biedt een op smartphone gebaseerde MFA-controle naast email-password of Active Directory/LDAP-verificatie om zich aan te melden bij de Matterendste server.

Ondersteunde smartphones zijn iOS, Android, Blackberry en Windows Phone-apparaten die in staat zijn om ` Google Authenticator <https://support.google.com/accounts/answer/1066447?hl=en> ` __. Andere dan die internet toegang te downloaden en te installeren van Google Authenticator, de telefoon gebruikt voor Mattermeeste MFA vereist geen toegang tot internet. .. opmerking: Als de MFA-implementatie afhankelijk is van Time-based One-time-wachtwoorden (TOTP), zorgt u ervoor dat de systeemtijd van de server juist is. Als er een afwijking is, kunnen gebruikers zich niet met succes aanmelden.

MFA inschakelen
------------

Deze optie is ingeschakeld door de systeembeheerder in de ` System Console <https: //docs.mattermost.com/administration/config-settings.html#mfa> ` __ under ** Authentication > MFA > Enable Multi-factor Authentication * *. 

Als deze optie is ingeschakeld, kunnen gebruikers ervoor kiezen om MFA op hun account te gebruiken in de ` Accountinstellingen <https: //docs.mattermost.com/help/settings/account-settings.html#multi-factor-authentication> ` __ menu onder ** Security > Multi-factor Authentication * *.

Handhaving van de MFA (E10)
-------------------

Deze optie kan worden ingeschakeld door de systeembeheerder in de ` System Console <https: //docs.mattermost.com/administration/config-settings.html#mfa> ` __ onder ** Authentication > MFA > Enforce Multi-factor Authentication * *.

Wanneer de MFA-handhaving is ingesteld op ** true**, worden gebruikers met e-mail of LDAP-verificatie die geen MFA-set hebben ingesteld, doorgestuurd naar de configuratiepagina van MFA wanneer ze zich aanmelden bij Matterbest. Ze kunnen pas toegang krijgen tot de site als de MFA-installatie is voltooid. Nieuwe gebruikers zijn vereist om MFA in te stellen tijdens het aanmelden.

Gebruikers zullen niet in staat zijn om MFA te verwijderen van hun account terwijl de handhaving is op. .. Opmerking:

  Inschakelen van de MFA-handhaving voorkomt dat gebruikers toegang tot de site tot de installatie is voltooid. Het wordt aanbevolen om de handhaving in te schakelen tijdens niet-piekuren wanneer mensen minder waarschijnlijk Matterbest gebruiken.
