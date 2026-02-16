"""DiagnosticJ1939SwMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)


class DiagnosticJ1939SwMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticJ1939SwMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("node", None, False, False, DiagnosticJ1939Node),  # node
        ("sw_component_prototype_composition_instance_ref", None, False, False, SwComponentPrototype),  # swComponentPrototypeCompositionInstanceRef
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticJ1939SwMapping."""
        super().__init__()
        self.node: Optional[DiagnosticJ1939Node] = None
        self.sw_component_prototype_composition_instance_ref: Optional[SwComponentPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticJ1939SwMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939SwMapping":
        """Create DiagnosticJ1939SwMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticJ1939SwMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticJ1939SwMapping since parent returns ARObject
        return cast("DiagnosticJ1939SwMapping", obj)


class DiagnosticJ1939SwMappingBuilder:
    """Builder for DiagnosticJ1939SwMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939SwMapping = DiagnosticJ1939SwMapping()

    def build(self) -> DiagnosticJ1939SwMapping:
        """Build and return DiagnosticJ1939SwMapping object.

        Returns:
            DiagnosticJ1939SwMapping instance
        """
        # TODO: Add validation
        return self._obj
