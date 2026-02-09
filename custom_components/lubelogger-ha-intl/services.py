"""Services for LubeLogger HA Intl."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import config_validation as cv

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

SERVICE_ADD_SERVICE_RECORD = "add_service_record"
SERVICE_ADD_ODOMETER_RECORD = "add_odometer_record"

SCHEMA_SERVICE_ADD_SERVICE_RECORD = vol.Schema(
    {
        vol.Required("vehicle_id"): cv.string,
        vol.Required("date"): cv.string,  # formato YYYY-MM-DD
        vol.Required("description"): cv.string,
        vol.Optional("odometer"): vol.Coerce(float),
        vol.Optional("cost"): vol.Coerce(float, default=0.0),
        vol.Optional("notes"): cv.string,
        vol.Optional("custom_fields"): dict,
    }
)

SCHEMA_SERVICE_ADD_ODOMETER_RECORD = vol.Schema(
    {
        vol.Required("vehicle_id"): cv.string,
        vol.Required("mileage"): vol.Coerce(float),
        vol.Optional("date"): cv.string,  # formato YYYY-MM-DD, opzionale
        vol.Optional("notes"): cv.string,
    }
)


async def async_register_services(hass: HomeAssistant) -> None:
    """Registra i servizi personalizzati per l'integrazione."""

    async def async_call_add_service_record(call: ServiceCall) -> None:
        """Aggiunge un nuovo record di manutenzione (service record)."""
        # Prendiamo il primo (e unico) coordinator configurato
        if not hass.data.get(DOMAIN):
            raise HomeAssistantError("Nessuna configurazione LubeLogger trovata")
        
        entry_id = next(iter(hass.data[DOMAIN]))
        coordinator = hass.data[DOMAIN][entry_id]
        client = coordinator.client

        try:
            result = await client.async_add_service_record(
                vehicle_id=call.data["vehicle_id"],
                date=call.data["date"],
                description=call.data["description"],
                odometer=call.data.get("odometer"),
                cost=call.data.get("cost", 0.0),
                notes=call.data.get("notes", ""),
                custom_fields=call.data.get("custom_fields", {}),
            )
            _LOGGER.info("Service record aggiunto con successo: %s", result)
            # Forza refresh dei dati per aggiornare i sensori
            await coordinator.async_refresh()
        except Exception as err:
            _LOGGER.error("Errore durante l'aggiunta del service record: %s", err)
            raise HomeAssistantError(f"Impossibile aggiungere service record: {err}")

    async def async_call_add_odometer_record(call: ServiceCall) -> None:
        """Aggiunge un nuovo record odometro (aggiorna i km)."""
        if not hass.data.get(DOMAIN):
            raise HomeAssistantError("Nessuna configurazione LubeLogger trovata")
        
        entry_id = next(iter(hass.data[DOMAIN]))
        coordinator = hass.data[DOMAIN][entry_id]
        client = coordinator.client

        try:
            result = await client.async_add_odometer_record(
                vehicle_id=call.data["vehicle_id"],
                mileage=call.data["mileage"],
                date=call.data.get("date"),
                notes=call.data.get("notes", ""),
            )
            _LOGGER.info("Odometer record aggiunto con successo: %s", result)
            await coordinator.async_refresh()
        except Exception as err:
            _LOGGER.error("Errore durante l'aggiunta del record odometro: %s", err)
            raise HomeAssistantError(f"Impossibile aggiungere record odometro: {err}")

    # Registrazione effettiva dei servizi
    hass.services.async_register(
        DOMAIN,
        SERVICE_ADD_SERVICE_RECORD,
        async_call_add_service_record,
        schema=SCHEMA_SERVICE_ADD_SERVICE_RECORD,
    )

    hass.services.async_register(
        DOMAIN,
        SERVICE_ADD_ODOMETER_RECORD,
        async_call_add_odometer_record,
        schema=SCHEMA_SERVICE_ADD_ODOMETER_RECORD,
    )

    _LOGGER.info("Servizi LubeLogger registrati: add_service_record e add_odometer_record")
