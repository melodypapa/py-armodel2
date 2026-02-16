"""ReferenceValueSpecification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class ReferenceValueSpecification(ValueSpecification):
    """AUTOSAR ReferenceValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("reference_value", None, False, False, DataPrototype),  # referenceValue
    ]

    def __init__(self) -> None:
        """Initialize ReferenceValueSpecification."""
        super().__init__()
        self.reference_value: Optional[DataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ReferenceValueSpecification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReferenceValueSpecification":
        """Create ReferenceValueSpecification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ReferenceValueSpecification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ReferenceValueSpecification since parent returns ARObject
        return cast("ReferenceValueSpecification", obj)


class ReferenceValueSpecificationBuilder:
    """Builder for ReferenceValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceValueSpecification = ReferenceValueSpecification()

    def build(self) -> ReferenceValueSpecification:
        """Build and return ReferenceValueSpecification object.

        Returns:
            ReferenceValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
