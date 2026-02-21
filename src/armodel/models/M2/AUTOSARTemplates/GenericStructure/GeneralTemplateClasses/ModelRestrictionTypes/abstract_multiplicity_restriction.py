"""AbstractMultiplicityRestriction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 422)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ModelRestrictionTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from abc import ABC, abstractmethod


class AbstractMultiplicityRestriction(ARObject, ABC):
    """AUTOSAR AbstractMultiplicityRestriction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    lower_multiplicity: Optional[PositiveInteger]
    upper_multiplicity: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize AbstractMultiplicityRestriction."""
        super().__init__()
        self.lower_multiplicity: Optional[PositiveInteger] = None
        self.upper_multiplicity: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractMultiplicityRestriction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractMultiplicityRestriction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lower_multiplicity
        if self.lower_multiplicity is not None:
            serialized = SerializationHelper.serialize_item(self.lower_multiplicity, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-MULTIPLICITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_multiplicity
        if self.upper_multiplicity is not None:
            serialized = SerializationHelper.serialize_item(self.upper_multiplicity, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-MULTIPLICITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractMultiplicityRestriction":
        """Deserialize XML element to AbstractMultiplicityRestriction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractMultiplicityRestriction object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractMultiplicityRestriction, cls).deserialize(element)

        # Parse lower_multiplicity
        child = SerializationHelper.find_child_element(element, "LOWER-MULTIPLICITY")
        if child is not None:
            lower_multiplicity_value = child.text
            obj.lower_multiplicity = lower_multiplicity_value

        # Parse upper_multiplicity
        child = SerializationHelper.find_child_element(element, "UPPER-MULTIPLICITY")
        if child is not None:
            upper_multiplicity_value = child.text
            obj.upper_multiplicity = upper_multiplicity_value

        return obj



class AbstractMultiplicityRestrictionBuilder:
    """Builder for AbstractMultiplicityRestriction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractMultiplicityRestriction = AbstractMultiplicityRestriction()

    def build(self) -> AbstractMultiplicityRestriction:
        """Build and return AbstractMultiplicityRestriction object.

        Returns:
            AbstractMultiplicityRestriction instance
        """
        # TODO: Add validation
        return self._obj
