# Git First Steps

Diese Übungen sollen Ihnen helfen, das Versionierungstool **Git** bedienen zu können.

## Getting started

Öffnen Sie ein Terminal (Git Bash oder WSL), um die folgenden Übungen zu absolvieren.
Legen Sie für diese Übung ein eigenes Verzeichnis auf Ihrer Festplatte an und wechseln Sie im Terminal in das Verzeichnis.

## Übung 1

Konfigurieren Sie git, indem Sie **global** Ihren Namen und Ihre studentische Email-Addresse (vorname.nachname@htwk-leipzig.de) setzen.

`git config --global user.name="<Vorname> <Nachname>"`
`git config --gobal user.email="<Ihre Email>"`

Überprüfen Sie, dass Ihre Änderungen akzeptiert wurden.

`git config --global --list` 

## Übung 2: Initialisierung I

Initiieren Sie ein git Repository in Ihrem soeben angelegten Verzeichnis (`git init`).
Lassen Sie sich danach die Inhalte ihres Verzeichnisses über `ls` und `ls -la` anzeigen. Welchen Unterschied bemerken Sie?

## Übung 3: Initialisierung II

Überprüfen Sie den Status Ihres git Repository mithilfe von `git status`.
Was passiert, wenn Sie das versteckte Verzeichnis aus Übung 2 löschen? Überprüfen Sie Ihre Vermutung, indem Sie das Verzeichnis mit `rm -rf .git` löschen und anschließend noch einmal `git status` ausführen.
Legen Sie anschließend ein neues Repository mithilfe von `git init` an.

## Übung 4: Tracken von Dateien

Legen Sie eine Datei `myfile.txt` an mit dem Inhalt "Hello git": `echo "Hello git" >> myfile.txt`.
Überprüfen Sie mithilfe des `cat`-Kommandos, dass der Inhalt erfolgreich in die Datei geschrieben wurde (und dass die Datei existiert).
Nutzen Sie `git status`, um den Zustand Ihres Repositories zu überprüfen. Sie werden sehen, dass die Datei myfile.txt von git erkannt, aber noch nicht getracked wird.
Fügen Sie die Datei zu dem Repository hinzu: `git add myfile.txt`.
Überprüfen Sie die Änderung mithilfe von `git status`.

## Übung 5: Erster Commit

Die Datei `myfile.txt` wird jetzt zwar getracked, ist aber noch nicht im Repository gespeichert. Hierfür müssen wir die Änderungen, die wir durch `git add` verfolgen, auch in das Repository übertragen. Dies geschieht mithilfe von `git commit -m "<Commit Message>"`, wobei der Parameter `-m` angibt, dass das folgende Argument die Commit-Message darstellt.
Führen Sie anschließend `git status` aus und überprüfen Sie die Änderungen.
Führen Sie danach `git log` aus und überprüfen Sie, dass Sie eine Ausgabe ähnlich zu folgender bekommen:
`commit 44e4fd0089781bdfeea04b72ee2767a1fdfa6f4b (HEAD -> main)`

Bei Ihnen wird sehr wahrscheinlich eine andere Zahlen-und-Buchstabenfolge stehen. Dies nennt man einen Hash und dieser dient dazu, einen Commit eindeutig zu identifizieren. Notieren Sie sich den Hash.

## Übung 6: Mehrere Commits

Bearbeiten Sie die Datei `myfile.txt` und fügen Sie ein paar Textzeilen hinzu.
Fügen Sie anschließend die Datei erneut dem Index hinzu und commiten Sie Ihre Änderungen in das lokale Repository.
Überprüfen Sie mit `git log`, dass es nun einen zweiten Commit gibt.
Überprüfen Sie mit `git show`, welche Änderungen Sie durchgeführt haben.

## Übung 7: Dateien wiederherstellen

Löschen Sie die Datei `myfile.txt` und vergewissern Sie sich, dass die Datei wirklich entfernt wurde (`ls`).
Stellen Sie die gelösche Datei aus Ihrem Reppository wieder her: `git restore myfile.txt` und vergewissern Sie sich, dass die Datei wieder im Verzeichnis vorhanden ist.

## Übung 8: Zwischen Commits wechseln

Lassen Sie sich Ihre bisherigen Commits mithifle von `git log` anzeigen.
Wir wollen nun den Inhalt aus Ihrem ersten Commit wiederherstellen.
Wechseln Sie hierfür mit `git reset <commit_hash_1>` zurück.
Stellen Sie den Zustand der Datei zum Zeitpunkt des ersten Commits wieder her.
Überprüfen Sie, dass der Inhalt der Datei myfile.txt tatsächlich geändert wurde.
Rufen Sie erneut `git log` auf. Was stellen Sie fest? Was passiert, wenn Sie `git reset <commit_hash_2>` eingeben und anschließend `git log` aufrufen?

## Übung 9: Branches

Erstellen Sie einen neuen Branch für Ihr Repository: `git branch <name>`
Branches helfen z.B. in der Entwicklung von Software, verschiedene Features parallel und relativ unabhängig voneinander zu entwickeln. Mithilfe von `git branch --list --all` können Sie sich alle Branches Ihres Repositories anzeigen lassen. Nachdem Sie den neuen Branch angelegt haben, befinden Sie sich allerdings immer noch in Ihrem urpsrünglichen Branch. Wechseln Sie den Branch: `git checkout new-branch`.
Legen Sie analog zu Übung 4 eine neue Datei "myfile2.txt" an und füllen Sie sie mit beliebigem Inhalt. Fügen Sie die Datei Ihrem Repository hinzu und commiten Sie Ihre Änderungen.


Wechseln Sie nun zurück zu Ihrem urpsrünglichen Branch. Überprüfen Sie den Inhalt Ihres Verzeichnisses. Was stellen Sie fest?