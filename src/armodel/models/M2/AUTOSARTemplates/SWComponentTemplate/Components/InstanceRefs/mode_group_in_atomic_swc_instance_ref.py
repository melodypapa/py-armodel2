"""ModeGroupInAtomicSwcInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class ModeGroupInAtomicSwcInstanceRef(ARObject):
    """AUTOSAR ModeGroupInAtomicSwcInstanceRef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, AtomicSwComponentType),  # base
        ("context_port", None, False, False, PortPrototype),  # contextPort
        ("target", None, False, False, ModeDeclarationGroup),  # target
    ]

    def __init__(self) -> None:
        """Initialize ModeGroupInAtomicSwcInstanceRef."""
        super().__init__()
        self.base: Optional[AtomicSwComponentType] = None
        self.context_port: Optional[PortPrototype] = None
        self.target: Optional[ModeDeclarationGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeGroupInAtomicSwcInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeGroupInAtomicSwcInstanceRef":
        """Create ModeGroupInAtomicSwcInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeGroupInAtomicSwcInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeGroupInAtomicSwcInstanceRef since parent returns ARObject
        return cast("ModeGroupInAtomicSwcInstanceRef", obj)


class ModeGroupInAtomicSwcInstanceRefBuilder:
    """Builder for ModeGroupInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeGroupInAtomicSwcInstanceRef = ModeGroupInAtomicSwcInstanceRef()

    def build(self) -> ModeGroupInAtomicSwcInstanceRef:
        """Build and return ModeGroupInAtomicSwcInstanceRef object.

        Returns:
            ModeGroupInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
