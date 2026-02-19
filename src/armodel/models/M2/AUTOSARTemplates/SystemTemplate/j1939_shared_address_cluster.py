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

    participatings: list[J1939Cluster]
    def __init__(self) -> None:
        """Initialize J1939SharedAddressCluster."""
        super().__init__()
        self.participatings: list[J1939Cluster] = []

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

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize participatings (list to container "PARTICIPATINGS")
        if self.participatings:
            wrapper = ET.Element("PARTICIPATINGS")
            for item in self.participatings:
                serialized = ARObject._serialize_item(item, "J1939Cluster")
                if serialized is not None:
                    wrapper.append(serialized)
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

        # Parse participatings (list from container "PARTICIPATINGS")
        obj.participatings = []
        container = ARObject._find_child_element(element, "PARTICIPATINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.participatings.append(child_value)

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
