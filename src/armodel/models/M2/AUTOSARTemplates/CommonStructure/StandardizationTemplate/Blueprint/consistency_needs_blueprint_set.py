"""ConsistencyNeedsBlueprintSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.consistency_needs import (
    ConsistencyNeeds,
)


class ConsistencyNeedsBlueprintSet(ARElement):
    """AUTOSAR ConsistencyNeedsBlueprintSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("consistency_needses", None, False, True, ConsistencyNeeds),  # consistencyNeedses
    ]

    def __init__(self) -> None:
        """Initialize ConsistencyNeedsBlueprintSet."""
        super().__init__()
        self.consistency_needses: list[ConsistencyNeeds] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ConsistencyNeedsBlueprintSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsistencyNeedsBlueprintSet":
        """Create ConsistencyNeedsBlueprintSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ConsistencyNeedsBlueprintSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ConsistencyNeedsBlueprintSet since parent returns ARObject
        return cast("ConsistencyNeedsBlueprintSet", obj)


class ConsistencyNeedsBlueprintSetBuilder:
    """Builder for ConsistencyNeedsBlueprintSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConsistencyNeedsBlueprintSet = ConsistencyNeedsBlueprintSet()

    def build(self) -> ConsistencyNeedsBlueprintSet:
        """Build and return ConsistencyNeedsBlueprintSet object.

        Returns:
            ConsistencyNeedsBlueprintSet instance
        """
        # TODO: Add validation
        return self._obj
