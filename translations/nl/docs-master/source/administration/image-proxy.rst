.. _Image-proxy:

Afbeeldingsproxy
== == == == == == == == == == == == == == == ==

Het gebruik van een image-proxy betekent dat alle aanvragen voor afbeeldingen van Mattermeeste clients via de proxy gaan in plaats van direct contact op te nemen met servers van derden. Dit helpt de privacy van gebruikers te beschermen door externe servers te voorkomen van het volgen van een afbeelding. Dit voorkomt ook het gebruik van tracking pixels (onzichtbare beelden die hetzelfde doen zonder dat de gebruiker zelfs een afbeelding ziet).

Bepaalde proxyservers bieden ook een laag cachegeheugen waarmee het laden van beelden sneller en betrouwdiger kan worden gemaakt. Deze caching helpt ook om berichten te behouden door ze te beschermen tegen dode beelden.

Als deze optie is ingeschakeld, moet de afbeeldingsproxy openbaar toegankelijk zijn voor zowel de Matterbest-client als de server.

Mattermeeste clients gebruiken de afbeeldingsproxy om alle externe afbeeldingen te laden. De Mattermeeste server zal de image-proxy indien mogelijk gebruiken, maar zal het niet gebruiken bij het aanvragen van content die mogelijk geen afbeelding is, zoals voor ` image previews of plaintext URL's <https://github.com/mattermost/mattermost-server/issues/11857> ` _.

Een afbeeldingsproxy kan worden geconfigureerd in ** System Console > Environment > Image Proxy * * (of ** System Console < Files > Storage * * in versies ouder dan 5.12).

Lokale afbeeldingsproxy
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

De lokale afbeeldingsproxy is beschikbaar als onderdeel van de implementatie van de Mattermeeste-server. Bij gebruik van de lokale image-proxy, worden afbeeldingen worden geserveerd aan clients via de server die anonieme gebruikers helpt. Als SSL is ingeschakeld op de server, biedt het een beveiligde verbinding. Deze methode biedt geen caching gedrag. .. Opmerking: 
   Als de lokale afbeeldingsproxy is ingeschakeld, worden aanvragen voor afbeeldingen die op het lokale netwerk worden gehost, nu beïnvloed door de instelling ` ` AllowUntrustedInternalConnections ` `. Zie ` documentation <https: //docs.mattermost.com/administration/config-settings.html#allow-untrusted-internal-connections-to> ` _ voor meer informatie of als u onbedoeld geblokkeerde afbeeldingen ziet. .. _atmos-camo:

Atmos/camo Image Proxy
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

De ` atmos/camo <https://github.com/atmos/camo> ` _ image proxy is een standalone image proxy die afzonderlijk kan worden ingezet vanaf de Mattertiste server. Het biedt aanvullende configuratieopties over de ingebouwde image-proxy, en het kan ook worden gebruikt als de isolatie tussen de Mattermeeste server en de afbeeldingsproxy gewenst is.

Als u een ` ` atmos/camo ` ` ` (https: //github.com/atmos/camo) instance hebt geïmplementeerd, moet u de instellingen van de proxy-instellingen voor afbeelding * op afstand URL* * en ** Opties voor niet-lokale afbeeldingsproxy * * opgeven. De ** Remote Image Proxy Options * * moeten worden ingesteld op de gedeelde sleutel van de afbeeldingsproxy die is opgegeven met de omgevingsvariabele ` ` CAMO_KEY ` ` die wordt gebruikt bij het instellen van de afbeeldingsproxy.

Als de afbeeldingsproxy bijvoorbeeld zich bevindt op ' `https: //image-proxy.mattermost.com ` `, wordt het als volgt geconfigureerd:

 -** Image Proxy Type * *: ` ` atmos/camo ` ` `
 -** Remote Image Proxy URL* *: ``https: //image-proxy.mattermost.com ` `
 -** Remote Image Proxy Options * *: ` ` CAMO_KEY ` `, dat is de geheime string die gebruikt wordt voor de
voorbeeld ` ` atmos/camo ` ` implementatie. .. image:: ../images/image-proxy.png
