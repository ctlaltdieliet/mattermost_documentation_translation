.. _custom-service-van-service:

Aangepaste servicevoorwaarden (Beta) (E20)
== == == == == == == == == == == == == == == == == == =

Beschikbaar in ` Enterprise Edition E20 en hoger <https://mattermost.com/pricing-self-managed/> ` __.

In Matterste Enterprise Edition E20 kunt u aangepaste Servicevoorwaarden voor uw teamleden aangeven voordat ze Matterbest op internet, desktop of mobiel kunnen benaderen.

Servicevoorwaarden configureren
--------------------------------

Aangepaste servicevoorwaarden inschakelen:

1. Ga naar ** System Console > Customization > Custom Terms of Service * * in eerdere versies of ** System Console > Compliance > Custom Terms of Service * * in versies na 5.12.
2. Set ** Enable Custom Terms of Service * * to ** true**.
3. Set ** Custom Terms of Service Text * * die uw voorwaarden bevat. Merk op dat Markdown-opmaak, inclusief lijsten, koppen en bouten, wordt ondersteund.
4. Set ** Re-Acceptatieperiode * *, die het aantal dagen voor de acceptatie van de Servicevoorwaarden bepaalt, en de voorwaarden moeten opnieuw worden geaccepteerd. Stel de waarde in op 0 als u niet wilt dat de voorwaarden vervallen.
5. Klik op ** Save**.

Eenmaal opgeslagen, moeten alle gebruikers de servicevoorwaarden accepteren door te klikken op ** I Agree * * de volgende keer dat ze inloggen, of op de volgende pagina vernieuwen. Als ze niet accepteren, worden ze afgemeld. .. Opmerking:

 Als u een update naar uw servicevoorwaarden maakt, zorg er dan voor dat u de serviceverbinding bijwerkt op ** System Console > Customization > Legal and Support > Terms of Service link * * in eerdere versies of ** System Console > Site Configuration > Customization * * in versies na 5.12. Deze link wordt voor alle gebruikers op elk logboek weergegeven en is gemakkelijk toegankelijk voor eindgebruikers nadat de voorwaarden zijn geaccepteerd.

Veelgestelde vragen
----------------------------

Wat gebeurt er als ik mijn voorwaarden voor de dienstverlening bijstel? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Er zijn geen gevolgen voor uw eindgebruikers. Gebruikers zullen gewoon nodig zijn om de nieuwe voorwaarden te accepteren bij de volgende login of pagina vernieuwen.

Hoe weet ik of mijn gebruikers akkoord gaan met de servicevoorwaarden? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Elke keer dat een gebruiker akkoord gaat met de servicevoorwaarden, wordt de overeenkomst vastgelegd in de database:

 -Een nieuw veld ` ` AcceptedServiceTermsId ` ` in de tabel ** Users** geeft de meest recente servicevoorwaarden aan die de gebruiker heeft geaccepteerd.
 -Elke keer dat een gebruiker de voorwaarden accepteert, wordt de actie vastgelegd in de tabel ** Audits**, met daarin de gebruikersnaam, de tijdsaanduiding van de acceptatie en andere relevante informatie.

Waarom is deze functie niet in Team Edition voor GDPR-naleving? ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Servicevoorwaarden worden aangeboden aan gebruikers bij het aanmelden en het maken van accounts, en beschikbaar voor gebruikers te allen tijde in de link die is opgegeven op ** System Console > Customization > Legal and Support > Terms of Service link * * in eerdere versies of ** System Console > Site Configuration > Customization * * in versies na 5.12.

Deze functie is bedoeld om te voldoen aan de nalevingsvereisten voor grote Enterprise-bedrijven.

Waarom zijn de aangepaste termen van de beta? ^ ^ ^ ^
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

Deze functie is geëtiketteerd als beta, terwijl we controleren de kwaliteit van de functie in verschillende scenario's. Bekende problemen zijn:

-Aanmelden mislukt wanneer aangepaste servicevoorwaarden zijn ingeschakeld en MFA wordt afgedwongen.
-De servicetekst verdwijnt in de systeemconsole op het moment dat de service wordt vernieuwd.
-De servicevoorwaarden worden onmiddellijk na een update naar termen geladen, in plaats van na aanmelding of op een pagina vernieuwen.
