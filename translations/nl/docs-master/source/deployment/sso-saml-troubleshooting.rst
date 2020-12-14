Problemen oplossen
---------------

Het volgende is het oplossen van problemen met betrekking tot veelvoorkomende foutmeldingen en problemen.

1. Kan niet overschakelen naar SAML-verificatie met succes

  Zorg er eerst voor dat u de ` XML Security Library <https://www.aleksey.com/xmlsec/download.html> ` __ op uw Matterste-instance hebt geïnstalleerd en dat ** het beschikbaar is in uw * * PATH.

  Ten tweede, zorg ervoor dat u elke stap van de SAML-configuratie hebt voltooid.

Als u nog steeds problemen hebt met de configuratie, raadpleeg dan verdere informatie over het oplossen van problemen of voel je vrij om te posten in ons ` Troubleshooting forum <https://mattermost.org/troubleshoot/> ` __ en we zullen blij zijn om te helpen met problemen tijdens de installatie.

2. Systeembeheerder sluit zichzelf op uit het systeem

  Als de systeembeheerder tijdens het SAML-configuratieproces buiten het systeem is vergrendeld, kunnen ze een bestaand account instellen op Systeembeheerder met behulp van ' een opdrachtregeltool <https: //docs.mattermost.com/deployment/on-boarding.html#creating-system-administrator-account-from-commandline> ` __.

3. Ontvangen foutbericht: ` Een account met die gebruikersnaam bestaat al. Neem contact op met de beheerder. ".

  Dit betekent meestal dat een bestaand account een andere verificatiemethode heeft ingeschakeld. Als dit het geval is, moet de gebruiker zich aanmelden met die methode (zoals e-mail en wachtwoord) en vervolgens hun aanmeldmethode wijzigen in SAML via ** Account Settings > Security > Sign-in method * *.

  Dit foutbericht kan ook worden ontvangen als het ` Username Attribute ` van hun SAML-legitimatiegegevens niet overeenkomt met de gebruikersnaam van hun Mattermeeste account. Als dit het geval is, kan de gebruiker het kenmerk bij hun ID-provider bijwerken (bijvoorbeeld terug naar de oude waarde als het eerder is bijgewerkt).

4. Fout ontvangen bericht: ` Een account met die e-mail bestaat al. Neem contact op met de beheerder. ".

  Dit betekent meestal dat een bestaand account een andere verificatiemethode heeft ingeschakeld. Als dit het geval is, moet de gebruiker zich aanmelden met die methode (zoals e-mail en wachtwoord) en vervolgens hun aanmeldmethode wijzigen in SAML via ** Account Settings > Security > Sign-in method * *.

  Dit foutbericht kan ook worden ontvangen als het 'E-mailkenmerk' van de SAML-legitimatiegegevens niet overeenkomt met het e-mailadres van hun Mattermeeste-account. Als dit het geval is, kan de gebruiker het kenmerk bij hun ID-provider bijwerken (bijvoorbeeld terug naar de oude waarde als het eerder is bijgewerkt).

5. Ontvangen foutbericht: ` SAML-aanmelding is mislukt omdat een van de kenmerken onjuist is. Neem contact op met de systeembeheerder. ".

  Controleer of alle kenmerken, inclusief 'Email Attribute' en 'Username Attribute', correct zijn in zowel de Identity Provider-configuratie als in ** System Console > SAML* *.
