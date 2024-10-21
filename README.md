# Git First Steps

Diese Übungen sollen Ihnen helfen, das Versionierungstool **Git** bedienen zu können.

## Getting started

Öffnen Sie ein Terminal (Git Bash oder WSL), um die folgenden Übungen zu absolvieren.
Legen Sie für diese Übung ein eigenes Verzeichnis auf Ihrer Festplatte an und wechseln Sie im Terminal in das Verzeichnis.

## Aufgabe 1

Konfigurieren Sie git, indem Sie **global** Ihren Namen und Ihre studentische Email-Addresse (vorname.nachname@htwk-leipzig.de) setzen.

`git config --global user.name="<Vorname> <Nachname>"`
`git config --gobal user.email="<Ihre Email>"`

Überprüfen Sie, dass Ihre Änderungen akzeptiert wurden.

`git config --global --list` 

## Aufgabe 2: Branch anlegen

Clonen Sie dieses Repository mittels git und Terminal und wechseln Sie anschließend in das Repository-Verzeichnis. Legen Sie einen neuen Branch an (`git branch <nutzername>`), wobei Sie `<nutzername>` durch Ihren HTWK-Loginnamen ersetzen.

Jetzt haben Sie zwar den Branch angelegt, befinden sich aber immer noch im Branch `main`. Dies können Sie überprüfen, indem Sie `git branch` eingeben. Wechseln Sie in den neu angelegten Branch: `git checkout <nutzername>`.

## Aufgabe 3: Branch löschen

Versuchen Sie, den erstellten Branch zu löschen: `git branch delete <nutzername>` bzw. `git branch rm <nutzername>`.
Überprüfen Sie das Ergebnis mittels `git branch`.
Löschen Sie die versehentlich erstellten Branches: `git branch -d delete rm`.

## Aufgabe 4: Push

Wenn Sie Dateien von Ihrem lokalen Repository zu einem remote Repository (hier: GitLab) hochladen wollen, spricht man davon, den Code zu pushen. Wichtig hierbei ist, dass Sie Ihre Änderungen commited haben.

Erstellen Sie in Ihrem lokalen git-Repository eine Datei `main.py` mit folgendem Inhalt:
```
import sortierVerfahren.py

print(bubbleSort([3,1,5,-1,7]))
```

Pushen Sie anschließend diese Datei in das remote Repository: `git push --set-upstream origin <branch>`

## Aufgabe 5: Add, Commit, Push

Überprüfen Sie die Ausgabe der vorigen Ausgabe. Diese sollte lauten: `Total 0 (delta 0), reused 0 (delta 0), pack-reused 0`

Grund hierfür ist, dass Sie lediglich die Informationen über Ihren Branch hochgeladen haben. Überprüfen Sie dies in GitLab, indem Sie Ihren Branch auswählen. Dieser sollte noch keine `main.py` enthalten:

![Branch in GitLab auswählen](https://gitlab.dit.htwk-leipzig.de/grundlagen-der-informatik/git-first-steps/-/blob/main/branch_selection.png)

Um Code zu pushen, muss dieser erst dem lokalen Repository zum Tracken hinzugefügt werden (`git add`), anschließend in das lokale Repository geladen werden (`git commit -m "<Ihre Message>"`) und erst dann können Sie den Code mittels `git push` hochladen.

`git add *`

`git commit -m "main.py erstellt"`

`git push`

Das `--set-upstream origin <branch>` können Sie nun weglassen, da es gesetzt bleibt.

Überprüfen Sie, dass Ihr Repository im Branch `<nutzername>` die vorgenommenen Änderungen aufweist.

## Aufgabe 6: fetch, merge, pull

a)

Legen Sie einen neuen branch `<nutzername>-bugfix` an und wechseln Sie in diesen.

Beheben Sie den Fehler in `sortierVerfahren.py` für BubbleSort. Pushen Sie Ihre Lösung in den `<nutzername>-bugfix` Branch:

`git add *`

`git commit -m "sortierVerfahren.py debugged"`

`git push`

Wechseln Sie nun in Ihren anderen Branch `<nutzername>` und überprüfen Sie den Inhalt von `sortierVerfahren.py`. Sind Ihre Änderungen vorhanden?

b)

Um nun die Änderungen von einem Branch in einem anderen Branch einzuspielen, spricht man von `mergen`, d.h. zusammenführen, verschmelzen. In dieser Aufgabe wollen wir die Änderungen im `remote`-Branch `<nutzername>-bugfix` in Ihren lokalen Branch `<nutzername>` übernehmen:

`git merge origin/<nutzername>-bugfix`

Überprüfen Sie, ob die Änderungen übernommen wurden.

## Aufgabe 7: git log

Lassen Sie sich nun einmal die logs für Ihre Arbeit anzeigen: `git log`. Hier sehen Sie die verschiedenen, getätigten Commits mit Ihren Hash-Werten. Diese Hexadezimal-Zahlen dienen der eindeutigen Identifikation eines Commits.

Ein Zeiger `HEAD` zeigt nun, auf welchem Commit und in welchem Branch Sie sich befinden: `commit <hashwert> (HEAD -> <nutzername>, ...)`. Außerdem zeigt er, welche Commits in welchem Branch vorhanden sind.

Der Stand müsste nun ungefähr wie folgt lauten:

Commit i `(HEAD -> <nutzername>, origin/<nutzername>-bugfix, <nutzername>-bugfix)`

Commit i-1 `origin/<nutzername>`

Commit i-2 `main`

## Aufgabe 8: merge in lokalem Branch

Ihr Branch `main` hängt nun einige Commits hinterher. Um lokale Branches zusammenzuführen, wechseln Sie in den Branch, in den Sie die Änderungen hinzufügen wollen und mergen Sie ihn mit dem anderen, ggf neueren Branch.

`git checkout main`

`git merge <nutzername>`

## Aufgabe 9: revert, reset, Detached Heads

Überprüfen Sie für diese Aufgabe, dass Sie sich im lokalen Branch `main` befinden.

Rufen Sie `git log` auf und merken Sie sich den Hashwert des `aktuellen Commits i` und des `Commits i-2`.

Es gibt Situationen, in denen Sie einen Commit rückgängig machen wollen und git stellt Ihnen zwei Möglichkeiten zur Verfügung: `git reset` und `git revert`. Der Unterschied ist, dass `git revert` einen neuen(!) Commit vollzieht, um auf den Stand eines alten Commits zurückzuwechseln:

`git revert <Commit-Hash i-2>`

Es sollte sich ggf ein Editor öffnen. Speichern Sie die Änderungen und beenden Sie den Editor (Strg+S, Strg+X in nano, :wq! in vim).

Checken Sie die Log-Einträge Ihres git-Repositories. Sie sollten nun einen `Commit i+1` sehen, der jedoch erstmal nur lokal existiert.

Meist will man in dieser Situation statt eines neuen Commits einfach seine Änderungen verwerfen. Dies funktioniert mithifle von:

`git reset --hard <Commit-Hash i>` bzw. `git reset --hard HEAD`

wobei das Flag `--hard` alle von Ihnen durchgeführten Änderungen verwirft.

## Aufgabe 10: git stash, git pop

