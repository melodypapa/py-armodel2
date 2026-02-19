"""CalibrationParameterValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 478)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2007)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_MeasurementAndCalibration_CalibrationParameter.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class CalibrationParameterValue(ARObject):
    """AUTOSAR CalibrationParameterValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    appl_init_value: Optional[ValueSpecification]
    impl_init_value: Optional[ValueSpecification]
    initialized: Optional[FlatInstanceDescriptor]
    def __init__(self) -> None:
        """Initialize CalibrationParameterValue."""
        super().__init__()
        self.appl_init_value: Optional[ValueSpecification] = None
        self.impl_init_value: Optional[ValueSpecification] = None
        self.initialized: Optional[FlatInstanceDescriptor] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CalibrationParameterValue":
        """Deserialize XML element to CalibrationParameterValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CalibrationParameterValue object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse appl_init_value
        child = ARObject._find_child_element(element, "APPL-INIT-VALUE")
        if child is not None:
            appl_init_value_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.appl_init_value = appl_init_value_value

        # Parse impl_init_value
        child = ARObject._find_child_element(element, "IMPL-INIT-VALUE")
        if child is not None:
            impl_init_value_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.impl_init_value = impl_init_value_value

        # Parse initialized
        child = ARObject._find_child_element(element, "INITIALIZED")
        if child is not None:
            initialized_value = ARObject._deserialize_by_tag(child, "FlatInstanceDescriptor")
            obj.initialized = initialized_value

        return obj



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
