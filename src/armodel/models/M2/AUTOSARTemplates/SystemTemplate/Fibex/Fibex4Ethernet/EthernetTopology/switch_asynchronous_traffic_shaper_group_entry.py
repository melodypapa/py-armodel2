"""SwitchAsynchronousTrafficShaperGroupEntry AUTOSAR element.

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


class SwitchAsynchronousTrafficShaperGroupEntry(Identifiable):
    """AUTOSAR SwitchAsynchronousTrafficShaperGroupEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    maximum: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SwitchAsynchronousTrafficShaperGroupEntry."""
        super().__init__()
        self.maximum: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchAsynchronousTrafficShaperGroupEntry":
        """Deserialize XML element to SwitchAsynchronousTrafficShaperGroupEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwitchAsynchronousTrafficShaperGroupEntry object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse maximum
        child = ARObject._find_child_element(element, "MAXIMUM")
        if child is not None:
            maximum_value = child.text
            obj.maximum = maximum_value

        return obj



class SwitchAsynchronousTrafficShaperGroupEntryBuilder:
    """Builder for SwitchAsynchronousTrafficShaperGroupEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchAsynchronousTrafficShaperGroupEntry = SwitchAsynchronousTrafficShaperGroupEntry()

    def build(self) -> SwitchAsynchronousTrafficShaperGroupEntry:
        """Build and return SwitchAsynchronousTrafficShaperGroupEntry object.

        Returns:
            SwitchAsynchronousTrafficShaperGroupEntry instance
        """
        # TODO: Add validation
        return self._obj
