"""AbstractRuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 462)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod


class AbstractRuleBasedValueSpecification(ValueSpecification, ABC):
    """AUTOSAR AbstractRuleBasedValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AbstractRuleBasedValueSpecification."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize AbstractRuleBasedValueSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractRuleBasedValueSpecification, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "AbstractRuleBasedValueSpecification":
        """Deserialize XML element to AbstractRuleBasedValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractRuleBasedValueSpecification object
        """
        # Delegate to parent class to handle inherited attributes
        return super(AbstractRuleBasedValueSpecification, cls).deserialize(element)



class AbstractRuleBasedValueSpecificationBuilder:
    """Builder for AbstractRuleBasedValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractRuleBasedValueSpecification = AbstractRuleBasedValueSpecification()

    def build(self) -> AbstractRuleBasedValueSpecification:
        """Build and return AbstractRuleBasedValueSpecification object.

        Returns:
            AbstractRuleBasedValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
