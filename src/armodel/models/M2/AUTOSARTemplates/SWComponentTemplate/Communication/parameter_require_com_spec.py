"""ParameterRequireComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 193)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class ParameterRequireComSpec(RPortComSpec):
    """AUTOSAR ParameterRequireComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "init_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # initValue
        "parameter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ParameterDataPrototype,
        ),  # parameter
    }

    def __init__(self) -> None:
        """Initialize ParameterRequireComSpec."""
        super().__init__()
        self.init_value: Optional[ValueSpecification] = None
        self.parameter: Optional[ParameterDataPrototype] = None


class ParameterRequireComSpecBuilder:
    """Builder for ParameterRequireComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterRequireComSpec = ParameterRequireComSpec()

    def build(self) -> ParameterRequireComSpec:
        """Build and return ParameterRequireComSpec object.

        Returns:
            ParameterRequireComSpec instance
        """
        # TODO: Add validation
        return self._obj
