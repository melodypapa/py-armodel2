"""DataInterface AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class DataInterface(PortInterface):
    """AUTOSAR DataInterface."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize DataInterface."""
        super().__init__()


class DataInterfaceBuilder:
    """Builder for DataInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataInterface = DataInterface()

    def build(self) -> DataInterface:
        """Build and return DataInterface object.

        Returns:
            DataInterface instance
        """
        # TODO: Add validation
        return self._obj
