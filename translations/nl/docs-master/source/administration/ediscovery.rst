.. _ediscovery:

Elektronische Discovery
== == == == == == == == == == == == == == == == == == =

Elektronische ontdekking (ook bekend als eDiscovery) verwijst naar een proces waarbij elektronische gegevens worden doorzocht met de bedoeling het in een juridische zaak als bewijs te gebruiken.

Deze pagina beschrijft hoe u gegevens kunt extraheren uit Matterbest voor eDiscovery. Er zijn drie primaire methoden die kunnen worden gebruikt om het doel van het extraheren van gebruikersgegevens uit Matterbest te bereiken:

-` Matterbest Compliance Exports <https://docs.mattermost.com/administration/compliance-export.html> ` __
-Mattermeest RESTful API
-Mattermeeste database met standaard SQL queries

Elk van de opties wordt besproken in detail hieronder. .. Opmerking:

  De proceshouder (ook wel "legal hold" genoemd) is een uitbreiding van eDiscovery waarin naast het zoeken naar records geen elektronisch opgeslagen informatie of papieren documenten kunnen worden vernietigd als zij relevant kunnen worden geacht voor een bestaande of toekomstige juridische zaak.

Meest complianceexporten
------------------------------------

Mattermeeste Enterprise E20 heeft nalevingsrapportexportmogelijkheden.

Matterbest kan nalevingsgerelateerde gegevens exporteren, inclusief de inhoud van berichten en die deze berichten kunnen hebben gezien, in drie formaten: Actiance XML, Global Relay EML en generieke CSV. Rapporten kunnen worden geconfigureerd voor het uitvoeren van een vertraging en worden opgeslagen op een gemeenschappelijke locatie.

Voor meer informatie over de export-functie en hoe u rapportage kunt instellen, raadpleegt u ' onze documentatie <https://docs.mattermost.com/administration/compliance-export.html> ` __.

Mattermeest RESTful-API
------------------------------------

De Matterelijkste API kan worden gebruikt voor het exporteren van de berichten van een gebruiker in CSV-nalevingsindeling die deel uitmaakt van Matterbest Enterprise E20. In de volgende sectie wordt beschreven hoe u de API gebruikt voor het maken en ophalen van een rapport voor een bepaalde gebruiker via de API. Houd er rekening mee dat volledige documentatie voor de Mattermeest API kan worden gevonden op https://api.mattermost.com.

Als u de API wilt gebruiken, moet u eerst verifiëren " zoals hier beschreven <https: //api.mattermost.com/#tag/authentication> ` __. Het account waarmee u verificatie uitvoert, moet ` ` beheer_system ` ` ` permissies hebben. Als u Curl gebruikt, kunt u verifiëren met de volgende opdracht: .. code-blok :: json

  curl -i -d '{ "login_id": "gebruikersnaam", "wachtwoord": "wachtwoord" }' https://yourmattermosturl/api/v4/users/login

Matterbest zal een reactie die er zo uit ziet: .. code-blok :: json

  HTTP/2 200-server: nginx/1.10.3 (Ubuntu)
  datum: Thu, 12 Jul 2018 14:43:45 GMT
  inhoudstype: application/json
  inhoud-lengte: 679
  set-cookie: MMAUTHTOKEN=yi94pwci6ibjfc9phbikhqutbe; Path=/; Expires=Sat, 11 Aug 2018 14:43:45 GMT; Max-Age = 2592000; HttpOnly; Secure
  set-cookie: MMUSERID=qfjzamfg47bu9gsyyfbqjk4s6a; Path=/; Vervallen = Sat, 11 Aug 2018 14:43:45 GMT; Max-Age = 2592000; Secure
  token: yi94pwci6ibjfc9phbikhqutbe
  x-aanvraag-id: 5y45pxyfxpb8updtge1zts39he
  x-version-id: 5.0.0.5.0.1.18c0fbd759664a85fe95132bb7fc04cf.true

Voeg de ` ` token ` ` waarde in de respons toe als onderdeel van de Autorisatiekop
op uw toekomstige API-aanvragen met de Bearer-methode, bijvoorbeeld:

