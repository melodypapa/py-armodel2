"""DdsTransportPriority AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 535)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsTransportPriority(ARObject):
    """AUTOSAR DdsTransportPriority."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    transport_priority: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DdsTransportPriority."""
        super().__init__()
        self.transport_priority: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsTransportPriority":
        """Deserialize XML element to DdsTransportPriority object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsTransportPriority object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse transport_priority
        child = ARObject._find_child_element(element, "TRANSPORT-PRIORITY")
        if child is not None:
            transport_priority_value = child.text
            obj.transport_priority = transport_priority_value

        return obj



class DdsTransportPriorityBuilder:
    """Builder for DdsTransportPriority."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsTransportPriority = DdsTransportPriority()

    def build(self) -> DdsTransportPriority:
        """Build and return DdsTransportPriority object.

        Returns:
            DdsTransportPriority instance
        """
        # TODO: Add validation
        return self._obj
