"""EthernetPriorityRegeneration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 128)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class EthernetPriorityRegeneration(Referrable):
    """AUTOSAR EthernetPriorityRegeneration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ingress_priority: Optional[PositiveInteger]
    regenerated: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize EthernetPriorityRegeneration."""
        super().__init__()
        self.ingress_priority: Optional[PositiveInteger] = None
        self.regenerated: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetPriorityRegeneration":
        """Deserialize XML element to EthernetPriorityRegeneration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetPriorityRegeneration object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ingress_priority
        child = ARObject._find_child_element(element, "INGRESS-PRIORITY")
        if child is not None:
            ingress_priority_value = child.text
            obj.ingress_priority = ingress_priority_value

        # Parse regenerated
        child = ARObject._find_child_element(element, "REGENERATED")
        if child is not None:
            regenerated_value = child.text
            obj.regenerated = regenerated_value

        return obj



class EthernetPriorityRegenerationBuilder:
    """Builder for EthernetPriorityRegeneration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetPriorityRegeneration = EthernetPriorityRegeneration()

    def build(self) -> EthernetPriorityRegeneration:
        """Build and return EthernetPriorityRegeneration object.

        Returns:
            EthernetPriorityRegeneration instance
        """
        # TODO: Add validation
        return self._obj
