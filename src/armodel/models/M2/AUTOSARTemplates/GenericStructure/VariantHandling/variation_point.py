"""VariationPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.condition_by_formula import (
    ConditionByFormula,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class VariationPoint(ARObject):
    """AUTOSAR VariationPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("blueprint", None, False, False, DocumentationBlock),  # blueprint
        ("sw_syscond", None, False, False, ConditionByFormula),  # swSyscond
    ]

    def __init__(self) -> None:
        """Initialize VariationPoint."""
        super().__init__()
        self.blueprint: Optional[DocumentationBlock] = None
        self.sw_syscond: Optional[ConditionByFormula] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert VariationPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariationPoint":
        """Create VariationPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            VariationPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to VariationPoint since parent returns ARObject
        return cast("VariationPoint", obj)


class VariationPointBuilder:
    """Builder for VariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariationPoint = VariationPoint()

    def build(self) -> VariationPoint:
        """Build and return VariationPoint object.

        Returns:
            VariationPoint instance
        """
        # TODO: Add validation
        return self._obj
