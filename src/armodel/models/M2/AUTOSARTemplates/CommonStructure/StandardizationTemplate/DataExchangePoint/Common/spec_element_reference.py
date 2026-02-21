"""SpecElementReference AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Common.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from abc import ABC, abstractmethod


class SpecElementReference(Identifiable, ABC):
    """AUTOSAR SpecElementReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    alternative: Optional[String]
    def __init__(self) -> None:
        """Initialize SpecElementReference."""
        super().__init__()
        self.alternative: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize SpecElementReference to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SpecElementReference, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize alternative
        if self.alternative is not None:
            serialized = SerializationHelper.serialize_item(self.alternative, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALTERNATIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SpecElementReference":
        """Deserialize XML element to SpecElementReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SpecElementReference object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SpecElementReference, cls).deserialize(element)

        # Parse alternative
        child = SerializationHelper.find_child_element(element, "ALTERNATIVE")
        if child is not None:
            alternative_value = child.text
            obj.alternative = alternative_value

        return obj



class SpecElementReferenceBuilder:
    """Builder for SpecElementReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SpecElementReference = SpecElementReference()

    def build(self) -> SpecElementReference:
        """Build and return SpecElementReference object.

        Returns:
            SpecElementReference instance
        """
        # TODO: Add validation
        return self._obj
