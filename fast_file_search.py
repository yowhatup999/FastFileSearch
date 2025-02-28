"""
Dateisuche auf allen verfügbaren Festplatten mit paralleler Verarbeitung.

Dieses Skript sucht nach einer spezifischen Datei auf allen verfügbaren Laufwerken
im System und beendet die Suche automatisch, sobald die Datei gefunden wurde.

Author: Yo
Date: 28.02.2025
"""

import os
import multiprocessing
import time

searchName = "GTA5.exe"


def searchDrive(drive: str, stopEvent: multiprocessing.Event) -> None:
    """
    Durchsucht ein angegebenes Laufwerk rekursiv nach der gewünschten Datei.

    :param drive: Der Laufwerksbuchstabe (z. B. 'C:\\').
    :param stopEvent: Gemeinsames Event, um alle Prozesse beim Fund zu stoppen.
    """
    print(f"Starte Suche auf Laufwerk: {drive}")
    try:
        for root, dirs, files in os.walk(drive, topdown=True, followlinks=False):

            # Abbruchbedingung: Wenn die Datei bereits in einem anderen Prozess gefunden wurde
            if stopEvent.is_set():
                print(f"Suche auf {drive} abgebrochen.")
                return

            try:
                if searchName in files:
                    print(f"Gefunden: {os.path.join(root, searchName)}")
                    stopEvent.set()  # Abbruchsignal an alle Prozesse senden
                    return
            except PermissionError:
                print(f"Berechtigungsfehler bei Zugriff auf: {root}")
            except OSError as osError:
                print(f"OS-Fehler bei Zugriff auf: {root} -> {osError}")
    except Exception as e:
        print(f"Allgemeiner Fehler auf {drive}: {e}")


def getDrives() -> list:
    """
    Ermittelt alle verfügbaren Laufwerke im System.

    :return: Eine Liste mit Laufwerksbuchstaben (z. B. ['C:\\', 'D:\\']).
    """
    drives = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        drive = f"{letter}:\\"
        if os.path.exists(drive):
            drives.append(drive)
    return drives


def startSearch():
    """
    Startet die parallele Suche auf allen verfügbaren Laufwerken
    und bricht die Suche sofort ab, wenn die Datei gefunden wurde.
    """
    startTime = time.time()
    drives = getDrives()
    print(f"Gefundene Laufwerke: {drives}")

    # Manager-Event zum sicheren Teilen des Abbruchsignals zwischen Prozessen
    with multiprocessing.Manager() as manager:
        stopEvent = manager.Event()

        # Parallele Verarbeitung mit maximal 4 Prozessen
        with multiprocessing.Pool(processes=4) as pool:
            pool.starmap(searchDrive, [(drive, stopEvent) for drive in drives])

    print(f"Suchdauer: {time.time() - startTime:.2f} Sekunden")


if __name__ == "__main__":
    startSearch()
