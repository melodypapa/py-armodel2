"""DataTransformation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class DataTransformation(Identifiable):
    """AUTOSAR DataTransformation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data", None, False, False, DataTransformationKindEnum),  # data
        ("execute_despite", None, True, False, None),  # executeDespite
        ("transformers", None, False, True, any (Transformation)),  # transformers
    ]

    def __init__(self) -> None:
        """Initialize DataTransformation."""
        super().__init__()
        self.data: Optional[DataTransformationKindEnum] = None
        self.execute_despite: Optional[Boolean] = None
        self.transformers: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataTransformation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataTransformation":
        """Create DataTransformation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataTransformation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataTransformation since parent returns ARObject
        return cast("DataTransformation", obj)


class DataTransformationBuilder:
    """Builder for DataTransformation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataTransformation = DataTransformation()

    def build(self) -> DataTransformation:
        """Build and return DataTransformation object.

        Returns:
            DataTransformation instance
        """
        # TODO: Add validation
        return self._obj
