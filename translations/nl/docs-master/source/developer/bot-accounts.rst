.. _bot-rekeningen:

Bot-accounts
== == == == == == == == == == == == == == == == == == == ==

Gebruik Bot Accounts om te integreren met Matterbest via ` plugins <https://developers.mattermost.com/extend/plugins/> ` _ of de ` Matterbest RESTful API <https://api.mattermost.com> ` _. Bot accounts toegang tot de RESTful API voor een bot door het gebruik van de :doc: ` personal access tokens functie <personal-access-tokens>`.

Bot accounts zijn net als gebruikersaccounts, met uitzondering van:

  -Kan niet ingelogd worden.
  -Kan niet gebruikt worden om andere bot accounts te maken.
  -Niet tellen als geregistreerde gebruiker en daarom niet meetwaarden voor de totale gebruikers van een licentie voor Enterprise Edition.

Aanvullende voordelen zijn:

  -Bot accounts kunnen worden ingeschakeld om te posten naar een kanaal in het systeem door systeembeheerders, met inbegrip van een prive-team, prive-kanaal of een Direct Message kanaal.
  -Integraties gemaakt door een gebruiker en gebonden aan een bot account niet meer breken als de gebruiker verlaat het bedrijf.
  -Eenmaal gemaakt, bot accounts gedragen net als gewone gebruikersaccounts en kan worden toegevoegd aan teams en kanalen vergelijkbaar met gebruikers.
  -Bot accounts zijn een veiliger manier om te integreren met Matterbest via de RESTful API en Plugin API, omdat er geen noodzaak is om gedeelde aanmeldingen te beheren met deze accounts.
  -` ` BOT ` ` tag wordt overal gebruikt in de UI waar bot accounts worden genoemd, waaronder berichten en gebruikerslijsten.

Merk op dat momenteel:

  -Bot accounts kunnen alleen worden gemaakt of beheerd door plugins of systeembeheerders.
  -Bot-accounts kunnen niet worden toegewezen aan webhooks of slash-opdrachten. Deze moeten nog steeds worden gemaakt door een gebruikersaccount.
  -Service-accounts zonder e-mailadres uit LDAP of SAML-systemen in Enterprise Edition worden nog niet ondersteund.

Als u verbeteringen wilt zien aan bot accounts, ' laat het ons weten in het Feature Proposal Forum <https://mattermost.uservoice.com> ` _. .. Inhoud:
  :backlinks: top
  :diepte: 1
  :lokaal:

Configuratie-instellingen
------------------------

Standaard kan plugins bot accounts aanmaken en beheren. Om het maken van het bot mogelijk te maken via de gebruikersinterface of de RESTful API:

1. Ga naar ** Systeemconsole > Integraties > Bot-accounts * *.
2. Instellen ** Inschakelen van Bot-account maken * * naar ` ` true ` ` `.

Eenmaal ingesteld kunnen systeembeheerders bot-accounts aanmaken voor integraties met behulp van de link ** Integraties > Bot-accounts * * in de opgegeven beschrijving.

Maken van bot-account
-----------------------

Hieronder zijn verschillende manieren om bot accounts te maken. Nadat het bot account is gemaakt, zorg ervoor dat:

1. Kopieer het gegenereerde bot toegangstoken voor uw integratie.
2. Voeg de bot account aan teams en kanalen die u wilt om te communiceren in.

Gebruikersinterface (UI) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

1. Ga naar ** Hoofdmenu > Integraties > Bot-accounts * *.
2. Klik op ** Add Bot Account * *.
3. Stel de ** Username** van de bot in. De gebruikersnaam moet beginnen met een letter en bevat tussen de 3 en 22 kleine letters, bestaande uit cijfers, letters en de symbolen ".", "-" en "_".
4. (Optioneel) Upload een afbeelding voor het pictogram ** Bot * *. Dit wordt gebruikt a
s het profielbeeld van de bot in de Mattermeeste gebruikersinterface.
5. (Optioneel) Stel een * * Weergavenaam * * en ** Beschrijving** in.
6. (Optioneel) Kies welke rol de bot moet hebben. De standaardwaarde is ** Member**. Als u ** System Admin * * toewijst, heeft de bot toegang tot schrijven in en lezen van alle openbare kanalen, private kanalen en directe berichten.
7. (Optioneel) Selecteer aanvullende machtigingen voor het account. Schakel de bot in om alle Mattermeeste kanalen, of alle Mattermeest openbare kanalen te posten.

Gebruik de RESTful API ` ` POST /bots ` ` voor het aanmaken van een bot. Moet toestemming hebben om bots te maken.

Zie onze ` API-documentatie <https: //api.mattermost.com/#tag/collision > ` _ voor meer informatie over het maken en beheren van bots via de API.

Om uw bot te machtigen via RESTful API gebruik ` ` curl -i -H 'autorisatie: Bearer <Access Token>' http://localhost: 8065/api/v4/users/me ` ` `. ** Access Token * * is niet het ` ` Token-ID ` ` en zal niet meer zichtbaar zijn als het eenmaal is gemaakt.

