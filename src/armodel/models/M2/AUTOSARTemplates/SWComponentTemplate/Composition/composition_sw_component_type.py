"""CompositionSwComponentType AUTOSAR element."""

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
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.instantiation_rte_event_props import (
    InstantiationRTEEventProps,
)
from armodel.models.M2.MSR.AsamHdo.Units.physical_dimension import (
    PhysicalDimension,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)


class CompositionSwComponentType(SwComponentType):
    """AUTOSAR CompositionSwComponentType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("components", None, False, True, any (SwComponent)),  # components
        ("connectors", None, False, True, SwConnector),  # connectors
        ("constant_values", None, False, True, ConstantSpecification),  # constantValues
        ("data_types", None, False, True, DataTypeMappingSet),  # dataTypes
        ("instantiation_rte_events", None, False, True, InstantiationRTEEventProps),  # instantiationRTEEvents
        ("physical", None, False, False, PhysicalDimension),  # physical
    ]

    def __init__(self) -> None:
        """Initialize CompositionSwComponentType."""
        super().__init__()
        self.components: list[Any] = []
        self.connectors: list[SwConnector] = []
        self.constant_values: list[ConstantSpecification] = []
        self.data_types: list[DataTypeMappingSet] = []
        self.instantiation_rte_events: list[InstantiationRTEEventProps] = []
        self.physical: Optional[PhysicalDimension] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CompositionSwComponentType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompositionSwComponentType":
        """Create CompositionSwComponentType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CompositionSwComponentType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CompositionSwComponentType since parent returns ARObject
        return cast("CompositionSwComponentType", obj)


class CompositionSwComponentTypeBuilder:
    """Builder for CompositionSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompositionSwComponentType = CompositionSwComponentType()

    def build(self) -> CompositionSwComponentType:
        """Build and return CompositionSwComponentType object.

        Returns:
            CompositionSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
