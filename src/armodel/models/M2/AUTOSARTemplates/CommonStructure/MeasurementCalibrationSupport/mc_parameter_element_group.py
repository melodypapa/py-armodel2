"""McParameterElementGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 181)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class McParameterElementGroup(ARObject):
    """AUTOSAR McParameterElementGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ram_location": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableDataPrototype,
        ),  # ramLocation
        "rom_location": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ParameterDataPrototype,
        ),  # romLocation
        "short_label": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # shortLabel
    }

    def __init__(self) -> None:
        """Initialize McParameterElementGroup."""
        super().__init__()
        self.ram_location: Optional[VariableDataPrototype] = None
        self.rom_location: Optional[ParameterDataPrototype] = None
        self.short_label: Optional[Identifier] = None


class McParameterElementGroupBuilder:
    """Builder for McParameterElementGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McParameterElementGroup = McParameterElementGroup()

    def build(self) -> McParameterElementGroup:
        """Build and return McParameterElementGroup object.

        Returns:
            McParameterElementGroup instance
        """
        # TODO: Add validation
        return self._obj
