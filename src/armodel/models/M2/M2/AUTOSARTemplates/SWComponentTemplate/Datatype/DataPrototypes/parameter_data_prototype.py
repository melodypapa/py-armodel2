"""ParameterDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 107)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2042)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 457)

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


class ParameterDataPrototype(AutosarDataPrototype):
    """AUTOSAR ParameterDataPrototype."""

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
        """Initialize ParameterDataPrototype."""
        super().__init__()
        self.init_value: Optional[ValueSpecification] = None


class ParameterDataPrototypeBuilder:
    """Builder for ParameterDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterDataPrototype = ParameterDataPrototype()

    def build(self) -> ParameterDataPrototype:
        """Build and return ParameterDataPrototype object.

        Returns:
            ParameterDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
