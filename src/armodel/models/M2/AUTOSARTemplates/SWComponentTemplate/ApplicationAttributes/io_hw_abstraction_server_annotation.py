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

    age: Optional[MultidimensionalTime]
    argument: Optional[ArgumentDataPrototype]
    bsw_resolution: Optional[Float]
    data_element: Optional[VariableDataPrototype]
    failure: Optional[PortPrototype]
    filtering: Optional[FilterDebouncingEnum]
    pulse_test: Optional[PulseTestEnum]
    trigger: Optional[Trigger]
    def __init__(self) -> None:
        """Initialize IoHwAbstractionServerAnnotation."""
        super().__init__()
        self.age: Optional[MultidimensionalTime] = None
        self.argument: Optional[ArgumentDataPrototype] = None
        self.bsw_resolution: Optional[Float] = None
        self.data_element: Optional[VariableDataPrototype] = None
        self.failure: Optional[PortPrototype] = None
        self.filtering: Optional[FilterDebouncingEnum] = None
        self.pulse_test: Optional[PulseTestEnum] = None
        self.trigger: Optional[Trigger] = None


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
