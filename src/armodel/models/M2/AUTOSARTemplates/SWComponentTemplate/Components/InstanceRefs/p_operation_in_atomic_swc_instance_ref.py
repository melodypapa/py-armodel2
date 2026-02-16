"""POperationInAtomicSwcInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.operation_in_atomic_swc_instance_ref import (
    OperationInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class POperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    """AUTOSAR POperationInAtomicSwcInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context_p_port_prototype", None, False, False, AbstractProvidedPortPrototype),  # contextPPortPrototype
        ("target_provided_operation", None, False, False, ClientServerOperation),  # targetProvidedOperation
    ]

    def __init__(self) -> None:
        """Initialize POperationInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_p_port_prototype: Optional[AbstractProvidedPortPrototype] = None
        self.target_provided_operation: Optional[ClientServerOperation] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert POperationInAtomicSwcInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "POperationInAtomicSwcInstanceRef":
        """Create POperationInAtomicSwcInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            POperationInAtomicSwcInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to POperationInAtomicSwcInstanceRef since parent returns ARObject
        return cast("POperationInAtomicSwcInstanceRef", obj)


class POperationInAtomicSwcInstanceRefBuilder:
    """Builder for POperationInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: POperationInAtomicSwcInstanceRef = POperationInAtomicSwcInstanceRef()

    def build(self) -> POperationInAtomicSwcInstanceRef:
        """Build and return POperationInAtomicSwcInstanceRef object.

        Returns:
            POperationInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
