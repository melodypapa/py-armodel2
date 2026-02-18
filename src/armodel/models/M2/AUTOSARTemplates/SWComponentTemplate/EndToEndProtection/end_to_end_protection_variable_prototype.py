"""EndToEndProtectionVariablePrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 215)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2022)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class EndToEndProtectionVariablePrototype(ARObject):
    """AUTOSAR EndToEndProtectionVariablePrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    receivers: list[VariableDataPrototype]
    sender: Optional[VariableDataPrototype]
    short_label: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize EndToEndProtectionVariablePrototype."""
        super().__init__()
        self.receivers: list[VariableDataPrototype] = []
        self.sender: Optional[VariableDataPrototype] = None
        self.short_label: Optional[Identifier] = None


class EndToEndProtectionVariablePrototypeBuilder:
    """Builder for EndToEndProtectionVariablePrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndProtectionVariablePrototype = EndToEndProtectionVariablePrototype()

    def build(self) -> EndToEndProtectionVariablePrototype:
        """Build and return EndToEndProtectionVariablePrototype object.

        Returns:
            EndToEndProtectionVariablePrototype instance
        """
        # TODO: Add validation
        return self._obj
