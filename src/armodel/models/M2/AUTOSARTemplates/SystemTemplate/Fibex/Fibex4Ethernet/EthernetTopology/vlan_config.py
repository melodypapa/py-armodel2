"""VlanConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 106)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class VlanConfig(Identifiable):
    """AUTOSAR VlanConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    vlan_identifier: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize VlanConfig."""
        super().__init__()
        self.vlan_identifier: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "VlanConfig":
        """Deserialize XML element to VlanConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VlanConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse vlan_identifier
        child = ARObject._find_child_element(element, "VLAN-IDENTIFIER")
        if child is not None:
            vlan_identifier_value = child.text
            obj.vlan_identifier = vlan_identifier_value

        return obj



class VlanConfigBuilder:
    """Builder for VlanConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VlanConfig = VlanConfig()

    def build(self) -> VlanConfig:
        """Build and return VlanConfig object.

        Returns:
            VlanConfig instance
        """
        # TODO: Add validation
        return self._obj
