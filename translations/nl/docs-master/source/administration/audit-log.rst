Auditlogboek v2 (Experimental) (E20)
== == == == == == == == == == == == == == == == == == =

Met een nieuw auditlogboek kunnen System Admins een uitgebreiere lijst van events bekijken voor meer diepgaande analyse. Daarnaast biedt het meer controle over waar de logboeken worden gegenereerd en opgeslagen.

Auditlogboek configureren in Matterbest
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Ng~

Voor het configureren van de Matterbest-server voor het gebruik van het nieuwe auditlogboek is het nodig om het ` `config.json `-bestand rechtstreeks te bewerken. Met de audit-instellingen worden auditrecords uitgevoerd naar syslog (lokale server of server op afstand via TLS) en naar een lokaal bestand. Syslog en lokale opslag van bestanden kunnen gelijktijdig worden ingeschakeld. Beide zijn standaard uitgeschakeld.

** Toegang tot configuratieopties voor auditlogboek * *

Open ` `config.json ` ` en navigeer naar de auditinstellingen. De volgende ` configuratieopties <https: //docs.mattermost.com/administration/config-settings.html#audit-settings> ` _ zijn beschikbaar:

-Syslog configuratie opties:

    -Instellingen inschakelen om auditrecords te schrijven naar een lokale of niet-lokale syslog
    -Geef het IP-adres op
    -Geef poort op
    -Gebruikers gegenereerde velden toevoegen
    -Certificaatinstellingen configureren

-Opties voor bestandsconfiguratie:

    -Schakel instellingen in om auditbestanden lokaal te schrijven
    -Geef bestandsgrootte op
    -Geef het backupinterval op
    -Voeg compressie toe
    -Stel maximumleeftijd in voor het beheren van bestandsrotatie

Logboekevents worden ondersteund ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ vinden

-Events die worden opgeroepen vanuit de Matterelijkste API
-Events die zijn opgeroepen vanuit mmctl-Events die zijn opgeroepen vanuit de verouderde CLI van Matterit

Gegevensmodel
~ ~ ~ ~ nopen ~ ~

Er wordt een enkel auditrecord verzonden voor elke event (` ` add ` `, ` ` delete ` `, ` ` login ` `, ` ` ... ` ` `). Er kunnen meerdere auditbare events worden verzonden voor een enkele API-aanroep. .. csv-table ::
    :header: "Naam", "Type", "Beschrijving"

    "ID.", "string", "auditrecord-ID." "CreateAt", "int64", "timestamp of record creation, UTC." "Level", "string", "e.g. ` ` audit-rest ` `, ` ` audit-app ` `, ` ` audit-model ` ` "" APIPath "," string "," rest eindpunt "
    "Event", "string", "e.g. ` ` add ` `, ` ` delete ` `, ` ` login ` `, ` ` ... ` ` "Status", "string", "e.g. ` ` poging ` `, ` ` success ` `, ` ` fail ` `, ` ` ... ` ` "UserId", "string", "ID van gebruiker die de API aanroept"
    "SessionId". "string", "ID van sessie die wordt gebruikt om de API aan te roepen"
    "Client", "string", "e.g. webapp, mmctl, user-agent "" IPAddress "," string "," IP-adres van client "
    "Meta", "map [ string] interface { }", "API-specifieke informatie (bijvoorbeeld gebruikers-ID dat wordt gewist)"

Logboekopslag
~ ~ ~ ~ nopen ~ ~

Auditrecords worden gescheiden opgeslagen van algemene logboekregistratie. De algemene logboekopslaglocatie is configureerbaar via ` ` LogSettings ` ` in het ` `config.json ` ` ` bestand.

Tijdens korte spans van onvermogen om te schrijven naar doelen, de audit records buffer in het geheugen met een cap. Op basis van typische volumes van auditrecords kan het veel minuten duren voordat de buffer wordt gevuld. Daarna worden de records verwijderd en wordt de event voor het verwijderen van records vastgelegd.

Als u syslog op afstand gebruikt, is de huidige beste praktijk om ook naar het lokale bestand te schrijven zodat er geen records verloren gaan. Merk op dat dit niet automatisch records uit het lokale bestand en
stuur het naar syslog wanneer syslog weer beschikbaar wordt.

Geplande uitbreidingen van het auditlogboek
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Om te zorgen dat auditlogboeken niet bewust beschadigd of beschadigd zijn, maakt u het mogelijk om de logboekengine te configureren voor het ondertekenen van logboekbestanden voor specifieke doelen. Wanneer een auditarchief niet veilig kan worden gemaakt, kunnen auditlogboeken worden opgeslagen op meerdere plaatsen (bijv. bestand en database), zodat ze desgewenst kunnen worden afgestemd.

Geplande verbeteringen in het loggen in het algemeen ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ >

-Discrete logniveaus toestaan. Op dit moment wordt er een toepassingsbreed logboekniveau geconfigureerd en worden alle logboekrecords verzonden die overeenkomen met dat niveau of lager. Deze logboekniveaus blijven bestaan, maar er worden ondersteuning voor nul of meer discrete logboekniveaus toegevoegd, wat betekent dat alleen records worden verzonden die overeenkomen met het huidige logboekniveau of een van de afzonderlijke niveaus. Binnen de logboekengine zal elk niveau onder 10 (` ` trace ` ` ` through ` ` critical ` `/` ` fatal ` ` `, plus ` ` reserved ` `) zich gedragen zoals het momenteel doet, maar elk niveau boven de 10 zal als discrete worden beschouwd. Auditrecords hebben een niveau hoger dan 10.

-Make logging engine verbeteringen geïmplementeerd via het ` ` mlog ` ` pakket en zal compatibel zijn met het bestaande gebruik.

-Laat logniveaus en discrete niveaus aan verschillende doelen (bestanden, databases, etc) via de configuratie.

Raadpleeg voor meer informatie het voorstel voor het vastleggen van verbeteringen in het logboek.
