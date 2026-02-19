"""IPv6ExtHeaderFilterList AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_IPv6HeaderFilterList.classes.json"""

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


class IPv6ExtHeaderFilterList(Identifiable):
    """AUTOSAR IPv6ExtHeaderFilterList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allowed_i_pv6_exts: list[PositiveInteger]
    def __init__(self) -> None:
        """Initialize IPv6ExtHeaderFilterList."""
        super().__init__()
        self.allowed_i_pv6_exts: list[PositiveInteger] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPv6ExtHeaderFilterList":
        """Deserialize XML element to IPv6ExtHeaderFilterList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPv6ExtHeaderFilterList object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse allowed_i_pv6_exts (list)
        obj.allowed_i_pv6_exts = []
        for child in ARObject._find_all_child_elements(element, "ALLOWED-I-PV6-EXTS"):
            allowed_i_pv6_exts_value = child.text
            obj.allowed_i_pv6_exts.append(allowed_i_pv6_exts_value)

        return obj



class IPv6ExtHeaderFilterListBuilder:
    """Builder for IPv6ExtHeaderFilterList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPv6ExtHeaderFilterList = IPv6ExtHeaderFilterList()

    def build(self) -> IPv6ExtHeaderFilterList:
        """Build and return IPv6ExtHeaderFilterList object.

        Returns:
            IPv6ExtHeaderFilterList instance
        """
        # TODO: Add validation
        return self._obj
