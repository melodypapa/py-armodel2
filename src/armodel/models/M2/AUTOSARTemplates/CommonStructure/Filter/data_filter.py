"""DataFilter AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    UnlimitedInteger,
)


class DataFilter(ARObject):
    """AUTOSAR DataFilter."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_filter_type_enum", None, False, False, DataFilterTypeEnum),  # dataFilterTypeEnum
        ("mask", None, True, False, None),  # mask
        ("max", None, True, False, None),  # max
        ("min", None, True, False, None),  # min
        ("offset", None, True, False, None),  # offset
        ("period", None, True, False, None),  # period
        ("x", None, True, False, None),  # x
    ]

    def __init__(self) -> None:
        """Initialize DataFilter."""
        super().__init__()
        self.data_filter_type_enum: Optional[DataFilterTypeEnum] = None
        self.mask: Optional[UnlimitedInteger] = None
        self.max: Optional[UnlimitedInteger] = None
        self.min: Optional[UnlimitedInteger] = None
        self.offset: Optional[PositiveInteger] = None
        self.period: Optional[PositiveInteger] = None
        self.x: Optional[UnlimitedInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataFilter to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataFilter":
        """Create DataFilter from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataFilter instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataFilter since parent returns ARObject
        return cast("DataFilter", obj)


class DataFilterBuilder:
    """Builder for DataFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataFilter = DataFilter()

    def build(self) -> DataFilter:
        """Build and return DataFilter object.

        Returns:
            DataFilter instance
        """
        # TODO: Add validation
        return self._obj
