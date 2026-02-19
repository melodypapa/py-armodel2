"""LinSporadicFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 429)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_unconditional_frame import (
    LinUnconditionalFrame,
)


class LinSporadicFrame(LinFrame):
    """AUTOSAR LinSporadicFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    substituteds: list[LinUnconditionalFrame]
    def __init__(self) -> None:
        """Initialize LinSporadicFrame."""
        super().__init__()
        self.substituteds: list[LinUnconditionalFrame] = []
    def serialize(self) -> ET.Element:
        """Serialize LinSporadicFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinSporadicFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize substituteds (list to container "SUBSTITUTEDS")
        if self.substituteds:
            wrapper = ET.Element("SUBSTITUTEDS")
            for item in self.substituteds:
                serialized = ARObject._serialize_item(item, "LinUnconditionalFrame")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinSporadicFrame":
        """Deserialize XML element to LinSporadicFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinSporadicFrame object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinSporadicFrame, cls).deserialize(element)

        # Parse substituteds (list from container "SUBSTITUTEDS")
        obj.substituteds = []
        container = ARObject._find_child_element(element, "SUBSTITUTEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.substituteds.append(child_value)

        return obj



class LinSporadicFrameBuilder:
    """Builder for LinSporadicFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinSporadicFrame = LinSporadicFrame()

    def build(self) -> LinSporadicFrame:
        """Build and return LinSporadicFrame object.

        Returns:
            LinSporadicFrame instance
        """
        # TODO: Add validation
        return self._obj
