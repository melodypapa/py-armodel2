"""IPv6ExtHeaderFilterSet AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList.i_pv6_ext_header_filter_list import (
    IPv6ExtHeaderFilterList,
)


class IPv6ExtHeaderFilterSet(ARElement):
    """AUTOSAR IPv6ExtHeaderFilterSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ext_header_filters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=IPv6ExtHeaderFilterList,
        ),  # extHeaderFilters
    }

    def __init__(self) -> None:
        """Initialize IPv6ExtHeaderFilterSet."""
        super().__init__()
        self.ext_header_filters: list[IPv6ExtHeaderFilterList] = []


class IPv6ExtHeaderFilterSetBuilder:
    """Builder for IPv6ExtHeaderFilterSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPv6ExtHeaderFilterSet = IPv6ExtHeaderFilterSet()

    def build(self) -> IPv6ExtHeaderFilterSet:
        """Build and return IPv6ExtHeaderFilterSet object.

        Returns:
            IPv6ExtHeaderFilterSet instance
        """
        # TODO: Add validation
        return self._obj
