"""ParameterSwComponentType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps.instantiation_data_def_props import (
    InstantiationDataDefProps,
)


class ParameterSwComponentType(SwComponentType):
    """AUTOSAR ParameterSwComponentType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("constants", None, False, True, ConstantSpecification),  # constants
        ("data_types", None, False, True, DataTypeMappingSet),  # dataTypes
        ("instantiation_data_defs", None, False, True, InstantiationDataDefProps),  # instantiationDataDefs
    ]

    def __init__(self) -> None:
        """Initialize ParameterSwComponentType."""
        super().__init__()
        self.constants: list[ConstantSpecification] = []
        self.data_types: list[DataTypeMappingSet] = []
        self.instantiation_data_defs: list[InstantiationDataDefProps] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ParameterSwComponentType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterSwComponentType":
        """Create ParameterSwComponentType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ParameterSwComponentType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ParameterSwComponentType since parent returns ARObject
        return cast("ParameterSwComponentType", obj)


class ParameterSwComponentTypeBuilder:
    """Builder for ParameterSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterSwComponentType = ParameterSwComponentType()

    def build(self) -> ParameterSwComponentType:
        """Build and return ParameterSwComponentType object.

        Returns:
            ParameterSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
