Schaal voor Enterprise == == == == == == == == == == ==

Matterbest is ontworpen om te schalen van kleine teams die worden gehost op een enkele server voor grote bedrijven die actief zijn in op clusters gebaseerde, zeer beschikbare implementatieconfiguraties. 

De serververeisten variëren op basis van het gebruik en het wordt ten zeerste aanbevolen dat de piloten worden uitgevoerd voordat de implementatie van het gehele bedrijf wordt uitgevoerd, om op basis van uw specifieke organisatorische behoeften een schatting te kunnen maken van het gebruik van de volledige schaal. 

Enkele Machine-implementatie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Organisaties kunnen meestal Matterbest uitvoeren op een enkele server met maximaal 2.000 gebruikers, hoewel er meer gebruikers zijn waargenomen op basis van verschillende gebruik-en serverconfiguraties.

-Zie ` install guides for step-by-step configuration instructions for single machine setup <https: //docs.mattermost.com/guides/administrator.html#installing-mattermost> ` __.
-Zie ` hardware and software requirements for hardware sizing <https://docs.mattermost.com/install/requirements.html> ` __.

Multi Machine-implementatie ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Implementaties tussen 2000 en 10.000 geregistreerde gebruikers met matig gebruik kunnen draaien op een standaard drie-machine Mattermeest implementatie met een proxy, een toepassingenserver en een databaseserver. Op deze schaal kunnen eisen van grotere organisaties meestal worden voldaan door gebruik te maken van krachtige hardware in een standaard configuratie. 

-Zie ` install guides for step-by-step configuratie instructies voor multi-machine setup. <https: //docs.mattermost.com/guides/administrator.html#installing-mattermost> ` __
-Zie ` hardware and software requirements for hardware sizing <https://docs.mattermost.com/install/requirements.html> ` __.

Implementatie op basis van clusters ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

*Beschikbaar in Enterprise Edition E20 *

Implementaties van meer dan 10.000 geregistreerde gebruikers met een matig gebruik kunnen worden ondersteund door het toevoegen van extra servers in clustergebaseerde, hoge-beschikbaarheidsconfiguratie. Tot op heden omvatte de grootste simulatie ` 70.000 gelijktijdige gebruikers op een enkel Matterfste exemplaar: <https://mattermost.com/blog/performance-scale-mattermost/> ` __.

Deze configuratie maakt gebruik van een werklastverdeler voor het distribueren van aanvragen van gebruikers over meerdere Mattermeeste toepassingenservers, waardoor het systeem de limieten van een enkele server kan overschrijden. 

Voor meer informatie raadpleegt u 'High Availability Deployment Guide for horizontal scaling setup <https://docs.mattermost.com/deployment/cluster.html>' __.

Voorbeeld van schaalverdeling ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze handleiding laat zien hoe u een budget voor grote Mattermeeste-implementaties kunt maken en bouwen.

Matterbest kan worden ingezet op locatie of op het cloud-platform van uw keuze, waaronder AWS, Google Cloud, Microsoft Azure en Oracle Cloud. Deze gids maakt gebruik van AWS als voorbeeld.

Op basis van de ` hardware requirements <https: //docs.mattermost.com/install/requirements.html#hardware-requirements> ` __, hier is de serverarchitectuur van Matterbest voor een implementatie van 10.000 gebruikers: .. image:: ../images/scaling-1.png

** Sizing Guide met behulp van AWS* *

Op AWS, raden wij het gebruik van de volgende EC2-server types als een b
aseline:

* App servers: m5.xlarge
* Database servers: r4.xlarge

Voor de toepassing van deze handleiding wordt uitgegaan van het gemiddelde gebruik (10 MB/gebruiker/maand met een 2x veiligheidsfactor) voor ` opslagramingen <https: //docs.mattermost.com/install/requirements.html#alternate-storage-calculations> ` __ en 200 MB/gebruiker/maand voor schattingen van de gegevensoverdracht. We zullen ook on-demand pricing met geen upfront betalingen, hoewel meer besparingen (meestal 40% of meer) kunnen worden bereikt met gereserveerde servers op 1-3 jaar toezeggingen en upfront betalingen.

