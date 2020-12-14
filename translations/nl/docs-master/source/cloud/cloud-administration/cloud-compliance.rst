Nalevingsrapportage en Oversight
-----------------------------------

Deze functie maakt het mogelijk dat de nalevingsexport wordt geproduceerd vanuit de systeemconsole, met alle query-en downloadacties die in een audithistorie zijn vastgelegd om het toezicht mogelijk te maken en ongeautoriseerde query's te voorkomen.

Nalevingsexporten kunnen worden gefilterd naar datumbereik, gebruikersaccount en trefwoordenlijst. Aanvragen van query's kunnen worden gedownload van de gebruikersinterface in de indeling ` ` .csv ` `, met een ` ` .json ` ` metabestand dat de query documenteert, en worden geplaatst in een directory die is ingesteld door de systeembeheerder.

Er kunnen ook dagelijkse nalevingsrapporten worden gegenereerd, ondersteuning van integratie met nalevingsoplossingen zoals ` Global Relay <https: //docs.mattermost.com/administration/compliance.html#global-relay-support> ` __.

Standaard bewaren alle Mattermeeste Editions alle berichten, inclusief bewerkingen en wisbewerkingen, samen met alle geüploade bestanden. Opmerking:
  Deze functie wordt vervangen door ` Compliance Export (Beta) <https://docs.mattermost.com/cloud/cloud-administration/compliance-export.html> ` _, en wordt in Matterbest in een toekomstige release verwijderd. We raden u aan te migreren naar het nieuwe systeem. Voor een voorbeeld-CSV-uitvoer van het nieuwe nalevingsexportsysteem, ` download hier een CSV-exportbestand <https://github.com/mattermost/docs/blob/master/source/samples/csv_export.zip> ` __.

Nalevingsrapportage inschakelen == == == == == == == == == == == == == == =

1. Ga naar ** System Console > Compliance > Compliance Monitoring * * and set the ** Enable Compliance Reporting * * value to ** true**.
2. (Optioneel) In ** Compliance Report Directory * * geeft u de directory op waarin voltooide nalevingsrapporten moeten worden geplaatst. De standaardwaarde is ` ` ./data/ ` ` als dit veld leeg is.
3. Klik op ** Save**.

Hierdoor wordt de optie voor het genereren van dagelijkse nalevingsrapporten ingeschakeld.

Dagelijkse nalevingsrapporten inschakelen
== == == == == == == == == == == == == == == ==

Na het inschakelen van nalevingsrapportage:

Ga naar ** Systeemconsole > Naleving > Nalevingscontrole * *, stel de waarde voor ** Enable Daily Report * * in op ** true** en selecteer ** Save**.

Uw systeem exporteert nu alle nieuwe berichten die zijn gepost binnen een periode van 24 uur als een ` ` .csv ` ` ` bestand naar de locatie die is opgegeven in ** Compliance Report Directory * *. Deze functie kan worden gebruikt in combinatie met gecentraliseerde procedures voor het rapporteren van nalevingsrapportage.

Nalevingsrapporten uitvoeren
== == == == == == == == == == ==

Compliance Reports zijn de export van alle berichten in Matterbest die overeenkomen met de rapportcriteria. U voert als volgt een rapport uit:

1. Ga naar ** System Console > Compliance > Compliance Monitoring * *.
2. Vul de volgende criteria in:

     -** Taaknaam: ** Naam het nalevingsrapport dat u gaat uitvoeren (bijvoorbeeld "HR Audit 455").
     -** From:** Begindatum voor zoeken in notatie JJJJ-MM-DD (bijv. "2016-03-11").
     -** To:** Einddatum van de zoekopdracht in de notatie JJJJ-MM-DD (bv. "2016-05-11").
     -** Emails:** Komma-gescheiden lijst van e-mailadressen van gebruikers van wie u de berichten wilt doorzoeken (bijv. ` `bill@example.com, bob@example.com ` ` `).
     -** Sleutelwerk:** Geef de woorden aan die in een bericht zouden worden opgenomen om te worden opgenomen in de resultaten van het nalevingsrapport.
