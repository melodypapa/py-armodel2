"""Schema configuration for AUTOSAR versions."""

import yaml
from pathlib import Path
from typing import Optional, Dict, Any


def load_schema_config(config_path: Optional[Path] = None) -> Dict[str, Any]:
    """Load schema configuration from YAML file.
    
    Args:
        config_path: Path to config.yaml, defaults to package config
        
    Returns:
        Configuration dictionary
    """
    if config_path is None:
        # Default to package config file
        config_path = Path(__file__).parent / "config.yaml"
    
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


__all__ = ["load_schema_config"]
