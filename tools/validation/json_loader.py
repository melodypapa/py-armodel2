"""JSON class loader for loading AUTOSAR class definitions from JSON files."""

import json
from pathlib import Path
from typing import Dict

from tools.validation.models import JSONClass, JSONMember


class JSONClassLoader:
    """Loader for JSON class definitions."""

    def __init__(self, packages_dir: str):
        """Initialize JSON class loader.

        Args:
            packages_dir: Directory containing package JSON files
        """
        self.packages_dir = Path(packages_dir)
        self.classes: Dict[str, JSONClass] = {}

    def load_all(self) -> Dict[str, JSONClass]:
        """Load all classes from JSON files.

        Returns:
            Dictionary mapping class names to JSONClass objects
        """
        if not self.packages_dir.exists():
            raise FileNotFoundError(f"JSON packages directory not found: {self.packages_dir}")

        # Load all .classes.json files
        for class_file in self.packages_dir.rglob("*.classes.json"):
            try:
                with open(class_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self._parse_package_data(data)
            except Exception as e:
                print(f"Warning: Failed to load {class_file}: {e}")

        return self.classes

    def _parse_package_data(self, data: dict) -> None:
        """Parse package JSON data.

        Args:
            data: Package JSON data
        """
        classes_data = data.get("classes", [])

        for class_data in classes_data:
            class_name = class_data.get("name", "")
            if not class_name:
                continue

            # Parse attributes
            attributes_data = class_data.get("attributes", {})
            attributes: Dict[str, JSONMember] = {}

            for attr_name, attr_data in attributes_data.items():
                if isinstance(attr_data, dict):
                    member = JSONMember(
                        type=attr_data.get("type", ""),
                        multiplicity=attr_data.get("multiplicity", "1"),
                        kind=attr_data.get("kind", "attribute"),
                        is_ref=attr_data.get("is_ref", False),
                        note=attr_data.get("note"),
                    )
                    attributes[attr_name] = member

            # Create JSON class
            json_class = JSONClass(
                name=class_name,
                package=class_data.get("package", ""),
                is_abstract=class_data.get("is_abstract", False),
                atp_type=class_data.get("atp_type"),
                parent=class_data.get("parent"),
                bases=class_data.get("bases", []),
                children=class_data.get("children", []),
                subclasses=class_data.get("subclasses", []),
                attributes=attributes,
            )

            self.classes[class_name] = json_class

    def load_skip_list(self, skip_list_file: str) -> set[str]:
        """Load skip_classes.yaml file.

        Args:
            skip_list_file: Path to skip_classes.yaml file

        Returns:
            Set of class names to skip
        """
        skip_classes: set[str] = set()

        try:
            import yaml
        except ImportError:
            return skip_classes

        skip_path = Path(skip_list_file)
        if not skip_path.exists():
            return skip_classes

        try:
            with open(skip_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                if data:
                    skip_classes = set(data.get("skip_classes", []))
        except Exception as e:
            print(f"Warning: Failed to load skip list: {e}")

        return skip_classes