"""ModeSwitchInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 113)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2039)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchInterface(PortInterface):
    """AUTOSAR ModeSwitchInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_group_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeSwitchInterface."""
        super().__init__()
        self.mode_group_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchInterface":
        """Deserialize XML element to ModeSwitchInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeSwitchInterface object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse mode_group_ref
        child = ARObject._find_child_element(element, "MODE-GROUP")
        if child is not None:
            mode_group_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.mode_group_ref = mode_group_ref_value

        return obj



class ModeSwitchInterfaceBuilder:
    """Builder for ModeSwitchInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchInterface = ModeSwitchInterface()

    def build(self) -> ModeSwitchInterface:
        """Build and return ModeSwitchInterface object.

        Returns:
            ModeSwitchInterface instance
        """
        # TODO: Add validation
        return self._obj
