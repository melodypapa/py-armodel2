"""BlueprintPolicyList AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 164)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_AbstractBlueprintStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.blueprint_policy import (
    BlueprintPolicy,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BlueprintPolicyList(BlueprintPolicy):
    """AUTOSAR BlueprintPolicyList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_number_of: PositiveInteger
    min_number_of: PositiveInteger
    def __init__(self) -> None:
        """Initialize BlueprintPolicyList."""
        super().__init__()
        self.max_number_of: PositiveInteger = None
        self.min_number_of: PositiveInteger = None

    def serialize(self) -> ET.Element:
        """Serialize BlueprintPolicyList to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BlueprintPolicyList, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_number_of
        if self.max_number_of is not None:
            serialized = ARObject._serialize_item(self.max_number_of, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_number_of
        if self.min_number_of is not None:
            serialized = ARObject._serialize_item(self.min_number_of, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintPolicyList":
        """Deserialize XML element to BlueprintPolicyList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BlueprintPolicyList object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BlueprintPolicyList, cls).deserialize(element)

        # Parse max_number_of
        child = ARObject._find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse min_number_of
        child = ARObject._find_child_element(element, "MIN-NUMBER-OF")
        if child is not None:
            min_number_of_value = child.text
            obj.min_number_of = min_number_of_value

        return obj



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
