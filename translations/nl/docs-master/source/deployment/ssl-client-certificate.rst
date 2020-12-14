Configuratie SSL-clientcertificaat (Beta)
== == == == == == == == == == == == == == == == == == == == == == == == == ==

Voer de volgende stappen uit om SSL-clientcertificaten te configureren voor uw browser en de Matterste Desktop Apps op Windows, Mac en Linux. SSL-clientcertificaten worden nog niet ondersteund op de Mattermeeste mobiele apps.

Voordat u begint, volgt u de ` officiële gidsen voor het installeren van Mattermeest <https: //docs.mattermost.com/guides/administrator.html#installing-mattermost> ` __ op uw systeem, inclusief NGINX-configuratie als een proxy met SSL en HTTP/2, en een geldig SSL-certificaat zoals Let's Encrypt.

Voor de toepassing van deze handleiding is de domeinnaam van de Mattermeest server ' `example.mattermost.com ` `, en het gebruikersaccount is ` ` mmuser ` ` met e-mail ` `mmuser@mattermost.com ` ` ` en wachtwoord ` ` mmuser-password ` `. .. Opmerking:
  Het genereren van de clientcertificaten in deze sectie is optioneel als u ze al eerder hebt gegenereerd.

Stel de wederzijdse TLS-verificatie in voor de webapp ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

1. Maak een ` certificate authority (CA) key <https://en.wikipedia.org/wiki/Certificate_authority> ` __ en een certificaat voor het ondertekenen van het clientcertificaat. Bij het tot stand brengen van een TLS-verbinding vraagt en valideert de NGINX proxy server een clientcertificaat van de web-app. .. code-blok :: geen

  openssl genrsa -des3 -out. Mattermost.key 4096 pas zin: capassword

    
... code-blok :: geen

  openssl req -new -x509 -days 365 -key.

  Naam land: US
  State: Maryland Locality Name: Meade Organization Name: Mattermost Organization Unit: Smarttotem Common Name: example.mattermost.com Email Address: admin@mattermost.com

2. Maak de client-side-sleutel voor ` ` mmuser ` ` met een passphrase en de aanvraag voor het ondertekenen van het certificaat: .. code-blok :: geen

  openssl genrsa -des3 -out mmuser-mattermost.key 1024

  wachtwoordzin: mmuser-passphrase .. code-blok :: geen

  openssl req -new -key mmuser-mattermost.key -out mmuser-mattermost.csr

  Naam land: US
  State: Maryland Locality Name: Meade Organization Name: Mattermost Organization Unit: Smarttotem Common Name: mmuser Email Address: mmuser@mattermost.com Challenge password: mmuser-passphrase

3. Onderteken het clientcertificaat van de gebruiker met het eerder gemaakte CA-certificaat: .. code-blok :: geen

  openssl x509 -req -days 365-in mmuser-mattermost.csr -CA. Mattermost.crt -CAkey. mattermost.key -set_serial 01 -out mmuser-mattermost.crt

4. Controleer het nieuw gegenereerde clientcertificaat voor ` ` mmuser ` `: .. code-blok :: geen

  openssl x509 -in mmouser-mattermost.crt -text -noout

5. Open het bestand ` ` /etc/nginx/sites-available/matterbest ` ` en wijzig de volgende regels, zodat de NGINX proxy server aanvragen en controleert het clientcertificaat: .. code-blok :: geen
  :onderstreepte lijnen: 4-5, 10-11, 16-17

  ssl op;
  ssl_certificate /etc/letsencrypt/live/example.mattermost.com/fullchain.pem; ssl_certificate_key /etc/letsencrypt/live/example.mattermost.com/privkey.pem
; ssl_client_certificate /opt/mattermost/config/.mattermost.crt; ssl_verify_client op;

  ...

  locatie ~ /api/v [ 0-9] +/(users/) ?websocket$ {
   proxy_set_header X-SSL-Client-Cert $ssl_client_cert; proxy_set_header X-SSL-Client-Cert-Onderwerp-DN $ssl_client_s_dn; ...

  locatie/{
   proxy_set_header X-SSL-Client-Cert $ssl_client_cert; proxy_set_header X-SSL-Client-Cert-Onderwerp-DN $ssl_client_s_dn; ...

6. Bevestig de CA-sleutel voor ` ` mmuser ` ` door de volgende curl-opdracht aan de proxy: .. code-blok :: geen

  curl -v -s -k -- key mmuser-mattermost.key -- cert mmuser-mattermost.crt:mmuser-passphrase https://example.mattermost.com

Je zou de Matterbest login pagina moeten zien. Als u het volgende ziet:

 -` ` Er is geen vereist SSL-certificaat verzonden ` `, er is iets fout gegaan. Bekijk de bovenstaande stappen en probeer het opnieuw.
 -` ` Fout bij lezen van X.509-sleutel of certificaatbestand: Decotie is mislukt. ` `, zorg ervoor dat het wachtwoord samen met het certificaat is opgenomen, omdat curl het niet apart vraagt. 

7. Genereer een PKCS12-bestand van de CA-sleutel en certificaat, om het certificaat te installeren in uw clientmachine om uw browser te gebruiken: .. code-blok :: geen

  openssl pkcs12 -export -out mmuser-mattermost.p12 -inkey mmuser-mattermost.key -in mmuser-mattermost.crt -certfile

  Voer het exportwachtwoord in: mmuser-passphrase

8. Herhaal stap 2-7 hierboven voor andere gebruikers.

9. Importeer het gegenereerde .p12-bestand in stap 7 in uw sleutelketen. In de Chrome-browser op macOS:

  1. Ga naar ** Instellingen > Geavanceerd > Privacy en veiligheid > Certificaten beheren * *. Hiermee opent u de app Keychain Access.
  2. Ga naar ** Bestand > Items importeren * * en selecteer het ` `mmuser-mattermost.p12 ` ` bestand.

10. Ga naar https://example.mattermost.com. U moet een voorgrondvenster voor het clientcertificaatverzoek bekijken.

Problemen oplossen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

` Volg dit proces <https://mattermost.org/troubleshoot/> ` __ om de configuratieproblemen op te lossen en om hulp te vragen.
