"""NvRequireComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class NvRequireComSpec(RPortComSpec):
    """AUTOSAR NvRequireComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "init_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # initValue
        "variable": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableDataPrototype,
        ),  # variable
    }

    def __init__(self) -> None:
        """Initialize NvRequireComSpec."""
        super().__init__()
        self.init_value: Optional[ValueSpecification] = None
        self.variable: Optional[VariableDataPrototype] = None


class NvRequireComSpecBuilder:
    """Builder for NvRequireComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvRequireComSpec = NvRequireComSpec()

    def build(self) -> NvRequireComSpec:
        """Build and return NvRequireComSpec object.

        Returns:
            NvRequireComSpec instance
        """
        # TODO: Add validation
        return self._obj