3. Klik
** Nalevingsrapport uitvoeren * *.

Het rapport wordt in de wachtrij geplaatst op het scherm onder de hierboven beschreven velden. De eigenschappen van elk nalevingsrapport worden als volgt uitgelegd:

-** Timestamp:** Tijd waarop het rapport werd aangevraagd.
-** Status:** ` ` running ` ` geeft aan dat het rapport wordt uitgevoerd; ` ` voltooid ` ` geeft aan dat het rapport voltooid is en klaar is om te downloaden.
-** Records:** Geeft het aantal zoekresultaten weer.
-** Type:** ` ` adhoc ` ` geeft aan dat het rapport is aangevraagd door queryvelden in te vullen; ` ` daily ` ` geeft aan dat het rapport een dagelijkse export is.
-** Beschrijving:** Taaknaam aangegeven in aanvraag.
-** Aangevraagd door: ** E-mail van de persoon die het rapport aanvraagt.
-** Params:** Parameters van het nalevingsrapport.

Elk nalevingsrapport bevat een link ** Download** die een gecomprimeerd bestand met de naam ` ` adhoc-[ UNIQUE_ID] .zip downloadt ` `. Inside het bestand is ` `meta.json ` `, die de parameters van de uitgevoerde zoekopdracht bevat en ` `posts.csv ` ` die de inhoud bevat van de berichten die door het verzoek worden gevonden.

Definitie van compliance query opgeslagen in ` `meta.json ` ` bestand ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

` `meta.json ` ` bevat de volgende informatie over de nalevingsquery: + --------------------- + --------------------------------------------------------------- + ----------------------------------- +
| Veld | Beschrijving | Voorbeeld | | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = +
| id | Uniek ID voor nalevingsquery | ja8z8egap7nq9kqetz3rt98khe | + --------------------- + --------------------------------------------------------------- + ----------------------------------- +
| create_at | Tijdstempel waarop nalevingsquery is uitgevoerd | 1463637842478 | + --------------------- + --------------------------------------------------------------- + ----------------------------------- +
| user_id | Mattermeeste gebruikers-ID voor persoon die query maakt | 3bq1shta93yztg3i6aiu1tzi5h | + --------------------- + --------------------------------------------------------------- + ----------------------------------- +
| status | Status van query: * voltooid * of * mislukt * | "voltooid" | + --------------------- + --------------------------------------------------------------- + ----------------------------------- +
| count | Aantal berichten gevonden die overeenkomen met trefwoord | 36 | + --------------------- + --------------------------------------------------------------- + ----------------------------------- +
| desc | Door gebruiker opgegeven beschrijving van nalevingsquery | Voorbeeld nalevingsrapport | + --------------------- + --------------------------------------------------------------- + ----------------------------------- +
| type | Type compliance query: * adhoc * or * daily * | "adhoc" | + --------------------- + --------------------------------------------------------------- + ----------------------------------- +
| start_at | Tijdstempel waarop query is gestart | 1451606400000 | + --------------------- + --------------------------------------------------------------- + ----------------------------------- +
| end_at | Tijdaanduiding waarvoor query is beëindigd | 1463529600000 | + --------------------- + --------------------------------------------------------------- + ----------------------------------- +
| trefwoorden | Door komma's gescheiden, hoofdletterongevoelige sleutelwoorden die overeenkomen met query | "drinken" | + --------------------- + --------------------------------------------------------------- + ----------------------------------- +
| e-mails | Door komma's gescheiden e-mails van gebruikers om te zoeken. Blanco retourneert alle | ``frank.yu@ha.ca, mary.li@hi.co ` ` | + --------------------- + --------------------------------------------------------------- + ----------------------------------- +

