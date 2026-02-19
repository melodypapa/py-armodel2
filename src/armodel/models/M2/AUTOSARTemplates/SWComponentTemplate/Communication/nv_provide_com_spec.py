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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    variable_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize NvProvideComSpec."""
        super().__init__()
        self.ram_block_init: Optional[ValueSpecification] = None
        self.rom_block_init: Optional[ValueSpecification] = None
        self.variable_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvProvideComSpec":
        """Deserialize XML element to NvProvideComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvProvideComSpec object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ram_block_init
        child = ARObject._find_child_element(element, "RAM-BLOCK-INIT")
        if child is not None:
            ram_block_init_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.ram_block_init = ram_block_init_value

        # Parse rom_block_init
        child = ARObject._find_child_element(element, "ROM-BLOCK-INIT")
        if child is not None:
            rom_block_init_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.rom_block_init = rom_block_init_value

        # Parse variable_ref
        child = ARObject._find_child_element(element, "VARIABLE")
        if child is not None:
            variable_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.variable_ref = variable_ref_value

        return obj



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
