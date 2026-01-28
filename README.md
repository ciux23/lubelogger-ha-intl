# LubeLogger International for Home Assistant

> Custom integration for [LubeLogger](https://www.lubelogger.com/), adapted for the **Metric System** (International Units).

## Features
- Creates a device for each vehicle in your LubeLogger instance.
- Sensors for: odometer, next maintenance, latest fuel fill-up, tax payments, service/repair/upgrade/supply records, and reminders.
- **International Unit Support**: Automatic conversion for European number formats (comma as decimal separator) and date formats (DD/MM/YYYY).

## Installation

### Via HACS (Recommended)
1. In HACS, go to **Integrations** → **Custom repositories**.
2. Add this repository URL: https://github.com/ciux23/lubelogger-ha-intl
3. Search for **"LubeLogger International"** and install it.
4. **Restart Home Assistant**.

## Configuration
1. Go to **Settings** → **Devices & Services** → **Add Integration**.
2. Search for **"LubeLogger International"**.
3. Enter your connection details:
- **URL**: Your LubeLogger server (e.g., `http://192.168.1.100:8447`)
- **Username**
- **Password**

## Translations
The integration supports multiple languages. Currently available:
- **English** (built-in)
- **Italian** (`it.json`)

### Contribute a new translation:
1. In the `custom_components/lubelogger-ha-intl/translations/` folder, create a new file (e.g., `de.json` for German).
2. Follow the structure of the existing [`it.json`](custom_components/lubelogger-ha-intl/translations/it.json) file.
3. Submit a Pull Request.

## Support
For issues or feature requests, please open an [Issue on GitHub](https://github.com/ciux23/lubelogger-ha-intl/issues).

## Credits
This integration is inspired by and based on the original [LubeLogger HA](https://github.com/hollowpnt92/lubelogger-ha) integration created by [hollowpnt92](https://github.com/hollowpnt92).

The main modifications in this "International" version include:
- Adaptation for the Metric System and European number/date formats.
- Addition of Italian translations.

---

# LubeLogger International per Home Assistant

> Integrazione personalizzata per [LubeLogger](https://www.lubelogger.com/), adattata per il **Sistema Metrico** (Unità Internazionali).

## Funzionalità
- Crea un dispositivo per ogni veicolo nella tua istanza LubeLogger.
- Sensori per: odometro, prossima manutenzione, ultimo rifornimento, tasse, servizi, riparazioni, upgrade, ricambi e promemoria.
- **Supporto Unità Internazionali**: Conversione automatica per formati numerici europei (virgola come separatore decimale) e formati data (GG/MM/AAAA).

## Installazione

### Via HACS (Consigliato)
1. In HACS, vai in **Integrazioni** → **Repository personalizzati**.
2. Aggiungi questo URL del repository: https://github.com/ciux23/lubelogger-ha-intl
3. Cerca **"LubeLogger International"** e installala.
4. **Riavvia Home Assistant**.

## Configurazione
1. Vai in **Impostazioni** → **Dispositivi e Servizi** → **Aggiungi Integrazione**.
2. Cerca **"LubeLogger International"**.
3. Inserisci i dati di connessione:
- **URL**: Il tuo server LubeLogger (es. `http://192.168.1.100:8447`)
- **Nome utente**
- **Password**

## Traduzioni
L'integrazione supporta più lingue. Attualmente disponibile:
- **Inglese** (incorporata)
- **Italiano** (`it.json`)

### Contribuire con una nuova traduzione:
1. Nella cartella `custom_components/lubelogger-ha-intl/translations/`, crea un nuovo file (es. `de.json` per il tedesco).
2. Segui la struttura del file esistente [`it.json`](custom_components/lubelogger-ha-intl/translations/it.json).
3. Invia una Pull Request.

## Supporto
Per problemi o richieste di funzionalità, apri una [Issue su GitHub](https://github.com/ciux23/lubelogger-ha-intl/issues).

## Riconoscimenti
Questa integrazione è ispirata e basata sull'integrazione originale [LubeLogger HA](https://github.com/hollowpnt92/lubelogger-ha) creata da [hollowpnt92](https://github.com/hollowpnt92).

Le principali modifiche in questa versione "International" includono:
- Adattamento per il Sistema Metrico e formati numerici/data europei.
- Aggiunta delle traduzioni italiane.
