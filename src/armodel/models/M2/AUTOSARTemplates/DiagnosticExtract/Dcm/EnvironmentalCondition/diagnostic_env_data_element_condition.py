"""DiagnosticEnvDataElementCondition AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_compare_condition import (
    DiagnosticEnvCompareCondition,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class DiagnosticEnvDataElementCondition(DiagnosticEnvCompareCondition):
    """AUTOSAR DiagnosticEnvDataElementCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "compare_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # compareValue
        "data_prototype": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataPrototype,
        ),  # dataPrototype
        "sw_data_def": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwDataDefProps,
        ),  # swDataDef
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEnvDataElementCondition."""
        super().__init__()
        self.compare_value: Optional[ValueSpecification] = None
        self.data_prototype: Optional[DataPrototype] = None
        self.sw_data_def: Optional[SwDataDefProps] = None


class DiagnosticEnvDataElementConditionBuilder:
    """Builder for DiagnosticEnvDataElementCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvDataElementCondition = DiagnosticEnvDataElementCondition()

    def build(self) -> DiagnosticEnvDataElementCondition:
        """Build and return DiagnosticEnvDataElementCondition object.

        Returns:
            DiagnosticEnvDataElementCondition instance
        """
        # TODO: Add validation
        return self._obj
