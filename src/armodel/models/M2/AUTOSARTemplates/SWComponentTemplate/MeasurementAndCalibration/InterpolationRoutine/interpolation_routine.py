"""InterpolationRoutine AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 430)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 46)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_MeasurementAndCalibration_InterpolationRoutine.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class InterpolationRoutine(ARObject):
    """AUTOSAR InterpolationRoutine."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    interpolation: Optional[BswModuleEntry]
    is_default: Optional[Boolean]
    short_label: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize InterpolationRoutine."""
        super().__init__()
        self.interpolation: Optional[BswModuleEntry] = None
        self.is_default: Optional[Boolean] = None
        self.short_label: Optional[Identifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "InterpolationRoutine":
        """Deserialize XML element to InterpolationRoutine object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InterpolationRoutine object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse interpolation
        child = ARObject._find_child_element(element, "INTERPOLATION")
        if child is not None:
            interpolation_value = ARObject._deserialize_by_tag(child, "BswModuleEntry")
            obj.interpolation = interpolation_value

        # Parse is_default
        child = ARObject._find_child_element(element, "IS-DEFAULT")
        if child is not None:
            is_default_value = child.text
            obj.is_default = is_default_value

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        return obj



class InterpolationRoutineBuilder:
    """Builder for InterpolationRoutine."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InterpolationRoutine = InterpolationRoutine()

    def build(self) -> InterpolationRoutine:
        """Build and return InterpolationRoutine object.

        Returns:
            InterpolationRoutine instance
        """
        # TODO: Add validation
        return self._obj
