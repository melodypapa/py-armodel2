"""DataPrototypeMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_mapping import (
    SubElementMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class DataPrototypeMapping(ARObject):
    """AUTOSAR DataPrototypeMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("first_data", None, False, False, AutosarDataPrototype),  # firstData
        ("first_to_second", None, False, False, DataTransformation),  # firstToSecond
        ("second_data", None, False, False, AutosarDataPrototype),  # secondData
        ("second_to_first", None, False, False, DataTransformation),  # secondToFirst
        ("sub_elements", None, False, True, SubElementMapping),  # subElements
        ("text_table", None, False, False, TextTableMapping),  # textTable
    ]

    def __init__(self) -> None:
        """Initialize DataPrototypeMapping."""
        super().__init__()
        self.first_data: Optional[AutosarDataPrototype] = None
        self.first_to_second: Optional[DataTransformation] = None
        self.second_data: Optional[AutosarDataPrototype] = None
        self.second_to_first: Optional[DataTransformation] = None
        self.sub_elements: list[SubElementMapping] = []
        self.text_table: TextTableMapping = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataPrototypeMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeMapping":
        """Create DataPrototypeMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataPrototypeMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataPrototypeMapping since parent returns ARObject
        return cast("DataPrototypeMapping", obj)


class DataPrototypeMappingBuilder:
    """Builder for DataPrototypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeMapping = DataPrototypeMapping()

    def build(self) -> DataPrototypeMapping:
        """Build and return DataPrototypeMapping object.

        Returns:
            DataPrototypeMapping instance
        """
        # TODO: Add validation
        return self._obj
