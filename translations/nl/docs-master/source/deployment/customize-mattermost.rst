Matterbest aanpassen
== == == == == == == == == == ==

Er zijn verschillende manieren om uw Mattertiste server aan te passen. 

Als het aanpassen van Matterbest, vermijd branding die kan worden verward met de Mattermeest merk. Het is bijvoorbeeld goed om te merken als "Healthcare Central" omdat het een compleet ander merk is. "Mattermeest Healthcare Central" is niet in orde, omdat het mogelijk kan worden verward met het Mattermeest merk. Zie de ` Mattermeest trademark guidelines <https://mattermost.org/trademark-standards-of-use/> ` __ voor meer informatie.

Hoewel u uw eigen copyright-bericht in de gebruikersinterface wilt toevoegen als u het nodig vindt dat uw wijzigingen door uw wijzigingen worden gerechtvaardigd, vragen wij u de Mattermeeste, Inc. auteursrechtvermelding niet te verwijderen uit de voettekst of het dialoogvenster Info.

Mattermeeste Webapp
-----------------

De Mattermeeste webapp is gelicentieerd onder de Apache 2.0 licentie. Als u de Mattermeeste-server wilt wijzigen en gebruiken, kunt u het volgende doen:

1. Installeer de Mattermeeste server door een van onze installatiehandleidingen te volgen
2. Fork de ` matterbest-webapp <https://github.com/mattermost/mattermost-webapp> ` __ repository
3. Maak uw wijzigingen 4. Voer ` ` make package ` ` ` maken ` ` `mattermost-webapp.tar.gz ` ` maken
5. Kopieer ` `matterbest-webapp-tar.gz ` ` naar de locatie Matterbest is geïnstalleerd in stap 1
6. Verwijder de bestaande map ` ` client ` `
7. Voer ` ` tar -xvf mattermost-webapp.tar.gz ` ` uit om uw nieuwe aangepaste ` ` client ` ` map uit te halen
8. Start uw Mattermeeste server opnieuw op

Het is mogelijk om bepaalde delen van de webapp zonder forking aan te passen met onze :doc: ` Custom Branding <../administration/branding> ` instellingen. 

Om het logo in e-mailmeldingen te vervangen, wijzigt u het bestand in de directory ` ` /images ` `. Als u het apppictogram wilt wijzigen, wijzigt u het bestand ` `/app/components/app_icon.js ` `.

Mattermeeste Server
-----------------

Er zijn een paar dingen die kunnen worden aangepast in de Matterendste server zonder forking. 

1. Wijzig de tekst in de meest overeenkomende interface door het ` `en.json ` bestand 2 te wijzigen. Help-en ondersteuningslinks aanpassen of verbergen door uw :ref: ` configuratie-instellingenmodifying` te wijzigen
3. Pas de e-mailmeldingen aan door de HTML-bestanden te bewerken in ` ` /templates ` `

Mattermeeste mobiele toepassingen
------------------------------

De Mattermeeste mobiele toepassingen kunnen worden aangepast als u ervoor kiest om zelf de apps te bouwen. 

U kunt de mobiele apps als volgt merken: 

1. Fork de ` matterbest-mobile <https://github.com/mattermost/mattermost-mobile> ` __ repository
2. Vervang de naam, afbeeldingen en alle sleuteltekstreeksen
3. :doc: ` De apps compileren <../mobile/mobile-compile-yourself> `
4. De apps implementeren in een appstore

Terwijl de meeste organisaties implementeren op interne enterprise app stores, bent u welkom om te implementeren op iTunes en Google Play, zolang de branding niet kan worden verward met officiële Mattermeeste producten.

Mattermeeste Desktop-toepassingen
-------------------------------

De Mattermeeste desktop applicaties kunnen worden aangepast als u ervoor kiest om zelf te bouwen van de apps. 

Ga als volgt te werk om de desktop apps 

1. De ` mattermost/desktop Fork
<https://github.com/mattermost/desktop> ` __ repository
2. Vervang de naam, afbeeldingen en alle sleuteltekstreeksen
3. Raadpleeg ` deze documentatie <https://github.com/mattermost/desktop/blob/master/docs/development.md> ` __ voor hulp bij het compileren van de apps
4. Deel de desktop applicatie met uw gebruikers
