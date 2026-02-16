"""RPortInCompositionInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import (
    PortInCompositionTypeInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)


class RPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """AUTOSAR RPortInCompositionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context", None, False, False, any (SwComponent)),  # context
        ("target_r_port_prototype", None, False, False, AbstractRequiredPortPrototype),  # targetRPortPrototype
    ]

    def __init__(self) -> None:
        """Initialize RPortInCompositionInstanceRef."""
        super().__init__()
        self.context: Optional[Any] = None
        self.target_r_port_prototype: Optional[AbstractRequiredPortPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RPortInCompositionInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RPortInCompositionInstanceRef":
        """Create RPortInCompositionInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RPortInCompositionInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RPortInCompositionInstanceRef since parent returns ARObject
        return cast("RPortInCompositionInstanceRef", obj)


class RPortInCompositionInstanceRefBuilder:
    """Builder for RPortInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RPortInCompositionInstanceRef = RPortInCompositionInstanceRef()

    def build(self) -> RPortInCompositionInstanceRef:
        """Build and return RPortInCompositionInstanceRef object.

        Returns:
            RPortInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
