"""DataTypeMappingSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_map import (
    DataTypeMap,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_request_type_map import (
    ModeRequestTypeMap,
)


class DataTypeMappingSet(ARElement):
    """AUTOSAR DataTypeMappingSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_type_maps", None, False, True, DataTypeMap),  # dataTypeMaps
        ("mode_request_type_maps", None, False, True, ModeRequestTypeMap),  # modeRequestTypeMaps
    ]

    def __init__(self) -> None:
        """Initialize DataTypeMappingSet."""
        super().__init__()
        self.data_type_maps: list[DataTypeMap] = []
        self.mode_request_type_maps: list[ModeRequestTypeMap] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataTypeMappingSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataTypeMappingSet":
        """Create DataTypeMappingSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataTypeMappingSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataTypeMappingSet since parent returns ARObject
        return cast("DataTypeMappingSet", obj)


class DataTypeMappingSetBuilder:
    """Builder for DataTypeMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataTypeMappingSet = DataTypeMappingSet()

    def build(self) -> DataTypeMappingSet:
        """Build and return DataTypeMappingSet object.

        Returns:
            DataTypeMappingSet instance
        """
        # TODO: Add validation
        return self._obj