De resultaten van de nalevingsquery worden opgeslagen in het bestand " `posts.csv ` ` ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

` `posts.csv ` ` bevat de volgende informatie over de resultaten van de nalevingsquery, één zoekresultaat per rij: + --------------------- + --------------------------------------------------------------- + ------------------------------- +
| Veld | Beschrijving | Voorbeeld | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = +
| TeamName | URL-naam van team | contosi | + --------------------- + --------------------------------------------------------------- + ------------------------------- +
| TeamDisplayName | Weergavenaam van team | Contosi Corporation | + --------------------- + --------------------------------------------------------------- + ------------------------------- +
| ChannelDisplayName | Weergavenaam van kanaal waarop sleutelwoord is gevonden | Community Heartbeat | + --------------------- + --------------------------------------------------------------- + ------------------------------- +
| ChannelName | URL-naam van kanaal | community-heartbeat | + --------------------- + --------------------------------------------------------------- + ------------------------------- +
| UserUsername | Gebruikersnaam van gebruiker posting het bericht met sleutelwoord | frank.yu |
+ --------------------- + -------------------------------------------------------
-------- + ------------------------------- +
| UserEmail | E-mail van gebruiker die het bericht plaatst op trefwoord | "frank.yu@contosi.com " | + --------------------- + --------------------------------------------------------------- + ------------------------------- +
| UserNickname | Nickname van gebruiker die het bericht plaatst met sleutelwoord | fan du | + --------------------- + --------------------------------------------------------------- + ------------------------------- +
| PostId | Uniek ID van berichtpost met sleutelwoord | xt9anyx6x3fx9y84aehgakdpze | + --------------------- + --------------------------------------------------------------- + ------------------------------- +
| PostCreateAt | Tijdstempel waarop post is gemaakt | 2016-03-02T16:01:59Z | + --------------------- + --------------------------------------------------------------- + ------------------------------- +
| PostDeletedAt | Tijdstempel waarop de post is gewist (indien van toepassing) | 2016-03-02T16:01:59Z | + --------------------- + --------------------------------------------------------------- + ------------------------------- +
| PostUpdatedAt | Tijdstempel waarop de post voor het laatst is bewerkt (indien van toepassing) | 2016-03-02T16:01:59Z | + --------------------- + --------------------------------------------------------------- + ------------------------------- +
| PostParentId | Uniek ID van bovenliggende post als post een reactie is | xt9anyx6x3fx9y84aehgakdpze | + --------------------- + --------------------------------------------------------------- + ------------------------------- +
| PostOriginalId | Uniek ID van post indien verwijderd of bewerkt | xt9anyx6x3fx9y84aehgakdpze | + --------------------- + --------------------------------------------------------------- + ------------------------------- +
| PostMessage | Message containing keyword | Drinking from the fire hose | + --------------------- + --------------------------------------------------------------- + ------------------------------- +
| PostFilenames | Comma gescheiden lijst van bestandsnamen gekoppeld aan post | [ "/f ../ho.png" ," /f ../hi.png"] |
+ --------------------- + --------------------------------------------------------------- + ------------------------------- +

Algemene relay-ondersteuning
== == == == == == == == == ==

Mattermeest dagelijkse compliance-rapporten zijn compatibel met Global Relay-nalevingsoplossingen via de conversie van de Matterbest ` ` .CSV ` ` export naar Global Relay ` ` EML ` ` ` bestanden.

-Deze conversie kan gedaan worden door in-house ontwikkelaars die eerder geschreven scripts om andere communicatiesystemen om te zetten in Global Relay-formaat op basis van de specifieke behoeften van uw organisatie.
-U kunt ook contact opnemen met uw Global Relay-accountmanager over een serviceproject om deze conversie tot stand te brengen.

U kunt ook de nieuwe 'Compliance Export (Beta)-functie <https://docs.mattermost.com/cloud/cloud-administration/compliance-export.html>' _ gebruiken voor de export van Global Relay.
