Contribuer au projet
Flux de travail
Partir de `main` à jour : `git switch main && git pull`
Créer une branche : `git switch -c <type>/<sujet>` (ex. `feat/reset`, `docs/journal`)
Committer (commits signés automatiquement) puis pousser : `git push -u origin HEAD`
Ouvrir une pull request avec `gh pr create`, en expliquant quoi, pourquoi et comment tester
Faire relire par l'autre membre : jamais de fusion sans approbation
Fusionner par squash : `gh pr merge <num> --squash --delete-branch`
Supprimer la branche locale : `git branch -D <branche>`
On ne committe jamais directement sur `main`.
Revue
Le relecteur récupère la branche (`gh pr checkout <num>`) et lance les tests.
Les corrections se font par un nouveau commit (pas de `--amend` ni de `--force` sur une branche partagée).
Pour mettre une branche à jour : `git fetch origin && git rebase origin/main`, puis `git push --force-with-lease`.
Convention de commits
Format Conventional Commits : `<type>(<portée>): <description>`


Type
Usage
`feat`
nouvelle fonctionnalité
`fix`
correction de bug
`docs`
documentation
`test`
ajout ou modification de tests
`refactor`
modification du code sans changer le comportement
`chore`
outillage, configuration
Exemple : `feat(api): ajouter la route POST /reset`
Lancer le projet et les tests
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
docker run -d --name redis -p 6379:6379 redis:8-alpine
pytest -q # tests unitaires (faux Redis)
pytest -m integration # tests avec le vrai Redis
pre-commit
pre-commit install # une fois, après le clone
pre-commit run --all-files # vérifier tout le dépôt
Si un hook modifie des fichiers, les ajouter (`git add`) puis committer à nouveau.
