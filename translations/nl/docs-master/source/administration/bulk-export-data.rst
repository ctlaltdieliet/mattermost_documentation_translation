Gegevens voor bulkuitvoer
== == == == == == == ==

Op dit moment ondersteunt de export kenmerken van de onderstaande objecten. Alle Mattermeeste Bulk Export-gegevensbestanden beginnen met een ` Version ` object als de eerste regel van het bestand. Dit geeft de versie aan van de bestandsindeling Matterelijkste Bulkimport waarmee de geëxporteerde gegevens compatibel zijn.

U kunt de volgende gegevenstypen exporteren:

-Teams
-Kanalen (openbaar en privé)
-Gebruikers
-Teamlidmaatschappen van gebruikers
-Gebruikers ' Kanaal lidmaatschappen
-meldingsvoorkeuren voor gebruikers
-Ambten (vaste, niet-repliek)
-Posts ' antwoorden
-Reacties
-Aangepaste Emoji
-Directe berichtenkanalen
-Directe berichten berichten .. opmerking:: Configuratie voor gegevenstypen, zoals het exporteren van specifieke gebieden van de server, het exporteren van extra typen berichten, machtigingen, bestandsbijlagen, webhooks en bot-berichten wordt nog niet ondersteund. Gewiste objecten worden ook nog niet ondersteund. Voor verzoeken om aanvullende attributen of objecten aan onze exporteur toe te voegen, voeg een functieaanvraag toe op ons ` feature idea forum <https://mattermost.uservoice.com/forums/306457-general> ` __.

Versieobject
-------------- .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">type</td>
      <td valign="middle">tekenreeks</td>
      <td>De tekenreeks "versie"</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">versie</td>
      <td valign="middle">nummer</td>
      <td>Het getal 1.</td>
    </tr>
  </table>
  
Teamobject
----------- .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">naam</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van het team.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">display_name</td>
      <td valign="middle">string</td>
      <td>De weergavenaam voor het team.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">type</td>
      <td valign="middle">tekenreeks</td>
      <td>Het type team. Er is een van de volgende waarden:<br>
          <kbd>"O"</kbd> voor een open team<br>
          <kbd>"I"</kbd> voor een team van alleen een uitnodiging.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">beschrijving</td>
      <td valign="middle">tekenreeks</td>
      <td>De beschrijving van het team.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">allow_open_invite</td>
      <td valign="middle">bool</td>
      <td>Of u open uitnodigingen wilt toestaan. Een van de volgende waarden heeft:<br>
        <kbd>"true"</kbd><br>
        <kbd>"false"</kbd></td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">schema</td>
      <td valign="mid
dle"> tekenreeks</td>
      <td>De naam van de machtigingsschema's die van toepassing is op dit team.</td>
    </tr>
  </table>

Kanaalobject
-------------- .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">team</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van het team waartoe dit kanaal behoort.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">naam</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van het kanaal.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">weergavenaam</td>
      <td valign="middle">tekenreeks</td>
      <td>De weergavenaam voor het kanaal.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">type</td>
      <td valign="middle">tekenreeks</td>
      <td>Het type kanaal. U hebt een van de volgende waarden:<br>
          <kbd>"O"</kbd> voor een openbaar kanaal.<br>
          <kbd>"P"</kbd> voor een besloten kanaal.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">header</td>
      <td valign="middle">string</td>
      <td>The channel header.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">purpose</td>
      <td valign="middle">string</td>
      <td>The channel purpose.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">scheme</td>
      <td valign="middle">string</td>
      <td>De naam van het machtigingsschema dat van toepassing is op dit team.</td>
    </tr>
  </table>
  
Gebruikersobject
----------- .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">gebruikersnaam</td>
      <td valign="middle">tekenreeks</td>
      <td>De gebruikersnaam van de gebruiker. Dit is het unieke ID voor de gebruiker.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">e-mail</td>
      <td valign="middle">tekenreeks</td>
      <td>Het e-mailadres van de gebruiker.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">auth_service</td>
      <td valign="middle">string</td>
      <td>De verificatieservice voor dit gebruikersaccount. Dit veld is niet aanwezig voor gebruiker/wachtwoordverificatie.<br>
        <kbd>"gitlab"</kbd> -GitLab-verificatie.<br>
        <kbd>"ldap"</kbd> -LDAP-verificatie (E10 en E20)<br>
        <kbd>"saml"</kbd> -Algemene verificatie op basis van SAML (E20)<br>
        <kbd>"google"</kbd> -Google OAuth-verificatie (E20)<br>
        <kbd>"office365"</kbd> -Microsoft Office 365 OAuth Authentication (E20)</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">auth_data</td>
      <td valign="middle">string</td>
      <td>De verificatiegegevens als <kbd>auth_service</kbd> wordt gebruikt. De waarde is afhankelijk van de opgegeven <kbd>auth_service</kbd> .<br>
        De gegevens zijn afkomstig van de volgende velden voor de respectievelijke auth_services:<br>
        <kbd>"gitlab"</kbd> -De waarde van het ID-kenmerk in de GitLab auth-gegevens.<br>
        <kbd>"ldap"</kbd> -De waarde van het LDAP-kenmerk dat is opgegeven als het "ID-kenmerk" in de Mattermost LDAP-configuratie.<br>
        <kbd>"saml"</kbd> -De waarde van het kenmerk voor het SAML-e-mailadres.<br>
        <kbd>"google"</kbd> -De waarde van het kenmerk OAuth-ID.<br>
        <kbd>"office365"</kbd> -De waarde van het kenmerk OAuth-ID.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">roepnaam</td>
      <td valign="middle">tekenreeks</td>
      <td>De bijnaam van de gebruiker.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">voornaam</td>
      <td valign="middle">tekenreeks</td>
      <td>De voornaam van de gebruiker.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">last_naam</td>
      <td valign="middle">tekenreeks</td>
      <td>De achternaam van de gebruiker.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">positie</td>
      <td valign="middle">tekenreeks</td>
      <td>De positie van de gebruiker.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">rollen</td>
      <td valign="middle">tekenreeks</td>
      <td>De rollen van de gebruiker. </td>
    </tr>
    <tr class="row-odd">
      <td valign="middle"> locale</td>
      <td valign="middle">tekenreeks</td>
      <td>De lokalisatieconfiguratie van de gebruiker.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">use_markdown_preview</td>
      <td valign="middle">bool</td>
      <td><kbd>"true"</kbd> als de gebruiker markdown-preview heeft ingeschakeld in het invoervak voor berichten.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">use_format</td>
      <td valign="middle">bool</td>
      <td><kbd>"true"</kbd> als de gebruiker post-opmaak heeft ingeschakeld voor links, emoji, tekststijlen en regeleinden.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle"> show_unread_section</td>
      <td valign="middle">reeks</td>
      <td><kbd>"true"</kbd> als de gebruiker ongelezen berichten heeft ingeschakeld op de flankbalk van het kanaal.</td>
    </tr> 
    <tr class="row-odd">
      <td valign="middle">thema</td>
      <td valign="middle">tekenreeks</td>
      <td>Het thema van de gebruiker. Geformatteerd als een Matterelijkste tekenreeks.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">military_time</td>
      <td valign="middle">string</td>
      <td><kbd>"true"</kbd> als de gebruiker een 24-uursnotatie heeft ingeschakeld. <kbd>"false"</kbd> als u een klok van 12 uur gebruikt.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">collapse_previews</td>
      <td valign="middle">tekenreeks</td>
      <td><kbd>"true"</kbd> als de gebruiker de koppelingspreview standaard samenvouwt. <kbd>"false"</kbd> als de gebruiker standaard previews van links uitvouwt.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">bericht_display</td>
      <td vali
gn="middle"> string</td>
      <td>De stijl die de gebruiker verkiest voor afgebeelde berichten. Opties zijn <kbd>"schoon"</kbd> als de gebruiker de standaardstijl of <kbd>"compact"</kbd> gebruikt als de gebruiker een compacte stijl gebruikt.</td>
    </tr> 
    <tr class="row-odd">
      <td valign="middle">channel_display_mode</td>
      <td valign="middle">string</td>
      <td><kbd>"full"</kbd> als de gebruikers kanaalberichten weergeven op de volledige breedte van het scherm of <kbd>"gecentreerd"</kbd> als de gebruiker een vaste breedte gebruikt, gecentreerd blok.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">bijlestutorial_step<td valign="middle">tekenreeks</td>
      <td><kbd>"1"</kbd>, <kbd>"2"</kbd>, of <kbd>"3"</kbd> geeft aan welke opgegeven zelfstudieprogramma om te beginnen met de gebruiker. <kbd>"999"</kbd> slaat het zelfstudieprogramma over.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">email_interval</td>
      <td valign="middle">tekenreeks</td>
      <td>E-mailbatchinterval voor gebruik tijdens bulkimport. </td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">delete_at</td>
      <td valign="middle">int64</td>
      <td>Tijdaanduiding van wanneer de gebruiker is gedeactiveerd.</td>
    </tr>    
    <tr class="row-odd">
      <td valign="middle">teams</td>
      <td valign="middle">array</td>
      <td>De teams waarvan de gebruiker lid is. Dit is een array van <b>UserTeamMembership</b> -objecten.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">notify_props</td>
      <td valign="middle">object</td>
      <td>De voorkeursinstellingen van de gebruiker, zoals gedefinieerd door het <b>UserNotifyProps</b> -object.</td>
    </tr>
  </table>