.. code-blok :: json

  curl -i -H ' Machtiging: Bearer yi94pwci6ibjfc9phbikhqutbe http://yourmattermosturl/api/v4/users/me

Wanneer u eenmaal bent geverifieerd, kunt u de compliance-API gebruiken om een nieuw nalevingsrapport te maken <https: //api.mattermost.com/#tag/compliance%2Fpaths%2F ~ 1compliance ~ 1reports%2Fpost> ` __. Het curl-gebaseerde voorbeeld hieronder laat zien hoe u een aanvraag stuurt die het authenticatietoken baseert en Matterbest vraagt om een rapport te maken dat berichten van Dec 31, 2017-8:15 PM naar Dec 31, 2018-8:15 PM voor een gebruiker met het e-mailadres craig@mattermost.com .. Opmerking:

  De gegevens in de JSON-payload moeten geformatteerd zijn als Unix Epoch. Een tool als https://www.epochconverter.com/ kan nuttig zijn bij het converteren naar en van de vereiste formaat. .. code-blok :: json

  curl -- header "Content-Type: application/json" \ -- request POST \
  -H 'Machtiging: Bearer yi94pwci6ibjfc9phbikhqutbe \ --data' { "id": "," create_at ": 0," user_id ":" craig "," status ":" "," count ": 0," desc ":" "," type ":" "," start_at ": 1514769359000," end_at ": 1546305359000," keywords ":" "," e-mails ":" craig@mattermost.com " } ' \
  https://yourmattermosturl/api/v4/compliance/reports

Als de post succesvol is, zal Matterbest een bericht terugsturen dat er als volgt uitziet, wat aangeeft dat de server het nalevingsexportproces uitvoert: .. code-blok :: json

  { "id": "du6kektczifqxexeroywpz3nbc", "create_at": 1531444617901, "user_id": "qfjzamfg47bu9gsyyfbqjk4s6a", "status": "running": 0, "desc": "", "type": "adhoc", "start_at": 1514769359000, "end_at": 1546305359000, "keywords": "", "emails" :"craig@mattermost.com " }

Wanneer het exportproces voltooid is (de uitvoeringstijd is gebaseerd op het aantal records om terug te keren en de huidige serverbelasting), dan moet u een andere HTTP Post-aanvraag naar Matterbest verzenden om een zip-bestand met het rapport dat er als volgt uitziet op te halen en te downloaden: .. code-blok :: json

  curl -- aanvraag GET \
  -H 'Machtiging: Bearer p9o1qx457fbc9gdrn3 9z9ah59o' \ --data '{ "status_code": 0, "id": "du6kektczifqxexeroywpz3nbc", "message": "", "requestion_id": "" }' \ -- output report-zip.zip \
  https://yourmattermosturl/api/v4/compliance/reports/du6kektczifqxexeroywpz3nbc/download

Bij het verzenden van de aanvraag moet u het rapport-ID ophalen uit de respons die Matterbest heeft teruggezonden bij het maken van het rapport. U moet ook een naam leveren om dat bestand veilig te maken. In het bovenstaande voorbeeld wordt het bestand opgeslagen als ` `report-zip.zip ` `.

Mattermeeste Database
------------------------------------

Het selecteren van berichten uit de Matterbest database met behulp van standaard SQL is vrij eenvoudig. Als u de gebruikersnaam weet, kan de volgende query worden gebruikt om alle berichten voor de opgegeven gebruiker te selecteren: .. code-block :: sql
  
  SELECT * FROM matterbest. Posts WHERE UserId = (SELECT Id FROM matterbest. Users WHERE Username = 'username ');

Als u de resultaten van de query wilt beperken op basis van de datum en tijd waarop de berichten zijn gepost, kunt u de bovenstaande query wijzigen in: .. code-block :: sql
  
  SELECT * FROM mat. Posts WHERE UserId = (select Id FROM matterbest. Users WHERE Username = 'username ' AND CreateAt > 1530405832000 AND CreateAt < 1532997832000); .. Opmerking: 
  De Matterendste database slaat datum/tijdstempels op in de Unix Epoch (https: //en.wikipedia.org/wiki/Unix_time) formaat en een tool als https://www.epochconverter.com/ kan nuttig zijn bij het converteren naar en van de vereiste indeling.
