"""AsynchronousServerCallResultPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 304)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 581)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServerCall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class AsynchronousServerCallResultPoint(AbstractAccessPoint):
    """AUTOSAR AsynchronousServerCallResultPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    asynchronous_server_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize AsynchronousServerCallResultPoint."""
        super().__init__()
        self.asynchronous_server_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize AsynchronousServerCallResultPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AsynchronousServerCallResultPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize asynchronous_server_ref
        if self.asynchronous_server_ref is not None:
            serialized = ARObject._serialize_item(self.asynchronous_server_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASYNCHRONOUS-SERVER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AsynchronousServerCallResultPoint":
        """Deserialize XML element to AsynchronousServerCallResultPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AsynchronousServerCallResultPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AsynchronousServerCallResultPoint, cls).deserialize(element)

        # Parse asynchronous_server_ref
        child = ARObject._find_child_element(element, "ASYNCHRONOUS-SERVER-REF")
        if child is not None:
            asynchronous_server_ref_value = ARRef.deserialize(child)
            obj.asynchronous_server_ref = asynchronous_server_ref_value

        return obj



class AsynchronousServerCallResultPointBuilder:
    """Builder for AsynchronousServerCallResultPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AsynchronousServerCallResultPoint = AsynchronousServerCallResultPoint()

    def build(self) -> AsynchronousServerCallResultPoint:
        """Build and return AsynchronousServerCallResultPoint object.

        Returns:
            AsynchronousServerCallResultPoint instance
        """
        # TODO: Add validation
        return self._obj
