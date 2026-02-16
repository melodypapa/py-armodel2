"""BswModeSenderPolicy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_mode_switch_ack_request import (
    BswModeSwitchAckRequest,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class BswModeSenderPolicy(ARObject):
    """AUTOSAR BswModeSenderPolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ack_request_request", None, False, False, BswModeSwitchAckRequest),  # ackRequestRequest
        ("enhanced_mode", None, True, False, None),  # enhancedMode
        ("provided_mode", None, False, False, ModeDeclarationGroup),  # providedMode
        ("queue_length", None, True, False, None),  # queueLength
    ]

    def __init__(self) -> None:
        """Initialize BswModeSenderPolicy."""
        super().__init__()
        self.ack_request_request: Optional[BswModeSwitchAckRequest] = None
        self.enhanced_mode: Optional[Boolean] = None
        self.provided_mode: Optional[ModeDeclarationGroup] = None
        self.queue_length: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswModeSenderPolicy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModeSenderPolicy":
        """Create BswModeSenderPolicy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswModeSenderPolicy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswModeSenderPolicy since parent returns ARObject
        return cast("BswModeSenderPolicy", obj)


class BswModeSenderPolicyBuilder:
    """Builder for BswModeSenderPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeSenderPolicy = BswModeSenderPolicy()

    def build(self) -> BswModeSenderPolicy:
        """Build and return BswModeSenderPolicy object.

        Returns:
            BswModeSenderPolicy instance
        """
        # TODO: Add validation
        return self._obj
