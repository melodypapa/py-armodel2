"""ModeSwitchSenderComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchSenderComSpec(PPortComSpec):
    """AUTOSAR ModeSwitchSenderComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    enhanced_mode: Optional[Boolean]
    mode_group_ref: Optional[ARRef]
    mode_switched_ack: Optional[Any]
    queue_length: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ModeSwitchSenderComSpec."""
        super().__init__()
        self.enhanced_mode: Optional[Boolean] = None
        self.mode_group_ref: Optional[ARRef] = None
        self.mode_switched_ack: Optional[Any] = None
        self.queue_length: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchSenderComSpec":
        """Deserialize XML element to ModeSwitchSenderComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeSwitchSenderComSpec object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse enhanced_mode
        child = ARObject._find_child_element(element, "ENHANCED-MODE")
        if child is not None:
            enhanced_mode_value = child.text
            obj.enhanced_mode = enhanced_mode_value

        # Parse mode_group_ref
        child = ARObject._find_child_element(element, "MODE-GROUP")
        if child is not None:
            mode_group_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.mode_group_ref = mode_group_ref_value

        # Parse mode_switched_ack
        child = ARObject._find_child_element(element, "MODE-SWITCHED-ACK")
        if child is not None:
            mode_switched_ack_value = child.text
            obj.mode_switched_ack = mode_switched_ack_value

        # Parse queue_length
        child = ARObject._find_child_element(element, "QUEUE-LENGTH")
        if child is not None:
            queue_length_value = child.text
            obj.queue_length = queue_length_value

        return obj



class ModeSwitchSenderComSpecBuilder:
    """Builder for ModeSwitchSenderComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchSenderComSpec = ModeSwitchSenderComSpec()

    def build(self) -> ModeSwitchSenderComSpec:
        """Build and return ModeSwitchSenderComSpec object.

        Returns:
            ModeSwitchSenderComSpec instance
        """
        # TODO: Add validation
        return self._obj
