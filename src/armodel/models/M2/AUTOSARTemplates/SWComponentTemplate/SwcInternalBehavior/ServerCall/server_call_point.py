"""ServerCallPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ServerCallPoint(AbstractAccessPoint):
    """AUTOSAR ServerCallPoint."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("operation_instance_ref", None, False, False, ClientServerOperation),  # operationInstanceRef
        ("timeout", None, True, False, None),  # timeout
    ]

    def __init__(self) -> None:
        """Initialize ServerCallPoint."""
        super().__init__()
        self.operation_instance_ref: Optional[ClientServerOperation] = None
        self.timeout: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ServerCallPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServerCallPoint":
        """Create ServerCallPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ServerCallPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ServerCallPoint since parent returns ARObject
        return cast("ServerCallPoint", obj)


class ServerCallPointBuilder:
    """Builder for ServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServerCallPoint = ServerCallPoint()

    def build(self) -> ServerCallPoint:
        """Build and return ServerCallPoint object.

        Returns:
            ServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj
