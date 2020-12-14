Prestatiebewaking (E20)
== == == == == == == == == == == == == == == =

*Beschikbaar in Enterprise Edition E20 *.

Dankzij de ondersteuning voor prestatiebewaking kan een Matterefste server de systeemgezondheid voor grote Enterprise-implementaties volgen door middel van integraties met ` Prometheus <https://prometheus.io/> ` __ en ` Grafana <https://grafana.org/> ` __.

De integratie ondersteunt het verzamelen van gegevens van verschillende Mattermeeste servers, met name handig als u Matterbest uitvoert in de hoge-beschikbaarheidsmodus <https://docs.mattermost.com/deployment/cluster.html> ` __. .. Inhoud:
    :backlinks: top

Implementatiehandleiding
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ details over de integratie van uw Mattermeest server met Prometheus en Grafana.

Installatie van Prometheus
-------------------------------------------------------

1-` Download een vooraf gecompileerd binair bestand voor Prometheus <https://prometheus.io/download/> ` __. Binaries zijn beschikbaar voor veel populaire distributies, waaronder Darwin, Linux en Windows.

Zie voor installatie-instructies ` Prometheus install guides <https://prometheus.io/docs/introduction/getting_started/> ` __.

2-De volgende instellingen worden aanbevolen in het configuratiebestand van Prometheus met de naam ` `prometheus.yml ` `: .. code:: yaml

    # mijn globale configuratie wereldwijd:
      scrape_interval: 60 # Standaard, scrape doelen elke 15 seconden.
      evaluatie_interval: 60 # Standaard, scrape doelen elke 15 seconden.
      # scrape_timeout is ingesteld op de globale standaard (10s).

      # Deze labels aan elke tijdreeks of alerts bijvoegen bij het communiceren met
      # externe systemen (federatie, opslag op afstand, Alertmanager).
      external_labels:
          monitor: 'mattermost-monitor'

    # Laad regels eenmaal en periodiek evalueren volgens de globale 'evaluation_interval'.
    rule_files:
      #-"first.rules "
      #-"second.rules "

    # Een scrape configuratie die exact één eindpunt bevat om te schrapen:
    Hier is het Prometheus zelf.
    scrape_configs:
      # De naam van de taak wordt toegevoegd als label ` job=<job_name>` naar alle tijdschalen die uit deze configuratie worden verwijderd.
      -job_name: 'prometheus'

        # De algemene standaard-en scrape-doelen van deze taak elke 5 seconden vervangen.
        # scrape_interval: 5s

        # metrics_path wordt standaard ingesteld op '/metrics'
        # schema is standaard 'http'.

        static_configs:
          -doelen: [ "<hostname1>:<port>", "<hostname2>:<port>"]

De parameter ` `<hostname1>:<port>` ` moet worden vervangen door het IP-adres en de poort van uw Mattermeest host om de gegevens te schrapen. Het maakt verbinding met ` ` /metrics ` ` met behulp van http. 

3-Schakel de prestaties in de Mattermeeste System Console in en geef het luisteradres op. Raadpleeg meer details in onze ` configuratie-instellingen-documentatie <https: //docs.mattermost.com/administration/config-settings.html#performance-monitoring-beta> ` __. Na het inschakelen van prestatiebewaking, moet u Matterbest opnieuw opstarten. .. image:: ../images/perf_monitoring_system_console.png
  :schaal: 70

4-Om de server te testen, gaat u naar ` `<ip>:<port>/metrics ` `.

5-Ten slotte wordt uitgevoerd. "
` vi prometheus.yml ` ` om de configuratie van Prometheus af te ronden.

Lees voor het starten van de Prometheus-service de " uitgebreide handleidingen van Prometheus <https: //prometheus.io/docs/introduction/getting_started/#starting-prometheus> ` __.

6-Nadat de service is gestart, hebt u toegang tot de gegevens in ` `<localhost>:<port>/graph ` `.

Terwijl u de Prometheus-dienst kunt gebruiken om grafieken te maken, zullen we ons richten op het maken van metrische en analytics dashboards in Grafana. .. opmerking:: Voor het oplossen van problemen, kijk op de ` Prometheus FAQ pagina <https://prometheus.io/docs/introduction/faq/> ` __.

Grafana installeren
-------------------------------------------------------

1-` Download een vooraf gecompileerd binair bestand voor Grafana <https://docs.grafana.org/installation/debian/> ` __ op Ubuntu of Debian. Binaries zijn ook beschikbaar voor andere distributies, waaronder Redhat, Windows en Mac.

Voor installatie-instructies, zie ` Grafana install guides <https://docs.grafana.org/installation/debian/> ` __

2-Het Grafana pakket is geïnstalleerd als een service, dus het is gemakkelijk om de server te starten. Zie de ` install guides <https://docs.grafana.org/installation/debian/> ` __ voor meer informatie.

