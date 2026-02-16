"""EvaluatedVariantSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.predefined_variant import (
    PredefinedVariant,
)


class EvaluatedVariantSet(ARElement):
    """AUTOSAR EvaluatedVariantSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("approval_status", None, True, False, None),  # approvalStatus
        ("evaluateds", None, False, True, PredefinedVariant),  # evaluateds
    ]

    def __init__(self) -> None:
        """Initialize EvaluatedVariantSet."""
        super().__init__()
        self.approval_status: NameToken = None
        self.evaluateds: list[PredefinedVariant] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EvaluatedVariantSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EvaluatedVariantSet":
        """Create EvaluatedVariantSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EvaluatedVariantSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EvaluatedVariantSet since parent returns ARObject
        return cast("EvaluatedVariantSet", obj)


class EvaluatedVariantSetBuilder:
    """Builder for EvaluatedVariantSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EvaluatedVariantSet = EvaluatedVariantSet()

    def build(self) -> EvaluatedVariantSet:
        """Build and return EvaluatedVariantSet object.

        Returns:
            EvaluatedVariantSet instance
        """
        # TODO: Add validation
        return self._obj
