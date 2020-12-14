E-mailsjablonen
== == == == == == == =

Mattermeeste heeft een paar e-mailsjablonen die worden verzonden wanneer een specifieke gebeurtenis optreedt.
Het grootste deel van de tijd dat deze sjablonen niet hoeven te worden gewijzigd.
In het geval dat aanvullende wijzigingen nodig zijn, worden alle beschikbare props in elke e-mail hieronder vermeld.
Het veld 'Inhoud' geeft een korte beschrijving van de prop. Controleer de i18n strings voor de exacte formulering.

De e-mailsjablonen bevinden zich in de directory Mattermeeste in de map ` ` templates ` `.
De bijbehorende tekenreeksen voor elke prop zijn te vinden in de map ` ` i18n ` `. 

... Opmerking:
  De props tussen verschillende e-mailsjablonen zijn niet interchangbaar zonder extra servercodewijzigingen.  

... waarschuwing:
  Wijzigingen die zijn aangebracht binnen de ` ` templates ` ` ` of ` ` i18n ` ` map kunnen tijdens een server update overschreven worden. Zorg ervoor dat ze dienovereenkomstig worden aangepast.


Beschikbare sjablonen
-------------------

E-mailvoettekst
~ ~ ~ ~ nopen ~ ~

** Purpose**:
Dit wordt toegevoegd aan alle uitgaande e-mails die door Matterbest worden verzonden. ** Props**: + -------------- + ------------------------------ + ----------------------------------- +
| Prop | Content | i18n String | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = +
| Voettekst | Bericht intro | api.templates.email_footer | + -------------- + ------------------------------ + ----------------------------------- +
| Organisatie | Naam van organisatie | api.templates.email_organization | + -------------- + ------------------------------ + ----------------------------------- +
| EmailInfo1 | Eerste regel van voettekst | api.templates.email_info1 | + -------------- + ------------------------------ + ----------------------------------- +
| EmailInfo2 | Tweede regel van voettekst | api.templates.email_info2 | + -------------- + ------------------------------ + ----------------------------------- +
| EmailInfo3 | Third line of footer | api.templates.email_info3 | + -------------- + ------------------------------ + ----------------------------------- +
| SupportEmail | E-mail voor Mattermeeste ondersteuning | -- |
+ -------------- + ------------------------------ + ----------------------------------- +


SendChangeUsernameEmail
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Purpose**:
Verzonden naar de gebruiker wanneer de gebruikersnaam is gewijzigd.

** Body Props * *: + --------- + ------------------------------ + -------------------------------------------- +
| Prop | Content | i18n String | + == == == == = + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
| SiteURL | URL van de meest overeenkomende server | -- | + --------- + ------------------------------ + -------------------------------------------- +
| Titel | Beristekop | api.templates.username_change_body.title |
+ --------- + ------------------------------ + ---------------------------------------
----- +
| Info | Message body | api.templates.username_change_body.info | + --------- + ------------------------------ + -------------------------------------------- +
| Waarschuwing | Waarschuwingstekst | api.templates.email_warning |
+ --------- + ------------------------------ + -------------------------------------------- +


SendEmailChangeVerifyEmail
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Purpose**:
Wordt verzonden naar de gebruiker als er een e-mailwijziging is aangevraagd. Bevat verificatie-link en -knop.

** Body Props * *: + -------------- + ------------------------------- + -------------------------------------------------- +
| prop | Content | i18n String | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
| SiteURL | URL van de meest overeenkomende server | -- | + -------------- + ------------------------------- + -------------------------------------------------- +
| Titel | Berichtkop | api.templates.email_change_verify_body.title | + -------------- + ------------------------------- + -------------------------------------------------- +
| Info | Message body | api.templates.email_change_verify_body.info | + -------------- + ------------------------------- + -------------------------------------------------- +
| VerifyUrl | URL voor e-mailverificatie | -- | + -------------- + ------------------------------- + -------------------------------------------------- +
| VerifyButton | Knop voor e-mailverificatie | api.templates.email_change_verify_body.button |
+ -------------- + ------------------------------- + -------------------------------------------------- +


SendEmailChangeEmail
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Purpose**:
Wordt verzonden naar de gebruiker wanneer e-mail is gewijzigd.

** Body Props * *: + --------- + ------------------------------ + ----------------------------------------- +
| Prop | Content | i18n String | + == == == == = + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = +
| SiteURL | URL van de meest overeenkomende server | -- | + --------- + ------------------------------ + ----------------------------------------- +
| Titel | Berichtkop | api.templates.email_change_body.title | + --------- + ------------------------------ + ----------------------------------------- +
| Info | Berichttekst | api.templates.email_change_body.info | + --------- + ------------------------------ + ----------------------------------------- +
| Waarschuwing | Waarschuwingstekst | api.templates.email_warning |
+ --------- + ------------------------------ + ----------------------------------------- +


SendVerifyEmail
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Purpose**:
Verzonden naar de gebruiker bij het maken van de account om het e-mailadres te verifiëren.

** Body Props * *: + ----------- + ------------------------------ + ----------------------------------- +
| Prop | Content | i18n String | + == == == == == = + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = +
| SiteURL | URL van de meest overeenkomende server | -- | + ----------- + ------------------------------ + ----------------------------------- +
| Titel | Berichtkop | api.templates.verify_body.title | + ----------- + ------------------------------ + ----------------------------------- +
| Info | Message body | api.templates.verify_body.info | + ----------- + ------------------------------ + ----------------------------------- +
| VerifyUrl | URL voor e-mailverificatie | -- | + ----------- + ------------------------------ + ----------------------------------- +
| Knop | Knop voor e-mailververering | api.templates.verify_body.button |
+ ----------- + ------------------------------ + ----------------------------------- +


SendSignInChangeEmail
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Purpose**:
Naar de gebruiker verzonden wanneer de aanmeldingsmethode is gewijzigd (d.w.z. van e-mail naar LDAP, enz.)

** Body Props * *: + --------- + ------------------------------ + ------------------------------------------------ +
| Prop | Content | i18n String | + == == == == = + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
| SiteURL | URL van de meest overeenkomende server | -- | + --------- + ------------------------------ + ------------------------------------------------ +
| Titel | Berichtkop | api.templates.signin_change_email.body.title | + --------- + ------------------------------ + ------------------------------------------------ +
| Info | Berichttekst | api.templates.signin_change_email.body.info | + --------- + ------------------------------ + ------------------------------------------------ +
| Waarschuwing | Waarschuwingstekst | api.templates.email_warning |
+ --------- + ------------------------------ + ------------------------------------------------ +


SendWelcomeEmail
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Purpose**:
Wordt verzonden naar de gebruiker als het account is gemaakt. Kan ook downloaden links naar Apps en e-mail controle links bevatten.

** Body Props * *: + ----------------- + ------------------------------ + ------------------------------------------------- +
| Prop | Content | i18n String | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = +
| SiteURL | URL van de meest overeenkomende server | -- | + ----------------- + ------------------------------ + ------------------------------------------------- +
| Titel | Berichtkop | api.templates.welcome_body.tit
le | + ----------------- + ------------------------------ + ------------------------------------------------- +
| Info | Berichtcorpus | api.templates.welcome_body.info | + ----------------- + ------------------------------ + ------------------------------------------------- +
| Knop | Knop voor bevestiging | api.templates.welcome_body.button | + ----------------- + ------------------------------ + ------------------------------------------------- +
| Info2 | Voortzetting van berichttekst | api.templates.welcome_body.info2 | + ----------------- + ------------------------------ + ------------------------------------------------- +
| Info3 | Voortzetting van berichttekst | api.templates.welcome_body.info3 |
+ ----------------- + ------------------------------ + ------------------------------------------------- +


** Optioneel Props * *: + ----------------- + ------------------------------ + ------------------------------------------------- +
| Prop | Content | i18n String | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = +
| AppDownloadInfo | Info for App Downloads | api.templates.welcome_body.app_download_info | + ----------------- + ------------------------------ + ------------------------------------------------- +
| AppDownloadLink | Download link for Apps | -- | + ----------------- + ------------------------------ + ------------------------------------------------- +
| VerifyUrl | Link voor verificatie | -- |
+ ----------------- + ------------------------------ + ------------------------------------------------- +


SendPasswordChangeEmail
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Purpose**:
Wordt verzonden naar de gebruiker wanneer het wachtwoord is gewijzigd.

** Body Props * *: + --------- + ------------------------------ + -------------------------------------------- +
| Prop | Content | i18n String | + == == == == = + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
| SiteURL | URL van de meest overeenkomende server | -- | + --------- + ------------------------------ + -------------------------------------------- +
| Titel | Berichtkop | api.templates.password_change_body.title | + --------- + ------------------------------ + -------------------------------------------- +
| Info | Berichttekst | api.templates.password_change_body.info | + --------- + ------------------------------ + -------------------------------------------- +
| Waarschuwing | Waarschuwingstekst | api.templates.email_warning |
+ --------- + ------------------------------ + -------------------------------------------- +


SendAccessTokenEmail
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Purpose**:
Wordt verzonden naar de gebruiker als er een toegangstoken is toegevoegd aan het account.

** Body Props * *: + --------- + ------------------------------ + ----------------------------------------------- +
| Prop | Content | i18n String | + == == == == = + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = +
| SiteURL | URL van de meest overeenkomende server | -- | + --------- + ------------------------------ + ----------------------------------------------- +
| Titel | Berichtkop | api.templates.user_access_token_body.title | + --------- + ------------------------------ + ----------------------------------------------- +
| Info | Berichttekst | api.templates.user_access_token_body.info | + --------- + ------------------------------ + ----------------------------------------------- +
| Waarschuwing | Waarschuwingstekst | api.templates.email_warning |
+ --------- + ------------------------------ + ----------------------------------------------- +


SendPasswordResetEmail
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Purpose**:
Wordt verzonden naar de gebruiker wanneer een verzoek om een wachtwoord is gestart.

** Body Props * *: + ---------- + ------------------------------ + ---------------------------------- +
| Prop | Content | i18n String | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
| SiteURL | URL van de meest overeenkomende server | -- | + ---------- + ------------------------------ + ---------------------------------- +
| Titel | Berichtkop | api.templates.reset_body.title | + ---------- + ------------------------------ + ---------------------------------- +
| Info1 | Message body | api.templates.reset_body.info1 | + ---------- + ------------------------------ + ---------------------------------- +
| Info2 | Voortzetting van berichttekst | api.templates.reset_body.info2 | + ---------- + ------------------------------ + ---------------------------------- +
| Reseturl | URL om wachtwoord opnieuw in te stellen | -- | + ---------- + ------------------------------ + ---------------------------------- +
| Knop | Knop voor bevestiging | api.templates.reset_body.button |
+ ---------- + ------------------------------ + ---------------------------------- +


SendMfaChangeEmail
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Purpose**:
Wordt verzonden naar de gebruiker wanneer de verificatiemethode voor meerdere factoren is gewijzigd.

** Body Props when MFA is geactiveerd * *: + --------- + ------------------------------ + ------------------------------------------ +
| Prop | Content | i18n String | + == == == == = + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
| SiteURL | URL van de meest overeenkomende server | -- | + --------- + ------------------------------ + ------------------------------------------ +
| Titel | Berichtkop | api.templates.mfa_activated_body.title | + --------- + ------------------------------ + ------------------------------------------ +
| Info | Berichttekst | api.templates.mfa_activated_body.info | + --------- + ------------------------------ + ------------------------------------------ +
| Waarschuwing | Waarschuwingstekst | api.templates.email_warning |
+ --------- + ------------------------------ + ------------------------------------------ +


** Body Props wanneer MFA wordt gedeactiveerd * *: + --------- + ------------------------------ + -------------------------------------------- +
| Prop | Content | i18n String | + == == == == = + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
| SiteURL | URL van de meest overeenkomende server | -- | + --------- + ------------------------------ + -------------------------------------------- +
| Titel | Berichtkop | api.templates.mfa_deactivated_body.title | + --------- + ------------------------------ + -------------------------------------------- +
| Info | Berichttekst | api.templates.mfa_deactivated_body.info | + --------- + ------------------------------ + -------------------------------------------- +
| Waarschuwing | Waarschuwingstekst | api.templates.email_warning |
+ --------- + ------------------------------ + -------------------------------------------- +


SendDeactivateAccountEmail
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Purpose**:
Wordt verzonden naar de gebruiker als het account is gedeactiveerd.

** Body Props * *: + --------- + ------------------------------ + ---------------------------------------- +
| Prop | Content | i18n String | + == == == == = + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
| SiteURL | URL van de meest overeenkomende server | -- | + --------- + ------------------------------ + ---------------------------------------- +
| Titel | Berichtkop | api.templates.deactivate_body.title | + --------- + ------------------------------ + ---------------------------------------- +
| Info | Berichttekst | api.templates.deactivate_body.info | + --------- + ------------------------------ + ---------------------------------------- +
| Waarschuwing | Waarschuwingstekst | api.templates.deactivate_body.warning |
+ --------- + ------------------------------ + ---------------------------------------- +


SendInviteEmails
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Purpose**:
Wordt verzonden naar de gebruiker wanneer de uitnodiging voor het team via e-mail is gebruikt.

** Body Props * *: + ----------- + -------------------------------------------------------------------- + ---------------------------------------- +
| Prop | Content | i18n String |
+ == == == == = + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
== == == == == == == == == == == == == == == == == == == == == == ==
| SiteURL | URL van de meest overeenkomende server | -- | + ----------- + -------------------------------------------------------------------- + ---------------------------------------- +
| Titel | Berichtkop | api.templates.invite_body.title | + ----------- + -------------------------------------------------------------------- + ---------------------------------------- +
| Info1 | Message body | api.templates.invite_body.info | + ----------- + -------------------------------------------------------------------- + ---------------------------------------- +
| Knop | Knop voor bevestiging | api.templates.invite_body.button | + ----------- + -------------------------------------------------------------------- + ---------------------------------------- +
| Extrainfo | Aanvullende info over Matterbest | api.templates.invite_body.extra_info | + ----------- + -------------------------------------------------------------------- + ---------------------------------------- +
| TeamURL | URL voor het team waarvoor de gebruiker is uitgenodigd | -- | + ----------- + -------------------------------------------------------------------- + ---------------------------------------- +
| Link | URL voor team uitnodigen (niet te verwarren met TeamURL) | -- |
+ ----------- + -------------------------------------------------------------------- + ---------------------------------------- +


NotificationEmailBody
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

** Purpose**:
Verzonden naar de gebruiker als bericht voor nieuwe berichten of nieuwe vermeldingen.

** Body Props * *: + ---------- + ------------------------------ + --------------------------------- +
| Prop | Content | i18n String | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = +
| SiteURL | URL van de meest overeenkomende server | -- | + ---------- + ------------------------------ + --------------------------------- +
| Knop | Knop om te posten | api.templates.post_body.button | + ---------- + ------------------------------ + --------------------------------- +
| TeamLink | URL naar team | -- |
+ ---------- + ------------------------------ + --------------------------------- +


Deze e-mail kan veranderen afhankelijk van de instellingen en het type kanaal waarop de melding is verzonden.

** Voor groepskanalen * *:

** Met volledige berichtinhoud ingeschakeld * *: + ------------ + ------------------ + ------------------------------------------------- +
| Prop | Content | i18n String | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = +
| BodyText | intro Bericht | app.notification.body.intro.group_message.full | + ------------ + ------------------ + ------------------------------------------------- +
| Info1 | Kanaalnaam | app.notification.body.text.group_message.full | + ------------ + ------------------ + ------------------------------------------------- +
| Info2 | Berichtinhoud | app.notification.body.text.group_message.full2 | + ------------ + ------------------ + ------------------------------------------------- +
| SenderName | Naam van afzender | -- | + ------------ + ------------------ + ------------------------------------------------- + ** Without**: + ---------- + --------------- + ---------------------------------------------------- +
| Prop | Content | i18n String | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
| BodyText | intro van bericht | app.notification.body.intro.group_message.generic | + ---------- + --------------- + ---------------------------------------------------- +
| Info | Tijdaanduiding | app.notification.body.text.group_message.generic |
+ ---------- + --------------- + ---------------------------------------------------- +


** Voor directe berichten * *:

** Met volledige berichtinhoud ingeschakeld * *: + ------------ + --------------------------- + ----------------------------------------- +
| Prop | Content | i18n String | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = +
| BodyText | intro Bericht | app.notification.body.intro.direct.full | + ------------ + --------------------------- + ----------------------------------------- +
| Info1 | Leeg voor directe berichten | -- | + ------------ + --------------------------- + ----------------------------------------- +
| Info2 | Berichtinhoud | app.notification.body.text.direct.full | + ------------ + --------------------------- + ----------------------------------------- +
| SenderName | Naam van afzender | -- | + ------------ + --------------------------- + ----------------------------------------- + ** Without**: + ---------- + --------------- + -------------------------------------------- +
| Prop | Content | i18n String | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
| BodyText | intro Bericht | app.notification.body.intro.direct.generic | + ---------- + --------------- + -------------------------------------------- +
| Info | Timestamp | app.notification.body.text.direct.generic |
+ ---------- + --------------- + -------------------------------------------- +


** Notificaties **:

** Met volledige berichtinhoud ingeschakeld * *: + ------------ + ------------------ + ----------------------------------------------- +
| Prop | Content | i18n String | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = +
| BodyText | intro Bericht | app.notification.body.intro.notification.full | + ------------ + ------------------ + ----------------------------------------------- +
| Info1 | Kanaalnaam | app.notification.body.text.notification.full | + ------------ + ------------------ + ----------------------------------------------- +
| Info2 | Berichtinhoud | app.notification.body.text.notification.full2 | + ------------ + ------------------ + ----------------------------------------------- +
| SenderName | Naam van afzender | -- | + ------------ + ------------------ + ----------------------------------------------- + ** Without**: + ---------- + ------------------------------ + -------------------------------------------------- +
| Prop | Content | i18n String | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
| BodyText | URL van de Mattermeeste server | app.notification.body.intro.notification.generic | + ---------- + ------------------------------ + -------------------------------------------------- +
| Info | Berichtkop | app.notification.body.text.notification.generic |
+ ---------- + ------------------------------ + -------------------------------------------------- +
