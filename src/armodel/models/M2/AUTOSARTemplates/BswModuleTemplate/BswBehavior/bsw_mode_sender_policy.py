"""BswModeSenderPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ack_request_request: Optional[BswModeSwitchAckRequest]
    enhanced_mode: Optional[Boolean]
    provided_mode_ref: Optional[ARRef]
    queue_length: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize BswModeSenderPolicy."""
        super().__init__()
        self.ack_request_request: Optional[BswModeSwitchAckRequest] = None
        self.enhanced_mode: Optional[Boolean] = None
        self.provided_mode_ref: Optional[ARRef] = None
        self.queue_length: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModeSenderPolicy":
        """Deserialize XML element to BswModeSenderPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModeSenderPolicy object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ack_request_request
        child = ARObject._find_child_element(element, "ACK-REQUEST-REQUEST")
        if child is not None:
            ack_request_request_value = ARObject._deserialize_by_tag(child, "BswModeSwitchAckRequest")
            obj.ack_request_request = ack_request_request_value

        # Parse enhanced_mode
        child = ARObject._find_child_element(element, "ENHANCED-MODE")
        if child is not None:
            enhanced_mode_value = child.text
            obj.enhanced_mode = enhanced_mode_value

        # Parse provided_mode_ref
        child = ARObject._find_child_element(element, "PROVIDED-MODE")
        if child is not None:
            provided_mode_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.provided_mode_ref = provided_mode_ref_value

        # Parse queue_length
        child = ARObject._find_child_element(element, "QUEUE-LENGTH")
        if child is not None:
            queue_length_value = child.text
            obj.queue_length = queue_length_value

        return obj



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
