"""RelativeTolerance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 398)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class RelativeTolerance(ARObject):
    """AUTOSAR RelativeTolerance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    relative: Optional[Integer]
    def __init__(self) -> None:
        """Initialize RelativeTolerance."""
        super().__init__()
        self.relative: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize RelativeTolerance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RelativeTolerance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize relative
        if self.relative is not None:
            serialized = SerializationHelper.serialize_item(self.relative, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RELATIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RelativeTolerance":
        """Deserialize XML element to RelativeTolerance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RelativeTolerance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RelativeTolerance, cls).deserialize(element)

        # Parse relative
        child = SerializationHelper.find_child_element(element, "RELATIVE")
        if child is not None:
            relative_value = child.text
            obj.relative = relative_value

        return obj



class RelativeToleranceBuilder:
    """Builder for RelativeTolerance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RelativeTolerance = RelativeTolerance()

    def build(self) -> RelativeTolerance:
        """Build and return RelativeTolerance object.

        Returns:
            RelativeTolerance instance
        """
        # TODO: Add validation
        return self._obj
