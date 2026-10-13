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
