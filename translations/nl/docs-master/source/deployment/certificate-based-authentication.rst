Verificatie op basis van certificaten (Experimental)
== == == == == == == == == == == == == == == == == == == == == == == == ==

*Beschikbaar als experimentele functie in Enterprise Edition E20 .*

Verificatie op basis van certificaten (CBA) kan worden gebruikt om een gebruiker of een apparaat te identificeren alvorens toegang te verlenen tot Matterbest, een extra beveiligingslaag voor toegang tot het systeem.

Voer de volgende stappen uit om gebruiker CBA te configureren voor uw browser en Matterbest Desktop Apps. Ondersteuning voor de Mattermeeste iOS en Android Apps is gepland. Er wordt verwacht dat u de certificaatdistributie voor elk persoonlijk apparaat (BYOD) en hun levenscyclusbeheer kunt beheren met een service zoals ` OpenSSL <https://www.openssl.org/> ` __.

Voordat u begint, volgt u de ` officiële gidsen voor het installeren van Mattermeest <https: //docs.mattermost.com/guides/administrator.html#installing-mattermost> ` __ op uw systeem, inclusief NGINX-configuratie als een proxy met SSL en HTTP/2, en een geldig SSL-certificaat, zoals Let's Encrypt. .. Inhoud:
  :backlinks: boven: lokaal:
  :diepte: 2

Wederzijdse TLS-verificatie instellen voor de Web App
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Dit is de eerste stap voor het instellen van certificaatverificatie. Als u nog geen wederzijdse TLS-verificatie hebt ingesteld, " zie onze documentatie voor meer informatie <https://docs.mattermost.com/deployment/ssl-client-certificate.html> ` __.

Stel Mattermeeste server in om aan te melden met een clientcertificaat ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

1. Zorg ervoor dat uw Mattermeeste server een licentie heeft met een geldige Enterprise Edition E20-licentie.
2. In ` ` ExperimentalSettings ` ` van het ` `config.json ` ` ` bestand, stel je ` ` ClientSideCertEnable ` ` ` aan ` ` true ` ` en ` ` ClientSideCertCheck ` ` naar een van de volgende waarden:

-` ` primary ` ` `-Nadat het clientcertificaat is geverifieerd, wordt de e-mail van de gebruiker opgehaald uit het certificaat en wordt gebruikt om zonder wachtwoord aan te melden.
-` ` secundair ` ` `-Nadat het clientcertificaat is geverifieerd, wordt de e-mail van de gebruiker opgehaald uit het certificaat en vergeleken met de e-mail die door de gebruiker is geleverd. Als deze overeenkomen, meldt de gebruiker zich aan met gewone e-mail-en wachtwoordgegevens.

Het ` `config.json ` ` bestand moet dan de volgende regels hebben. code-blok :: tekst

  "Experimentalinstellingen": {
      "ClientSideCertEnable": true, "ClientSideCertCheck": "secundair"
  },

3. Start de Matterigste server opnieuw op.

Op Ubuntu 14.04 en RHEL 6: .. code-block :: tekst

  sudo opnieuw starten matterbest

Op Ubuntu 16.04, Debian Stretch, en RHEL 7: .. code-block :: tekst

  sudo systemctl restart matterbest

4. Ga naar https://example.mattermost.com en probeer u aan te melden. Voor de server moet het x.509-certificaat een ` ` emailAddress ` ` hebben dat gelijk is aan de e-mail van de Matterbest gebruiker.