Command Line Interface (CLI) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

U kunt de volgende CLI-opdracht gebruiken om een bestaande gebruikersaccount te converteren naar een bot: .. code-blok :: tekst

  user converteren user@example.com -- bot

Naast e-mail kunt u de gebruiker identificeren met de gebruikersnaam of het gebruikers-ID.

Bot accounts die zijn geconverteerd van gebruikersaccounts zullen hun verificatiegegevens gewist als ze waren e-mail/wachtwoord accounts. De verificatiegegevens die door LDAP/SAML worden gesynchroniseerd, worden niet gewist, zodat LDAP/SAML-synchronisatie correct wordt uitgevoerd.

^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Plugins kunnen bot accounts aanmaken door middel van een ` ` EnsureBot ` ` helper-functie. Zie voor een voorbeeld ` the Demo Plugin <https: //github.com/mattermost/mattermost-plugin-demo/blob/master/server/configuration.go#L210-L217 > ` _.

Bots gemaakt door een plugin gebruik maken van de plugin's ID als de maker, tenzij anders aangegeven door de plugin.

Technische noten
-----------------------

Gegevensmodel ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Elk bot-account heeft een rij in de tabel ** Users** en de tabel ** Botswana **. De items zijn gekoppeld aan ` ` User.Id = Bot.UserId ` `.

Het Bots-tabelschema wordt als volgt beschreven: .. csv-table ::
    :header: "Veld", "Beschrijving", "Type", "Vereist"

    "UserId", "Gebruikers-ID van de bot gebruiker", "string", "Y" "Gebruikersnaam", "Gebruikersnaam van het bot-account", "string", "Y" "DisplayName", "Naam van het bot-account", "N" "Beschrijving", "Beschrijving van het bot-account", "string", "N" "OwnerId", "Gebruiker ID van de eigenaar van de bot", "string", "Y" "CreateAt", "Unix timestamp of creation time", "int64", "Y" "UpdateAt", "Unix timestamp of update time", "int64", "Y" "DeleteAt", "Unix timestamp of deletion time", "int64", "Y"

Veelgestelde vragen
-----------------------------

Moet ik al mijn integraties voor het gebruik van bot rekeningen migreren? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Voor uw integraties met behulp van RESTful API en plugins, ja. Om dit te doen, kunt u ofwel een bestaand account converteren naar een bot, of een nieuwe bot account maken met behulp van de bovenstaande stappen.

Als je eenmaal een bot account hebt gemaakt, gebruik dan het gegenereerde token om toegang te krijgen tot de RESTful API voor een bot en interactie in de Matterendste server.

Voor uw webhook-en slash-commando-integraties, kunt u ze niet migreren om bot accounts te gebruiken, omdat ze op dit moment een gebruikersaccount nodig hebben. Echter, een optie is om te migreren van de webhooks of slash-commando ' s naar een plugin, die op zijn beurt kan gebruik maken bot accounts.

Wat gebeurt er als een plugin een bot-account gebruikt dat al bestaat als een gebruikersaccount? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Voor een concreet voorbeeld, stel dat je de ` Matterbest GitHub plugin <https://github.com/mattermost/mattermost-plugin-github> ` _, die gebruik maakt van een ` ` github ` ` bot account, inschakelt, terwijl een bestaande ` ` github ` ` user account is gemaakt voor webhook integraties.

Zodra de plugin is ingeschakeld, de plugin posten als de ` ` github ` ` ` account, maar zonder een ` BOT ` tag. Er wordt een foutbericht vastgelegd in de serverlogboeken waarin de systeembeheerder wordt aanbevolen om de ` ` github ` ` ` gebruiker naar een bot-account te converteren door het uitvoeren van ` ` matterbest user convert <username> -- bot ` ` ` in de CLI.

Als de gebruiker een bestaand gebruikersaccount is dat u wilt behouden, wijzigt u de gebruikersnaam en start u de Matterendste server opnieuw, waarna de plugin een bot-account met de naam ` ` github ` ` maakt.

Hoe converteer ik een bestaande rekening naar een bot-account? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Gebruik de volgende CLI-opdracht om een bestaande gebruikersaccount te converteren naar een bot: .. code-blok :: tekst

  user converteren user@example.com -- bot

Naast e-mail kunt u de gebruiker identificeren met de gebruikersnaam of het gebruikers-ID.

Bot accounts die zijn geconverteerd van gebruikersaccounts zullen hun verificatiegegevens gewist als ze waren e-mail/wachtwoord accounts. De verificatiegegevens die door LDAP/SAML worden gesynchroniseerd, worden niet gewist, zodat LDAP/SAML-synchronisatie correct wordt uitgevoerd.

Hoe kan ik snel testen of mijn bot account werkt? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Voeg de bot toe aan een team en kanaal waar je bij hoort, gebruik dan de volgende curl commando om te posten met de bot: .. code-blok :: tekst

  curl -i -X POST -H 'Content-Type: application/json' -d '{ "channel_id": "<channel-id>", "bericht": "Dit is een bericht van een bot", "props": { "attachments": [ { "voorwendsel": "Look some text", "text": "This is text" }] } }' -H 'Authorization: Bearer <bot-access-token>' <mattermost-url>/api/v4/posts

de volgende parameters vervangen:

-` ` ` ` ` ` met het kanaal waaraan je de bot toevoegde
-` ` ` ` ` ` met het bot access token gegenereerd toen je de bot-account aangemaakt
-` ` ` ` ` ` met je Matterendste domein, bijvoorbeeld ` `https: //example.mattermost.com ` ` `

