"""AliasNameAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 175)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 968)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)


class AliasNameAssignment(ARObject):
    """AUTOSAR AliasNameAssignment."""

    flat_instance: Optional[FlatInstanceDescriptor]
    identifiable: Optional[Identifiable]
    label: Optional[MultilanguageLongName]
    short_label: Optional[String]
    def __init__(self) -> None:
        """Initialize AliasNameAssignment."""
        super().__init__()
        self.flat_instance: Optional[FlatInstanceDescriptor] = None
        self.identifiable: Optional[Identifiable] = None
        self.label: Optional[MultilanguageLongName] = None
        self.short_label: Optional[String] = None


class AliasNameAssignmentBuilder:
    """Builder for AliasNameAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AliasNameAssignment = AliasNameAssignment()

    def build(self) -> AliasNameAssignment:
        """Build and return AliasNameAssignment object.

        Returns:
            AliasNameAssignment instance
        """
        # TODO: Add validation
        return self._obj
