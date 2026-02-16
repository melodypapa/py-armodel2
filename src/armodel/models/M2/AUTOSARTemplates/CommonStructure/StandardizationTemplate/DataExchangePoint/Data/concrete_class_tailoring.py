"""ConcreteClassTailoring AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.data_format_element_scope import (
    DataFormatElementScope,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class ConcreteClassTailoring(DataFormatElementScope):
    """AUTOSAR ConcreteClassTailoring."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("validation_root", None, True, False, None),  # validationRoot
    ]

    def __init__(self) -> None:
        """Initialize ConcreteClassTailoring."""
        super().__init__()
        self.validation_root: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ConcreteClassTailoring to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConcreteClassTailoring":
        """Create ConcreteClassTailoring from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ConcreteClassTailoring instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ConcreteClassTailoring since parent returns ARObject
        return cast("ConcreteClassTailoring", obj)


class ConcreteClassTailoringBuilder:
    """Builder for ConcreteClassTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConcreteClassTailoring = ConcreteClassTailoring()

    def build(self) -> ConcreteClassTailoring:
        """Build and return ConcreteClassTailoring object.

        Returns:
            ConcreteClassTailoring instance
        """
        # TODO: Add validation
        return self._obj
