"""RModeInAtomicSwcInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class RModeInAtomicSwcInstanceRef(ARObject):
    """AUTOSAR RModeInAtomicSwcInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, AtomicSwComponentType),  # base
        ("context_mode_group_prototype", None, False, False, ModeDeclarationGroup),  # contextModeGroupPrototype
        ("context_port_prototype", None, False, False, AbstractRequiredPortPrototype),  # contextPortPrototype
        ("target_mode_declaration", None, False, False, ModeDeclaration),  # targetModeDeclaration
    ]

    def __init__(self) -> None:
        """Initialize RModeInAtomicSwcInstanceRef."""
        super().__init__()
        self.base: Optional[AtomicSwComponentType] = None
        self.context_mode_group_prototype: Optional[ModeDeclarationGroup] = None
        self.context_port_prototype: Optional[AbstractRequiredPortPrototype] = None
        self.target_mode_declaration: Optional[ModeDeclaration] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RModeInAtomicSwcInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RModeInAtomicSwcInstanceRef":
        """Create RModeInAtomicSwcInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RModeInAtomicSwcInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RModeInAtomicSwcInstanceRef since parent returns ARObject
        return cast("RModeInAtomicSwcInstanceRef", obj)


class RModeInAtomicSwcInstanceRefBuilder:
    """Builder for RModeInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RModeInAtomicSwcInstanceRef = RModeInAtomicSwcInstanceRef()

    def build(self) -> RModeInAtomicSwcInstanceRef:
        """Build and return RModeInAtomicSwcInstanceRef object.

        Returns:
            RModeInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
