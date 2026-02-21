"""FMAttributeValue AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 42)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
    FMAttributeDef,
)


class FMAttributeValue(ARObject):
    """AUTOSAR FMAttributeValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    definition_ref: Optional[ARRef]
    value: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize FMAttributeValue."""
        super().__init__()
        self.definition_ref: Optional[ARRef] = None
        self.value: Optional[Numerical] = None

    def serialize(self) -> ET.Element:
        """Serialize FMAttributeValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMAttributeValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize definition_ref
        if self.definition_ref is not None:
            serialized = SerializationHelper.serialize_item(self.definition_ref, "FMAttributeDef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFINITION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMAttributeValue":
        """Deserialize XML element to FMAttributeValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMAttributeValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMAttributeValue, cls).deserialize(element)

        # Parse definition_ref
        child = SerializationHelper.find_child_element(element, "DEFINITION-REF")
        if child is not None:
            definition_ref_value = ARRef.deserialize(child)
            obj.definition_ref = definition_ref_value

        # Parse value
        child = SerializationHelper.find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        return obj



class FMAttributeValueBuilder:
    """Builder for FMAttributeValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMAttributeValue = FMAttributeValue()

    def build(self) -> FMAttributeValue:
        """Build and return FMAttributeValue object.

        Returns:
            FMAttributeValue instance
        """
        # TODO: Add validation
        return self._obj
