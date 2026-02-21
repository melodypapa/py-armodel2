"""AbstractCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod


class AbstractCondition(ARObject, ABC):
    """AUTOSAR AbstractCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AbstractCondition."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize AbstractCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCondition":
        """Deserialize XML element to AbstractCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractCondition object
        """
        # Delegate to parent class to handle inherited attributes
        return super(AbstractCondition, cls).deserialize(element)



class AbstractConditionBuilder:
    """Builder for AbstractCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCondition = AbstractCondition()

    def build(self) -> AbstractCondition:
        """Build and return AbstractCondition object.

        Returns:
            AbstractCondition instance
        """
        # TODO: Add validation
        return self._obj
