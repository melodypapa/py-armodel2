"""DataPrototypeReference AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DataPrototypeReference(ARObject):
    """AUTOSAR DataPrototypeReference."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tag_id", None, True, False, None),  # tagId
    ]

    def __init__(self) -> None:
        """Initialize DataPrototypeReference."""
        super().__init__()
        self.tag_id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataPrototypeReference to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeReference":
        """Create DataPrototypeReference from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataPrototypeReference instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataPrototypeReference since parent returns ARObject
        return cast("DataPrototypeReference", obj)


class DataPrototypeReferenceBuilder:
    """Builder for DataPrototypeReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeReference = DataPrototypeReference()

    def build(self) -> DataPrototypeReference:
        """Build and return DataPrototypeReference object.

        Returns:
            DataPrototypeReference instance
        """
        # TODO: Add validation
        return self._obj
