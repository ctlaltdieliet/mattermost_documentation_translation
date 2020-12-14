Beheerderstaken
== == == == == == == == == =

Dit document bevat instructies voor algemene beheertaken, waaronder enkele aanbevelingen voor taken om uw Matterste-instance voor te bereiden op gebruikers aan boord.

Taken aan de slag -----------------------
1. Zodra u Matterbest hebt geïnstalleerd en gebruikt, zorg er dan voor dat alle configuratie-instellingen op de juiste manier zijn ingesteld onder ** Systeemconsole > Omgeving * * inclusief:-Web Server
 -Database
 -Bestandsopslag
 -SMTP
 -Push Notification Server 
  
Deze instellingen kunnen ook worden ingesteld in het bestand ` `config.json ` `. Zie onze ` configuratie-instellingen documentatie <https://docs.mattermost.com/administration/config-settings.html> ` __ voor een volledige lijst van alle configuratie-instellingen. 

2. Instellingen onder ** Systeemconsole > Siteconfiguratie * * aanpassen om te bepalen hoe gebruikers met de site communiceren.  
Zorg ervoor dat u de Support Email en Help Link in Matterbest bij ** System Console > Site Configuration > Customization * * bijwerkt om uw gebruikers een resource voor wachtwoordresets of vragen op hun Mattermeeste account aan te bieden.

 -De Support Email wordt gebruikt voor e-mailmeldingen en tijdens het zelfstudieprogramma voor gebruikers om vragen te stellen.
 -De Help Link is op de Matterbest login pagina, teken-up pagina's, en het hoofdmenu en kan worden gebruikt om te linken naar uw helpdesk ticketing systeem.  
 
Deze instellingen kunnen ook worden ingesteld in het bestand ` `config.json ` `.  Zie onze ` configuratie-instellingen documentatie <https://docs.mattermost.com/administration/config-settings.html> ` __ voor een volledige lijst van alle configuratie-instellingen.  

3. Begin aan de onboard gebruikers door het inschakelen van het maken van accounts of door het aansluiten van een verificatieservice om te helpen met gebruikersconfiguratie.  

 -Gebruikers kunnen vooraf worden geconfigureerd met migratie en bulkladen van gegevensprocessen op basis van eerdere samenwerkingssystemen. Zie onze ` migratiehandleiding <https: //docs.mattermost.com/administration/migrating.html#migration-guide> ` _ en ` bulk loading documentation <https://docs.mattermost.com/deployment/bulk-loading.html> ` _ voor meer informatie.
 -` AD/LDAP authentication <https: //docs.mattermost.com/deployment/sso-ldap.html#active-directory-ldap-setup-e10-e20 > ` _ en ` SAML authentication <https://docs.mattermost.com/deployment/sso-saml.html> ` _ zijn beschikbaar voor Enterprise Edition, het leveren van identiteitenbeheer, enkelvoudige aanmelding en automatische accountprovisioning.   

4. Schakel integraties en plugins in om de werkstromen en toolsets van uw team in Matterbest aan te sluiten. 

 -Om integraties zoals webhooks, slash-commando's, OAuth2.0 en bots in te schakelen, om ** System Console > Integraties * * te gaan. Meer informatie over deze integraties kan gevonden worden ` hier <https://docs.mattermost.com/guides/integration.html> ` _.-Om plugins in te schakelen en te beheren, gaat u naar ** System Console > Plugins * *.  Mattermore biedt een ` integratie markt <https://integrations.mattermost.com/> ` _ waar u alle beschikbare plugins beschikbaar voor uploaden kunt zien. 

Als uw organisatie meer structuur en projectbeheerartefacten nodig heeft voor de implementatie
ion van Matterbest, zie onze ` Enterprise roll out checklist <https://docs.mattermost.com/getting-started/enterprise-roll-out-checklist.html> ` __.

Belangrijke beheerberichten ------------------------------ ** DO NOT manipuleren de Mattermeeste database * *

 Verwijder met name NIET rechtstreeks gegevens uit de database. Matterbest is ontworpen als een continu archief en kan niet ondersteund worden na handmatige manipulatie.
 -Als u een team of gebruiker permanent wilt verwijderen, gebruik dan het 'Command Line Tool <https://docs.mattermost.com/administration/command-line-tools.html>' __.

