"""IoHwAbstractionServerAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    FilterDebouncingEnum,
    PulseTestEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.argument_data_prototype import (
    ArgumentDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
        PortPrototype,
    )



class IoHwAbstractionServerAnnotation(GeneralAnnotation):
    """AUTOSAR IoHwAbstractionServerAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    age: Optional[MultidimensionalTime]
    argument_ref: Optional[ARRef]
    bsw_resolution: Optional[Float]
    data_element_ref: Optional[ARRef]
    failure_ref: Optional[ARRef]
    filtering: Optional[FilterDebouncingEnum]
    pulse_test: Optional[PulseTestEnum]
    trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize IoHwAbstractionServerAnnotation."""
        super().__init__()
        self.age: Optional[MultidimensionalTime] = None
        self.argument_ref: Optional[ARRef] = None
        self.bsw_resolution: Optional[Float] = None
        self.data_element_ref: Optional[ARRef] = None
        self.failure_ref: Optional[ARRef] = None
        self.filtering: Optional[FilterDebouncingEnum] = None
        self.pulse_test: Optional[PulseTestEnum] = None
        self.trigger_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IoHwAbstractionServerAnnotation":
        """Deserialize XML element to IoHwAbstractionServerAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IoHwAbstractionServerAnnotation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IoHwAbstractionServerAnnotation, cls).deserialize(element)

        # Parse age
        child = ARObject._find_child_element(element, "AGE")
        if child is not None:
            age_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.age = age_value

        # Parse argument_ref
        child = ARObject._find_child_element(element, "ARGUMENT")
        if child is not None:
            argument_ref_value = ARObject._deserialize_by_tag(child, "ArgumentDataPrototype")
            obj.argument_ref = argument_ref_value

        # Parse bsw_resolution
        child = ARObject._find_child_element(element, "BSW-RESOLUTION")
        if child is not None:
            bsw_resolution_value = child.text
            obj.bsw_resolution = bsw_resolution_value

        # Parse data_element_ref
        child = ARObject._find_child_element(element, "DATA-ELEMENT")
        if child is not None:
            data_element_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.data_element_ref = data_element_ref_value

        # Parse failure_ref
        child = ARObject._find_child_element(element, "FAILURE")
        if child is not None:
            failure_ref_value = ARObject._deserialize_by_tag(child, "PortPrototype")
            obj.failure_ref = failure_ref_value

        # Parse filtering
        child = ARObject._find_child_element(element, "FILTERING")
        if child is not None:
            filtering_value = FilterDebouncingEnum.deserialize(child)
            obj.filtering = filtering_value

        # Parse pulse_test
        child = ARObject._find_child_element(element, "PULSE-TEST")
        if child is not None:
            pulse_test_value = PulseTestEnum.deserialize(child)
            obj.pulse_test = pulse_test_value

        # Parse trigger_ref
        child = ARObject._find_child_element(element, "TRIGGER")
        if child is not None:
            trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.trigger_ref = trigger_ref_value

        return obj



class IoHwAbstractionServerAnnotationBuilder:
    """Builder for IoHwAbstractionServerAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IoHwAbstractionServerAnnotation = IoHwAbstractionServerAnnotation()

    def build(self) -> IoHwAbstractionServerAnnotation:
        """Build and return IoHwAbstractionServerAnnotation object.

        Returns:
            IoHwAbstractionServerAnnotation instance
        """
        # TODO: Add validation
        return self._obj
