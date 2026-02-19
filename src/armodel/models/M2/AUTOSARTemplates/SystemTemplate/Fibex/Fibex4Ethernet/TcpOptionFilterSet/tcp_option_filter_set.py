"""TcpOptionFilterSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_TcpOptionFilterSet.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet.tcp_option_filter_list import (
    TcpOptionFilterList,
)


class TcpOptionFilterSet(ARElement):
    """AUTOSAR TcpOptionFilterSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_option_filter_list_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize TcpOptionFilterSet."""
        super().__init__()
        self.tcp_option_filter_list_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpOptionFilterSet":
        """Deserialize XML element to TcpOptionFilterSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TcpOptionFilterSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TcpOptionFilterSet, cls).deserialize(element)

        # Parse tcp_option_filter_list_refs (list from container "TCP-OPTION-FILTER-LISTS")
        obj.tcp_option_filter_list_refs = []
        container = ARObject._find_child_element(element, "TCP-OPTION-FILTER-LISTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tcp_option_filter_list_refs.append(child_value)

        return obj



class TcpOptionFilterSetBuilder:
    """Builder for TcpOptionFilterSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpOptionFilterSet = TcpOptionFilterSet()

    def build(self) -> TcpOptionFilterSet:
        """Build and return TcpOptionFilterSet object.

        Returns:
            TcpOptionFilterSet instance
        """
        # TODO: Add validation
        return self._obj
