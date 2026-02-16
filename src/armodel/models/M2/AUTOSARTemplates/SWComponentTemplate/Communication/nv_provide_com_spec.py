"""NvProvideComSpec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ram_block_init", None, False, False, ValueSpecification),  # ramBlockInit
        ("rom_block_init", None, False, False, ValueSpecification),  # romBlockInit
        ("variable", None, False, False, VariableDataPrototype),  # variable
    ]

    def __init__(self) -> None:
        """Initialize NvProvideComSpec."""
        super().__init__()
        self.ram_block_init: Optional[ValueSpecification] = None
        self.rom_block_init: Optional[ValueSpecification] = None
        self.variable: Optional[VariableDataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NvProvideComSpec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvProvideComSpec":
        """Create NvProvideComSpec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NvProvideComSpec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NvProvideComSpec since parent returns ARObject
        return cast("NvProvideComSpec", obj)


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
