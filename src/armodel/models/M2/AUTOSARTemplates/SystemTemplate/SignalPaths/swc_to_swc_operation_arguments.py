"""SwcToSwcOperationArguments AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class SwcToSwcOperationArguments(ARObject):
    """AUTOSAR SwcToSwcOperationArguments."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("direction", None, False, False, any (SwcToSwcOperation)),  # direction
        ("operations", None, False, True, ClientServerOperation),  # operations
    ]

    def __init__(self) -> None:
        """Initialize SwcToSwcOperationArguments."""
        super().__init__()
        self.direction: Optional[Any] = None
        self.operations: list[ClientServerOperation] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcToSwcOperationArguments to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToSwcOperationArguments":
        """Create SwcToSwcOperationArguments from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcToSwcOperationArguments instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcToSwcOperationArguments since parent returns ARObject
        return cast("SwcToSwcOperationArguments", obj)


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