3-De standaard HTTP-poort is ` ` 3000 ` ` ` en de standaard gebruikersnaam en wachtwoord zijn ` ` admin ` ` `.

4-Een Mattermeeste gegevensbron moet worden toegevoegd, met instellingen gedefinieerd in de screenshot hieronder. .. image:: ../images/mattermost_datasource.png .. opmerking:: Raadpleeg voor het oplossen van problemen de ` Grafana Troubleshooting page <https://docs.grafana.org/installation/troubleshooting/> ` __.

Voor gebruikershandleidingen en zelfstudieprogramma's controleert u de 'Grafana-documentatie voor meer informatie <https://docs.grafana.org/guides/basic_concepts/>' __.

Aan de slag
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Vragen

Om aan de slag te gaan, kunt u drie voorbeelddashboards downloaden die in Grafana worden gedeeld:

 -` Matterbest Performance KPI Metrics <https://grafana.com/dashboards/2539> ` __, die belangrijke meetgegevens bevat voor het bewaken van de prestaties en de systeemgezondheid.
 -` Matterbest Performance Monitoring <https://grafana.com/dashboards/2542> ` __, die gedetailleerde diagrammen voor prestatiebewaking bevat.
 -` Matterbest Performance Monitoring (Bonus Metrics) <https://grafana.com/dashboards/2545> ` __, die extra meetgegevens bevat, zoals e-mails verzonden of verzonden bestanden, die belangrijk kunnen zijn om te monitoren in sommige implementaties.

Zie ` deze gids <https://docs.grafana.org/reference/export_import/> ' __ om te leren hoe u Grafana dashboards kunt importeren vanuit de gebruikersinterface of vanuit de HTTP API.

Statistieken
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Vragen

Matterbest biedt de volgende statistische gegevens over de prestaties bij de integratie met Prometheus en Grafana.

Aangepaste Mattermeeste Gebruikscijfers
-------------------------------------------------------

Hieronder vindt u een lijst van de aangepaste Mattermeeste metrics die kunnen worden gebruikt voor het bewaken van de prestaties van uw systeem:

API-gebruikscijfers:

    -` ` mattermost_api_time ` `: De totale tijd in seconden om een bepaalde API handler uit te voeren.

Gebruikscijfers voor cache:

    -` ` mattermost_cache_etag_hit_total ` `: Het totale aantal ETag cache-hits voor een bepaalde cache.
    -` ` mattermost_cache_etag_miss_total ` `: Het totale aantal ETag cache-mist voor een API-aanroep.
    -` ` mattermost_cache_mem_hit_total ` `: Het totale aantal hits in de geheugencache voor een bepaalde cache.
    -` ` mattermost_cache_mem_invalidation_total ` `: Het totale aantal invalidaties van de geheugencache voor een bepaalde cache.
    -` ` mattermost_cache_mem_miss_total ` `: Het totale aantal cache-missers voor een bepaalde cache.

De bovenstaande cijfers kunnen worden gebruikt voor het berekenen van ETag en geheugen cache hit tarieven in de tijd. .. afbeelding:: ../images/perf_monitoring_caching_metrics.png

Clustergebruikscijfers:

    -` ` mattermost_cluster_cluster_request_duration_seconden ` `: De totale duur in seconden van de interserverclusteropdrachten.
    -` ` mattermost_cluster_cluster_requests_total ` `: Het totale aantal inter-node verzoeken.
    -` ` mattermost_cluster_event_type_totalen ` `: Het totale aantal clusteraanvragen dat voor elk type is verzonden.

Databasecijfers:

    -` ` mattermost_db_master_connections_total ` `: Het totale aantal verbindingen met de masterdatabase.
    -` ` mattermost_db_read_replica_connections_total ` `: Het totale aantal verbindingen met alle gelezen replica-databases.
    -` ` mattermost_db_search_replica_connections_total ` `: Het totale aantal verbindingen met alle zoekreplica-databases.
    -` ` mattermost_db_store_time ` `: De totale tijd in seconden om een bepaalde database store methode uit te voeren.

HTTP-gegevens:

    -` ` mattermost_http_errors_total ` `: Het totale aantal http API-fouten.
    -` ` mattermost_http_request_duration_seconds ` `: De totale duur in seconden van de http API-aanvragen.
    -` ` mattermost_http_requests_total ` `: Het totale aantal http API-aanvragen. .. image:: ../images/perf_monitoring_http_metrics.png

Aanmeldingsplicht en sessiegegevens:

    -` ` mattermost_http_websockets_total ` ` Het totale aantal WebSocket-verbindingen met de server.
    -` ` mattermost_login_logins_fail_total ` `: Het totale aantal mislukte aanmeldingen.
    -` ` mattermost_login_logins_total ` `: Het totale aantal succesvolle aanmeldingen.

Berichtengebruikscijfers:

    -` ` mattermost_post_broadcasts_total ` `: Het totale aantal verzonden WebSocket-uitzendingen omdat er een post is gemaakt.
    -` ` mattermost_post_emails_sent_total ` `: Het totale aantal e-mails dat is verzonden omdat er een post is gemaakt.
    -` ` mattermost_post_file_attachments_total ` `: Het totale aantal bestandsbijlagen dat is gemaakt omdat er een post is gemaakt.
    -` ` mattermost_post_pushes_sent_total ` `: Het totale aantal mobiele push-meldingen dat is verzonden omdat er een post is gemaakt.
    -` ` mattermost_post_total ` `: Het totale aantal gecreëerde posten.
    -` ` mattermost_post_webhooks_totalen ` `: Het totale aantal webhook-posts gemaakt. .. image:: ../images/perf_monitoring_messaging_metrics.png

Gebruikscijfers verwerken:

    -` ` mattermost_process_cpu_seconds_total ` `: Totale gebruiker en systeem CPU-tijd besteed in seconden.
    -` ` mattermost_process_max_fds ` `: Maximum aantal open bestandsdescriptors.
    -` ` mattermost_process_open_fds ` `: Aantal open bestandsdescriptors.
    -` ` mattermost_process_resident_memory_bytes ` `
Grootte van intern geheugen in bytes.
    -` ` mattermost_process_start_time_seconds ` `: Begintijd van het proces sinds unix epoch in seconden.
    -` ` mattermost_process_virtual_memory_bytes ` `: Virtuele geheugengrootte in bytes.

Zoekgegevens:

    -` ` mattermost_search_posts_searches_duration_seconds_sum ` `: De totale duur, in seconden, van zoekquery-aanvragen.
    -` ` mattermost_search_posts_searches_duration_seconds_count ` `: Het totale aantal zoekquery-aanvragen.

WebSocket-gebruikscijfers:

    -` ` mattermost_websocket_broadcasts_total ` `: Het totale aantal WebSocket-uitzendingen dat per type wordt verzonden.
    -` ` mattermost_websocket_event_total ` `: Het totale aantal WebSocket-events dat per type wordt verzonden.
    
Gebruikscijfers logboekregistratie:

    -` ` logger_queue_used ` `: Huidige logwachtrij niveau (s).
    -` ` logger_logged_total ` `: Het totale aantal uitgezonden logboekrecords.
    -` ` logger_error_total ` `: Het totale aantal logfouten.
    -` ` logger_dropped_total ` `: Het totale aantal logboekrecords is verwijderd.
    -` ` logger_blocked_total ` `: Het totale aantal geblokkeerde logboekrecords.

Standaard GO-gebruikscijfers
-------------------------------------------------------

De Prometheus-integratie biedt ook standaard GO-gebruikscijfers voor de runtime profileringsgegevens en systeembewaking van de HTTP-server, zoals:

    -` ` go_memstats_alloc_bytes ` ` voor geheugengebruik
    -` ` go_goroutines ` ` voor GO routines
    -` ` go_gc_duration_seconds ` ` voor opschoning duur
    -` ` go_memstats_heap_objects ` ` ` voor object tracking op de hoop

