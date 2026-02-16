"""TriggerPortAnnotation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TriggerPortAnnotation(GeneralAnnotation):
    """AUTOSAR TriggerPortAnnotation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("trigger", None, False, False, Trigger),  # trigger
    ]

    def __init__(self) -> None:
        """Initialize TriggerPortAnnotation."""
        super().__init__()
        self.trigger: Optional[Trigger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TriggerPortAnnotation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TriggerPortAnnotation":
        """Create TriggerPortAnnotation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TriggerPortAnnotation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TriggerPortAnnotation since parent returns ARObject
        return cast("TriggerPortAnnotation", obj)


class TriggerPortAnnotationBuilder:
    """Builder for TriggerPortAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerPortAnnotation = TriggerPortAnnotation()

    def build(self) -> TriggerPortAnnotation:
        """Build and return TriggerPortAnnotation object.

        Returns:
            TriggerPortAnnotation instance
        """
        # TODO: Add validation
        return self._obj
