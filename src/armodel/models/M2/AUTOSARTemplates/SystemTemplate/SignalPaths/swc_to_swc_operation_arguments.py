"""SwcToSwcOperationArguments AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class SwcToSwcOperationArguments(ARObject):
    """AUTOSAR SwcToSwcOperationArguments."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    direction: Optional[Any]
    operations: list[ClientServerOperation]
    def __init__(self) -> None:
        """Initialize SwcToSwcOperationArguments."""
        super().__init__()
        self.direction: Optional[Any] = None
        self.operations: list[ClientServerOperation] = []
    def serialize(self) -> ET.Element:
        """Serialize SwcToSwcOperationArguments to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize direction
        if self.direction is not None:
            serialized = ARObject._serialize_item(self.direction, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize operations (list to container "OPERATIONS")
        if self.operations:
            wrapper = ET.Element("OPERATIONS")
            for item in self.operations:
                serialized = ARObject._serialize_item(item, "ClientServerOperation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToSwcOperationArguments":
        """Deserialize XML element to SwcToSwcOperationArguments object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcToSwcOperationArguments object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse direction
        child = ARObject._find_child_element(element, "DIRECTION")
        if child is not None:
            direction_value = child.text
            obj.direction = direction_value

        # Parse operations (list from container "OPERATIONS")
        obj.operations = []
        container = ARObject._find_child_element(element, "OPERATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.operations.append(child_value)

        return obj



class SwcToSwcOperationArgumentsBuilder:
    """Builder for SwcToSwcOperationArguments."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToSwcOperationArguments = SwcToSwcOperationArguments()

    def build(self) -> SwcToSwcOperationArguments:
        """Build and return SwcToSwcOperationArguments object.

        Returns:
            SwcToSwcOperationArguments instance
        """
        # TODO: Add validation
        return self._obj