UserNotifyProps-object
----------------------

Dit object is lid van het gebruikersobject. .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">desktop</td>
      <td valign="middle">tekenreeks</td>
      <td>Preference voor het verzenden van desktopmeldingen. Dit is een van de volgende waarden:<br>
      <kbd>"all"</kbd> -Voor alle activiteiten.<br>
      <kbd>"vermelding"</kbd> -Alleen voor vermeldingen.<br>
      <kbd>"none"</kbd> -Nooit.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">desktop_sound</td>
      <td valign="middle">tekenreeks</td>
      <td>Preference for desktop notification sound. Wordt een van de volgende waarden:<br>
      ""true"</kbd> -Geluid wordt afgespeeld.<br>
      <kbd>"false"</kbd> -Geluid wordt niet afgespeeld.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">e-mail</td>
      <td valign="middle">tekenreeks</td>
      <td>Preference voor e-mailmeldingen. Een van de volgende waarden is:<br>
      <kbd>"true"</kbd> -E-mailmeldingen worden onmiddellijk verzonden.<br>
      <kbd>"false"</kbd> -E-mailmeldingen worden niet verzonden.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mobile</td>
      <td valign="middle">string</td>
      <td>Preference for verzenden mobile push notifications. Een van de volgende waarden is:<br>
      <kbd>"all"</kbd> -Voor alle activiteiten.<br>
      <kbd>"vermelding"</kbd> -Alleen voor vermeldingen.<br>
      <kbd>"none"</kbd> -Nooit.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mobile_push_status</td>
      <td valign="middle">tekenreeks</td>
      <td>Preference voor wanneer push-berichten worden geactiveerd. Zal een van de volgende waarden zijn:<br>
      <kbd>"online"</kbd> -Wanneer online, afwezig of offline.<br>
      <kbd>"away"</kbd> -Wanneer afwezig of offline.<br>
      <kbd>"offline"</kbd> -Wanneer offline.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">kanaal</td>
      <td valign="middle">tekenreeks</td>
      <td>Preference voor de vraag oftrigger, @channelen @here trigger worden genoemd. Een van de volgende waarden is:<br>
      <kbd>"true"</kbd> -Mentions worden geactiveerd.<br>
      <kbd>"false"</kbd> -Mentions worden niet geactiveerd.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">commentaar</td>
      <td valign="middle">tekenreeks</td>
      <td>Voorschrift voor antwoorden op antwoorden. Dit is een van de volgende waarden:<br>
      <kbd>"any"</kbd> -Triggermeldingen op berichten in antwoordthreads die de gebruiker start of neemt.<br>
      <kbd>"root"</kbd> -Triggermeldingen op berichten in threads die de gebruiker start.<br>
      <kbd>"never"</kbd> -Hiermee worden berichten in antwoordthreads niet geactiveerd als de gebruiker wordt genoemd.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mention_keys</td>
      <td valign="middle">string</td>
      <td>Preference for custom non-case-sensitive words that trigger vermeldt. Woorden worden van elkaar gescheiden door komma's.</td>
    </tr>
  </table>

UserTeamMembership-object
------------------------- .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">naam</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van het team waarvan deze gebruiker lid is.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">rollen</td>
      <td valign="middle">tekenreeks</td>
      <td>De rollen die de gebruiker binnen dit team heeft. </td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">thema</td>
      <td valign="middle"> tekenreeks</td>
      <td>Het thema van de gebruiker voor dit team. Geformatteerd als een Matterelijkste tekenreeks.</td>
    </tr>
     <tr class="row-odd">
      <td valign="middle">kanalen</td>
      <td valign="middle">array</td>
      <td>De kanalen in dit team waarvan de gebruiker lid is. Wordt afgebeeld als een array van <b>UserChannelMembership</b> -objecten.</td>
    </tr>
  </table>

UserChannelMembership-object
---------------------------- .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">naam</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van het kanaal in het bovenliggende team waarvan deze gebruiker lid is.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">rollen</td>
      <td valign="middle">tekenreeks</td>
      <td>De rollen die de gebruiker heeft binnen dit kanaal. </td>
    </tr>
        <tr class="row-odd">
      <td valign="middle"> notify_props</td>
      <td valign="middle">object</td>
      <td>De voorkeuren voor aanmelding voor deze gebruiker in dit kanaal, zoals gedefinieerd door hetobjectChannelNotifyProps</b> -object.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">favoriet</td>
      <td valign="middle">boolean</td>
      <td>Of het kanaal is gemarkeerd als favoriet voor deze gebruiker. Een van de volgende waarden is:<br>
          <kbd>"true"</kbd> -Ja.<br>
          <kbd>"false"</kbd> -Nee.</td>
    </tr>
  </table>

