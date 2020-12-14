Mattermeest incidentbeheer
== == == == == == == == == == == == == == ==

*Beschikbaar in Matterste Enterprise Edition E20, Mattervery Cloud Professional en Mattermeeste Cloud Enterprise.*

Incidenten zijn situaties die een onmiddellijke reactie vereisen en profiteren van een duidelijk omschreven proces dat leidt tot een oplossing. Met Mattermeeste Incident Management kan uw team incidenten vanuit Matterbest coördineren, beheren en oplossen. 

Een beter antwoord op een incident helpt u bij het bieden van meer betrouwbare diensten, naast het verkrijgen van inzichten met incidentrapporten en het opnemen van leerlingen met speelboeken.

-Automatisch een nieuw kanaal maken dat kan worden georganiseerd in de linker zijbalk met behulp van aangepaste categorieën.
-Gebruik playbooks om geautomatiseerde acties uit te voeren, zoals het maken van een Jira-ticket, start een Zoom oproep, of zoek uit wie is op-call in Opsgenie.
-iterate en verfijnen van processen na elk incident.

Wanneer incidenten worden bewaakt, gecoördineerd en effectief worden gemeten, kunt u transparantie toevoegen, de effectiviteit maximaliseren en kosten besparen door de tijd te besparen die nodig is om te reageren op incidenten en om incidenten op te lossen. .. Inhoud:
  :diepte: 2 :lokaal:
  :backlinks: item
  
API-documentatie
-----------------

De Matterbest Incident Management API-specificatie is beschikbaar ` hier <https://github.com/mattermost/mattermost-plugin-incident-management/blob/master/server/api/api.yaml> ` _.

Mattermeeste incidentbeheer installeren
-----------------------------------------

*Voor zelfbeheerde implementaties *

Mattermeeste Incident Management is beschikbaar in de Plugin Marketplace. U kunt downloaden en installeren van de plugin van Matterbest.

1. Open ** System Console > Plugin Management * *.
2. Zoek naar ** Incident Response * * met behulp van de zoekbalk of blader door de lijst handmatig.
3. Kies ** Install**.
4. Volgende, selecteer ** Configure**.
5. Selecteer ** true** om de plugin in te schakelen.
6. Kies ** Save**.

Als u het hoofdmenu opent, is ** Playbooks & Incidenten * * beschikbaar als menuoptie.

*Voor Cloud-implementaties *

Mattermeeste Incident Management is opgenomen in het Mattermeeste Cloud-werkgebied en is standaard ingeschakeld.

Schuine streep naar rechts
--------------------

Schuine strepen naar rechts zijn snelkoppelingen die worden gebruikt om acties in Matterbest uit te voeren. Als u de beschikbare schuine strepen naar links in Matterbest wilt bekijken, wordt boven het tekstinvoerveld de optie ' `/` ` en een lijst met opties voor schuine strepen naar links afgebeeld. De autocomplete suggesties helpen door het geven van een formaat voorbeeld in zwarte tekst en een korte beschrijving van de slash-commando in grijze tekst.

Mattermeeste Incident Management bevat ingebouwde schuine strepen naar links:

