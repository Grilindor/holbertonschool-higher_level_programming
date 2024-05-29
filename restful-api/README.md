1) A brief summary explaining the differences between HTTP and HTTPS.

En termes simples, la principale différence entre HTTP et HTTPS réside dans la sécurité des données échangées entre votre navigateur et le site Web que vous visitez :

 - HTTP (Hypertext Transfer Protocol) : Les données échangées sont envoyées en texte brut, ce qui signifie qu'elles peuvent potentiellement être interceptées par des pirates informatiques. C'est un protocole non sécurisé.

 - HTTPS (Hypertext Transfer Protocol Secure) : Avec HTTPS, les données sont cryptées avant d'être échangées, ce qui rend la communication plus sécurisée. Les sites Web HTTPS utilisent un certificat SSL/TLS pour sécuriser les données et garantir une connexion plus sûre entre votre navigateur et le serveur du site Web.


2) A depiction or outline of the structure of an HTTP request and response

voici un exemple simplifié de la structure d'une requête et d'une réponse HTTP :

Requête HTTP (GET): GET /api/data HTTP/1.1 Host: www.example.com User-Agent: Mozilla/5.0 Accept: application/json

Réponse HTTP (200 OK): ``` HTTP/1.1 200 OK Content-Type: application/json Content-Length: 56

{ "id": 1, "name": "John Doe", "age": 30 } ```

Dans cet exemple, la requête GET est envoyée au serveur pour récupérer des données à partir de l'URL "/api/data". Le serveur renvoie une réponse avec un code de statut 200 OK, indiquant que la requête a réussi. Les données sont au format JSON et comprennent un objet avec les champs "id", "name" et "age".


3) Lists of common HTTP methods and status codes with their descriptions and possible use cases.

 - GET : utilisé pour demander des données à un serveur. Utilisé lorsque vous souhaitez récupérer des informations à partir d'une ressource spécifiée. Par exemple, récupérer une page Web, récupérer des données à partir d'une API ou télécharger un fichier.

 - POST : utilisé pour soumettre des données à un serveur pour créer une nouvelle ressource. Cette méthode est couramment utilisée lorsque vous souhaitez envoyer des données au serveur pour les traiter ou les stocker. Par exemple, soumettre un formulaire sur un site Web, créer un nouveau compte utilisateur ou envoyer des données à enregistrer dans une base de données.

 - PUT : Utilisé pour mettre à jour ou remplacer une ressource existante sur le serveur. Il est utilisé lorsque vous souhaitez mettre à jour entièrement une ressource avec de nouvelles données. Par exemple, mettre à jour les informations d'un utilisateur, modifier un article de blog ou remplacer un fichier sur le serveur.

 - DELETE : utilisé pour supprimer une ressource spécifiée du serveur. Cette méthode est utilisée lorsque vous souhaitez supprimer une ressource du serveur. Par exemple, supprimer un compte utilisateur, supprimer un fichier ou supprimer un enregistrement d'une base de données.


GET :
200 OK : La requête a réussi et les données demandées sont renvoyées.
404 Not Found : La ressource demandée n'a pas été trouvée sur le serveur.

POST :
201 Created : La requête a réussi et une nouvelle ressource a été créée.
400 Bad Request : La requête du client est incorrecte ou mal formée.

PUT :
200 OK : La requête a réussi et la ressource a été mise à jour.
404 Not Found : La ressource à mettre à jour n'a pas été trouvée.

DELETE :
204 No Content : La ressource a été supprimée avec succès.
404 Not Found : La ressource à supprimer n'a pas été trouvée.
