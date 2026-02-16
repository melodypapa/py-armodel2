"""ParameterProvideComSpec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class ParameterProvideComSpec(PPortComSpec):
    """AUTOSAR ParameterProvideComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("init_value", None, False, False, ValueSpecification),  # initValue
        ("parameter", None, False, False, ParameterDataPrototype),  # parameter
    ]

    def __init__(self) -> None:
        """Initialize ParameterProvideComSpec."""
        super().__init__()
        self.init_value: Optional[ValueSpecification] = None
        self.parameter: Optional[ParameterDataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ParameterProvideComSpec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterProvideComSpec":
        """Create ParameterProvideComSpec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ParameterProvideComSpec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ParameterProvideComSpec since parent returns ARObject
        return cast("ParameterProvideComSpec", obj)


class ParameterProvideComSpecBuilder:
    """Builder for ParameterProvideComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterProvideComSpec = ParameterProvideComSpec()

    def build(self) -> ParameterProvideComSpec:
        """Build and return ParameterProvideComSpec object.

        Returns:
            ParameterProvideComSpec instance
        """
        # TODO: Add validation
        return self._obj
