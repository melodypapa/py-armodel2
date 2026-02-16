"""InternalBehavior AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class InternalBehavior(Identifiable):
    """AUTOSAR InternalBehavior."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("constants", None, False, True, ParameterDataPrototype),  # constants
        ("constant_values", None, False, True, ConstantSpecification),  # constantValues
        ("data_types", None, False, True, DataTypeMappingSet),  # dataTypes
        ("exclusive_areas", None, False, True, ExclusiveArea),  # exclusiveAreas
        ("exclusive_area_nestings", None, False, True, ExclusiveAreaNestingOrder),  # exclusiveAreaNestings
        ("static_memories", None, False, True, VariableDataPrototype),  # staticMemories
    ]

    def __init__(self) -> None:
        """Initialize InternalBehavior."""
        super().__init__()
        self.constants: list[ParameterDataPrototype] = []
        self.constant_values: list[ConstantSpecification] = []
        self.data_types: list[DataTypeMappingSet] = []
        self.exclusive_areas: list[ExclusiveArea] = []
        self.exclusive_area_nestings: list[ExclusiveAreaNestingOrder] = []
        self.static_memories: list[VariableDataPrototype] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InternalBehavior to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InternalBehavior":
        """Create InternalBehavior from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InternalBehavior instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InternalBehavior since parent returns ARObject
        return cast("InternalBehavior", obj)


class InternalBehaviorBuilder:
    """Builder for InternalBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InternalBehavior = InternalBehavior()

    def build(self) -> InternalBehavior:
        """Build and return InternalBehavior object.

        Returns:
            InternalBehavior instance
        """
        # TODO: Add validation
        return self._obj
