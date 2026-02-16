"""NvRequireComSpec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class NvRequireComSpec(RPortComSpec):
    """AUTOSAR NvRequireComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("init_value", None, False, False, ValueSpecification),  # initValue
        ("variable", None, False, False, VariableDataPrototype),  # variable
    ]

    def __init__(self) -> None:
        """Initialize NvRequireComSpec."""
        super().__init__()
        self.init_value: Optional[ValueSpecification] = None
        self.variable: Optional[VariableDataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NvRequireComSpec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvRequireComSpec":
        """Create NvRequireComSpec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NvRequireComSpec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NvRequireComSpec since parent returns ARObject
        return cast("NvRequireComSpec", obj)


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
