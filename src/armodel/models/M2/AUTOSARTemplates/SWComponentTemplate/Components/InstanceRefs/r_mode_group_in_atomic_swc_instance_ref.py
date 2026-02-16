"""RModeGroupInAtomicSWCInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.mode_group_in_atomic_swc_instance_ref import (
    ModeGroupInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class RModeGroupInAtomicSWCInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    """AUTOSAR RModeGroupInAtomicSWCInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context_r_port_prototype", None, False, False, AbstractRequiredPortPrototype),  # contextRPortPrototype
        ("target_mode", None, False, False, ModeDeclarationGroup),  # targetMode
    ]

    def __init__(self) -> None:
        """Initialize RModeGroupInAtomicSWCInstanceRef."""
        super().__init__()
        self.context_r_port_prototype: Optional[AbstractRequiredPortPrototype] = None
        self.target_mode: Optional[ModeDeclarationGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RModeGroupInAtomicSWCInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RModeGroupInAtomicSWCInstanceRef":
        """Create RModeGroupInAtomicSWCInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RModeGroupInAtomicSWCInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RModeGroupInAtomicSWCInstanceRef since parent returns ARObject
        return cast("RModeGroupInAtomicSWCInstanceRef", obj)


class RModeGroupInAtomicSWCInstanceRefBuilder:
    """Builder for RModeGroupInAtomicSWCInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RModeGroupInAtomicSWCInstanceRef = RModeGroupInAtomicSWCInstanceRef()

    def build(self) -> RModeGroupInAtomicSWCInstanceRef:
        """Build and return RModeGroupInAtomicSWCInstanceRef object.

        Returns:
            RModeGroupInAtomicSWCInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
