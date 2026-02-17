"""PortInterfaceMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 119)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)


class PortInterfaceMappingSet(ARElement):
    """AUTOSAR PortInterfaceMappingSet."""

    port_interfaces: list[PortInterfaceMapping]
    def __init__(self) -> None:
        """Initialize PortInterfaceMappingSet."""
        super().__init__()
        self.port_interfaces: list[PortInterfaceMapping] = []


class PortInterfaceMappingSetBuilder:
    """Builder for PortInterfaceMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortInterfaceMappingSet = PortInterfaceMappingSet()

    def build(self) -> PortInterfaceMappingSet:
        """Build and return PortInterfaceMappingSet object.

        Returns:
            PortInterfaceMappingSet instance
        """
        # TODO: Add validation
        return self._obj
