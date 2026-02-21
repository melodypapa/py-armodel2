"""BlueprintGenerator AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 424)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintGenerator.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class BlueprintGenerator(ARObject):
    """AUTOSAR BlueprintGenerator."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    expression: Optional[VerbatimString]
    introduction: Optional[DocumentationBlock]
    def __init__(self) -> None:
        """Initialize BlueprintGenerator."""
        super().__init__()
        self.expression: Optional[VerbatimString] = None
        self.introduction: Optional[DocumentationBlock] = None

    def serialize(self) -> ET.Element:
        """Serialize BlueprintGenerator to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BlueprintGenerator, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize expression
        if self.expression is not None:
            serialized = SerializationHelper.serialize_item(self.expression, "VerbatimString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXPRESSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize introduction
        if self.introduction is not None:
            serialized = SerializationHelper.serialize_item(self.introduction, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTRODUCTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintGenerator":
        """Deserialize XML element to BlueprintGenerator object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BlueprintGenerator object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BlueprintGenerator, cls).deserialize(element)

        # Parse expression
        child = SerializationHelper.find_child_element(element, "EXPRESSION")
        if child is not None:
            expression_value = SerializationHelper.deserialize_by_tag(child, "VerbatimString")
            obj.expression = expression_value

        # Parse introduction
        child = SerializationHelper.find_child_element(element, "INTRODUCTION")
        if child is not None:
            introduction_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.introduction = introduction_value

        return obj



class BlueprintGeneratorBuilder:
    """Builder for BlueprintGenerator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintGenerator = BlueprintGenerator()

    def build(self) -> BlueprintGenerator:
        """Build and return BlueprintGenerator object.

        Returns:
            BlueprintGenerator instance
        """
        # TODO: Add validation
        return self._obj
