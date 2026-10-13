Question 1 :
Premier commit de fonctionnalité (`feat(api): en-tête X-Visites-Version`) : 13h19.
PR #1 ouverte à 13h23, fusionnée sur main à 14h13. Délai de 55 minutes.
Il a surtout été allongé par l'attente de la relecture et par nos erreurs de branche (commit fait sur main par erreur).

Question 2 :
- toutes les commandes git (branches, commits, rebase, conflits, tags)
- la signature SSH des commits et des tags
- Conventional Commits, pre-commit et ruff, pytest, Docker.

Question 3 :
La forge authentifie la personne qui pousse, pas l'auteur de chaque commit.
Le nom et l'e-mail d'un commit sont déclaratifs : n'importe qui peut les imiter.
La signature est stockée dans le commit lui-même : elle reste vérifiable si
quelqu'un d'autre pousse nos commits, si le dépôt est migré vers une autre forge,
ou si un compte de la forge est compromis.

Ce qui nous a pris le plus de temps :
le conflit qui ne se déclenchait pas car les titres étaient identiques

TP2 :

Question 1:
La revue obligatoire, mais elle n'est pas fiable car dans notre simulation, la PR contenant le jeton a été approuvée manuellement.
Automatiquement gitleaks en pre-commit (local, contournable avec '--no-verify' ou s'il n'est pas installé), gitleaks dans la CI comme contrôle requis (TP03), et le Secret Scanning push protection de GitHub (côté serveur, mais seulement sur des base déjà connu).
La plus fiable reste le contrôle automatique côté serveur (contrôle requis dans le ruleset), car personne ne peut le contourner ni l'oublier.

Question 2:
Non, les hooks ne sont pas clonés avec le dépôt : chacun doit lancer
'pre-commit install', et 'git commit --no-verify' les ignore. Nous l'avons
constaté (commit du faux jeton passé avant l'installation du hook). Il faut
lancer gitleaks dans le pipeline CI sur chaque PR et le déclarer comme
contrôle requis dans le ruleset.



Question 3 :
Pratiquement aucun : des bots surveillent en continu le flux public de GitHub et récupèrent les secrets en quelques minutes. Il faut le considérer compromis immédiatement. GitHub Secret Scanning prévient les fournisseurs partenaires, et certains jetons sont révoqués automatiquement :
jetons GitHub eux-même PyPI, npm, Slack… AWS met les clés exposées en quarantaine.

Ce qui nous a pris le plus de temps :
la clé de signature manquante sur GitHub
l'ordre des PR (CODEOWNERS avant Dependabot)