Algemene taken
------------

** Systeembeheeraccount maken vanaf de opdrachtregel * *
 -Als de systeembeheerder de organisatie verlaat of anderszins niet beschikbaar is, kunt u de opdrachtregelinterface * systeem_admin * toewijzen aan een bestaande gebruiker. In de directory ` ` /opt/mattermeest ` ` typt u ` ` sudo -u matterbest bin/mattermeest roles system_admin { user-name } ` `, waarbij * { user-name } * de gebruikersnaam is van de persoon met de nieuwe rol. Meer informatie over het gebruik van de opdrachtregelinterface vindt u in 'Command Line Tools <https://docs.mattermost.com/administration/command-line-tools.html>' _.
 -De gebruiker moet zich afmelden en opnieuw aanmelden voordat de rol * system_admin * wordt toegepast. ** Migreren naar AD/LDAP of SAML vanuit e-mail-gebaseerde authenticatie * *
 -Als u Enterprise Edition hebt, kunt u migreren van e-mailverificatie naar Active Directory/LDAP of naar SAML Single Sign-on. Voor het instellen van Active Directory/LDAP raadpleegt u ` Active Directory/LDAP Setup (E10/E20) <https: //docs.mattermost.com/deployment/sso-ldap.html#active-directory-ldap-setup-e10-e20 > ` _. Voor het instellen van SAML Single Sign-on, zie ` SAML Single-Sign-On (E20) <https://docs.mattermost.com/deployment/sso-saml.html> ` _.
 -Nadat de nieuwe verificatiemethode is ingeschakeld, kunnen bestaande gebruikers de nieuwe methode pas gebruiken als ze naar ** Account Settings > Security > Sign-in method * * gaan en op ** Switch klikken om AD/LDAP* * * of ** Switch te gebruiken om SAML Single Sign-** te gebruiken. Nadat ze zijn verwisseld, kunnen ze hun e-mailadres en wachtwoord niet meer gebruiken om in te tekenen.  

* * Een gebruiker deactiveren * *
 -Systeembeheerders kunnen naar ** System Console > Gebruikers * * gaan voor een lijst van alle gebruikers op de server. De lijst kan worden doorzocht en gefilterd om het gemakkelijker te maken om de gebruiker te vinden. Klik op de rol van de gebruiker en klik in het menu dat wordt geopend op ** Deactivate**.
 -Om de audithistorie te behouden, worden gebruikers meestal nooit verwijderd uit het systeem. Als een gebruiker permanent wordt verwijderd (bijvoorbeeld voor de doeleinden van ` GDPR <https://gdpr-info.eu/> ` __), kan een ` CLI-tool <https://docs.mattermost.com/administration/command-line-tools.html> ` _ worden gebruikt om dit te doen.
 -Merk op dat AD/LDAP-gebruikersaccounts van Mattermost niet kunnen worden gedeactiveerd; ze moeten worden gedeactiveerd vanuit uw Active Directory.

** Controleren op een geldige licentie in Enterprise Edition zonder in te loggen * *
 -Open het logbestand ` `mattermost.log ` ` `. Het is meestal in de ` ` mattermost/logs/ ` ` directory, maar kan elders op je systeem staan. Zoek het laatste voorval van een logboekitem dat begint met de tekst ` ` [ INFO] Licentiesleutel ` `. Als de licentiesleutel geldig is, moet de volledige regel overeenkomen met het volgende voorbeeld:

    .. code-blok :: tekst

      [ 2017/05/19 16:51:40 UTC] [ INFO] Licentie sleutel geldige unlocking enterprise functies. ** Upgraden Matterbest * *
 -Mattermeeste releases updates maandelijks naar ` Mattermeeste Team Edition <https://mattermost.com/> ` _ en ` Mattermeest Enterprise Edition <https://mattermost.com/pricing-self-managed/> ` _. De ` Matterbest Changelog <https://docs.mattermost.com/administration/changelog.html> ` _ geeft alle informatie over wijzigingen in elke versie. We raden servers aan te upgraden vaak om te blijven met kritische bug fixes en beveiligingsfixes.-Volg de stappen die worden beschreven in de ` upgrade documentatie <https://docs.mattermost.com/administration/upgrade.html> ` _ voor het uitvoeren van upgrades.
