"""CalibrationParameterValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 478)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2007)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_MeasurementAndCalibration_CalibrationParameter.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class CalibrationParameterValue(ARObject):
    """AUTOSAR CalibrationParameterValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "appl_init_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # applInitValue
        "impl_init_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # implInitValue
        "initialized": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FlatInstanceDescriptor,
        ),  # initialized
    }

    def __init__(self) -> None:
        """Initialize CalibrationParameterValue."""
        super().__init__()
        self.appl_init_value: Optional[ValueSpecification] = None
        self.impl_init_value: Optional[ValueSpecification] = None
        self.initialized: Optional[FlatInstanceDescriptor] = None


class CalibrationParameterValueBuilder:
    """Builder for CalibrationParameterValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CalibrationParameterValue = CalibrationParameterValue()

    def build(self) -> CalibrationParameterValue:
        """Build and return CalibrationParameterValue object.

        Returns:
            CalibrationParameterValue instance
        """
        # TODO: Add validation
        return self._obj
