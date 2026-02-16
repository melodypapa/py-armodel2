"""TcpOptionFilterSet AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet.tcp_option_filter_list import (
    TcpOptionFilterList,
)


class TcpOptionFilterSet(ARElement):
    """AUTOSAR TcpOptionFilterSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tcp_option_filter_lists": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TcpOptionFilterList,
        ),  # tcpOptionFilterLists
    }

    def __init__(self) -> None:
        """Initialize TcpOptionFilterSet."""
        super().__init__()
        self.tcp_option_filter_lists: list[TcpOptionFilterList] = []


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
