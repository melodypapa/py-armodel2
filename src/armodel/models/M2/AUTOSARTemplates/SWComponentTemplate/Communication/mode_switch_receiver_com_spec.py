"""ModeSwitchReceiverComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 191)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchReceiverComSpec(RPortComSpec):
    """AUTOSAR ModeSwitchReceiverComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    enhanced_mode: Optional[Boolean]
    mode_group_ref: Optional[ARRef]
    supports: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize ModeSwitchReceiverComSpec."""
        super().__init__()
        self.enhanced_mode: Optional[Boolean] = None
        self.mode_group_ref: Optional[ARRef] = None
        self.supports: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchReceiverComSpec":
        """Deserialize XML element to ModeSwitchReceiverComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeSwitchReceiverComSpec object
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

        # Parse supports
        child = ARObject._find_child_element(element, "SUPPORTS")
        if child is not None:
            supports_value = child.text
            obj.supports = supports_value

        return obj



class ModeSwitchReceiverComSpecBuilder:
    """Builder for ModeSwitchReceiverComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchReceiverComSpec = ModeSwitchReceiverComSpec()

    def build(self) -> ModeSwitchReceiverComSpec:
        """Build and return ModeSwitchReceiverComSpec object.

        Returns:
            ModeSwitchReceiverComSpec instance
        """
        # TODO: Add validation
        return self._obj
