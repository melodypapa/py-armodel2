"""J1939NmCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 691)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class J1939NmCluster(NmCluster):
    """AUTOSAR J1939NmCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    address_claim: Optional[Boolean]
    uses_dynamic: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize J1939NmCluster."""
        super().__init__()
        self.address_claim: Optional[Boolean] = None
        self.uses_dynamic: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize J1939NmCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939NmCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize address_claim
        if self.address_claim is not None:
            serialized = ARObject._serialize_item(self.address_claim, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ADDRESS-CLAIM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize uses_dynamic
        if self.uses_dynamic is not None:
            serialized = ARObject._serialize_item(self.uses_dynamic, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USES-DYNAMIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939NmCluster":
        """Deserialize XML element to J1939NmCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939NmCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939NmCluster, cls).deserialize(element)

        # Parse address_claim
        child = ARObject._find_child_element(element, "ADDRESS-CLAIM")
        if child is not None:
            address_claim_value = child.text
            obj.address_claim = address_claim_value

        # Parse uses_dynamic
        child = ARObject._find_child_element(element, "USES-DYNAMIC")
        if child is not None:
            uses_dynamic_value = child.text
            obj.uses_dynamic = uses_dynamic_value

        return obj



class J1939NmClusterBuilder:
    """Builder for J1939NmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939NmCluster = J1939NmCluster()

    def build(self) -> J1939NmCluster:
        """Build and return J1939NmCluster object.

        Returns:
            J1939NmCluster instance
        """
        # TODO: Add validation
        return self._obj
