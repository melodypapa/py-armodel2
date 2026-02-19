"""ParameterRequireComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 193)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class ParameterRequireComSpec(RPortComSpec):
    """AUTOSAR ParameterRequireComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    init_value: Optional[ValueSpecification]
    parameter_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ParameterRequireComSpec."""
        super().__init__()
        self.init_value: Optional[ValueSpecification] = None
        self.parameter_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterRequireComSpec":
        """Deserialize XML element to ParameterRequireComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ParameterRequireComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ParameterRequireComSpec, cls).deserialize(element)

        # Parse init_value
        child = ARObject._find_child_element(element, "INIT-VALUE")
        if child is not None:
            init_value_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.init_value = init_value_value

        # Parse parameter_ref
        child = ARObject._find_child_element(element, "PARAMETER")
        if child is not None:
            parameter_ref_value = ARObject._deserialize_by_tag(child, "ParameterDataPrototype")
            obj.parameter_ref = parameter_ref_value

        return obj



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
