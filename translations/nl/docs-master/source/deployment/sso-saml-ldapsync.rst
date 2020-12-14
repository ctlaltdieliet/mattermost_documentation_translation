SAML-synchronisatie met AD/LDAP configureren
------------------------------------------------------

Naast het configureren van SAML-aanmelding kunt u ook de synchronisatie van SAML-accounts met AD/LDAP configureren. Wanneer geconfigureerd:

 -Matterendste query's AD/LDAP voor relevante accountgegevens en SAML-accounts bijgewerkt op basis van wijzigingen in kenmerken (voornaam, achternaam en roepnaam)
 -Accounts uitgeschakeld in AD/LDAP worden in Matterbest inactief gemaakt en hun actieve sessies worden ingetrokken zodra Mattermore de kenmerken synchroniseert.

SAML-synchronisatie met AD/LDAP configureren:

1. Ga naar ** System Console > Authentication > SAML 2.0 * * (or ** System Console > SAML* * in versions prior to 5.12) and set ** Enable Synchronizing SAML Accounts With AD/LDAP* * to ` true ` `.
2. Ga naar ** System Console > Authentication > AD/LDAP* * (or ** System Console > AD/LDAP* * in versions prior to 5.12) en set ** Enable Synchronization with AD/LDAP* * to ` ` true ` `.
3. Stel de rest van de AD/LDAP-instellingen in op basis van ` configuration settings documentation <https: //docs.mattermost.com/administration/config-settings.html#ad-ldap> ` __ om Matterbest met uw AD/LDAP-server te verbinden.

 -Als u de AD/LDAP-aanmelding niet wilt inschakelen, houd dan ** Inteken inschakelen met AD/LDAP* * als ` ` false ` `.

4. Instellen ** Syncroniseringsinterval * * om op te geven hoe vaak Matterbest SAML-gebruikersaccounts synchroniseert met AD/LDAP. De standaardinstelling is 60 minuten. Als u onmiddellijk na het uitschakelen van een account wilt synchroniseren, gebruikt u de knop "AD/LDAP Synchronize Now" in ** Systeemconsole > AD/LDAP* * in eerdere versies of ** Systeemconsole * * > ** Authenticatie** > ** AD/LDAP* * in versies na 5.12.
5. Om Matterbest met succes te testen op uw AD/LDAP-server, klikt u op de knop ** AD/LDAP Test * *.

Als de synchronisatie met AD/LDAP is ingeschakeld, worden gebruikerskenmerken gesynchroniseerd met AD/LDAP op basis van hun e-mailadres. Als een gebruiker met een bepaald e-mailadres geen AD/LDAP-account heeft, worden deze in Matterbest gedeactiveerd op de volgende AD/LDAP-synchronisatie. Om het account opnieuw te activeren:

1. Voeg de gebruiker toe aan uw AD/LDAP-server.
2. Alle caches in Matterbest gebruiken in ** Systeemconsole > Webserver > Alle Caches * * (of ** Systeemconsole > Configuratie > Alle Caches * * in versies ouder dan 5.12).
3. AD/LDAP-synchronisatie uitvoeren in ** System Console > Authentication > AD/LDAP > AD/LDAP Synchronize Now * * (of ** System Console > AD/LDAP > AD/LDAP Synchronize Now * * in versies ouder dan 5.12).
4. Alle caches opnieuw opschonen in Matterbest in ** Systeemconsole > Webserver > Alle Caches * * (of ** Systeemconsole > Configuratie > Alle Caches * * in versies ouder dan 5.12 verwijderen), waardoor de account in Matterbest opnieuw wordt geactiveerd.

  .. opmerking:
    Als een gebruiker wordt gedeactiveerd van AD/LDAP, worden deze in Matterbest gedeactiveerd op de volgende synchronisatie. Ze worden weergegeven als "Inactief" in de lijst van gebruikers van de systeemconsole, alle sessies zullen verlopen en ze kunnen zich niet aanmelden bij Matterbest.

    Als een gebruiker is gedeactiveerd van SAML, zal hun sessie niet vervallen tot ze gedeactiveerd zijn van AD/L
DAP. Maar ze zullen niet in staat zijn om zich terug te melden bij Matterbest.

  .. opmerking:
    SAML-synchronisatie met AD/LDAP is ontworpen voor het ophalen van gebruikerskenmerken zoals de voornaam en de achternaam van uw AD/LDAP, en niet om de verificatie te controleren.

    Het gebruikersfilter kan met name niet worden gebruikt om te bepalen wie zich bij Matterbest kan aanmelden, dit moet worden bestuurd door de groepsmachtigingen van uw SAML-serviceprovider.

Zie :ref: ` technische beschrijving van SAML-synchronisatie met AD/LDAP <sso-saml-technical>` voor meer informatie.

SAML-gegevens overschrijven met AD/LDAP-gegevens
~ ~ ~ ~ > ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden ~ ~ ~ ~

U kunt ook kiezen voor het overschrijven van SAML-bindgegevens met AD/LDAP-gegevens. Voor meer informatie over het binden van een gebruiker met het SAML ID-kenmerk, raadpleegt u deze ` documentation <https: //docs.mattermost.com/deployment/sso-saml-okta.html#bind-authentication-to-id-attribute-in-plaats-of-email> ` __.

Dit proces overschrijft SAML-e-mailadres met AD/LDAP-e-mailadresgegevens of SAML-ID-kenmerk met AD/LDAP-ID-kenmerk indien geconfigureerd. We raden u aan deze configuratie met het SAML ID-kenmerk te gebruiken om ervoor te zorgen dat nieuwe gebruikers niet worden gemaakt wanneer het e-mailadres voor een gebruiker wordt gewijzigd.

Om ervoor te zorgen dat bestaande gebruikersaccounts in dit proces niet worden uitgeschakeld, moet u ervoor zorgen dat de SAML-ID's overeenkomen met de LDAP-ID's, door gegevens uit beide systemen te exporteren en de ID-gegevens te vergelijken. Het toewijzen van ID-kenmerken voor zowel AD/LDAP als SAML binnen Matterbest tot velden die dezelfde gegevens bevatten, zorgt ervoor dat de ID's ook overeenkomen.

1. Stel de SAML ` ` Id Attribute ` ` on ** System Console > Authentication > SAML 2.0 * * > ** Id Attribute * * (of ** System Console > SAML > Id Attribute * * in versies ouder dan 5.12)
2. Set ** System Console > Authentication > SAML 2.0 > Override SAML bind data with AD/LDAP information * * (or ** System Console > SAML > Override SAML bind data with AD/LDAP information * * in versions prior to 5.12) to ` ` true ` `.
3. Set ** System Console * * > ** Authentication** > ** SAML 2.0 * * > ** Enable Synchronizing SAML Accounts With AD/LDAP* * (or ** System Console > SAML > Enable Synchronizing SAML Accounts With AD/LDAP* * in versions prior to 5.12) naar ` true ` `.
4. Voer de AD/LDAP-synchronisatie uit in ** System Console > Authentication > AD/LDAP > AD/LDAP Synchronize Now * * (of ** System Console > AD/LDAP > AD/LDAP Synchronize Now * * in versies ouder dan 5.12).
