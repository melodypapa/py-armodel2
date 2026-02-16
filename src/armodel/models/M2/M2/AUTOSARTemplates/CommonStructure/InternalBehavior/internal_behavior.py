"""InternalBehavior AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "constants": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ParameterDataPrototype,
        ),  # constants
        "constant_values": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ConstantSpecification,
        ),  # constantValues
        "data_types": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DataTypeMappingSet,
        ),  # dataTypes
        "exclusive_areas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ExclusiveArea,
        ),  # exclusiveAreas
        "exclusive_area_nestings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ExclusiveAreaNestingOrder,
        ),  # exclusiveAreaNestings
        "static_memories": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableDataPrototype,
        ),  # staticMemories
    }

    def __init__(self) -> None:
        """Initialize InternalBehavior."""
        super().__init__()
        self.constants: list[ParameterDataPrototype] = []
        self.constant_values: list[ConstantSpecification] = []
        self.data_types: list[DataTypeMappingSet] = []
        self.exclusive_areas: list[ExclusiveArea] = []
        self.exclusive_area_nestings: list[ExclusiveAreaNestingOrder] = []
        self.static_memories: list[VariableDataPrototype] = []


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
