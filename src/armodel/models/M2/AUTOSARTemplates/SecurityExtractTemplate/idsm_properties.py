"""IdsmProperties AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_rate_limitation import (
    IdsmRateLimitation,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_traffic_limitation import (
    IdsmTrafficLimitation,
)


class IdsmProperties(IdsCommonElement):
    """AUTOSAR IdsmProperties."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rate_limitations: list[IdsmRateLimitation]
    traffic_limitations: list[IdsmTrafficLimitation]
    def __init__(self) -> None:
        """Initialize IdsmProperties."""
        super().__init__()
        self.rate_limitations: list[IdsmRateLimitation] = []
        self.traffic_limitations: list[IdsmTrafficLimitation] = []

    def serialize(self) -> ET.Element:
        """Serialize IdsmProperties to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IdsmProperties, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize rate_limitations (list to container "RATE-LIMITATIONS")
        if self.rate_limitations:
            wrapper = ET.Element("RATE-LIMITATIONS")
            for item in self.rate_limitations:
                serialized = ARObject._serialize_item(item, "IdsmRateLimitation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize traffic_limitations (list to container "TRAFFIC-LIMITATIONS")
        if self.traffic_limitations:
            wrapper = ET.Element("TRAFFIC-LIMITATIONS")
            for item in self.traffic_limitations:
                serialized = ARObject._serialize_item(item, "IdsmTrafficLimitation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmProperties":
        """Deserialize XML element to IdsmProperties object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsmProperties object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IdsmProperties, cls).deserialize(element)

        # Parse rate_limitations (list from container "RATE-LIMITATIONS")
        obj.rate_limitations = []
        container = ARObject._find_child_element(element, "RATE-LIMITATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rate_limitations.append(child_value)

        # Parse traffic_limitations (list from container "TRAFFIC-LIMITATIONS")
        obj.traffic_limitations = []
        container = ARObject._find_child_element(element, "TRAFFIC-LIMITATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.traffic_limitations.append(child_value)

        return obj



class IdsmPropertiesBuilder:
    """Builder for IdsmProperties."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmProperties = IdsmProperties()

    def build(self) -> IdsmProperties:
        """Build and return IdsmProperties object.

        Returns:
            IdsmProperties instance
        """
        # TODO: Add validation
        return self._obj
