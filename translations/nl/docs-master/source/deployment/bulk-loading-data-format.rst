.. _data-formaat:

Gegevensindeling
== == == == == =

Het invoergegevensbestand moet een geldige 'JSONL' zijn
<https://jsonlines.org> ` __ bestand met de volgende objecten, elk op een eigen regel in het bestand. De objecten moeten voorkomen in het bestand in de afgebeelde volgorde.

Versie Verplicht. Het versieobject moet de eerste regel in het bestand zijn en moet slechts één keer voorkomen. De versie is de versie van de bulk importeur tool, die momenteel ` ` 1 ` `. Scheme Optioneel. Indien aanwezig, moeten de programma-objecten na het versieobject maar vóór alle teamobjecten worden uitgevoerd.
Emoji Optioneel. Indien aanwezig, moeten Emoji-objecten optreden na de versie-objecten, maar vóór alle teamobjecten.
Team (optioneel). Teamobjecten moeten, indien aanwezig, worden uitgevoerd na alle objecten van de regeling en vóór eventuele kanaalobjecten.
Kanaal is optioneel. Als dit het geval is, moeten Kanaalobjecten na alle teamobjecten en voor alle gebruikersobjecten optreden.
Gebruiker (optioneel). Gebruikersobjecten moeten, indien aanwezig, worden uitgevoerd na de objecten van het team en het kanaal in het bestand en vóór eventuele postobjecten. Elk gebruikersobject definieert de teams en kanalen waarvan de gebruiker lid is. Als de bijbehorende teams en kanalen zich niet in het gegevensbestand bevinden, moeten ze aanwezig zijn in de database van Mattermost.
Post-facultatief. Indien aanwezig, moeten na het laatste gebruikersobject na het laatste gebruikersobject posten worden gebruikt, maar vóór alle DirectChannel-objecten. Elk Posterobject definieert het team, het kanaal en de gebruikersnaam van de gebruiker die het bericht heeft geplaatst. Als het bijbehorende team, kanaal of gebruiker zich niet in het gegevensbestand bevinden, moeten deze aanwezig zijn in de database van Mattermost.
DirectChannel-optioneel. Als dit het geval is, moeten DirectChannel-objecten na alle objecten in het bestand en vóór eventuele DirectPost-objecten worden uitgevoerd.
DirectPost (facultatief). Indien aanwezig, moeten DirectPost-objecten na alle andere objecten in het bestand optreden. Elk DirectPost-object definieert de gebruikersnamen van de kanaalleden en de gebruikersnaam van de gebruiker die het bericht heeft geplaatst. Als de bijbehorende gebruikersnamen niet in het gegevensbestand staan, moeten deze aanwezig zijn in de database Mattermost.

Met uitzondering van het versieobject heeft elk object een veld of een combinatie van velden die als uniek ID van dat object worden gebruikt. Het bulklaadprogramma gebruikt het unieke ID om te bepalen of het object dat wordt geïmporteerd een nieuw object of een update van een bestaand object is.

De ID's voor elk object staan in de volgende tabel: .. csv-table :: Objecten en hun unieke ID's
  :header: Object, Uniek ID

  Versie, Niet van toepassing, * naam *
  Rol, * naam *
  Emoji, * naam *
  Team, * naam *
  Kanaal, "* name*, * team*"
  Gebruiker, * gebruikersnaam *
  UserNotifyProps, * gebruikersnaam *
  UserTeamMembership, "* team*, * gebruikersnaam*"
  UserChannelMembership, "* team*, * channel*, * gebruikersnaam*"
  Post, "* channel*, * message*, * create_at*"
  Antwoord, "* post*, * message*, * create_at*"
  Reactie, "* post*, * emoji_name*, * create_at*"
  Bijlage, "* pad*"
  DirectChannel, * leden *
  DirectPost, "* channel_members*, * user*, * message*, * create_at *"

Het volgende fragment komt uit een bestand dat twee teams importeert, elk wi
Twee kanalen, veel gebruikers, en vele posten. .. code-block :: javascript :linenos:

  { "type": "versie", ... }
  { "type": "team", "team": { "name": "TeamA", ... } }
  { "type": "team", "team": { "name": "TeamB", ... } }
  { "type": "channel", "channel": { "team": "TeamA", "name": "ChannelA1", ... } }
  { "type": "channel", "channel": { "team": "TeamA", "name": "ChannelA2", ... } }
  { "type": "channel", "channel": { "team": "TeamB", "name": "ChannelB1", ... } }
  { "type": "channel", "channel": { "team": "TeamB", "name": "ChannelB1", ... } }
  { "type": "user", "user": { "username": "user001", ... } }
  { "type": "gebruiker", "gebruiker": { "gebruikersnaam": "user002", ... } }
  { "type": "user", "user": { "username": "user003", ... } }
  { "type": "gebruiker", ... }
  { "type": "gebruiker", ... }
  { "type": "gebruiker", ... }.
  .
  .
  { "type": "post", { "team": "TeamA", "name": "ChannelA1", "user": "user001", ... } }
  { "type": "post", { "team": "TeamA", "name": "ChannelA1", "user": "user001", ... } }
  { "type": "post", { "team": "TeamA", "name": "ChannelA1", "user": "user001", ... } }.
  .
  .

Versieobject
--------------

