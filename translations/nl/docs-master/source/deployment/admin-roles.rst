== == == == == == == == == == == == == == == == == Aanvullende Systeembeheerrollen (E20)
== == == == == == == == == == == == == == == == == ==

Vanaf v5.28 kunnen systeembeheerders rollen toewijzen aan leden, waardoor ze alleen toegang krijgen tot de aangewezen gebieden van de systeemconsole. Hierdoor kunnen andere leden van uw organisatie bepaalde beheertaken uitvoeren zonder toegang te hebben tot alle systeembeheermogelijkheden.

-** Systeembeheer: ** De System Manager heeft machtigingen voor lezen/schrijven voor beheergebieden van de systeemconsole, zoals gebruikersbeheer en integraties (met uitzondering van machtigingen). Deze rol heeft alleen leestoegang tot verificatie, rapportage en licentieinterfaces.
-** User Manager: ** De rol User Manager kan alle gebruikersbeheergebieden lezen/schrijven (met uitzondering van permissies). De verificatieinterface is alleen-lezen.
-** Alleen beheerders lezen: ** Deze rol heeft toegang tot alle pagina's van de systeemconsole, maar heeft geen schrijftoegang tot alle pagina's.

Rollen worden toegewezen via de opdrachtregel, met de opdracht ' mmctl <https://docs.mattermost.com/administration/mmctl-cli-tool.html> ` _.

Elke rol heeft een set standaardmachtigingen en als een gebruiker een rol toegewezen krijgt, kunnen ze toegang krijgen tot de systeemconsole. De items die ze kunnen bekijken zijn afhankelijk van de rol die ze zijn toegewezen.

** Systeembeheer * *

  -Lezen/schrijven
      -Gebruikersbeheer
      -Milieu
      -Siteconfiguratie
      -Integraties
  -Alleen lezen
     -(Gebruikersbeheer) Machtigingen
     -Uitgave/licentie
     -Rapportage
     -Verificatie
     -Plugins

** Gebruikersbeheer * *

  -Lezen/schrijven
      -Gebruikersbeheer-Groepen
         -Teams
         -Kanalen-Alleen Lezen
      -(Gebruikersbeheer) Machtigingen
      -Verificatie

** Alleen Lezen Beheer * *

  -Alleen lezen
     -Alle pagina's binnen de systeemconsole

Beheerrollen toewijzen
---------------------

Systeembeheerders kunnen rollen toewijzen en machtigingen wijzigen met het hulpprogramma mmctl. Dit kan lokaal of op afstand worden gedaan.

De notatie van de mmctl-opdracht is:

