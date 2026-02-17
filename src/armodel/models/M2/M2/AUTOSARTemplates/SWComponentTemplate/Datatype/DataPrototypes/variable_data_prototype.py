"""VariableDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 107)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2077)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 256)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 29)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 223)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class VariableDataPrototype(AutosarDataPrototype):
    """AUTOSAR VariableDataPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "init_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # initValue
    }

    def __init__(self) -> None:
        """Initialize VariableDataPrototype."""
        super().__init__()
        self.init_value: Optional[ValueSpecification] = None


class VariableDataPrototypeBuilder:
    """Builder for VariableDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableDataPrototype = VariableDataPrototype()

    def build(self) -> VariableDataPrototype:
        """Build and return VariableDataPrototype object.

        Returns:
            VariableDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
