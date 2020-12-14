Uitgebreide ondersteuning release
== == == == == == == == == == == ==

Wat is een Extended Support Release?
------------------------------------ Tijdens elke maandelijkse release zijn Matterbest-backports hoge of hoge beveiligingsfixes voor de severity van de vorige drie maandelijkse releases. Uitgebreide Support Releases (ESR ' s) zijn releases die backports ontvangen voor beveiligingsfixes en grote bug fixes voor de lengte van hun levenscyclus. .. Belangrijk:
  Ondersteuning voor server ` Extended Support Release <https://docs.mattermost.com/administration/extended-support-release.html> ` _ (ESR) 5.19 is tot het einde van de levenscyclus gekomen. Upgraden naar server v5.25 of hoger is vereist.

Wat is de levenscyclus van een Extended Support Release?
------------------------------------------------------ De meeste zorgen voor een ESR wanneer er een aanzienlijk aantal nieuwe functies en verbeteringen aan het product zijn toegevoegd en deze nieuwe functies voldoende tijd hebben gehad om zich te stabiliseren. Een nieuw ESR wordt tweemaal per jaar uitgebracht in januari en juli. Een ESR wordt gedurende 9 maanden ondersteund om klanten voldoende tijd te geven om te testen en te upgraden naar het volgende ESR.

Wanneer een ESR aan het einde van zijn levenscyclus staat, zullen er vooraf aankondigingen worden gedaan om de mensen tijd te geven om een nieuwere ESR-versie te testen, te certificeren en in gebruik te nemen voordat de ondersteuning eindigt. Er wordt een duidelijk upgradepad opgegeven tussen de ESR-versies. 

Nadat een release zijn einde van het leven bereikt, zullen er geen verdere updates voor die versie worden verstrekt.

Zie 'Release Lifecycle documentation <https://docs.mattermost.com/administration/release-lifecycle.html>' voor een volledige lijst van levenscycli voor elke release van Matterit.

Om updates te ontvangen over Extended Support Releases, meld u aan voor onze maillijst ` hier <https://eepurl.com/dCKn2P> ` __. .. afbeelding:: ../images/ESR20212.png

Wat is opgenomen in een Extended Support Release dot release? 
------------------------------------------------------------ De releases voor ESR-versies bevatten hoge-of hoge-impactbeveiligingsfixes en bugrapefixes. Ze bevatten geen wijzigingen van de productfunctionaliteit of nieuwe functies. 

Wie moet gebruik maken van een Extended Support Release? 
------------------------------------------- ESR's zijn bedoeld voor organisaties die stabiliteit hechten aan de nieuwste functies en verbeteringen, of die een lang intern test-en certificeringsproces hebben om te worden onderworpen aan een upgrade.

Als uw organisatie er de voorkeur aan geeft om de nieuwste functies en verbeteringen te hebben, is het mogelijk dat Extended Support Releases niet de beste oplossing voor u is.

Hoe installeer ik de Extended Support Release?
---------------------------------------------- Volg onze normale ` install <https: //docs.mattermost.com/guides/administrator.html#installing-mattermost> ` __ of ` upgrade <https://docs.mattermost.com/administration/upgrade.html> ` __ guides. Volg de ` belangrijke upgrade notes <https://docs.mattermost.com/administration/important-upgrade-notes.html> ` _ voor alle versies sinds de huidige ESR-versie die u momenteel hebt geïnstalleerd. Zie ook ' het changelog < https: //
docs.mattermost.com/administration/changelog.html> ` _ voor een lijst van database-, API-en config.json-updates voor elke release.

Bij het downloaden van de Matterbest versie kiest u een Extended Support Release uit de onderstaande lijst.

Wat zijn de ondersteunde versies van de Extended Support Release? 
----------------------------------------------------------------- + ------------- + ---------------- + ------------------ + ------------------ + -------------------------------------------------------------------------------------------- + -----------------------------------------------------
| Versie | Release Datum | Einde van ondersteuning | Einde van ondersteuning | Laatste Dot Release downloaden link | Upgrade Notes | + == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
| 5.25 | Kwaliteit | 16 juli 2020 | 15 april 2021 | ` 5.25.7 <https://releases.mattermost.com/5.25.7/mattermost-5.25.7-linux-amd64.tar.gz> ` _ | De xmlsec1-gebaseerde SAML bibliotheek is uitgeschakeld in |
| | | | | | |-gunst van de opnieuw ingeschakelde en verbeterde SAML-bibliotheek | + ------------- + ---------------- + ------------------ + ------------------ + -------------------------------------------------------------------------------------------- + ----------------------------------------------------- +
| 5.19 | Kwaliteit | 16 januari 2020 | 15 oktober 2020 | ` 5.19.3 <https://releases.mattermost.com/5.19.3/mattermost-5.19.3-linux-amd64.tar.gz> ` _ | | + ------------- + ---------------- + ------------------ + ------------------ + -------------------------------------------------------------------------------------------- + ----------------------------------------------------- +
| 5.9 | Kwaliteit | 16 april 2019 | 15 april 2020 | ` 5.9.8 <https://releases.mattermost.com/5.9.8/mattermost-5.9.8-linux-amd64.tar.gz> ` _ | Upgrade naar 5.0 voordat u een upgrade uitvoert naar 5.9 | + ------------- + ---------------- + ------------------ + ------------------ + -------------------------------------------------------------------------------------------- + ----------------------------------------------------- +
| 4.10 | Kwaliteit | Mei 16, 2018 | 15 juli 2019 | ` 4.10.10 <https://releases.mattermost.com/4.10.10/mattermost-4.10.10-linux-amd64.tar.gz> ` _ | |
+ ------------- + ---------------- + ------------------ + ------------------ + -------------------------------------------------------------------------------------------- + -----------------------------------------------------

Hoe herstel ik een eerdere Extended Support Release?
----------------------------------------------------- Voordat u een upgrade uitvoert, zorg er dan voor dat u een volledige backup hebt gemaakt van uw huidige versie.  U kunt de database en de vorige versie herstellen als u een upgrade wilt aanbrengen.  Houd er rekening mee dat eerdere ESR-versies aan het einde van de ondersteuningsdatum vallen.

Waarom wordt een Extended Support Release ondersteund voor 9 maanden en niet langer?
------------------------------------------------------------------------- We hebben 9 maanden gekozen omdat de overhead voor het onderhouden van een ESR hoog is (en hoger wordt hoe langer het ondersteuningstijdvak is).
Als we het steunvenster verhogen, vermindert het hoeveel we het product kunnen ontwikkelen. We hebben specifiek gekozen "ESR" in plaats van "LTS", omdat het niet bedoeld is om een multi-jaar lange termijn ondersteuning release te zijn. De termijn van 9 maanden wordt in geen geval verlengd.

Kunnen klanten betalen voor uitgebreide ondersteuning?
--------------------------------------- Op dit punt zijn we niet van plan om klanten te laten betalen voor uitgebreide ondersteuning, maar we zijn open om te bespreken opties voor dit. Neem contact op met uw Customer Success Manager als u aanvullende vereisten hebt voor uitgebreide ondersteuning.

Hoe waarschuwen we klanten over nieuwe en gedeprecieerde Extended Support Releases?
------------------------------------------------------------------------------

Voor een nieuw komende ESR, sturen we een e-mail aankondiging 2 maanden van tevoren. We voegen ook een herinnering aan onze release aankondiging, changelog en via een Forum post (` zie voorbeeld <https://forum.mattermost.org/t/upcoming-extended-support-release-updates/8526> ` _).

Voor een gedeprecieerde ESR sturen we 3 maanden van tevoren een email aankondiging. We voegen ook herinneringen toe aan onze release aankondigingen, changelogs, ` belangrijke upgrade notes <https://docs.mattermost.com/administration/important-upgrade-notes.html> ` _, en onze ` Forum site <https://forum.mattermost.org/> ` _.

Om updates te ontvangen over Extended Support Releases, meldt u zich aan voor onze maillijst ` hier <https://eepurl.com/dCKn2P> ` _.
