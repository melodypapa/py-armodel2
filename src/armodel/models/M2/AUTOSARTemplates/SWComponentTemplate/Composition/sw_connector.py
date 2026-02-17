"""SwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 307)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 80)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2061)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)


class SwConnector(Identifiable):
    """AUTOSAR SwConnector."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "mapping": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PortInterfaceMapping,
        ),  # mapping
    }

    def __init__(self) -> None:
        """Initialize SwConnector."""
        super().__init__()
        self.mapping: Optional[PortInterfaceMapping] = None


class SwConnectorBuilder:
    """Builder for SwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwConnector = SwConnector()

    def build(self) -> SwConnector:
        """Build and return SwConnector object.

        Returns:
            SwConnector instance
        """
        # TODO: Add validation
        return self._obj
