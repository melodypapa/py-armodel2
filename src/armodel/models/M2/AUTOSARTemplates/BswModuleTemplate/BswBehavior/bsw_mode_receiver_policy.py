"""BswModeReceiverPolicy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class BswModeReceiverPolicy(ARObject):
    """AUTOSAR BswModeReceiverPolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("enhanced_mode", None, True, False, None),  # enhancedMode
        ("required_mode", None, False, False, ModeDeclarationGroup),  # requiredMode
        ("supports", None, True, False, None),  # supports
    ]

    def __init__(self) -> None:
        """Initialize BswModeReceiverPolicy."""
        super().__init__()
        self.enhanced_mode: Optional[Boolean] = None
        self.required_mode: Optional[ModeDeclarationGroup] = None
        self.supports: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswModeReceiverPolicy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModeReceiverPolicy":
        """Create BswModeReceiverPolicy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswModeReceiverPolicy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswModeReceiverPolicy since parent returns ARObject
        return cast("BswModeReceiverPolicy", obj)


class BswModeReceiverPolicyBuilder:
    """Builder for BswModeReceiverPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeReceiverPolicy = BswModeReceiverPolicy()

    def build(self) -> BswModeReceiverPolicy:
        """Build and return BswModeReceiverPolicy object.

        Returns:
            BswModeReceiverPolicy instance
        """
        # TODO: Add validation
        return self._obj
