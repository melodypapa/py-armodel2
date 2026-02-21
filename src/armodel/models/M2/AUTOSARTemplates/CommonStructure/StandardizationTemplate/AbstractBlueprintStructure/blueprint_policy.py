"""BlueprintPolicy AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_AbstractBlueprintStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from abc import ABC, abstractmethod


class BlueprintPolicy(ARObject, ABC):
    """AUTOSAR BlueprintPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    attribute_name: String
    def __init__(self) -> None:
        """Initialize BlueprintPolicy."""
        super().__init__()
        self.attribute_name: String = None

    def serialize(self) -> ET.Element:
        """Serialize BlueprintPolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BlueprintPolicy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize attribute_name
        if self.attribute_name is not None:
            serialized = SerializationHelper.serialize_item(self.attribute_name, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATTRIBUTE-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintPolicy":
        """Deserialize XML element to BlueprintPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BlueprintPolicy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BlueprintPolicy, cls).deserialize(element)

        # Parse attribute_name
        child = SerializationHelper.find_child_element(element, "ATTRIBUTE-NAME")
        if child is not None:
            attribute_name_value = child.text
            obj.attribute_name = attribute_name_value

        return obj



class BlueprintPolicyBuilder:
    """Builder for BlueprintPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintPolicy = BlueprintPolicy()

    def build(self) -> BlueprintPolicy:
        """Build and return BlueprintPolicy object.

        Returns:
            BlueprintPolicy instance
        """
        # TODO: Add validation
        return self._obj