Voor informatie over het instellen van runtime profilering raadpleegt u het ` pprof-pakket GO-documentatie <https://golang.org/pkg/net/http/pprof/> ` __. U kunt ook de pagina ` ` ip:port/metrics ` ' bezoeken voor een volledige lijst met gebruikscijfers met beschrijvingen.

Als deze optie is ingeschakeld, kunt u de profileringsregel uitvoeren door

    ` ` go tool pprof channel http://localhost:<port>/debug/pprof/profile ` `

waarbij u ` ` localhost ` ` kunt vervangen door de servernaam. De profileringsrapporten zijn beschikbaar in ` `<ip>:<port>` `, waaronder:

    -` ` /debug/pprof/ ` ` ` voor CPU-profilering
    -` ` /debug/pprof/cmdline/ ` ` voor opdrachtregelprofilering
    -` ` /debug/pprof/symbol/ ` ` voor symbolenprofilering
    -` ` /debug/pprof/goroutine/ ` ` voor GO routine-profilering
    -` ` /debug/pprof/heap/ ` ` voor heapprofilering
    -` ` /debug/pprof/threadcreate/ ` ` voor threads profilering
    -` ` /debug/pprof/block/ ` ` voor blokprofilering .. image:: ../images/perf_monitoring_go_metrics.png

Veelgestelde vragen
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Vragen

Waarom Zijn Diagramlabels Moeilijk Te Onderscheiden?
-------------------------------------------------------

De diagramlabels die worden gebruikt in serverfilters en legendes zijn gebaseerd op de hostnaam van uw machines. Als de hostnamen vergelijkbaar zijn, zal het moeilijk zijn om de labels te onderscheiden.

U kunt meer beschrijvende hostnamen voor uw machines instellen of de weergavenaam wijzigen met een ` ` relabel_config ` ` in ` Prometheus configuratie <https: //prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config> ` __.