-` ` /incident start ` `-Start een nieuw incident.
-` ` /incident end ` `-Einde van een lopend incident.
-` ` /incidentherstart ` `-Een beëindigd incident opnieuw starten.
-` ` /incidentcontrole [ controlelijst #] [ item #] ` `-Check/uncheck het item in de controlelijst.
-` ` /incident kondigen ~ [ kanalen] ` ` `-Announce het huidige incident in andere kanalen.
-` ` /incidentlijst ` `-Lijst van al uw incidenten.
-` ` /incidentcommandant [@username] ` `-Toon of wijzig de huidige commandant.
-` ` /incident info ` `-Toon een som
Mary van het huidige incident.
-` ` /incidentstadium [ next/prev] ` `-Verplaatsen naar de volgende of vorige fase.

Het toevoegen van schuine strepen naar taken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Slash-opdrachten kunnen worden toegevoegd aan taken om acties te initiëren als onderdeel van uw afspeelboek.

Hier zijn enkele voorbeelden:

-Voeg een communicatietaak met de naam ** Sync omhoog * * met de slash-opdracht ` ` /zoom hello ` `. Als u de schuine streep naar rechts uitvoert, start u een inzoomen op het incidentkanaal. Als u Jitsi hebt geïnstalleerd, kunt u ` ` /jitsi hello ` ` gebruiken.-Een van uw taken kan vereisen dat de kanaalkop wordt gewijzigd in een nieuwe status. Maak een taak met de naam ** Change header * * met de slash-opdracht ` ` /header new header ` `.

Testgegevens genereren ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

U kunt de testopdrachten gebruiken om incidenten te maken die worden gevuld met willekeurige gegevens. Deze incidenten worden vermeld op de pagina voor het inzicht van het incident.

-` ` /incident test create-incident ` `: Deze opdracht accepteert een playbook-ID (dat kan worden gekozen uit de playbooks de gebruiker is lid van, met behulp van het autocomplete systeem), een tijdsaanduiding, en een incident naam. Hiermee wordt een permanent incident gemaakt met de aanmaakdatum die is ingesteld op de opgegeven tijdsaanduiding. Een voorbeeldopdracht ziet er als volgt uit: ` ` /incident test create-incident 6utgh6qg7p8ndeef9edc583cpc 2020-11-23 PR-Testing ` `.

-` ` /incident test bulk-data ` `: Deze opdracht accepteert een aantal lopende incidenten, een aantal beëindigd incidenten, een begin en een einddatum, en een optioneel zaad. Het creëert zo veel lopende en beëindigd incidenten zoals gespecificeerd, allemaal met hun aanmaakdatum willekeurig gekozen tussen de begin-en einddatum. Het zaad, indien beschikbaar, wordt gebruikt om reproduceerbare resultaten te verkrijgen. De namen van de incidenten worden willekeurig gekozen uit een lijst van incidentnamen en een lijst van valse bedrijfsnamen die in de code zijn gedefinieerd. Een voorbeeldopdracht is: ` ` /incident test bulk-data 10 3 2020-01-31 2020-11-22 2 ` `.

Speelboeken en incidenten
-----------------------

Incidenten en playbooks worden geassocieerd met teams in Matterbest. Incidentkanalen worden gemaakt op basis van afspeelboeken, die bepalen of een incidentkanaal openbaar of privé is. Lees meer over ` publieke en private kanalen <https://docs.mattermost.com/help/getting-started/organizing-conversations.html> ` _.

Alleen leden van het team waarin het afspeelboek of incident is gedefinieerd, hebben toegang. Playbook-lidmaatschap is onafhankelijk van het incident lidmaatschap.

-Leden van een draaiboek kunnen een incident starten met behulp van dat afspeelboek, en de etappes en stappen van het afspeelboek bewerken.
-Leden van een incident kunnen de huidige status van het incident wijzigen en nieuwe leden uitnodigen voor het incidentkanaal.

Tijdens een actief incident, wilt u zich richten op het triaging en het oplossen van het probleem zo snel mogelijk. Het plannen van uw incident ondersteuning strategie voor op tijd met playbooks is de beste manier om incidenten soepel verlopen. Een draaiboek is een recept voor het oplossen van een incident. In een playbook, kunt u vooruit plannen, zodat tijdens een incident responders precies weten wat te doen. Zorg ervoor dat u een retrospectieve analyse te plannen om te itereren op het ontwerp van uw playbooks na het incident eindigt.

Binnen elk playbook kunt u stadia en taken maken om ervoor te zorgen dat items worden geadresden en voltooid in sequentiële volgorde. De taken kunnen optioneel worden gekoppeld aan een schuine streep naar rechts en worden toegewezen aan afzonderlijke teamleden.

Eenmaal voltooid kunnen de incidentkanalen worden geëxporteerd met behulp van de optie voor het exporteren van kanalen voor analyse. Teams kunnen knelpunten in het incident identificeren door de tijdsverschillen te zien tussen het voltooien van checklistitems en het opnemen van de noodzakelijke wijzigingen in het afspeelboek voor volgend incident.

Een draaiboek maken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Er moet een afspeelboek worden gedefinieerd voordat een incident wordt gestart.

1. Navigeer naar ** Hoofdmenu > Playbooks & Incidenten * *.
2. Selecteer een sjabloon, of ** + Maak een Playbook * * om vanaf het begin een nieuw playbook te starten.
4. Naam uw draaiboek.
5. Wijzig de * * Standaardfase * *, het definiëren van een of meer stappen die moeten worden genomen door de leden van het incident.
   * Optioneel gebruiken beschrijvingen voor stappen om extra context toe te voegen voor leden van het incident. Beschrijvingen ondersteunen een beperkte vorm van markdown, met inbegrip van tekststijlen en hyperlinks.
   * Desgewenst kunt u een schuine streep naar rechts definiëren met de stap, waardoor de voltooiing van de stappen in het incident wordt vereenvoudigd.
6. Configureren of het incidentkanaal openbaar of privé moet zijn binnen het team.
7. Deel dit afspeelboek met andere leden van het team zodat ze het afspeelboek kunnen gebruiken om een incident te starten en de inhoud te bewerken.

Een afspeelboek bewerken ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

U kunt op elk gewenst moment een afspeelboek bewerken. De wijzigingen worden echter alleen toegepast op toekomstige incidenten-niet de actieve incidenten of incidenten die eerder dat afspeelboek hebben gebruikt.

Ga naar ** Hoofdmenu > Playbooks & Incidenten * * en selecteer het afspeelboek dat u wilt bewerken. U kunt:

-Wijzig het kanaaltype gemaakt met dit afspeelboek.
-Deel het draaiboek.
-Wis een stadium en de bijbehorende taken.
-Voeg nieuwe taken toe aan een bestaand stadium.
-Bewerk taken in een bestaand stadium.
-Bewerk de schuine streep naar rechts in bestaande taken.
-Voeg nieuwe stadia en taken toe.

Het verwijderen van een playbook ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

1. Navigeer naar ** Hoofdmenu > Playbooks & Incidenten * *.
2. Selecteer het menu ** Action** naast de naam van het afspeelboek.
3. Selecteer ** Delete**.
4. Bevestig dat u * * Afspeelboek * * wilt wissen.

Het starten van een incident ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Om een incident te starten, voert u een van de volgende stappen uit:

-Gebruik de schuine streep */incident starten * vanaf een willekeurig kanaal.
-Selecteer het afschermpictogram in de kanaalkop en selecteer ** + Incident starten * *.
-Gebruik het contextmenu van een bericht en selecteer ** Start incident * *.

U moet een afspeelboek selecteren en uw incident benoemen voordat u kunt selecteren ** Start Incident * *. De beschrijving van het incident is optioneel. Alleen afspeelboeken waarvan u lid bent, staan vermeld in het vervolgkeuzemenu ** Playbook**.

De maker van een incident wordt automatisch toegevoegd als eerste lid en wordt de gezagvoerder. Om commanders te veranderen, klikt u op de naam van de huidige commandant in de RHS en selecteert u de nieuwe commandant. Alleen leden van het kanaal m
ay worden geselecteerd als commandanten. Als u de commandant wilt wijzigen in een gebruiker die zich niet in het kanaal bevindt, voegt u de gebruiker eerst toe aan het kanaal.

Deelnemen aan een incident
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Wanneer een incident is gestart, wordt het toegevoegd aan de lijst van kanalen in het Mattermeeste team.

Als een incidentkanaal persoonlijke nieuwe deelnemers is, kunnen deze alleen worden toegevoegd aan een incidentkanaal door een kanaallid. Als het incident openbaar is, is er geen uitnodiging nodig-zoek naar, en join, het kanaal via ** Browse Kanalen * * in Matterbest.

Een incident beëindigen ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Incidentleden kunnen een incident beëindigen met de schuine streep naar rechts '` /incident' ` vanuit het incidentkanaal. Het beëindigen van een incidentsignaal voor alle deelnemers dat het probleem is opgelost.

Een incident opnieuw starten ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Een beëindigd incident kan op elk moment opnieuw worden gestart met ` ` /incident restart ` ` vanuit het incident kanaal of via ** Restart Incident * * in de RHS. Sommige playbooks kunnen stadia en taken definiëren om te voltooien nadat een incident is opgelost, zoals het plannen en voltooien van een post-mortem.

Status van incident en informatie
-------------------------------

Om de status van uw actieve incident (en) te bekijken selecteert u ** Hoofdmenu > Playbooks & Incidenten * *. Selecteer het tabblad ** Incident** om een lijst met incidenten in uw team te bekijken. Selecteer de incidentnaam om een samenvatting van het incident te bekijken, naar het kanaal te springen of het kanaal te exporteren.

Om informatie over lopende incidenten te bekijken, selecteert u het pictogram ** Incidenten ** in de kop van een kanaal om de RHS te openen waar alle lopende incidenten worden weergegeven. Selecteer ** Ga naar Incident Channel * * om het relevante kanaal te openen en zie:

-De incident commandant
-Het huidige stadium
-De resterende taken
-De voltooide taken

U kunt ook:

-Wijs een stap toe aan uzelf of een ander incidentlid.
-Mark een stap als ** Compleet ** of ** Incomplete**.
-Start een automatische actie.
-Nieuwe leden uitnodigen voor het kanaal.

Kanaal exporteren
--------------

Zie de ` Channel Export plugin-documentatie <https://mattermost.gitbook.io/channel-export-plugin> ` _ voor meer informatie. Woordenlijst --------

-** Commander:** De meest verantwoordelijke gebruiker die momenteel verantwoordelijk is voor de overgang van een incident van lopend naar einde.
-** Incident:** Een gebeurtenis die de gecoördineerde acties van een of meer Mattermeeste gebruikers vereist. Een incident is aan de gang of is beëindigd.
-** Incident kanaal: ** Een Mattermeeste kanaal gewijd aan real-time conversatie over het incident.
-** Incident insight-pagina: ** De incidentdetails en de analysepagina, die ook de downloadlink voor het kanaal exporteren. Het is niet beschikbaar op mobiel.
-** Incidentsectie: ** Een gebruiker die toegang heeft tot het corresponderende incidentkanaal.
-** Playbook:** Een op taken gebaseerd proces dat wordt gevolgd om een incident op te lossen.
-** Playbook-configuratiepagina: ** De afspeelboekconfiguratie en -bewerkingspagina. Het is niet beschikbaar op mobiel.
-** Stage:** Een geheel van taken die zijn gegroepeerd om een specifiek doel van de werkstroom te bereiken, die over het algemeen moet worden voltooid voordat u verder gaat met de volgende fase van het proces voor het oplossen van incidenten.
-** Tasks:** De afzonderlijke stappen die nodig zijn om de stadia van een incident te voltooien. Taken kunnen optioneel worden toegewezen aan specifieke incidentdeelnemers in fasen.
-** De RHS: ** De incidentlijst en de incidentgegevens die worden weergegeven aan de rechterkant (RHS) van de web-app. Het is niet beschikbaar op mobiel.
