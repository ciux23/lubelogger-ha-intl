"""The LubeLogger integration."""
from __future__ import annotations

import logging
import json
import os

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN
from .coordinator import LubeLoggerDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]

# Config schema for integrations that only use config entries
CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)


async def load_translations() -> dict:
    """Load translation files from the translations directory."""
    translations = {}
    current_dir = os.path.dirname(__file__)
    translations_dir = os.path.join(current_dir, "translations")
    
    if not os.path.exists(translations_dir):
        _LOGGER.debug("No translations directory found")
        return translations
    
    for filename in os.listdir(translations_dir):
        if filename.endswith('.json'):
            lang = filename.split('.')[0]
            filepath = os.path.join(translations_dir, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    translations[lang] = json.load(f)
                _LOGGER.debug("Loaded translations for language: %s", lang)
            except Exception as e:
                _LOGGER.error("Error loading translation file %s: %s", filename, e)
    
    return translations


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the LubeLogger integration."""
    _LOGGER.debug("LubeLogger integration is being set up")
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up LubeLogger from a config entry."""
    _LOGGER.info("Setting up LubeLogger integration entry: %s", entry.title)
    
    try:
        # Load translations
        translations = await load_translations()
        
        coordinator = LubeLoggerDataUpdateCoordinator(hass, entry)
        await coordinator.async_config_entry_first_refresh()

        # Store coordinator and translations
        hass.data.setdefault(DOMAIN, {})
        hass.data[DOMAIN][entry.entry_id] = {
            "coordinator": coordinator,
            "translations": translations
        }

        await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
        
        _LOGGER.info("LubeLogger integration setup completed successfully")
        return True
    except Exception as err:
        _LOGGER.exception("Error setting up LubeLogger integration: %s", err)
        return False


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    _LOGGER.info("Unloading LubeLogger integration entry: %s", entry.title)
    
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)
        _LOGGER.info("LubeLogger integration unloaded successfully")
    else:
        _LOGGER.warning("Failed to unload LubeLogger integration platforms")

    return unload_ok
