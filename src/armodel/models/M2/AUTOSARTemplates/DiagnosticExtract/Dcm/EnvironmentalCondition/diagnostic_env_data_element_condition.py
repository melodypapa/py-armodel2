"""DiagnosticEnvDataElementCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("compare_value", None, False, False, ValueSpecification),  # compareValue
        ("data_prototype", None, False, False, DataPrototype),  # dataPrototype
        ("sw_data_def", None, False, False, SwDataDefProps),  # swDataDef
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEnvDataElementCondition."""
        super().__init__()
        self.compare_value: Optional[ValueSpecification] = None
        self.data_prototype: Optional[DataPrototype] = None
        self.sw_data_def: Optional[SwDataDefProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEnvDataElementCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvDataElementCondition":
        """Create DiagnosticEnvDataElementCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEnvDataElementCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEnvDataElementCondition since parent returns ARObject
        return cast("DiagnosticEnvDataElementCondition", obj)


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
