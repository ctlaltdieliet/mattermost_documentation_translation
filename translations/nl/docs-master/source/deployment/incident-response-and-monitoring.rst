Actie voor respons en bewaking van incidenten
== == == == == == == == == == == == == == == == == == == == == ==

Onze ' Integration-directory <https://integrations.mattermost.com> ` _ heeft verschillende integraties om incidentrespons en bewakingshulpmiddelen in Matterbest aan te sluiten.

Hier zijn enkele populaire opties hieronder, met inbegrip van self-hosted on-prem of zelf-gehoste private cloud-oplossingen, en vendor-gehoste SaaS-oplossingen.

AWS CloudWatch SNS
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

 -Twee-weg integratie tussen Matterbest en Amazon AWS SNS, ontwikkeld door Carlos Tadeu Panato Junior, ondersteund door Matterbest.
 -Ontvangen SNS meldingen van Alerts gemaakt door Amazon AWS CloudWatch en verzonden via AWS SNS.
 -Haal operationele gegevens en bruikbare inzichten om Matterbest te bewaken om te observeren en te reageren op systeembrede veranderingen in de prestaties.
 -Broncode + docs: https://github.com/mattermost/mattermost-plugin-aws-SNS

Nagios
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

 -Stuur meldingen van een Nagios monitoring instantie naar een Mattermeeste kanaal voor het oplossen van problemen, ontwikkeld door NDrive.
 -Kan gebruikt worden voor andere compatibele software zoals Icinga.
 -Broncode + docs: https://github.com/NDrive/nagios-mattermost

Splunk
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

 -Een Matterigste omgeving bewaken.
 -Stuur applicatie-performance inzichten naar elke Mattermeeste kanaal voor betere probleemoplossing en monitoring, en om het systeem uptime te verhogen.
 -Documenten: http://datatomix.com/?p=433, geschreven door Christian Johannsen.

Pagerplicht
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

 -Krijg automatische informatie over de toestand van een incident te Matterbest, ontwikkeld door PagerDuty.
 -Verzend incident-updates voor elke PagerDuty Service naar een Mattermeeste kanaal te optimaliseren incident resolutie tijd en proces.
 -Documenten: https://www.pagerduty.com/docs/guides/mattermost-integration-guide/

Opsgenie
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

 -Twee-weg integratie tussen Opsgenie en Matterit, ontwikkeld door Opsgenie.
 -Stuur waarschuwingsberichten van uw Opsgenie incident boards naar Mattermeeste kanalen.
 -Gebruik slash-opdrachten om snelle acties te ondernemen, zoals het erkennen, toewijzen, maken en sluiten van waarschuwingen in de Mattermeeste gebruikersinterface.
 -Documenten: https://docs.opsgenie.com/docs/mattermost-integration 

Prometheus Alertmanager
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

 -Twee-weg integratie tussen Alertmanager en Matterbest, ontwikkeld door Carlos Tadeu Panato Junior.
 -Handle waarschuwingen verzonden door clienttoepassingen zoals de Prometheus-server en route ze naar de juiste ontvangers integraties zoals e-mail, PagerDuty, of Opsgenie.
 -Broncode + docs: https://github.com/cpanato/mattermost-plugin-alertmanager

Heeft u een voorstel voor een incident response en monitoring integratie? ' Laat het ons weten in het featurevoorstel forum <https://mattermost.uservoice.com/forums/306457-general?category_id=202591> ` _.

Heb je een integratie gebouwd? ` Laat ons weten <https://integrations.mattermost.com/submit-an-integration/> ` _ en we delen in onze ` Integrations Directory <https://integrations.mattermost.com> ` ` _.
