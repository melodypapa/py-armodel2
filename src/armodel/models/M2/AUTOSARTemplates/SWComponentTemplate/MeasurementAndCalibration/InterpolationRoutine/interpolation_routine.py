"""InterpolationRoutine AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 430)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 46)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_MeasurementAndCalibration_InterpolationRoutine.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class InterpolationRoutine(ARObject):
    """AUTOSAR InterpolationRoutine."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "interpolation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswModuleEntry,
        ),  # interpolation
        "is_default": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # isDefault
        "short_label": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # shortLabel
    }

    def __init__(self) -> None:
        """Initialize InterpolationRoutine."""
        super().__init__()
        self.interpolation: Optional[BswModuleEntry] = None
        self.is_default: Optional[Boolean] = None
        self.short_label: Optional[Identifier] = None


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
