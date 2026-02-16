"""DataTypeMap AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
    AbstractImplementationDataType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)


class DataTypeMap(ARObject):
    """AUTOSAR DataTypeMap."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("application_data_type", None, False, False, ApplicationDataType),  # applicationDataType
        ("implementation", None, False, False, AbstractImplementationDataType),  # implementation
    ]

    def __init__(self) -> None:
        """Initialize DataTypeMap."""
        super().__init__()
        self.application_data_type: Optional[ApplicationDataType] = None
        self.implementation: Optional[AbstractImplementationDataType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataTypeMap to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataTypeMap":
        """Create DataTypeMap from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataTypeMap instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataTypeMap since parent returns ARObject
        return cast("DataTypeMap", obj)


class DataTypeMapBuilder:
    """Builder for DataTypeMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataTypeMap = DataTypeMap()

    def build(self) -> DataTypeMap:
        """Build and return DataTypeMap object.

        Returns:
            DataTypeMap instance
        """
        # TODO: Add validation
        return self._obj
