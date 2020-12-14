.. _dev-setup-probleemoplossing:

Problemen oplossen voor installatie en build
== == == == == == == == == == == == == == == =

Buildfouten
------------

macOS: Ik krijg de volgende fout bij het uitvoeren van ` ` make run ` `: "Kan geen verbinding maken met de Docker-daemon"
  Als u Docker Tools hebt geïnstalleerd (in tegenstelling tot Docker for Mac), controleer dan of de docker-machine actief is.

  ` ` docker-machine start dev ` ` `

macOS: Ik krijg de volgende fout of iets dergelijks bij het uitvoeren van ` ` make run ` `: "Module build mislukt: Error: dyld: Bibliotheek niet geladen: /usr/local/opt/libpng/lib/libpng16.16.dylib" libpng moet worden bijgewerkt omdat het wordt gebruikt door een van onze afhankelijkheden. Als u geen libpng hebt geïnstalleerd via Homebrew, start u

  ` ` brew install libpng ` `

  Als libpng al geïnstalleerd is via Homebrew, kunt u het bijwerken met de volgende opdracht:

  ` ` brew update & & brew upgrade libpng ` `

Ik krijg de volgende fout bij het uitvoeren van ` ` make run ` `: "Failed to ping db err: dial tcp 192.168.99.100:3306: getsockopt: connection geweigerd"
  Het lijkt erop dat uw MySQL database niet draait. Als je ` ` docker ps ` ` uitvoert, zou je een lijn als

  .. code-blok :: tekst

    ecb17c10973d mysql:5.7 "/entrypoint.sh mysql" 2 weken geleden Up 24 uur 0.0.0.0:3306-> 3306/tcp matterbest-mysql

  Als dit niet het geval is, verwijdert u ' ` make clean-docker ` ` alle bestaande Docker-containers, zodat ze opnieuw worden gemaakt wanneer u ` ` make run ` ` belt.

Ik krijg de volgende foutmelding bij het uitvoeren van ` ` make run ` `: "Error start server, err: listen tcp: 8065: bind: adres al in gebruik"
  Er is waarschijnlijk nog een andere Matterinstance die al actief is. U kunt ` ` make stop ` ` gebruiken om het te stoppen voordat het uitvoeren van ` ` make run ` ` opnieuw.

  Als er geen andere kopie is van Matterbest en u moet de poort wijzigen waarop Matterbest actief is, kunt u dit doen door de instelling ` ` ListenAddress ` ` in de sectie *ServiceSettings * van ` `config/config.json ` ` te wijzigen.

macOS: Ik krijg de volgende fout of iets dergelijks bij het uitvoeren van ` ` make run ` `: [ EROR] Fout bij ping DB reproberen in 10 seconden err = Fout 1045: Toegang geweigerd voor gebruiker 'mmuser' @ 'localhost' (met wachtwoord: JA) Het lijkt erop dat 'mmuser' niet wordt gemaakt als gebruiker in uw MySQL-database. Maak daarom de nieuwe gebruiker met behulp van de volgende opdracht: ` ` CREATE USER 'mmuser' @ 'localhost' IDENTIFIED BY 'mostest'; ` `

  Verleen alle machtigingen aan de gebruiker met behulp van de opdracht:

  ` ` VERLEEN ALLE BEVOEGDHEDEN AAN *. * AAN '
  mmuser '@ 'localhost'; ` `

  Laad de bevoegdheden opnieuw, zodat de wijzigingen kunnen worden weergegeven: ` ` FLUSH PRIVILEGES; ` `

Testfouten
--------------

Ik krijg de volgende fout bij het uitvoeren van ` ` make test ` `: t. Run undefined (type * testing.T heeft geen veld of methode Run)
  U moet upgraden naar Go 1.9. We ondersteunen geen eerdere versies dan dat.

Andere fouten
------------

Ik zie geen foutmeldingen, maar ik heb geen toegang tot http://localhost: 8065
  Het is mogelijk dat de server een fout heeft gemeld, maar dat deze is overgeslagen vanwege alle uitvoer van het JavaScript-compileerprogramma. Probeer ' ` make run-server ` ` te laten draaien op zichzelf om
zie de uitvoer. Als u nog steeds geen foutberichten ziet, gaat u verder met het volgende gedeelte.

Ik zie niets dat bij de console is vastgelegd als Matterbest actief is. U kunt het vastleggen van de console inschakelen in het gedeelte *LogSettings * van uw ` `config/config.json ` ` door *EnableConsole * in te stellen op ` ` true ` `.

Ik kan niet inloggen op Matterbest omdat ik geen account heb Je kunt een account maken met behulp van de volgende opdracht:

  ` ` go build -o matterbest & & ./matterbest user create -- email user@example.com -- username test1-password mypassword ` `

  Desgewenst kunt u met de volgende opdracht een systeembeheerder maken:

  ` ` go build -o matterbest & & ./matterbest user create -- email user@example.com -- username test1--password mypassword -- system_admin ` `
