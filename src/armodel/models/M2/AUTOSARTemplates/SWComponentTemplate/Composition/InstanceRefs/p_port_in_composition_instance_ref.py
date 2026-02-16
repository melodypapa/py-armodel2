"""PPortInCompositionInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import (
    PortInCompositionTypeInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)


class PPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """AUTOSAR PPortInCompositionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context", None, False, False, any (SwComponent)),  # context
        ("target_p_port_prototype", None, False, False, AbstractProvidedPortPrototype),  # targetPPortPrototype
    ]

    def __init__(self) -> None:
        """Initialize PPortInCompositionInstanceRef."""
        super().__init__()
        self.context: Optional[Any] = None
        self.target_p_port_prototype: Optional[AbstractProvidedPortPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PPortInCompositionInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PPortInCompositionInstanceRef":
        """Create PPortInCompositionInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PPortInCompositionInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PPortInCompositionInstanceRef since parent returns ARObject
        return cast("PPortInCompositionInstanceRef", obj)


class PPortInCompositionInstanceRefBuilder:
    """Builder for PPortInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PPortInCompositionInstanceRef = PPortInCompositionInstanceRef()

    def build(self) -> PPortInCompositionInstanceRef:
        """Build and return PPortInCompositionInstanceRef object.

        Returns:
            PPortInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
