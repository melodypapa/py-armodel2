"""NvProvideComSpec AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class NvProvideComSpec(PPortComSpec):
    """AUTOSAR NvProvideComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ram_block_init": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # ramBlockInit
        "rom_block_init": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # romBlockInit
        "variable": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableDataPrototype,
        ),  # variable
    }

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
