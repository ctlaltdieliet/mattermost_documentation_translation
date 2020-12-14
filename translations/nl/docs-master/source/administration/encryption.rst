Versleutelingsopties
== == == == == == == == == == == =

Matterbest biedt encryptie-in-transit en encryptie-op-rust mogelijkheden. Deze pagina begeleidt u bij het instellen van de juiste versleutelingbeveiliging.

Encryptie is niet vereist voor GDPR, hoewel het kan worden gebruikt als een extra bescherming tegen data inbreuk. .. Inhoud:
  :backlinks: boven: lokaal:

Encryptie-in-transit
-----------------------

Mattermeest ondersteunt TLS-encryptie met inbegrip van AES-256 met 2048-bit RSA op alle data transmissies tussen Mattermeeste clienttoepassingen en de Mattermeeste server. U kunt ofwel TLS instellen op de Mattermeeste Server of een proxy installeren zoals NGINX en TLS instellen voor de proxy. Raadpleeg onze ` configuration guide voor meer informatie <https://docs.mattermost.com/install/config-tls-mattermost.html> ` __.

Verbindingen met Active Directory/LDAP kunnen optioneel worden beveiligd met TLS of stunnel <https: //docs.mattermost.com/administration/config-settings.html#id9> ` __.

Roddelversleuteling (Experimental):
-----------------------

In een modus voor hoge beschikbaarheid ondersteunt Matterbest de versleuteling van clustergegevens in-transit bij het gebruik van het roddelprotocol.  

De versleuteling gebruikt standaard AES-256 en is niet configureerbaar. Het is echter mogelijk om de waarde handmatig in te stellen in de ` ` Systems ` ` tabel voor de ` ` ClusterEncryptionKey ` ` rij. Een sleutel is een bytereeks geconverteerd naar base64. Deze kan worden ingesteld op een lengte van 16, 24 of 32 bytes om respectievelijk AES-128, AES-192 of AES-256 te selecteren.


Versleuteling-op-rust
-----------------------

Database
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Versleuteling-op-rust is beschikbaar voor berichten via hardware-en softwareschijf-versleutelingsoplossingen die worden toegepast op de Mattermeeste-database, die zich op de eigen server bevindt in uw infrastructuur. De versleutelingsopties op het schijfniveau zijn gedocumenteerd voor zowel ' MySQL <https://www.percona.com/blog/2016/04/08/mysql-data-at-rest-encryption/> ` __ als ` PostgreSQL <https://www.postgresql.org/docs/8.1/static/encryption-options.html> ` __.

Bestandsopslag
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Voor lokale opslag of opslag via Minio is encryptie beschikbaar voor bestanden die zijn opgeslagen via hardware-en software-schijfversleutelingsoplossingen die op de server worden toegepast.

Voor Amazon ' s eigen S3-systeem, is encryptie-op-rest beschikbaar via ` server-side encryption with Amazon S3-managed keys <https: //docs.mattermost.com/administration/config-settings.html#enable-server-side-encryption-for-amazon-s3> ` __ in Enterprise Edition E20.
