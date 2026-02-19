"""SwitchStreamGateEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 142)

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


class SwitchStreamGateEntry(Identifiable):
    """AUTOSAR SwitchStreamGateEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    internal_priority: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SwitchStreamGateEntry."""
        super().__init__()
        self.internal_priority: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamGateEntry":
        """Deserialize XML element to SwitchStreamGateEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwitchStreamGateEntry object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse internal_priority
        child = ARObject._find_child_element(element, "INTERNAL-PRIORITY")
        if child is not None:
            internal_priority_value = child.text
            obj.internal_priority = internal_priority_value

        return obj



class SwitchStreamGateEntryBuilder:
    """Builder for SwitchStreamGateEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchStreamGateEntry = SwitchStreamGateEntry()

    def build(self) -> SwitchStreamGateEntry:
        """Build and return SwitchStreamGateEntry object.

        Returns:
            SwitchStreamGateEntry instance
        """
        # TODO: Add validation
        return self._obj
