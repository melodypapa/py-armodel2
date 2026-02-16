"""OperationInSystemInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class OperationInSystemInstanceRef(ARObject):
    """AUTOSAR OperationInSystemInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, System),  # base
        ("context", None, False, False, RootSwCompositionPrototype),  # context
        ("context_port", None, False, False, PortPrototype),  # contextPort
        ("target_operation", None, False, False, ClientServerOperation),  # targetOperation
    ]

    def __init__(self) -> None:
        """Initialize OperationInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.context: Optional[RootSwCompositionPrototype] = None
        self.context_port: PortPrototype = None
        self.target_operation: Optional[ClientServerOperation] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert OperationInSystemInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "OperationInSystemInstanceRef":
        """Create OperationInSystemInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            OperationInSystemInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to OperationInSystemInstanceRef since parent returns ARObject
        return cast("OperationInSystemInstanceRef", obj)


class OperationInSystemInstanceRefBuilder:
    """Builder for OperationInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OperationInSystemInstanceRef = OperationInSystemInstanceRef()

    def build(self) -> OperationInSystemInstanceRef:
        """Build and return OperationInSystemInstanceRef object.

        Returns:
            OperationInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
