"""PortInCompositionTypeInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class PortInCompositionTypeInstanceRef(ARObject):
    """AUTOSAR PortInCompositionTypeInstanceRef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("abstract_context", None, False, False, any (SwComponent)),  # abstractContext
        ("base", None, False, False, CompositionSwComponentType),  # base
        ("target_port", None, False, False, PortPrototype),  # targetPort
    ]

    def __init__(self) -> None:
        """Initialize PortInCompositionTypeInstanceRef."""
        super().__init__()
        self.abstract_context: Optional[Any] = None
        self.base: Optional[CompositionSwComponentType] = None
        self.target_port: Optional[PortPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PortInCompositionTypeInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortInCompositionTypeInstanceRef":
        """Create PortInCompositionTypeInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PortInCompositionTypeInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PortInCompositionTypeInstanceRef since parent returns ARObject
        return cast("PortInCompositionTypeInstanceRef", obj)


class PortInCompositionTypeInstanceRefBuilder:
    """Builder for PortInCompositionTypeInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortInCompositionTypeInstanceRef = PortInCompositionTypeInstanceRef()

    def build(self) -> PortInCompositionTypeInstanceRef:
        """Build and return PortInCompositionTypeInstanceRef object.

        Returns:
            PortInCompositionTypeInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
