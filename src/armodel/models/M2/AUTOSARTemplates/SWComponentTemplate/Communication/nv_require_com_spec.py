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
