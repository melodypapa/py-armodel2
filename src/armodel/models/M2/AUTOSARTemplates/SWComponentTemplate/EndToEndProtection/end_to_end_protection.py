"""EndToEndProtection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 214)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 384)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class EndToEndProtection(Identifiable):
    """AUTOSAR EndToEndProtection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    end_to_ends: list[EndToEndProtection]
    def __init__(self) -> None:
        """Initialize EndToEndProtection."""
        super().__init__()
        self.end_to_ends: list[EndToEndProtection] = []
    def serialize(self) -> ET.Element:
        """Serialize EndToEndProtection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EndToEndProtection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize end_to_ends (list to container "END-TO-ENDS")
        if self.end_to_ends:
            wrapper = ET.Element("END-TO-ENDS")
            for item in self.end_to_ends:
                serialized = ARObject._serialize_item(item, "EndToEndProtection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndProtection":
        """Deserialize XML element to EndToEndProtection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndProtection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EndToEndProtection, cls).deserialize(element)

        # Parse end_to_ends (list from container "END-TO-ENDS")
        obj.end_to_ends = []
        container = ARObject._find_child_element(element, "END-TO-ENDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.end_to_ends.append(child_value)

        return obj



class EndToEndProtectionBuilder:
    """Builder for EndToEndProtection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndProtection = EndToEndProtection()

    def build(self) -> EndToEndProtection:
        """Build and return EndToEndProtection object.

        Returns:
            EndToEndProtection instance
        """
        # TODO: Add validation
        return self._obj