Vervalt de tokens voor de toegang tot bot? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Nee, maar u kunt uw integratie automatiseren om het token te rouleren met de REST API <https: //api.mattermost.com/#tag/users%2Fpaths%2F ~ 1users ~ 1%7Buser_id%7D ~ 1tokens%2Fpost> ` _.

Voor meer informatie over toegangstokens, zie :doc: ` de persoonlijke
toegang tot tokensdocumentation`.

Maken botrekeningen het gemakkelijker om iemand anders te imiteren zoals de CEO of een HR-coördinator? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Misschien wel. Op dit moment kan een System Admin uitschakelen van het overschrijven van de profielfoto en de gebruikersnaam van integraties om te voorkomen dat imitatie, maar dit is niet het geval voor bot accounts. Mitigations:

-` ` BOT ` ` tag wordt overal gebruikt in de UI waar bot accounts worden genoemd, waaronder berichten en gebruikerslijsten.
-Voor Direct Message kanalen maakt de kanaalheader onderscheid tussen de bot en een gewone gebruikersaccount met een ` ` BOT ` ` tag.

Wat gebeurt er wanneer een gebruiker die eigenaar is van bot accounts is uitgeschakeld? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Standaard worden bot-accounts die worden beheerd door de gedeactiveerde gebruiker uitgeschakeld voor verbeterde beveiliging. Degenen met permissies voor het beheren van bot accounts kunnen ze opnieuw inschakelen in ** Hoofdmenu > Integraties > Bot-accounts * *.

Wij raden sterk aan het creëren van nieuwe tokens voor de bot, om ervoor te zorgen dat de gebruiker die gedeactiveerd is niet langer toegang heeft tot lees-of schrijf gegevens in het systeem via het bot toegangstoken.

Als u liever een bot-account wilt hebben na deactivering van de gebruiker, stelt u ` ` DisableBotswana WhenOwnerIsDeactivated ` ` in op ` ` false ` ` in het ` `config.json ` ` bestand.

Kan bot accounts bewerken via de RESTful API ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

-Ja, Standaard kunnen bot accounts hun eigen berichten bijwerken.

Als u niet in staat bent om postings te bewerken als bot, controleer dan het volgende:
1. In plaats van een schuine streep te gebruiken om direct te reageren, gebruikt u een API-aanroep voor de eerste interactie met een gebruiker om berichtbewerkingen mogelijk te maken.
2. Als uw systeem gebruik maakt van ` advanced permissions <https://docs.mattermost.com/deployment/advanced-permissions.html> ` _, dan kan postedits worden uitgeschakeld voor gebruikers.

Als geen van de bovenstaande hulp om uw bezorgdheid op te lossen, hebt u ook de mogelijkheid om te kiezen welke rol de bot rekening heeft. Als System Admin is gekozen, kunnen ze alle berichten in het systeem bijwerken, samen met andere machtigingen voor Systeembeheer. Houd er rekening mee dat het geven van de rol Systeembeheer aan een bot-account hen in staat stelt met andere machtigingen voor systeembeheer, zodat dit met zorg moet gebeuren.

Als AD/LDAP of SAML sync ingeschakeld is, moet u bot accounts hebben om een e-mailadres in AD/LDAP of SAML te hebben? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Als AD/LDAP of SAML-synchronisatie is ingeschakeld, kunt u bot-accounts maken met behulp van de bovenstaande stappen. Deze bot accounts vereisen geen e-mailadres.

Als u service accounts van AD/LDAP of SAML naar Matterbest moet synchroniseren en ze als bot accounts gebruikt, ' please contact us <https://mattermost.com/contact-us> ` _ om in detail te bespreken. Het is niet nodig om service accounts te synchroniseren en ze te gebruiken als bot accounts om te voldoen aan uw use case.

Hoe worden bot-rekeningen geïdentificeerd in de nalevingsexport? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Vanaf v5.14 wordt een veld met de naam ` ` UserType ` ` toegevoegd aan de nalevingsexport, inclusief Global Relay, Actiance en CSV. Het veld geeft aan of een bericht is gepost door een ` ` gebruiker ` ` of door een ` ` t ` t ` ` rekening.
