"""AsynchronousServerCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 581)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServerCall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.server_call_point import (
    ServerCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class AsynchronousServerCallPoint(ServerCallPoint):
    """AUTOSAR AsynchronousServerCallPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize AsynchronousServerCallPoint."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize AsynchronousServerCallPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AsynchronousServerCallPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AsynchronousServerCallPoint":
        """Deserialize XML element to AsynchronousServerCallPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AsynchronousServerCallPoint object
        """
        # Delegate to parent class to handle inherited attributes
        return super(AsynchronousServerCallPoint, cls).deserialize(element)



class AsynchronousServerCallPointBuilder:
    """Builder for AsynchronousServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AsynchronousServerCallPoint = AsynchronousServerCallPoint()

    def build(self) -> AsynchronousServerCallPoint:
        """Build and return AsynchronousServerCallPoint object.

        Returns:
            AsynchronousServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj
