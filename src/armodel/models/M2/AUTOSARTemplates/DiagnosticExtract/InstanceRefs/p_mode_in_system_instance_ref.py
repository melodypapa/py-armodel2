"""PModeInSystemInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class PModeInSystemInstanceRef(ARObject):
    """AUTOSAR PModeInSystemInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, System),  # base
        ("context", None, False, False, RootSwCompositionPrototype),  # context
        ("context_mode_group", None, False, False, ModeDeclarationGroup),  # contextModeGroup
        ("context_p_port_prototype", None, False, False, AbstractProvidedPortPrototype),  # contextPPortPrototype
        ("target_mode", None, False, False, ModeDeclaration),  # targetMode
    ]

    def __init__(self) -> None:
        """Initialize PModeInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.context: Optional[RootSwCompositionPrototype] = None
        self.context_mode_group: Optional[ModeDeclarationGroup] = None
        self.context_p_port_prototype: Optional[AbstractProvidedPortPrototype] = None
        self.target_mode: Optional[ModeDeclaration] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PModeInSystemInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PModeInSystemInstanceRef":
        """Create PModeInSystemInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PModeInSystemInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PModeInSystemInstanceRef since parent returns ARObject
        return cast("PModeInSystemInstanceRef", obj)


class PModeInSystemInstanceRefBuilder:
    """Builder for PModeInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PModeInSystemInstanceRef = PModeInSystemInstanceRef()

    def build(self) -> PModeInSystemInstanceRef:
        """Build and return PModeInSystemInstanceRef object.

        Returns:
            PModeInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