` ` mmctl permissies rol [ rolnaam] [ gebruikersnaam ...] ` ` `

** Om de rol van System Manager te verlenen aan één gebruiker met de naam Bob Smith: **

` ` mmctl machtigingen rol toewijzen system_manager bob-smith ` `

** Om de rol van User Manager te verlenen aan twee gebruikers, Bob Smith en Sue Clark: **

` ` mmctl permissies rol wijs system_user_manager bob-smith sue-clark ` `

** Om de rol Read Only Admin toe te kennen aan twee gebruikers, Bob Smith en Sue Clark: **

` ` mmctl machtigingen rol toewijzen system_read_only_admin bob-smith sue-clark ` `

** Om de rol van System Manager te verwijderen van een enkele gebruiker genaamd Bob Smith: **

` ` mmctl permissies rol unassign system_manager bob-smith ` `

Machtigingen van beheerrollen bewerken (Geavanceerd)
------------------------------------------------------

Elk van de beheerdersrollen heeft gedefinieerd, de standaardbevoegdheden zoals hierboven beschreven. 

Systeembeheerders kunnen lees-en schrijftoegang verlenen tot andere gebieden van de systeemconsole, en leestoegang (met inbegrip van standaardtoegang) voor elke rol verlenen. Dit wordt voltooid met het mmctl-gereedschap, lokaal of
op afstand.

De notatie van de mmctl-opdracht is:

` ` mmctl permissies toevoegen [ rolnaam] [ toestemming ...] ` `

** Om schrijftoegang te verlenen tot de verificatiesectie van de systeemconsole voor alle gebruikers met de rol User Manager: **

` ` mmctl permissies toevoegen system_user_manager sysconsole_write_authentication ` `

** Om alleen-lezen toegang te verlenen tot de verificatiesectie van de systeemconsole voor alle gebruikers met de rol User Manager: **

` ` mmctl machtigingen verwijderen system_user_manager sysconsole_read_authentication ` `

** Om schrijftoegang te verwijderen tot de verificatiesectie van de systeemconsole voor alle gebruikers met de rol User Manager: **

` ` mmctl machtigingen verwijderen system_user_manager sysconsole_write_authentication ` `

Beheerdersrollen en bevoegdheden --------------------------- ** Roles**

-` ` system_manager ` `
-` ` system_user_manager ` `
-` ` system_read_only_admin ` ` ** Privileges**

-` ` PERMISSION_SYSCONSOLE_READ_ABOUT ` `
-` ` PERMISSION_SYSCONSOLE_WRITE_ABOUT ` `

-` ` PERMISSION_SYSCONSOLE_READ_REPORTING ` `
-` ` PERMISSION_SYSCONSOLE_WRITE_REPORTING ` `

-` ` PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_USERS ` `
-` ` PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_USERS ` `

-` ` PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_GROUPS ` `
-` ` PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_GROUPS ` `

-` ` PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_TEAMS ` `
-` ` PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_TEAMS ` `

-` ` PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_CHANNELS ` `
-` ` PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_CHANNELS ` `

-` ` PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_PERMISSIONS ` `
-` ` PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_PERMISSIONS ` `

-` ` PERMISSION_SYSCONSOLE_READ_ENVIRONMENT ` `
-` ` PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT ` `

-` ` PERMISSION_SYSCONSOLE_READ_SITE ` `
-` ` PERMISSION_SYSCONSOLE_WRITE_SITE ` `

-` ` PERMISSION_SYSCONSOLE_READ_AUTHENTICATION ` `
-` ` PERMISSION_SYSCONSOLE_WRITE_AUTHENTICATION ` `

-` ` PERMISSION_SYSCONSOLE_READ_PLUGINS ` `
-` ` PERMISSION_SYSCONSOLE_WRITE_PLUGINS ` `

-` ` PERMISSION_SYSCONSOLE_READ_INTEGRATIONS ` `
-` ` PERMISSION_SYSCONSOLE_WRITE_INTEGRATIONS ` `

-` ` PERMISSION_SYSCONSOLE_READ_COMPLIANCE ` `
-` ` PERMISSION_SYSCONSOLE_WRITE_COMPLIANCE ` `

-` ` PERMISSION_SYSCONSOLE_READ_EXPERIMENTAL ` `
-` ` PERMISSION_SYSCONSOLE_WRITE_EXPERIMENTAL ` `

Veelgestelde vragen
--------------------------

Kan een User Manager of System Manager de e-mail of het wachtwoord van een beheerder resetten zonder hun medeweten? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Dit is niet mogelijk met de standaardbevoegdheden van deze rollen. De mogelijkheid om wachtwoorden of e-mailadressen van beheerders opnieuw in te stellen, is beperkt tot systeembeheerders.  

Kan een User Manager of System Manager het configuratiebestand openen? 
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

-Ja, Ze hebben echter alleen toegang tot het lezen van werkelijke waarden en het wijzigen van waarden in overeenstemming met hun machtigingen. Als de juiste leesmachtigingen niet bestaan, worden de standaardwaarden afgebeeld.

Zijn alle acties van beheerdersrollen vastgelegd? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Elke wijziging die door een beheerder wordt gemaakt, is opgenomen in het auditlogboek.

Kan een System Manager hun eigen machtigingen wijzigen of hun rol verhogen? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Nee. Systeemmanagers kunnen hun rol niet verhogen en zijn niet in staat om de rol van andere leden te verhogen.

Kan een van de nieuwe rollen API sleutels/wachtwoorden of andere gevoelige informatie in de System Console (zoals SMTP, AWS, Elastic Search) ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Nee, wachtwoordinformatie is alleen zichtbaar voor systeembeheerders en wordt geobfuseerd voor andere rollen.

Als de downloadlinks voor nalevingsexporten zijn ingeschakeld in de systeemconsole, kan een Read Only Admin de rapporten downloaden? 
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Alleen rollen die expliciet toegang krijgen tot ** Systeemconsole > Naleving * * hebben toegang tot het downloaden van nalevingsrapporten. 

Kan een van de nieuwe rollen force-join Private-kanalen? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Ja op dit moment kunnen ze echter, zullen we verbeteren van dit gedrag in de toekomst met een prompt die hen laat weten dat ze in een prive-kanaal. We zijn ook van plan om een machtiging toe te voegen waarmee de mogelijkheid om toegang te krijgen tot private kanalen zou worden verwijderd.

Kan ik een nieuwe rol creëren of een bestaande rol klonen? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Nee, maar we zijn actief op zoek naar feedback over deze mogelijkheid.

Kan ik een LDAP-filter gebruiken om deze rollen toe te wijzen? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Nee, maar we overwegen deze functionaliteit voor een toekomstige verbetering.

Kan ik de rollen hernoemen? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Dit wordt in aanmerking genomen voor toekomstige ontwikkelingen.

Kan System Manager of User Manager een andere beheerder of beheerder verlagen of deactiveren? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Geen machtiging verleent de machtiging om een andere beheerder te deactiveren of te degraderen. 

Kan System Manager of User Manager beheerdersrollen toewijzen of niet toewijzen? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Alleen de systeembeheerder heeft toegang tot de rollen voor het bewerken van het systeem.
