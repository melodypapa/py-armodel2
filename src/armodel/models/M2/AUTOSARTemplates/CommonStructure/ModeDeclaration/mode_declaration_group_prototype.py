"""ModeDeclarationGroupPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 42)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 323)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 113)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2038)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 233)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwCalibrationAccessEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeDeclarationGroupPrototype(Identifiable):
    """AUTOSAR ModeDeclarationGroupPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_calibration_access: Optional[SwCalibrationAccessEnum]
    type_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeDeclarationGroupPrototype."""
        super().__init__()
        self.sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
        self.type_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationGroupPrototype":
        """Deserialize XML element to ModeDeclarationGroupPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeDeclarationGroupPrototype object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sw_calibration_access
        child = ARObject._find_child_element(element, "SW-CALIBRATION-ACCESS")
        if child is not None:
            sw_calibration_access_value = child.text
            obj.sw_calibration_access = sw_calibration_access_value

        # Parse type_ref
        child = ARObject._find_child_element(element, "TYPE")
        if child is not None:
            type_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.type_ref = type_ref_value

        return obj



class ModeDeclarationGroupPrototypeBuilder:
    """Builder for ModeDeclarationGroupPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclarationGroupPrototype = ModeDeclarationGroupPrototype()

    def build(self) -> ModeDeclarationGroupPrototype:
        """Build and return ModeDeclarationGroupPrototype object.

        Returns:
            ModeDeclarationGroupPrototype instance
        """
        # TODO: Add validation
        return self._obj