ChannelNotifyProps-object
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Dit object is lid van het object ChannelMembership. .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">desktop</td>
      <td valign="middle">tekenreeks</td>
      <td>Preference voor het verzenden van desktopmeldingen. Een van de volgende waarden:<br>
      <kbd>"default"</kbd> -Globale standaardwaarde.<br>
      <kbd>"all"</kbd> -Voor alle activiteiten.<br>
      <kbd>"vermelding"</kbd> -Alleen voor vermeldingen.<br>
      <kbd>"none"</kbd> -Nooit.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mobiel</td>
      <td valign="middle">tekenreeks</td>
      <td>Voorwoord voor het verzenden van mobiele meldingen. Wordt een van de volgende waarden:<br>
      <kbd>"default"</kbd> -Globale standaardwaarde.<br>
      <kbd>"all"</kbd> -Voor alle activiteiten.<br>
      <kbd>"vermelding"</kbd> -Alleen voor vermeldingen.<br>
      <kbd>"none"</kbd> -Nooit.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mark_unread</td>
      <td valign="middle">tekenreeks</td>
      <td>Preference voor markeerkanaal als ongelezen. Wordt een van de volgende waarden:<br>
          <kbd>"all"</kbd> -Voor alle ongelezen berichten.<br>
          <kbd>"vermelding"</kbd> -Alleen voor vermeldingen.</td>
    </tr>
  </table>

Object posten
----------- .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">team</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van het team waarin deze post zich bevindt.</td>
    </tr
>
    <tr class="row-odd">
      <td valign="middle">channel</td>
      <td valign="middle">string</td>
      <td>De naam van het kanaal waarin deze post zich bevindt.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">gebruiker</td>
      <td valign="middle">tekenreeks</td>
      <td>De gebruikersnaam van de gebruiker voor deze post.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">bericht</td>
      <td valign="middle">tekenreeks</td>
      <td>Het bericht dat de post bevat.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">props</td>
      <td valign="middle">object</td>
      <td>De rekwi's voor een bericht. Bevat extra opmaakinformatie die wordt gebruikt door integraties en bot posts. Voor een meer gedetailleerde uitleg raadpleegt u de <a href="https://docs.mattermost.com/developer/message-attachments.html">documentatie van berichtbijlagen</a>.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle">int</td>
      <td>De tijdsaanduiding voor de posting, in milliseconden sinds de Unix-periode.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">reacties</td>
      <td valign="middle">array</td>
      <td>De emoji-reacties op deze post. Dit is een array van reactisobjecten.</td>
  </table>
  
Object beantwoorden
------------ .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">gebruiker</td>
      <td valign="middle">tekenreeks</td>
      <td>De gebruikersnaam van de gebruiker voor dit antwoord.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">bericht</td>
      <td valign="middle">tekenreeks</td>
      <td>Het bericht dat het antwoord bevat.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle"> int</td>
      <td>De tijdsaanduiding voor het antwoord, in milliseconden sinds het Unix-tijdperk.</td>
    </tr>
  </table>
  
Reactieobject
---------------

Dit object is lid van het object Post. .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">gebruiker</td>
      <td valign="middle">tekenreeks</td>
      <td>De gebruikersnaam van de gebruiker voor dit antwoord.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">emoji_name</td>
      <td valign="middle">string</td>
      <td>De emoji van de reactie.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle">int</td>
      <td>De tijdaanduiding voor het antwoord, in milliseconden sinds het Unix-tijdperk.</td>
    </tr>
  </table>

Emoji-object
------------ .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">naam</td>
      <td valign="middle">tekenreeks</td>
      <td>De naam van de emoji.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">afbeelding</td>
      <td valign="middle">tekenreeks</td>
      <td>Het pad (absoluut of ten opzichte van de huidige werkdirectory) naar het afbeeldingsbestand voor deze emoji.</td>
    </tr>
  </table>
  
DirectChannel-object
-------------------- .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">leden</td>
      <td valign="middle">array</td>
      <td>Lijst van kanaalleden.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">koptekst</td>
      <td valign="middle">tekenreeks</td>
      <td>De kanaalkop.</td>
    </tr>
  </table>
  
DirectPost-object
----------------- .. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Veldnaam</th>
      <th class="head">Type</th>
      <th class="head">Beschrijving</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">gebruiker</td>
      <td valign="middle">tekenreeks</td>
      <td>De gebruikersnaam van de gebruiker voor deze post.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">bericht</td>
      <td valign="middle">tekenreeks</td>
      <td>Het bericht dat de post bevat.</td>
    </tr>
        <tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle"> int</td>
      <td>De tijdsaanduiding voor de post, in milliseconden sinds de Unix-periode.</td>
  </table>