Het versieobject moet het eerste object in het gegevensbestand zijn en kan slechts één keer voorkomen.  De versie vertegenwoordigt de versie van het bulk import tool en is momenteel ` ` 1 ` ` `. 

Voorbeeld van versie-object
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Voor de duidelijkheid wordt het object afgebeeld met behulp van de reguliere JSON-opmaak, maar in het gegevensbestand kan het niet over meerdere regels worden verspreid. Het moet allemaal op één lijn staan. code-block :: javascript

  {
    "type": "version", "version": 1
  }

Velden van het versieobject
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">type</td>
      <td valign="middle">tekenreeks</td>
      <td>Moet de reeks "versie" zijn</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">versie</td>
      <td valign="middle"> getal</td>
      <td>Moet het getal 1 zijn.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
  </table>

Schema-object
-------------

Schema-objecten vertegenwoordigen Machtigingen schema's in het Mattermeeste machtigingen systeem. Indien aanwezig, moeten de programma-objecten na het versieobject en vóór eventuele teamobjecten worden uitgevoerd.

Voorbeeld Schema-object
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Voor de duidelijkheid wordt het object afgebeeld met behulp van de reguliere JSON-opmaak, maar in het gegevensbestand kan het niet over meerdere regels worden verspreid. Het moet allemaal op één lijn staan. code-block :: javascript

  {
    "type": "scheme", "scheme": {
      "naam": "custom_scheme_name", "display_name": "Custom Scheme Name", "description": "This is a custom override scheme.", "scope": "team", "default_team_admin_role": {
        "name": "custom_scheme_team_admin_role", "display_name": "Custom Scheme Team Admin Role", "description": "This is the default team admin role for the custom scheme.", "permissions": [ "add_user_to_team", "manage_team_roles"], }, "default_team_user_role": {
        "naam": "custom_scheme_team_user_role", "display_name": "Custom Scheme Team User Role", "description": "This is the default team user role for the custom scheme.", "permissions": [ "create_public_channel", "create_private_channel"], }, "default_channel_admin_role": {
        "naam": "custom_scheme_channel_admin_role", "display_name": "Custom Scheme Channel Admin Role", "description": "This is the default channel admin role for the custom scheme.", "permissions": [ "manage_private_channel_members", "manage_channel_roles"], }, "default_channel_user_role": {
        "naam": "custom_scheme_channel_user_role", "display_name": "Custom Scheme Channel User Role", "description": "This is the default channel user role for the custom scheme.", "permissions": [ "manage_public_channel_members", "manage_public_channel_properties"], }, }
  }

Velden van het object van de regeling
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ n~ ~ raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">naam</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van de regeling.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">weergavenaam</td>
      <td valign="middle"> tekenreeks</td>
      <td>De weergavenaam voor de regeling.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">bereik</td>
      <td valign="middle">tekenreeks</td>
      <td>Het bereik voor de regeling. Moet "team" of "channel" zijn.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">beschrijving</td>
      <td valign="middle">tekenreeks</td>
      <td>De beschrijving van de regeling.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">default_team_admin_role</td>
      <td valign="middle"><b>Rol</b> object</td>
      <td>De standaardrol die wordt toegepast op teambeheerders in teams die van deze regeling gebruikmaken. Dit veld is verplicht
Als het bereik van de regeling is ingesteld op "team", moet u anders <b>niet</b> aanwezig zijn.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">default_team_user_role</td>
      <td valign="middle"><b>Rol</b> object</td>
      <td>De standaardrol die wordt toegepast op teamgebruikers in teams die van deze regeling gebruikmaken. Dit veld is verplicht als het toepassingsgebied van het schema is ingesteld op "team", anders moet <b>niet</b> aanwezig zijn.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">default_channel_admin_role</td>
      <td valign="middle"><b>Rol</b> object</td>
      <td>De standaardrol die wordt toegepast op Kanaalbeheerders in kanalen die deze regeling gebruiken. Dit veld is verplicht voor zowel "team"-als "channel"-bereikschema's.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">default_channel_user_role</td>
      <td valign="middle"><b>Rol</b> object</td>
      <td>De standaardrol die wordt toegepast op kanaalgebruikers in kanalen die deze regeling gebruiken. Dit veld is verplicht voor zowel "team"-als "channel" -bereikschema's.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
  </table>

Velden van het rol-object
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Dit object is lid van het object van de regeling. .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">naam</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van de regeling.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">weergavenaam</td>
      <td valign="middle"> tekenreeks</td>
      <td>De weergavenaam voor de regeling.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">beschrijving</td>
      <td valign="middle">tekenreeks</td>
      <td>De beschrijving van de regeling.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">machtigingen</td>
      <td valign="middle">array</td>
      <td>De machtigingen die de rol moet verlenen. Dit is een array van tekenreeksen waarbij de tekenreeksen de namen zijn van individuele machtigingen in het Mattermeest-machtigingssysteem.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
  </table>

Emoji-object
------------

Emoji-objecten vertegenwoordigen aangepaste Emoji. Als dit het geval is, moeten de Emoji-objecten na het versieobject en vóór eventuele teamobjecten optreden.

Voorbeeld Emoji-object
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Voor de duidelijkheid wordt het object afgebeeld met behulp van de reguliere JSON-opmaak, maar in het gegevensbestand kan het niet over meerdere regels worden verspreid. Het moet allemaal op één lijn staan. code-block :: javascript

  {
  "type": "emoji", "emoji": {
    "naam": "custom-emoji-troll", "image": "bulkdata/emoji/trollolol.png "
    }
  }

Velden van het Emoji-object
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">naam</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van de emoji.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">afbeelding</td>
      <td valign="middle">tekenreeks</td>
      <td>Het pad (absoluut of relatief ten opzichte van de huidige werkdirectory) naar het afbeeldingsbestand voor deze emoji.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
  </table>

Teamobject
-----------

Als dit het geval is, moeten de teamobjecten na het versieobject en vóór de kanaalobjecten optreden.

Voorbeeld Team-object
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Voor de duidelijkheid wordt het object afgebeeld met behulp van de reguliere JSON-opmaak, maar in het gegevensbestand kan het niet over meerdere regels worden verspreid. Het moet allemaal op één lijn staan. code-block :: javascript

  {
  "type": "team", "team": {
    "naam": "teamnaam", "display_name": "Teamweergavenaam", "type": "O", "beschrijving": "Teambeschrijving", "allow_open_invite": true }
  }

Velden van het teamobject
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot><tr><td colspan="5">[ 1] Niet gevalideerd, maar er treedt een fout op als er geen sprake is van een dergelijke regeling in de werkstand Toepassen.</td></tr></tfoot>
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">naam</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van het team.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">weergavenaam</td>
      <td valign="middle">tekenreeks</td>
      <td>De weergavenaam voor het team.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">type</td>
      <td valign="middle">tekenreeks</td>
      <td>Het type team. U kunt een van de volgende waarden hebben:<br>
          <kbd>"O"</kbd> voor een open team<br>
          <kbd>"I"</kbd> voor een team van alleen een uitnodiging.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">beschrijving</td>
      <td valign="middle">tekenreeks</td>
      <td>De beschrijving van het team.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">allow_open_invite</td>
      <td valign="middle">bool</td>
      <td>Of u open uitnodigingen wilt toestaan. Moet een van de volgende waarden hebben:<br>
        <kbd>true</kbd><br>
        <kbd>false</kbd>
      </td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">schema</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van de regeling die moet worden toegepast op dit team.</td>
      <td align="center" valign="middle">Nee [ 1]</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
  </table>

Kanaalobject
--------------

Als dit het geval is, moeten Kanaalobjecten na alle teamobjecten en voor alle gebruikersobjecten optreden.

Kanaalobject voorbeeld
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Voor de duidelijkheid wordt het object afgebeeld met behulp van de reguliere JSON-opmaak, maar in het gegevensbestand kan het niet over meerdere regels worden verspreid. Het moet allemaal op één lijn staan. code-block :: javascript

  {
    "type": "kanaal", "kanaal": {
      "team": "teamnaam", "naam": "channel-name", "display_name": "Kanaalnaam", "type": "O", "header": "The Channel Header", "purpose": "The Channel Purpose", }
  }

Velden van het Kanaal-object
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot><tr><td colspan="5">[ 1] Niet gevalideerd, maar er treedt een fout op als er geen team/schema aanwezig is in de werkstand Toepassen.</td></tr></tfoot>
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">team</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van het team waartoe dit kanaal behoort.</td>
      <td align="center " valign="middle"> Nee [ 1]</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">naam</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van het kanaal.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">weergavenaam</td>
      <td valign="midd
le"> tekenreeks</td>
      <td>De weergavenaam voor het kanaal.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">type</td>
      <td valign="middle">tekenreeks</td>
      <td>Het type kanaal. Kan een van de volgende waarden hebben:<br>
          <kbd>"O"</kbd> voor een openbaar kanaal.<br>
          <kbd>"P"</kbd> voor een besloten kanaal.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">koptekst</td>
      <td valign="middle">tekenreeks</td>
      <td>De kanaalkop.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">doel</td>
      <td valign="middle">tekenreeks</td>
      <td>Het kanaaldoel.</td>
      <td align="center " valign="middle"> Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">schema</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van de regeling die moet worden toegepast op dit team.</td>
      <td align="center" valign="middle">Nee [ 1]</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
  </table>

Gebruikersobject
-----------

Gebruikersobjecten moeten, indien aanwezig, worden uitgevoerd na de objecten van het team en het kanaal in het bestand en vóór eventuele postobjecten.

Voorbeeld van gebruikersobject
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Voor de duidelijkheid wordt het object afgebeeld met behulp van de reguliere JSON-opmaak, maar in het gegevensbestand kan het niet over meerdere regels worden verspreid. Het moet allemaal op één lijn staan. code-block :: javascript

  {
    "type": "gebruiker", "gebruiker": {
      "profile_image": "avatar.png", "username": "username", "email": "email@example.com "," auth_service ":" "," auth_data ":" "," password ":" passw0rd "," bobuser "," first_name ":" Bob "," last_name ":" User "," position ":" Senior Developer "," roles ":" system_user "," locale ":" pt_BR "," teams ": [
        {
          "naam": "teamnaam", "thema": " {
              \" awayIndicator \": \"#DBBD4E\", \" buttonBg \": \"#23A1FF\", \" buttonColor \": \" centerChannelBg \": \"centerChannelBg\", \" centerChannelColor \": \" centerChannelColor \": \" codeTheme \", \" linkColor \": \" linkColor \": \" mentionBg \": \" mentionColor \": \"mentionHighlightBg\", \" mentionHighlightBg \": \"#2f81b7\", \" newMessageSeparator \": \" newMessageSeparator \": \"newMessageSeparator\", \" onlineIndicator \": \"onlineIndicator\", \" sidebarBg \": \"sidebarHeaderBg\", \" sidebarHeaderBg \": \"#3481B9\", \" sidebarHeaderTextColor \": \"sidebarHeaderTextColor\",
              \" sidebarText \": \"#333333\", \" sidebarTextActiveBorder \": \"#378FD2\", \" sidebarTextActiveColor \": \"sidebarTextActiveColor\", \" sidebarTextHoverBg \": \"#e6f2fa\", \" sidebarUnreadText \": \"#333333\", } "," rollen ":" team_user team_admin "," kanalen ": [
            {
              "naam": "channel-name", "roles": "channel_user", "notify_props": {
                "desktop": "default", "mark_unread": "all"
              }
            }
          ]
        }
      ]
    }
  }

Velden van het gebruikersobject
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">profielafbeelding</td>
      <td valign="middle">tekenreeks</td>
      <td>De profielafbeelding van de gebruiker. Dit moet een bestaand bestandspad zijn.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">gebruikersnaam</td>
      <td valign="middle">tekenreeks</td>
      <td>De gebruikersnaam van de gebruiker. Dit is het unieke ID voor de gebruiker.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">e-mail</td>
      <td valign="middle">tekenreeks</td>
      <td>Het e-mailadres van de gebruiker.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">auth_service</td>
      <td valign="middle">tekenreeks</td>
      <td>De verificatieservice voor dit gebruikersaccount. Als dit niet is opgegeven, wordt standaard verificatie op basis van wachtwoorden gebruikt. Moet een van de volgende waarden zijn:authentication<kbd>""</kbd> of niet aangeleverd-wachtwoordverificatie.<br>
        <kbd>"gitlab"</kbd> -GitLab-verificatie.<br>
        <kbd>"ldap"</kbd> -LDAP-verificatie (E10 en E20)<br>
        <kbd>"saml"</kbd> -Generieke SAML-verificatie (E20)<br>
        <kbd>"google"</kbd> -Google OAuth-verificatie (E20)<br>
        <kbd>"office365"</kbd> -Microsoft Office 365 OAuth Authentication (E20)</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">auth_data</td>
      <td valign="middle"> tekenreeks</td>
      <td>De verificatiegegevens als <kbd>auth_service</kbd> wordt gebruikt. De waarde is afhankelijk van de opgegeven <kbd>auth_service</kbd> .<br>
        De gegevens zijn afkomstig van de volgende velden voor de respectievelijke auth_services:<br>
        <kbd>""</kbd> of niet opgegeven-moet worden weggelaten.<br>
        <kbd>"gitlab"</kbd> -De waarde van het ID-kenmerk in de Gitlab auth-gegevens.<br>
        <kbd>"ldap"</kbd> -De waarde van het LDAP-kenmerk dat is opgegeven als het "ID-kenmerk" in de Mattermost LDAP-configuratie.<br>
        <kbd>"saml"</kbd> -De waarde van het kenmerk SAML Email address.<br>
        <kbd>"google"</kbd> -De waarde van het kenmerk OAuth-ID.<br>
        <kbd>"office365"</kbd> -De waarde van het kenmerk OAuth-ID.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">wachtwoord</td>
      <td valign="middle">tekenreeks</td>
      <td>Een wachtwoord voor de gebruiker. Kan alleen aanwezig zijn als er een op wachtwoord gebaseerde verificatie wordt gebruikt. Wanneer verificatie op basis van wachtwoorden wordt gebruikt en het wachtwoord niet aanwezig is, genereert het bulklaadprogramma een wachtwoord.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">roepnaam</td>
      <td valign="middle">tekenreeks</td>
      <td>De roepnaam van de gebruiker.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">voornaam</td>
      <td valign="middle">tekenreeks</td>
      <td>De voornaam van de gebruiker.</td>
      <td align="center " valign="middle"> Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">last_naam</td>
      <td valign="middle">tekenreeks</td>
      <td>De achternaam van de gebruiker.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">positie</td>
      <td valign="middle">tekenreeks</td>
      <td>De positie van de gebruiker.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">rollen</td>
      <td valign="middle"> tekenreeks</td>
      <td>De rollen van de gebruiker. Moet een van de volgende waarden zijn:<br>
        <kbd>"system_user"</kbd><br>
        <kbd>"system_admin system_user "</kbd></td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">locale</td>
      <td valign="middle">tekenreeks</td>
      <td>De locale van de gebruiker. Dit moet een geldige locale zijn waarvoor Mattermost is gelokaliseerd.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">delete_at</td>
      <td valign="middle">int64</td>
      <td>Tijdaanduiding voor wanneer de gebruiker is gedeactiveerd.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">teams</td>
      <td valign="middle">array</td>
      <td>De teams waarvan de gebruiker lid wordt. Dit moet een array zijn van <b>UserTeamMembership</b> -objecten.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">thema</td>
      <td valign="middle">tekenreeks</td>
      <td>Het thema van de gebruiker. Geformatteerd als een Mattermeest themalreeks.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">military_time</td>
      <td valign="middle">string</td>
      <td>Hoe vaak moet worden afgebeeld voor deze gebruiker. Moet een van de volgende waarden zijn:<br>
        <kbd>"true"</kbd> -24-uursnotatie gebruiken.<br>
        <kbd>"false"</kbd> -Gebruik 12 uur klok.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">inklap_previews</td>
      <td valign="middle">tekenreeks</td>
      <td>Of u de koppelingspreviews standaard wilt samenvouwen of uitvouwen. Moet een van de volgende waarden zijn:<br>
        <kbd>"true"</kbd> -Ingevouwen standaard.<br>
        <kbd>"false"</kbd> -Vervallen standaard.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">berichtvenster</td>
      <td valign="middle">tekenreeks</td>
      <td>Welke stijl voor afgebeelde berichten. Moet een van de volgende waarden zijn:<br>
        <kbd>"clean"</kbd> -Gebruik de standaardstijl.<br>
        <kbd>"compact"</kbd> -Gebruik de compacte stijl.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">channel_display_mode</td>
      <td valign="middle">tekenreeks</td>
      <td>Hoe kanaalberichten worden weergegeven. Moet een van de volgende waarden zijn:<br>
        <kbd>"full"</kbd> -Gebruik de volledige breedte van het scherm.<br>
        <kbd>"gecentreerd"</kbd> -Gebruik een vaste breedte, gecentreerd blok.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">bijlestutorial_step<td valign="middle">tekenreeks</td>
      <td>Waar het zelfstudieprogramma moet worden gestart. Moet een van de volgende waarden zijn:<br>
        <kbd>"1"</kbd>, <kbd>"2"</kbd> of <kbd>"3"</kbd> -Starten vanuit de opgegeven instructiestap.<br>
        <kbd>"999"</kbd> -Sla het zelfstudieprogramma over.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">use_markdown_preview</td>
      <td valign="middle">bool</td>
      <td>Voorbeeld van markdown-indeling van berichten inschakelen. Kan de volgende waarden hebben:<br>
          <kbd>"True"</kbd> <br>
          <kbd>"False"</kbd> </td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    <tr class="row-odd">
<td valign="middle">use_format</td>
      <td valign="middle">bool</td>
      <td>Post-indeling inschakelen voor links, emoji, tekststijlen en regeleinden. Kan een van de volgende waarden hebben:<br>
          <kbd>"True"</kbd> <br>
          <kbd>"False"</kbd> </td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    <tr class="row-odd">
      <td valign="middle">show_unread_section</td>
      <td valign="middle">bool</td>
      <td>Enable unread messages at top of channel sidebar. Kan een van de volgende waarden hebben:<br>
          <kbd>"True"</kbd> <br>
          <kbd>"False"</kbd> </td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
     <tr class="row-odd">
      <td valign="middle">email_interval</td>
      <td valign="middle">tekenreeks</td>
      <td>Geef een e-mailbatchinterval op tijdens het importeren van bulk. Kan een van de volgende waarden hebben:<br>
          <kbd>"immediate"</kbd> -Emails worden onmiddellijk verzonden.  <br>
          <kbd>"vijftien"</kbd> -Emails worden om de 15 minuten verzonden en verzonden.<br>
          <kbd>"uur"</kbd> -Emails worden elk uur verzonden.<br> </td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
     </tr>
    <tr class="row-odd">
      <td valign="middle">notify_props</td>
      <td valign="middle"><b>UserNotifyProps</b> -object</td>
      <td>De voorkeuren van de gebruiker, zoals gedefinieerd door hetobjectUserNotifyProps</b> -object.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
  </table>

Velden van het object UserNotifyProps
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Dit object is lid van het gebruikersobject. .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot><tr><td colspan="5">[ 1] Niet gevalideerd, maar er treedt een fout op als er geen team aanwezig is in de werkstand Toepassen.</td></tr></tfoot>
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">desktop</td>
      <td valign="middle">tekenreeks</td>
      <td>Preference voor het verzenden van desktopmeldingen. Moet een van de volgende waarden zijn:<br>
      <kbd>"all"</kbd> -Voor alle activiteiten.<br>
      <kbd>"vermelding"</kbd> -Alleen voor vermeldingen.<br>
      <kbd>"none"</kbd> -Nooit.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">desktop_sound</td>
      <td valign="middle">tekenreeks</td>
      <td>Preference for desktop notification sound. Moet een van de volgende waarden zijn:<br>
      <kbd>"true"</kbd> -Geluid wordt afgespeeld.<br>
      <kbd>"false"</kbd> -Geluid wordt niet afgespeeld.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">e-mail</td>
      <td valign="middle">tekenreeks</td>
      <td>Voorvoorkeur voor e-mailmeldingen. Moet een van de volgende waarden zijn:<br>
      <kbd>"true"</kbd> -E-mailmeldingen worden verzonden op basis van de instelling email_interval <br>
      <kbd>"false"</kbd> -E-mailmeldingen worden niet verzonden.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mobiel</td>
      <td valign="middle">tekenreeks</td>
      <td>Voorreferentie voor het verzenden van mobiele push-berichten. Moet een van de volgende waarden zijn:<br>
      <kbd>"all"</kbd> -Voor alle activiteiten.<br>
      <kbd>"vermelding"</kbd> -Alleen voor vermeldingen.<br>
      <kbd>"none"</kbd> -Nooit.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mobile_push_status</td>
      <td valign="middle">tekenreeks</td>
      <td>Preference voor wanneer push-berichten worden geactiveerd. Moet een van de volgende waarden zijn:<br>
      <kbd>"online"</kbd> -Wanneer online, afwezig of offline.<br>
      <kbd>"away"</kbd> -Wanneer afwezig of offline.<br>
      <kbd>"offline"</kbd> -Wanneer offline.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">kanaal</td>
      <td valign="middle">tekenreeks</td>
      <td>Of @all, @channel en @here worden geactiveerd. Moet een van de volgende waarden zijn:<br>
      <kbd>"true"</kbd> -Mentions worden geactiveerd.<br>
      <kbd>"false"</kbd> -Mentions worden niet geactiveerd.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">commentaar</td>
      <td valign="middle">tekenreeks</td>
      <td>Voorschrift voor antwoorden op antwoorden. Moet een van de volgende waarden zijn:<br>
      <kbd>"any"</kbd> -Triggermeldingen op berichten in antwoordthreads die de gebruiker start of neemt.<br>
      <kbd>"root"</kbd> -Triggermeldingen op berichten in threads die de gebruiker start.<br>
      <kbd>"never"</kbd> -Hiermee worden meldingen op berichten in antwoordthreads niet geactiveerd als de gebruiker wordt genoemd.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mentie_sleutels</td>
      <td valign="middle">tekenreeks</td>
      <td>Voorverwijzing voor aangepaste niet-hoofdlettergebruik Gevoelige woorden die melding maken. Woorden moeten van elkaar worden gescheiden door komma's.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
  </table>

Velden van het object UserTeamMembership
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Dit object is lid van het gebruikersobject. .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot><tr><td colspan="5">[ 1] Niet gevalideerd, maar er treedt een fout op als er geen team aanwezig is in de werkstand Toepassen.</td></tr></tfoot>
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">naam</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van het team dat deze gebruiker lid moet zijn.</td>
      <td align="center " valign="middle"> Nee [ 1]</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">thema</td>
      <td valign="middle">tekenreeks</td>
      <td>Het thema van de gebruiker voor het opgegeven team. Geformatteerd als een Mattermeest themalreeks.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">rollen</td>
      <td valign="middle">tekenreeks</td>
      <td>De rollen die de gebruiker binnen dit team moet hebben. Moet een van de volgende waarden zijn:<br>
          <kbd>"team_user"</kbd><br>
          <kbd>"team_admin team_user "</kbd>
      </td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">kanalen</td>
      <td valign="middle">array</td>
      <td>De kanalen in dit team waarvan de gebruiker lid moet worden. Dit moet een array zijn van <b>UserChannelMembership</b> -objecten.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
  </table>

Velden van het object UserChannelMembership
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Dit object is lid van het TeamMembership-object. .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot><tr><td colspan="5">[ 1] Niet gevalideerd, maar er treedt een fout op als het bovenliggende kanaal niet bestaat bij het uitvoeren van de toepassing.</td></tr></tfoot>
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">naam</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van het kanaal in het bovenliggende team dat deze gebruiker heeft moet lid zijn van.</td>
      <td align="center" valign="middle">Nee [ 1]</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">rollen</td>
      <td valign="middle">tekenreeks</td>
      <td>De rollen die de gebruiker binnen dit kanaal moet hebben. Moet een van de volgende waarden zijn:<br>
          <kbd>"channel_user"</kbd><br>
          <kbd>"channel_user channel_admin "</kbd>
      </td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">notify_props</td>
      <td valign="middle">object</td>
      <td>De voorkeuren voor berichten voor deze gebruiker in dit kanaal. Dit moet eenobjectChannelNotifyProps</b> -object zijn</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">favoriet</td>
      <td valign="middle">booleaansboolean<td>Of het kanaal het favoriet is. Moet een van de volgende waarden zijn:<br>
          <kbd>"true"</kbd> -Ja.<br>
          <kbd>"false"</kbd> -Nee.</td>
      </td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
  </table>

Velden van het object ChannelNotifyProps
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Geven

Dit object is lid van het object ChannelMembership. .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">desktop</td>
      <td valign="middle">tekenreeks</td>
      <td>Preference voor het verzenden van desktopmeldingen. Moet een van de volgende waarden zijn:<br>
      <kbd>"default"</kbd> -Algemene standaardwaarde.<br>
      <kbd>"all"</kbd> -Voor alle activiteiten.<br>
      <kbd>"vermelding"</kbd> -Alleen voor vermeldingen.<br>
      <kbd>"none"</kbd> -Nooit.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mobiel</td>
      <td valign="middle">tekenreeks</td>
      <td>Voorvoorkeur voor het verzenden van mobiele meldingen. Moet een van de volgende waarden zijn:<br>
      <kbd>"default"</kbd> -Globale standaardwaarde.<br>
      <kbd>"all"</kbd> -Voor alle activiteiten.<br>
      <kbd>"vermelding"</kbd> -Alleen voor vermeldingen.<br>
      <kbd>"none"</kbd> -Nooit.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mark_unread</td>
      <td valign="middle">tekenreeks</td>
      <td>Preference voor markeerkanaal als ongelezen. Moet een van de volgende waarden zijn:<br>
          <kbd>"all"</kbd> -Voor alle ongelezen berichten.<br>
          <kbd>"vermelding"</kbd> -Alleen voor vermeldingen.
      </td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
  </table>

Object posten
-----------

Na het laatste gebruikersobject in het bestand, maar vóór eventuele DirectChannel-objecten, moeten deze objecten na het laatste object van de gebruiker worden uitgevoerd.

Voorbeeld na object
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Voor de duidelijkheid wordt het object afgebeeld met behulp van de reguliere JSON-opmaak, maar in het gegevensbestand kan het niet over meerdere regels worden verspreid. Het moet allemaal op één lijn staan. code-block :: javascript

  {
    "type": "post", "post": {
      "team": "teamnaam", "channel": "channel-name", "user": "username", "message": "The post message", "props": {
        "bijlagen": [ {
          "Dit is het excuus van de bijlage", "tekst": "Dit is de bijlagetekst."
        }]
      }, "create_at": 140012340013, "flagged_by": [
        "gebruikersnaam1", "gebruikersnaam2", "gebruikersnaam3"
      ], "antwoorden": [ {
        "gebruiker": "gebruikersnaam4", "bericht": "Het antwoordbericht", "create_at": 140012352049, "bijlagen": [ {
            "path": "/some/valid/file/path/1"
        }], }, {
        "gebruiker": "gebruikersnaam5", "bericht": "Ander antwoordbericht", "create_at": 140012353057, }], "reacties": [ {
        "gebruiker": "gebruikersnaam6", "emoji_name": "+ 1", "create_at": 140012356032, }, {
        "gebruiker": "username7", "emoji_name": "heart", "create_at": 140012359034, }], "attachments": [ {
        "path": "/some/valid/file/path/1" }, {
        "pad": "/een/valid/bestand/pad/2"
      }]
    }
  }


Velden van het object Post
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ n~ ~ ~ ~ ~ raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot>
      <tr>
        <td colspan="5">[ 1] Niet gevalideerd, maar er treedt een fout op als het team niet bestaat bij het uitvoeren van de toepassing.<br>
        [ 2] Niet gevalideerd, maar er treedt een fout op als het kanaal niet aanwezig is in het bijbehorende team bij het uitvoeren van de werkstand toepassen.<br>
        [ 3] Niet gevalideerd, maar er treedt een fout op als de gebruiker niet bestaat bij het uitvoeren van de werkstand Toepassen.
        </td>
      </tr>
    </tfoot>
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">team</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van het team waarin deze post zich bevindt.</td>
      <td align="center" valign="middle">Nee [ 1]</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle"> kanaal</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van het kanaal waarin deze post zich bevindt.</td>
      <td align="center" valign="middle">Nee [ 2]</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">gebruiker</td>
      <td valign="middle">tekenreeks</td>
      <td>De gebruikersnaam van de gebruiker voor deze post.</td>
      <td align="center" valign="middle">Nee [ 3]</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">bericht</td>
      <td valign="middle">tekenreeks</td>
      <td>Het bericht dat de posting bevat.</td>
      <td align="cent
" valign="middle"> Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">props</td>
      <td valign="middle">object</td>
      <td>De rekwi's voor een post. Bevat extra opmaakinformatie die wordt gebruikt door integraties en bot posts. Voor een meer gedetailleerde uitleg raadpleegt u de <a href="https://docs.mattermost.com/developer/message-attachments.html">documentatie van berichtbijlagen</a>.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle">int</td>
      <td>De tijdsaanduiding voor de posting, in milliseconden sinds de Unix-periode.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">flagged_by</td>
      <td valign="middle">Matrix</td>
      <td>Moet een lijst bevatten van leden die de post hebben gemarkeerd.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">antwoorden</td>
      <td valign="middle">array</td>
      <td>De posts in antwoord op deze post. Dit moet een array zijn van <a href="#fields-of-the-reply-object">Beantwoorden</a> objecten.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">reacties</td>
      <td valign="middle">array</td>
      <td>De emoji-reacties op deze post. Dit moet een array zijn van <a href="#fields-of-the-reaction-object">Reactie</a> -objecten.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">bijlagen</td>
      <td valign="middle">array</td>
      <td>Bestandsbijlagen die aan dit bericht zijn gekoppeld. Dit moet een array zijn van <a href="#fields-of-the-attachment-object">Attachment</a> -objecten.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
  </table>

Velden van het antwoordobject
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Dit object is lid van het object Post/DirectPost. .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">gebruiker</td>
      <td valign="middle">tekenreeks</td>
      <td>De gebruikersnaam van de gebruiker voor dit antwoord.</td>
      <td align="center" valign="middle">Nee [ 3]</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">bericht</td>
      <td valign="middle">tekenreeks</td>
      <td>Het bericht dat het antwoord bevat.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    <td align="center" valign="middle"><tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle">int</td>
      <td>De tijdsaanduiding voor het antwoord, in milliseconden sinds de Unix-periode.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    <td align="center" valign="middle"><tr class="row-odd">
      <td valign="middle">flagged_by</td>
      <td valign="middle">array</td>
      <td>Moet een lijst van leden bevatten die hebben .Nee</td>
      <td align="center" valign="middle"><td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">reacties</td>
      <td valign="middle">array</td>
      <td>De emoji-reacties op deze post. Dit moet een array zijn van <a href="#fields-of-the-reaction-object">reactie</a> -objecten.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">bijlagen</td>
      <td valign="middle">matrix</td>
      <td>De bestandsbijlagen van deze post. Dit moet een array zijn van <a href="#fields-of-the-attachment-object">Attachment</a> -objecten.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
  </table>

Velden van het reactieobject
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Ng~

Dit object is lid van het object Post/DirectPost. .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">gebruiker</td>
      <td valign="middle">tekenreeks</td>
      <td>De gebruikersnaam van de gebruiker voor dit antwoord.</td>
      <td align="center" valign="middle">Nee [ 3]</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">emoji_name</td>
      <td valign="middle">tekenreeks</td>
      <td>De emoji van de reactie.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle">int</td>
      <td>De tijdsaanduiding voor het antwoord, in milliseconden sinds het Unix-tijdperk.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
  </table>

Velden van het bijlageobject
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Vragen

Dit object is lid van het object Post/DirectPost. .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
   <tfoot>
      <tr>
        <td colspan="5">
          [ 1] Niet gevalideerd, maar er treedt een fout op als het bestandspad niet wordt gevonden of toegankelijk is tijdens het uitvoeren van de toepassing.
        </td>
      </tr>
    </tfoot>
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">pad</td>
      <td valign="middle">tekenreeks</td>
      <td>Het pad naar het bestand dat aan de post moet worden gekoppeld.</td>
      <td align="center" valign="middle">Nee [ 1]</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
  </table>

DirectChannel-object
--------------------

Een direct kanaal kan van twee tot acht gebruikers zijn als leden van het kanaal. Als er slechts twee leden zijn, behandelt Matterbest het als een Direct Message kanaal. Als er drie of meer leden zijn, behandelt Matterbest het als een groepsberichtenkanaal.

Voorbeeld DirectChannel-object
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Voor de duidelijkheid wordt het object afgebeeld met behulp van de reguliere JSON-opmaak, maar in het gegevensbestand kan het niet over meerdere regels worden verspreid. Het moet allemaal op één lijn staan. code-block :: javascript

  {
    "type": "direct_channel", "direct_channel": {
      "leden": [
        "gebruikersnaam1", "gebruikersnaam2", "gebruikersnaam3"
      ], "header": "The Channel Header", "favorited_by": [
        "gebruikersnaam1", "gebruikersnaam2", "gebruikersnaam3"
      ]
    }
  }

Velden van het DirectChannel-object
~ ~ ~ ~ nopen ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot>
      <tr>
        <td colspan="5">[ 1] Niet gevalideerd, maar er treedt een fout op als een of meer van de gebruikers niet bestaan wanneer ze actief zijn.
        </td>
      </tr>
    </tfoot>
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">leden</td>
      <td valign="middle">array</td>
      <td>Moet een lijst van leden bevatten, met een minimum van twee gebruikersnamen en maximaal acht gebruikersnamen.</td>
      <td align="center" valign="middle">Nee [ 1]</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">koptekst</td>
      <td valign="middle">tekenreeks</td>
      <td>De kanaalkop.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">favorited_by</td>
      <td valign="middle">array</td>
      <td>Moet een lijst bevatten van leden die het kanaal hebben begunstigd.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center " valign="middle"> Nee</td>
    </tr>
  </table>

DirectPost-object
-----------------

DirectPost-objecten moeten worden uitgevoerd na alle andere objecten in het bestand.

Voorbeeld DirectPost-object
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Voor de duidelijkheid wordt het object afgebeeld met behulp van de reguliere JSON-opmaak, maar in het gegevensbestand kan het niet over meerdere regels worden verspreid. Het moet allemaal op één lijn staan. code-block :: javascript

  {
    "type": "direct_post", "direct_post": {
      "kanaal_leden": [
        "gebruikersnaam1", "gebruikersnaam2", "gebruikersnaam3",], "gebruiker": "gebruikersnaam2", "bericht": "Hallo Groep Kanaal", "create_at": 140012340013, "flagged_by": [
        "gebruikersnaam1", "gebruikersnaam2", "gebruikersnaam3"
      ], "antwoorden": [ {
        "gebruiker": "gebruikersnaam4", "bericht": "Het antwoordbericht", "create_at": 140012352049, }, {
        "gebruiker": "gebruikersnaam5", "bericht": "Ander antwoordbericht", "create_at": 140012353057, }], "reacties": [ {
        "gebruiker": "gebruikersnaam6", "emoji_name": "+ 1", "create_at": 140012356032, }, {
        "gebruiker": "gebruikersnaam7", "emoji_name": "heart", "create_at": 140012359034, }]
    }
  }

Velden van het object DirectPost
~ ~ ~ ~ ~ ~ A ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot>
      <tr>
        <td colspan="5">[ 1] Niet gevalideerd, maar er treedt een fout op als er geen kanalen een identieke lijst bevatten als deze in de werkstand Toepassen wordt uitgevoerd.<br>[ 2] Niet gevalideerd, maar er treedt een fout op als de gebruiker niet bestaat bij het uitvoeren van de toepassing.
        </td>
      </tr>
    </tfoot>
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
      <th class="head">Validated</th>
      <th class="head">Verplicht</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle"> channel_members</td>
      <td valign="middle">array</td>
      <td>Moet een lijst van leden bevatten, met minimaal twee gebruikersnamen en maximaal acht gebruikersnamen.</td>
      <td align="center" valign="middle">Nee [ 1]</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">gebruiker</td>
      <td valign="middle">tekenreeks</td>
      <td>De gebruikersnaam van de gebruiker voor deze post.</td>
      <td align="center" valign="middle">Nee [ 2]</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">bericht</td>
      <td valign="middle"> tekenreeks</td>
      <td>Het bericht dat de post bevat.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle"><tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle">int</td>
      <td>De tijdsaanduiding voor de post, in milliseconden sinds de Unix-periode.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Ja</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">flagged_by</td>
      <td valign="middle">array</td>
      <td>Moet een lijst bevatten van leden die de vlag hebben gemarkeerd van de post.</td>
      <td align="center" valign="middle">Nee</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">antwoorden</td>
      <td valign="middle">array</td>
      <td>De posts in antwoord op deze directe post. Dit moet een array zijn van <a href="#fields-of-the-reply-object">Beantwoorden</a> objecten.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">reacties</td>
      <td valign="middle">array</td>
      <td>De emoji-reacties op deze directe post. Dit moet een array zijn van <a href="#fields-of-the-reaction-object">reactie</a> -objecten.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
        <tr class="row-odd">
      <td valign="middle">bijlagen</td>
      <td valign="middle">matrix</td>
      <td>De bijlagen bij deze directe post. Dit moet een array zijn van <a href="#fields-of-the-attachment-object">Attachment</a> -objecten.</td>
      <td align="center" valign="middle">Ja</td>
      <td align="center" valign="middle">Nee</td>
    </tr>
  </table>
