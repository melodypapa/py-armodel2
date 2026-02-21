"""J1939SharedAddressCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 694)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.j1939_cluster import (
    J1939Cluster,
)


class J1939SharedAddressCluster(Identifiable):
    """AUTOSAR J1939SharedAddressCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    participating_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize J1939SharedAddressCluster."""
        super().__init__()
        self.participating_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize J1939SharedAddressCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939SharedAddressCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize participating_refs (list to container "PARTICIPATING-REFS")
        if self.participating_refs:
            wrapper = ET.Element("PARTICIPATING-REFS")
            for item in self.participating_refs:
                serialized = ARObject._serialize_item(item, "J1939Cluster")
                if serialized is not None:
                    child_elem = ET.Element("PARTICIPATING-REF")
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
    def deserialize(cls, element: ET.Element) -> "J1939SharedAddressCluster":
        """Deserialize XML element to J1939SharedAddressCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939SharedAddressCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939SharedAddressCluster, cls).deserialize(element)

        # Parse participating_refs (list from container "PARTICIPATING-REFS")
        obj.participating_refs = []
        container = ARObject._find_child_element(element, "PARTICIPATING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.participating_refs.append(child_value)

        return obj



class J1939SharedAddressClusterBuilder:
    """Builder for J1939SharedAddressCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939SharedAddressCluster = J1939SharedAddressCluster()

    def build(self) -> J1939SharedAddressCluster:
        """Build and return J1939SharedAddressCluster object.

        Returns:
            J1939SharedAddressCluster instance
        """
        # TODO: Add validation
        return self._obj
