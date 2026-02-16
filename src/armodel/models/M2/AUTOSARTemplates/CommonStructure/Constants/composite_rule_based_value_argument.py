"""CompositeRuleBasedValueArgument AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class CompositeRuleBasedValueArgument(ARObject):
    """AUTOSAR CompositeRuleBasedValueArgument."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize CompositeRuleBasedValueArgument."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CompositeRuleBasedValueArgument to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompositeRuleBasedValueArgument":
        """Create CompositeRuleBasedValueArgument from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CompositeRuleBasedValueArgument instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CompositeRuleBasedValueArgument since parent returns ARObject
        return cast("CompositeRuleBasedValueArgument", obj)


class CompositeRuleBasedValueArgumentBuilder:
    """Builder for CompositeRuleBasedValueArgument."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompositeRuleBasedValueArgument = CompositeRuleBasedValueArgument()

    def build(self) -> CompositeRuleBasedValueArgument:
        """Build and return CompositeRuleBasedValueArgument object.

        Returns:
            CompositeRuleBasedValueArgument instance
        """
        # TODO: Add validation
        return self._obj
