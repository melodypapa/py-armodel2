"""DdsHistory AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 537)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsHistoryKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsHistory(ARObject):
    """AUTOSAR DdsHistory."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    history_kind: Optional[DdsHistoryKindEnum]
    history_order: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DdsHistory."""
        super().__init__()
        self.history_kind: Optional[DdsHistoryKindEnum] = None
        self.history_order: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsHistory":
        """Deserialize XML element to DdsHistory object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsHistory object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse history_kind
        child = ARObject._find_child_element(element, "HISTORY-KIND")
        if child is not None:
            history_kind_value = DdsHistoryKindEnum.deserialize(child)
            obj.history_kind = history_kind_value

        # Parse history_order
        child = ARObject._find_child_element(element, "HISTORY-ORDER")
        if child is not None:
            history_order_value = child.text
            obj.history_order = history_order_value

        return obj



class DdsHistoryBuilder:
    """Builder for DdsHistory."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsHistory = DdsHistory()

    def build(self) -> DdsHistory:
        """Build and return DdsHistory object.

        Returns:
            DdsHistory instance
        """
        # TODO: Add validation
        return self._obj
