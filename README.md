# Git First Steps

Diese Übungen sollen Ihnen helfen, das Versionierungstool **Git** bedienen zu können.

## Getting started

Öffnen Sie ein Terminal (Git Bash oder WSL), um die folgenden Übungen zu absolvieren.

a) Konfigurieren Sie git, indem Sie **global** Ihren Namen und Ihre studentische Email-Addresse (vorname.nachname@htwk-leipzig.de) setzen.

`git config --global user.name "<vorname>.<nachname>"`

`git config --gobal user.email "<Ihre Email>"`

Überprüfen Sie, dass Ihre Änderungen akzeptiert wurden.

`git config --global --list`

Die Ausgabe sollte wie folgt aussehen:

```
user.email=<Ihre Email>
user.name=<Ihr_Name.Ihr_Vorname>
```

b) Legen Sie sich nun noch ein Access Token an, das Sie sich speichern müssen, da es nach dem Erstellen nicht wieder angezeigt werden kann. Das Personal Access Token kann angelegt werden unter: https://gitlab.dit.htwk-leipzig.de/-/user_settings/personal_access_tokens Stellen Sie sicher, dass Sie die Checkboxen mit "api", "read_repository" und "write_repository" aktivieren.

c) Legen Sie für diese Übung ein eigenes Verzeichnis auf Ihrer Festplatte an und wechseln Sie im Terminal in das Verzeichnis.

## Aufgabe 1

Clonen Sie dieses Repository mittels git und Terminal:
`git clone https://<vorname.nachname>:<your_access_token>@gitlab.dit.htwk-leipzig.de/grundlagen-der-informatik/git-first-steps.git`

Anschließend wechseln Sie in das heruntergeladene Verzeichnis:
`cd git-first-steps`

## Aufgabe 2: Branch anlegen

Sie haben nun den `main`-Branch aus dem Remote-Repository auf Ihrem lokalen Rechner heruntergeladen. Allerdings ist der `main`-Branch geschützt, um zu verhindern, dass durch einen Upload ungewollt versehentliche Änderungen übernommen werden. Man arbeitet mit `Branches`, um eine bessere, aufgabenzentrierte Übersicht zu haben und nicht gleichzeitig an der selben Code-Base zu schreiben.

 Legen Sie einen neuen Branch an (`git branch <nutzername>`), wobei Sie `<nutzername>` durch Ihren HTWK-Loginnamen ersetzen.

Jetzt haben Sie zwar den Branch angelegt, befinden sich aber immer noch im Branch `main`. Dies können Sie überprüfen, indem Sie `git branch` eingeben. Wechseln Sie in den neu angelegten Branch: `git checkout <nutzername>`.

## Aufgabe 3: Branch löschen

Versuchen Sie, den erstellten Branch zu löschen: `git branch delete <nutzername>` bzw. `git branch rm <nutzername>`.
Überprüfen Sie das Ergebnis mittels `git branch`.
Löschen Sie die versehentlich erstellten Branches: `git branch -d delete rm`.

## Aufgabe 4: Erster Push

Diese Aufgabe dient dazu, nochmal nachzuvollziehen, was an den einzelnen "Orten" (Ihr Rechner, GitLab im Browser) passiert.

Wenn Sie Dateien von Ihrem lokalen Repository zu einem remote Repository (hier: GitLab) hochladen wollen, spricht man davon, den Code zu `push`en. Wichtig hierbei ist, dass Sie Ihre Änderungen `commit`ed haben.

Erstellen Sie in Ihrem lokalen git-Repository eine Datei `main.py` mit folgendem Inhalt:
```
import sortierVerfahren.py

print(bubbleSort([3,1,5,-1,7]))
```

Pushen Sie anschließend diese Datei in das remote Repository: `git push --set-upstream origin <nutzername>`

Überprüfen Sie die Ausgabe der vorigen Ausgabe. Diese sollte lauten: `Total 0 (delta 0), reused 0 (delta 0), pack-reused 0`

Im Browser in GitLab sollten Sie nun feststellen, dass Sie einen neuen Branch angezeigt bekommen, aber dieser Branch noch keine Dateien beinhaltet:

![Branch in GitLab auswählen](https://gitlab.dit.htwk-leipzig.de/grundlagen-der-informatik/git-first-steps/-/blob/main/branch_selection.png)

## Aufgabe 5: Add, Commit, Push

Grund für die "fehlenden Dateien" ist, dass Sie lediglich die Informationen über Ihren Branch hochgeladen haben, da die Dateien nicht getracked und committed waren.

Um Code zu pushen, muss dieser erst dem lokalen Repository zum Tracken hinzugefügt werden. Überprüfen Sie mit `git status`, welche Änderungen Sie vollzogen haben und welche bereits getrackt werden. Fügen Sie nun die `main.py` zum Tracking hinzu (`git add`). Anschließend müssen die getrackten Änderungen in das lokale Repository geladen werden (`git commit -m "<Ihre Message>"`) und erst dann können Sie den Code mittels `git push` in das remote Repository (GitLab) hochladen.

Überprüfen Sie mittels `git status` den Zustand Ihres lokalen Repositories.

Fügen Sie nun alle Dateien (`*` für alle) dem Tracking hinzu.

`git add *`

Nun fügen Sie Ihre Änderungen von Ihrem Workspace zum lokalen Repository hinzu:

`git commit -m "main.py erstellt"`

Nun sollte `git status` anzeigen, dass alle Änderungen aus Ihrem Workspace im lokalen Repository vermerkt sind. Jetzt können Sie den Code vom lokalen Repository in das Remote Repository (GitLab) hochladen.

`git push`

Überprüfen Sie in Ihrem Browser, dass nun auch in Ihrem Branch die Code-Änderungen und der Commit-Eintrag vorhanden sind.

<strong>Hinweis:</strong>Das `--set-upstream origin <branch>` können Sie nun weglassen, da es gesetzt bleibt.