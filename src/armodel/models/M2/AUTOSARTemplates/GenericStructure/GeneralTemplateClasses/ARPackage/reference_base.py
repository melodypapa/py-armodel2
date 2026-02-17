"""ReferenceBase AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 72)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ARPackage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    ReferrableSubtypesEnum,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
        ARPackage,
    )



class ReferenceBase(ARObject):
    """AUTOSAR ReferenceBase."""

    global_elements: list[ReferrableSubtypesEnum]
    global_ins: list[ARPackage]
    is_default: Boolean
    package: Optional[ARPackage]
    short_label: Identifier
    def __init__(self) -> None:
        """Initialize ReferenceBase."""
        super().__init__()
        self.global_elements: list[ReferrableSubtypesEnum] = []
        self.global_ins: list[ARPackage] = []
        self.is_default: Boolean = None
        self.package: Optional[ARPackage] = None
        self.short_label: Identifier = None


class ReferenceBaseBuilder:
    """Builder for ReferenceBase."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceBase = ReferenceBase()

    def build(self) -> ReferenceBase:
        """Build and return ReferenceBase object.

        Returns:
            ReferenceBase instance
        """
        # TODO: Add validation
        return self._obj
