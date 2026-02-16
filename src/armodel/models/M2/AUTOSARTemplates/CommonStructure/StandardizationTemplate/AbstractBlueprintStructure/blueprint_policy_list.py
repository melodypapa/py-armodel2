"""BlueprintPolicyList AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.blueprint_policy import (
    BlueprintPolicy,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BlueprintPolicyList(BlueprintPolicy):
    """AUTOSAR BlueprintPolicyList."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_number_of", None, True, False, None),  # maxNumberOf
        ("min_number_of", None, True, False, None),  # minNumberOf
    ]

    def __init__(self) -> None:
        """Initialize BlueprintPolicyList."""
        super().__init__()
        self.max_number_of: PositiveInteger = None
        self.min_number_of: PositiveInteger = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BlueprintPolicyList to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintPolicyList":
        """Create BlueprintPolicyList from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BlueprintPolicyList instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BlueprintPolicyList since parent returns ARObject
        return cast("BlueprintPolicyList", obj)


class BlueprintPolicyListBuilder:
    """Builder for BlueprintPolicyList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintPolicyList = BlueprintPolicyList()

    def build(self) -> BlueprintPolicyList:
        """Build and return BlueprintPolicyList object.

        Returns:
            BlueprintPolicyList instance
        """
        # TODO: Add validation
        return self._obj
