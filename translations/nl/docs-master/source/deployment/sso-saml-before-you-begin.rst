Voordat U Begint
----------------

Voordat u begint, moet u de XML-beveiligingsbibliotheek installeren.

1. Zorg ervoor dat u beschikt over de ` XML Security Library <https://www.aleksey.com/xmlsec/download.html> ` __ geïnstalleerd op uw Matterinstance. De XML Security Library wordt meestal opgenomen als onderdeel van Debian GNU/Linux.

2. Installeer de * xmlsec1-openssl * bibliotheek
 -Op Ubuntu: ` ` sudo apt-get install xmlsec1 ` `
 -Op RHEL: ` ` sudo yum install xmlsec1-openssl ` `

3. Genereer versleutelingscertificaten voor het versleutelen van de SAML-verbinding.
  a. Je kunt het ` Bash script <https://github.com/mattermost/docs/tree/master/source/scripts/generate-certificates> ` __ gebruiken van de * mattermost/docs * repository op GitHub, of een andere geschikte methode.
  b. Sla de twee gegenereerde bestanden op. Zij zijn de persoonlijke sleutel en de publieke sleutel. In de systeemconsole wordt verwezen naar respectievelijk de ** Serviceverlener Private Key * * en het ** Service Provider Public Certificate * *.
