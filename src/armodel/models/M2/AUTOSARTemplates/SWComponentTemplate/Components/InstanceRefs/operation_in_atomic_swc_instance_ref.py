"""OperationInAtomicSwcInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class OperationInAtomicSwcInstanceRef(ARObject):
    """AUTOSAR OperationInAtomicSwcInstanceRef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, AtomicSwComponentType),  # base
        ("context_port", None, False, False, PortPrototype),  # contextPort
        ("target_operation", None, False, False, ClientServerOperation),  # targetOperation
    ]

    def __init__(self) -> None:
        """Initialize OperationInAtomicSwcInstanceRef."""
        super().__init__()
        self.base: Optional[AtomicSwComponentType] = None
        self.context_port: Optional[PortPrototype] = None
        self.target_operation: Optional[ClientServerOperation] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert OperationInAtomicSwcInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "OperationInAtomicSwcInstanceRef":
        """Create OperationInAtomicSwcInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            OperationInAtomicSwcInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to OperationInAtomicSwcInstanceRef since parent returns ARObject
        return cast("OperationInAtomicSwcInstanceRef", obj)


class OperationInAtomicSwcInstanceRefBuilder:
    """Builder for OperationInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OperationInAtomicSwcInstanceRef = OperationInAtomicSwcInstanceRef()

    def build(self) -> OperationInAtomicSwcInstanceRef:
        """Build and return OperationInAtomicSwcInstanceRef object.

        Returns:
            OperationInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
