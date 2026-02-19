"""NvRequireComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class NvRequireComSpec(RPortComSpec):
    """AUTOSAR NvRequireComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    init_value: Optional[ValueSpecification]
    variable_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize NvRequireComSpec."""
        super().__init__()
        self.init_value: Optional[ValueSpecification] = None
        self.variable_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvRequireComSpec":
        """Deserialize XML element to NvRequireComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvRequireComSpec object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse init_value
        child = ARObject._find_child_element(element, "INIT-VALUE")
        if child is not None:
            init_value_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.init_value = init_value_value

        # Parse variable_ref
        child = ARObject._find_child_element(element, "VARIABLE")
        if child is not None:
            variable_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.variable_ref = variable_ref_value

        return obj



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
