"""ClassTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_content_conditional import (
    ClassContentConditional,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.variation_restriction_with_severity import (
    VariationRestrictionWithSeverity,
)
from abc import ABC, abstractmethod


class ClassTailoring(ARObject, ABC):
    """AUTOSAR ClassTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    class_contents: list[ClassContentConditional]
    multiplicity: Optional[Any]
    variation: Optional[VariationRestrictionWithSeverity]
    def __init__(self) -> None:
        """Initialize ClassTailoring."""
        super().__init__()
        self.class_contents: list[ClassContentConditional] = []
        self.multiplicity: Optional[Any] = None
        self.variation: Optional[VariationRestrictionWithSeverity] = None
    def serialize(self) -> ET.Element:
        """Serialize ClassTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize class_contents (list to container "CLASS-CONTENTS")
        if self.class_contents:
            wrapper = ET.Element("CLASS-CONTENTS")
            for item in self.class_contents:
                serialized = ARObject._serialize_item(item, "ClassContentConditional")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize multiplicity
        if self.multiplicity is not None:
            serialized = ARObject._serialize_item(self.multiplicity, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MULTIPLICITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variation
        if self.variation is not None:
            serialized = ARObject._serialize_item(self.variation, "VariationRestrictionWithSeverity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClassTailoring":
        """Deserialize XML element to ClassTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClassTailoring object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse class_contents (list from container "CLASS-CONTENTS")
        obj.class_contents = []
        container = ARObject._find_child_element(element, "CLASS-CONTENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.class_contents.append(child_value)

        # Parse multiplicity
        child = ARObject._find_child_element(element, "MULTIPLICITY")
        if child is not None:
            multiplicity_value = child.text
            obj.multiplicity = multiplicity_value

        # Parse variation
        child = ARObject._find_child_element(element, "VARIATION")
        if child is not None:
            variation_value = ARObject._deserialize_by_tag(child, "VariationRestrictionWithSeverity")
            obj.variation = variation_value

        return obj



class ClassTailoringBuilder:
    """Builder for ClassTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClassTailoring = ClassTailoring()

    def build(self) -> ClassTailoring:
        """Build and return ClassTailoring object.

        Returns:
            ClassTailoring instance
        """
        # TODO: Add validation
        return self._obj
