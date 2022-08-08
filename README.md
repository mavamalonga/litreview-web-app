<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>LITReview</h1>
	<p>
		LITReview est un site web qui permet a ses utilisateurs de consulter ou de solliciter une critique de livres à la demande.
	</p>
	<h3>Fonctionnement</h3>
	<article>
		<ul>
			<li>Système d'authentification</li>
			<li>Publier une critique</li> 
			<li>Consulter son flux d'actualité</li>
			<li>Répondre à une critique</li>
			<li>Supprimer ou modifier un post</li>
			<li>Système d'abonnement</li>
			...
		</ul>
	</article>
	<h3>Installation</h3>
	<p>Assurez vous d'avoir installé le gestionnaire de version git et le gestionnaire de paquets python pip.<br>
	Ouvrez le terminal git et, suivez les étapes ci-dessous.<br>
	</p>
	<article>
		<ul>
			<li><code>git clone https://github.com/mavamalonga/litreview-web-app.git</code></li>
			<li><code>cd litreview-web-app</code></li>
			<li><code>python -m venv env</code></li>
			<li><code>env\Scripts\activate.bat</code></li>
			<li><code>pip install -r requirements.txt</code></li>
		</ul>
	</article>
	<h3>Exécution</h3>
	<ul>
		<li><code>python manage.py runserver</code></li>
	</ul>
	<p>Les données du programme seront sauvegardés dans un fichier sqlite.db dans le repertoire principal.</p>
	<p>Pour toute autre question, contactez moi à l'adresse suivante : mavamalonga.alpha@gmail.com</p>
	</article>
</body>
</html>