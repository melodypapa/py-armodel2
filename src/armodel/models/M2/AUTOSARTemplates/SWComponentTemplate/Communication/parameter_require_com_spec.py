"""ParameterRequireComSpec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class ParameterRequireComSpec(RPortComSpec):
    """AUTOSAR ParameterRequireComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("init_value", None, False, False, ValueSpecification),  # initValue
        ("parameter", None, False, False, ParameterDataPrototype),  # parameter
    ]

    def __init__(self) -> None:
        """Initialize ParameterRequireComSpec."""
        super().__init__()
        self.init_value: Optional[ValueSpecification] = None
        self.parameter: Optional[ParameterDataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ParameterRequireComSpec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterRequireComSpec":
        """Create ParameterRequireComSpec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ParameterRequireComSpec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ParameterRequireComSpec since parent returns ARObject
        return cast("ParameterRequireComSpec", obj)


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
