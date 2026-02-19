"""RuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 331)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.rule_arguments import (
    RuleArguments,
)


class RuleBasedValueSpecification(ARObject):
    """AUTOSAR RuleBasedValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    arguments: Optional[RuleArguments]
    max_size_to_fill: Optional[Integer]
    rule: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize RuleBasedValueSpecification."""
        super().__init__()
        self.arguments: Optional[RuleArguments] = None
        self.max_size_to_fill: Optional[Integer] = None
        self.rule: Optional[Identifier] = None
    def serialize(self) -> ET.Element:
        """Serialize RuleBasedValueSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize arguments
        if self.arguments is not None:
            serialized = ARObject._serialize_item(self.arguments, "RuleArguments")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARGUMENTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_size_to_fill
        if self.max_size_to_fill is not None:
            serialized = ARObject._serialize_item(self.max_size_to_fill, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SIZE-TO-FILL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rule
        if self.rule is not None:
            serialized = ARObject._serialize_item(self.rule, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RuleBasedValueSpecification":
        """Deserialize XML element to RuleBasedValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RuleBasedValueSpecification object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse arguments
        child = ARObject._find_child_element(element, "ARGUMENTS")
        if child is not None:
            arguments_value = ARObject._deserialize_by_tag(child, "RuleArguments")
            obj.arguments = arguments_value

        # Parse max_size_to_fill
        child = ARObject._find_child_element(element, "MAX-SIZE-TO-FILL")
        if child is not None:
            max_size_to_fill_value = child.text
            obj.max_size_to_fill = max_size_to_fill_value

        # Parse rule
        child = ARObject._find_child_element(element, "RULE")
        if child is not None:
            rule_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.rule = rule_value

        return obj



class RuleBasedValueSpecificationBuilder:
    """Builder for RuleBasedValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RuleBasedValueSpecification = RuleBasedValueSpecification()

    def build(self) -> RuleBasedValueSpecification:
        """Build and return RuleBasedValueSpecification object.

        Returns:
            RuleBasedValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
