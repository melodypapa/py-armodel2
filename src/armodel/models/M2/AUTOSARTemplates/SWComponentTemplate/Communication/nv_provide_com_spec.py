"""NvProvideComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class NvProvideComSpec(PPortComSpec):
    """AUTOSAR NvProvideComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ram_block_init: Optional[ValueSpecification]
    rom_block_init: Optional[ValueSpecification]
    variable: Optional[VariableDataPrototype]
    def __init__(self) -> None:
        """Initialize NvProvideComSpec."""
        super().__init__()
        self.ram_block_init: Optional[ValueSpecification] = None
        self.rom_block_init: Optional[ValueSpecification] = None
        self.variable: Optional[VariableDataPrototype] = None


class NvProvideComSpecBuilder:
    """Builder for NvProvideComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvProvideComSpec = NvProvideComSpec()

    def build(self) -> NvProvideComSpec:
        """Build and return NvProvideComSpec object.

        Returns:
            NvProvideComSpec instance
        """
        # TODO: Add validation
        return self._obj
