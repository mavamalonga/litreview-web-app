<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>LITReview</h1>
	<p>
		LITReview est un site web qui permet a ses utilisateurs de consulter ou de solliciter une critique de livres à la demande.
	</p>
	<h2>Exécution</h2>
	<ul>
		<li>Se déplacer dans le répertoire racine epic-events <code>cd litreview</code></li>
		<li>Lancer le serveur django <code>python manage.py runserver</code></li>
	</ul>
	<h3>Fonctionnement</h3>
	<p>Pour int�ragir avec le site web, l'utilisateur doit se cr�er un compte personnel avec une adresse mail et mot de passe.<br>A chaque connexion au site l'utilisateur doit saisir ses identifiant afin d'acceder � son compte.<br>
	utilisateur peut poster des critiques ou r�pondre aux publications d'autres membres de la 
	communaut�.<br>
	Un syst�me d'abonnement permet de suivre d'autres membres de la communaut� ainsi pouvoir r�agir � leurs publications.
	</p>
	<article>
		<ul>
			<li>Syst�me d'authentification</li>
			<li>Publier une critique (joindre un fichier avec le post)</li> 
			<li>Poster une critique sur un post de son flux d'actualit�</li>
			<li>Supprimer ou modifier un post</li>
			<li>Syst�me d'abonnement (suivre d'autres utilisteurs)</li>
			...
		</ul>
	</article>
	<h3>Installation</h3>
	<p>
	Assurez vous d'avoir install� le gestionnaire de version git et le gestionnaire de paquets python pip. <br>Ouvrez le terminal git et, suivez les �tapes ci-dessous.<br>
	</p>
	<article>
		<ul>
			<li>Initialise le r�pertoire courant avec la commande<br> 
				<mark>git init</mark></li>
			<li>Clonez le respository github en local <br>
				<mark>git clone https://github.com/mavamalonga/litreview-web-app.git</mark>
			<li>Placez vous dans le r�pertoire principal du projet et, cr�ez un environnement virtuel
				<br><mark>python -m venv env</mark></li>
			<li>Lancez l'environnement virtuel<br>
				<mark>env\Scripts\activate.bat</mark></li>
			<li>Installez les paquets python avec le gestionnaire de paquets pip<br>
				<mark>pip install -r requirements.txt</mark></li>
			<li>Lancez les migrations de la database avec les commandes suivantes : <br>
				<mark>python manage.py makemigrations</mark><br>
				<mark><mark>python manage.py migrate</mark></mark></li>
			<li>Enfin lancez le programme en activant le serveur local avec le fichier manage.py<br>
				<mark>py manage.py runserver</mark></li>
		</ul>
	<p>Les donn�es du programme seront sauvegard�s dans un fichier sqlite.db dans le repertoire principal.</p>
	<p>Pour toute autre question, contactez moi � l'adresse suivante : mavamalonga.alpha@gmail.com</p>
	</article>
</body>
</html>