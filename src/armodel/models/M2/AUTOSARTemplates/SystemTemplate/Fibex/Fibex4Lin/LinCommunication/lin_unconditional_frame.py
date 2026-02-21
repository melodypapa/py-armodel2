"""LinUnconditionalFrame AUTOSAR element.

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
from armodel.serialization import SerializationHelper


class LinUnconditionalFrame(LinFrame):
    """AUTOSAR LinUnconditionalFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize LinUnconditionalFrame."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize LinUnconditionalFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinUnconditionalFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinUnconditionalFrame":
        """Deserialize XML element to LinUnconditionalFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinUnconditionalFrame object
        """
        # Delegate to parent class to handle inherited attributes
        return super(LinUnconditionalFrame, cls).deserialize(element)



class LinUnconditionalFrameBuilder:
    """Builder for LinUnconditionalFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinUnconditionalFrame = LinUnconditionalFrame()

    def build(self) -> LinUnconditionalFrame:
        """Build and return LinUnconditionalFrame object.

        Returns:
            LinUnconditionalFrame instance
        """
        # TODO: Add validation
        return self._obj
