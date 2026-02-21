"""IPv6ExtHeaderFilterSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_IPv6HeaderFilterList.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList.i_pv6_ext_header_filter_list import (
    IPv6ExtHeaderFilterList,
)


class IPv6ExtHeaderFilterSet(ARElement):
    """AUTOSAR IPv6ExtHeaderFilterSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ext_header_filter_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize IPv6ExtHeaderFilterSet."""
        super().__init__()
        self.ext_header_filter_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize IPv6ExtHeaderFilterSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPv6ExtHeaderFilterSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ext_header_filter_refs (list to container "EXT-HEADER-FILTER-REFS")
        if self.ext_header_filter_refs:
            wrapper = ET.Element("EXT-HEADER-FILTER-REFS")
            for item in self.ext_header_filter_refs:
                serialized = SerializationHelper.serialize_item(item, "IPv6ExtHeaderFilterList")
                if serialized is not None:
                    child_elem = ET.Element("EXT-HEADER-FILTER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPv6ExtHeaderFilterSet":
        """Deserialize XML element to IPv6ExtHeaderFilterSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPv6ExtHeaderFilterSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPv6ExtHeaderFilterSet, cls).deserialize(element)

        # Parse ext_header_filter_refs (list from container "EXT-HEADER-FILTER-REFS")
        obj.ext_header_filter_refs = []
        container = SerializationHelper.find_child_element(element, "EXT-HEADER-FILTER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ext_header_filter_refs.append(child_value)

        return obj



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
