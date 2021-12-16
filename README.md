<header>
<h1>Présentaion</h1>
<p>LITReview est un site web qui permet a ses utilisateurs de consulter ou de solliciter une critique de livres à la demande</p>
</header>

<body>
<section>
<h2>Fonctionnement</h2>

<p>Pour intéragir avec le site web, l'utilisateur doit se créer un compte personnel avec une adresse mail et mot de passe.<br>A chaque connexion au site l'utilisateur doit saisir ses identifiant afin d'acceder à son compte.<br>
utilisateur peut poster des critiques ou répondre aux publications d'autres membres de la 
communauté.<br>
Un système d'abonnement permet de suivre d'autres membres de la communauté ainsi pouvoir réagir à leurs publications.
</p>
<article>
	<ul>
		<li>Système d'authentification</li>
		<li>Publier une critique (joindre un fichier avec le post)</li> 
		<li>Poster une critique sur un post de son flux d'actualité</li>
		<li>Supprimer ou modifier un post</li>
		<li>Système d'abonnement (suivre d'autres utilisteurs)</li>
		...
	</ul>
</article>
</section>
<section>
<h3>Installation</h3>
<p>
Assurez vous d'avoir installé en local le gestionnaire de version git et le gestionnaire de paquets python pip. <br>Ouvrez le terminal git et, suivez les étapes ci-dessous.<br>
</p>
<article>
	<ul>
		<li>Initialise le répertoire courant avec la commande<br> 
			<mark>git init</mark></li>
		<li>Clonez le respository github en local <br>
			<mark>git clone https://github.com/mavamalonga/litreview-web-app.git</mark>
		<li>Placez vous dans le répertoire principal du projet et, créez un environnement virtuel
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
<p>
Les données du programme seront sauvegardés dans un fichier sqlite.db dans le repertoire principal.
</p>

<p>
Pour toute autre question, contactez moi à l'adresse suivante : mavamalonga.alpha@gmail.com
</p>
</article>
</section>
</body>
