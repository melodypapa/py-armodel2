"""FMFeatureRestriction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 32)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class FMFeatureRestriction(Identifiable):
    """AUTOSAR FMFeatureRestriction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    restriction_and_attributes: Optional[Any]
    def __init__(self) -> None:
        """Initialize FMFeatureRestriction."""
        super().__init__()
        self.restriction_and_attributes: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize FMFeatureRestriction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFeatureRestriction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize restriction_and_attributes
        if self.restriction_and_attributes is not None:
            serialized = SerializationHelper.serialize_item(self.restriction_and_attributes, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESTRICTION-AND-ATTRIBUTES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureRestriction":
        """Deserialize XML element to FMFeatureRestriction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureRestriction object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeatureRestriction, cls).deserialize(element)

        # Parse restriction_and_attributes
        child = SerializationHelper.find_child_element(element, "RESTRICTION-AND-ATTRIBUTES")
        if child is not None:
            restriction_and_attributes_value = child.text
            obj.restriction_and_attributes = restriction_and_attributes_value

        return obj



class FMFeatureRestrictionBuilder:
    """Builder for FMFeatureRestriction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureRestriction = FMFeatureRestriction()

    def build(self) -> FMFeatureRestriction:
        """Build and return FMFeatureRestriction object.

        Returns:
            FMFeatureRestriction instance
        """
        # TODO: Add validation
        return self._obj
