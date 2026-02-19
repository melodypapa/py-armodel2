"""BswAsynchronousServerCallResultPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 80)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BswAsynchronousServerCallResultPoint(BswModuleCallPoint):
    """AUTOSAR BswAsynchronousServerCallResultPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    asynchronous: Optional[Any]
    def __init__(self) -> None:
        """Initialize BswAsynchronousServerCallResultPoint."""
        super().__init__()
        self.asynchronous: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize BswAsynchronousServerCallResultPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswAsynchronousServerCallResultPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize asynchronous
        if self.asynchronous is not None:
            serialized = ARObject._serialize_item(self.asynchronous, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASYNCHRONOUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswAsynchronousServerCallResultPoint":
        """Deserialize XML element to BswAsynchronousServerCallResultPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswAsynchronousServerCallResultPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswAsynchronousServerCallResultPoint, cls).deserialize(element)

        # Parse asynchronous
        child = ARObject._find_child_element(element, "ASYNCHRONOUS")
        if child is not None:
            asynchronous_value = child.text
            obj.asynchronous = asynchronous_value

        return obj



class BswAsynchronousServerCallResultPointBuilder:
    """Builder for BswAsynchronousServerCallResultPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswAsynchronousServerCallResultPoint = BswAsynchronousServerCallResultPoint()

    def build(self) -> BswAsynchronousServerCallResultPoint:
        """Build and return BswAsynchronousServerCallResultPoint object.

        Returns:
            BswAsynchronousServerCallResultPoint instance
        """
        # TODO: Add validation
        return self._obj