Als implementatie op schaal van meer dan 5000 gebruikers, worden extra servers toegevoegd voor prestatiebelastingsverdeling en voor het leveren van extra redundantie (zie onze ` High Availability Cluster guide <https: //docs.mattermost.com/deployment/cluster.html#mattermost-server-configuration> ` __).

` Deze spreadsheet <https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vRkhRPFsf1_91AXFbqnmUT0UnpdZ1ZagbiTw9sfuBAL21ncnu7fynZ3yDrp22-LXCeXh0-xF_NFFPp3/pubhtml> ` __ toont hoeveel hardware je nodig hebt voor verschillende-sized Mattermeeste implementaties en geeft een schatting van hoeveel elk kost. Het bevat links naar AWS ' s kostencalculator voor verschillende implementatiegrootten. De kleinere implementatievoorbeelden (d.w.z. 1.000 gebruikers en 5.000 gebruikers) zijn aan de conservatieve kant, met aparte servers per functie die gemakkelijk kan worden opgeschaald als Matterbest wordt uitgerold. 

Hier is een voorbeeld van de hardware die je nodig hebt voor een implementatie van 10.000 gebruikers: .. image:: ../images/scaling-3.PNG

Voor meer informatie, kijk op onze ` Administrator's Guide <https://docs.mattermost.com/guides/administrator.html> ` __.

Hosting-aanbeveling voor 100.000 + gebruikers ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

De volgende matrix presenteert de belangrijkste kenmerken voor een succesvolle multi-regio Mattermeeste implementatie die schubben tot 100.000 gebruikers met ondersteuning voor hoge beschikbaarheid en geografisch gebaseerd verkeer routing in op het terrein, AWS, en Azure implementaties. .. csv-table ::
    :header: "Functie", "Op Het Terrein", "Amazon AWS", "Azure"

    "Multi-regio/datacenterondersteuning", "Ja", "Regio's: 16", "Regio's: 54"
    "Auto scaling voor Matterigste knooppunten", "Ja-met behulp van een oplossing zoals Kubernetes", "` AWS Auto Scaling <https://aws.amazon.com/ec2/autoscaling/> ` __", "` Azure Autoscale <https://azure.microsoft.com/en-us/features/autoscale/> ` __"
    "Geografische verkeersroutering", "Ja", "` Route 53 <https://aws.amazon.com/route53/> ` __", "` Azure DNS <https://azure.microsoft.com/en-us/services/dns/> ` __"
    "Load balancing", "Yes", "` Elastic Load Balancer <https://aws.amazon.com/elasticloadbalancing/> ` __", "` Azure Load Balancer <https://azure.microsoft.com/en-us/services/load-balancer/> ` __" "Multi-region, HA storage", "Yes", "` S3 <https://aws.amazon.com/s3/> ` __", "?"" Multi-region, HA MySQL "," Yes-using a solution like Galera "," ` Aurora <https://aws.amazon.com/rds/aurora/> ` __/` RDS for MySQL <https://aws.amazon.com/rds/mysql/> ` __ "," ` Azure MySQL <https://azure.microsoft.com/en-us/services/mysql/> ` __" "Multi-region, HA PostgreSQL "," Yes "," ` Aurora <https://aws.amazon.com/rds/aurora/> ` __/` RDS for PostgreSQL <https://aws.amazon.com/rds/postgresql/> ` __ "," ` Azure PostgreSQL <https://azure.microsoft.com/en-us/services/postgresql/> ` __" "Multi-region, HA elasticsearch "," Yes "," ` Amazon Elasticsearch Service <https://aws.amazon.com/elasticsearch-service/> ` __ ", "No"
