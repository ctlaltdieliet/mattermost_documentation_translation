Health Check
== == == == == == =

Deze pagina beschrijft hoe u de health check-probes kunt configureren voor een Mattertiste server.

Voordat u begint, moet u een actieve Matterigste server hebben. Als u dit niet doet, kunt u Matterbest op verschillende distributies installeren <https: //docs.mattermost.com/guides/administrator.html#installing-mattermost> ` __ of een 'Kubernetes cluster implementeren met Minikube <https://github.com/mattermost/mattermost-kubernetes>' __. Merk op dat 'hoogst beschikbare Matterbest-cluster <https://docs.mattermost.com/deployment/cluster.html> ` __ beschikbaar is in' Enterprise Edition E20 <https://mattermost.com/pricing-self-managed/> ` __.

U kunt een gezondheidscontrole uitvoeren met twee methoden:

` ` /ping ` ` APIv4-eindpunt
-------------------------

In Mattermeest versie 3.10 en hoger kunt u het ` GET /system/ping APIv4 endpoint <https: //api.mattermost.com/#tag/system%2Fpaths%2F ~ 1system ~ 1ping%2Fget> ` __ gebruiken om de systeemgezondheid te controleren.

Hieronder vindt u een voorbeeldaanvraag. Het eindpunt controleert of de server actief is op basis van de configuratie-instelling ` ` GoRoutineHealthThreshold ' `.

-Als ` ` GoRoutineHealthThreshold ` ` en het aantal goroutines op de server die drempel overschrijdt, wordt de server als ongezond beschouwd.
-Als ` ` GoRoutineHealthThreshold ` ` niet is ingesteld of het aantal goroutines onder de drempelwaarde ligt, wordt de server als gezond beschouwd.

Dit eindpunt kan ook worden geleverd aan planners zoals ` Kubernetes <https: //kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/#before-you-begin> ` __. .. code-blok :: gaan

  import "github.com/mattermost/mattermost-server/model" Client: = model.NewAPIv4Client ("https://your-matterbest-url.com")
  Client.Login ("email@domain.com", "Password1 ")
  
  // Status GetPing, err: = Client.GetPing ()

Mattermeeste probe
-----------------

De ` Matterbest Probe <https://github.com/csduarte/mattermost-probe> ` __ pings een Mattermeeste server met behulp van een verscheidenheid van sondes.

Deze probes kunnen worden geconfigureerd om de kernfuncties te controleren, waaronder het verzenden en ontvangen van berichten, het samenvoegen van kanalen, het pingen van een aanmeldingspagina en het zoeken naar gebruikers en kanalen.

Het project wordt aangeleverd door de meest open source community. Suggesties en bijdragen voor het project zijn welkom.
