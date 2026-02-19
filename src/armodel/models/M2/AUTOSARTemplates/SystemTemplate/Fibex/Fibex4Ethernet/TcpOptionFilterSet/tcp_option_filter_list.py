"""TcpOptionFilterList AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_TcpOptionFilterSet.classes.json"""

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


class TcpOptionFilterList(Identifiable):
    """AUTOSAR TcpOptionFilterList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allowed_tcp_options: list[PositiveInteger]
    def __init__(self) -> None:
        """Initialize TcpOptionFilterList."""
        super().__init__()
        self.allowed_tcp_options: list[PositiveInteger] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpOptionFilterList":
        """Deserialize XML element to TcpOptionFilterList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TcpOptionFilterList object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse allowed_tcp_options (list)
        obj.allowed_tcp_options = []
        for child in ARObject._find_all_child_elements(element, "ALLOWED-TCP-OPTIONS"):
            allowed_tcp_options_value = child.text
            obj.allowed_tcp_options.append(allowed_tcp_options_value)

        return obj



class TcpOptionFilterListBuilder:
    """Builder for TcpOptionFilterList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpOptionFilterList = TcpOptionFilterList()

    def build(self) -> TcpOptionFilterList:
        """Build and return TcpOptionFilterList object.

        Returns:
            TcpOptionFilterList instance
        """
        # TODO: Add validation
        return self._obj
