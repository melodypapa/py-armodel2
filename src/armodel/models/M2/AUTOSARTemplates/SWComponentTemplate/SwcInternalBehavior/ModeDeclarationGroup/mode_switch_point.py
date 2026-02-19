"""ModeSwitchPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 323)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 633)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ModeDeclarationGroup.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchPoint(AbstractAccessPoint):
    """AUTOSAR ModeSwitchPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_group_swc_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeSwitchPoint."""
        super().__init__()
        self.mode_group_swc_instance_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchPoint":
        """Deserialize XML element to ModeSwitchPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeSwitchPoint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse mode_group_swc_instance_ref
        child = ARObject._find_child_element(element, "MODE-GROUP-SWC-INSTANCE-REF")
        if child is not None:
            mode_group_swc_instance_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.mode_group_swc_instance_ref = mode_group_swc_instance_ref_value

        return obj



class ModeSwitchPointBuilder:
    """Builder for ModeSwitchPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchPoint = ModeSwitchPoint()

    def build(self) -> ModeSwitchPoint:
        """Build and return ModeSwitchPoint object.

        Returns:
            ModeSwitchPoint instance
        """
        # TODO: Add validation
        return self._obj
