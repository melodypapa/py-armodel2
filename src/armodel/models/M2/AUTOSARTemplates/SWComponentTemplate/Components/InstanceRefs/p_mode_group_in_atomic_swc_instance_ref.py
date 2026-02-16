"""PModeGroupInAtomicSwcInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.mode_group_in_atomic_swc_instance_ref import (
    ModeGroupInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class PModeGroupInAtomicSwcInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    """AUTOSAR PModeGroupInAtomicSwcInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context_p_port_prototype", None, False, False, AbstractProvidedPortPrototype),  # contextPPortPrototype
        ("target_mode", None, False, False, ModeDeclarationGroup),  # targetMode
    ]

    def __init__(self) -> None:
        """Initialize PModeGroupInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_p_port_prototype: Optional[AbstractProvidedPortPrototype] = None
        self.target_mode: Optional[ModeDeclarationGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PModeGroupInAtomicSwcInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PModeGroupInAtomicSwcInstanceRef":
        """Create PModeGroupInAtomicSwcInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PModeGroupInAtomicSwcInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PModeGroupInAtomicSwcInstanceRef since parent returns ARObject
        return cast("PModeGroupInAtomicSwcInstanceRef", obj)


class PModeGroupInAtomicSwcInstanceRefBuilder:
    """Builder for PModeGroupInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PModeGroupInAtomicSwcInstanceRef = PModeGroupInAtomicSwcInstanceRef()

    def build(self) -> PModeGroupInAtomicSwcInstanceRef:
        """Build and return PModeGroupInAtomicSwcInstanceRef object.

        Returns:
            PModeGroupInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
