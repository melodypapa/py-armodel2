"""InnerPortGroupInCompositionInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)


class InnerPortGroupInCompositionInstanceRef(ARObject):
    """AUTOSAR InnerPortGroupInCompositionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, CompositionSwComponentType),  # base
        ("contexts", None, False, True, any (SwComponent)),  # contexts
        ("target", None, False, False, PortGroup),  # target
    ]

    def __init__(self) -> None:
        """Initialize InnerPortGroupInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.contexts: list[Any] = []
        self.target: Optional[PortGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InnerPortGroupInCompositionInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InnerPortGroupInCompositionInstanceRef":
        """Create InnerPortGroupInCompositionInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InnerPortGroupInCompositionInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InnerPortGroupInCompositionInstanceRef since parent returns ARObject
        return cast("InnerPortGroupInCompositionInstanceRef", obj)


class InnerPortGroupInCompositionInstanceRefBuilder:
    """Builder for InnerPortGroupInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InnerPortGroupInCompositionInstanceRef = InnerPortGroupInCompositionInstanceRef()

    def build(self) -> InnerPortGroupInCompositionInstanceRef:
        """Build and return InnerPortGroupInCompositionInstanceRef object.

        Returns:
            InnerPortGroupInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
